---
title: Setup HTTPS Using Apache On CentOS 7
date: 2016-11-15T04:58:38+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/setup-ssl-using-apache-on-centos-7/
categories:
  - Linux
  - Networking
tags:
  - Cloud
  - Certificates
  - WebServer
  - Setup
---
<!--more-->

### Description:

After converting from NoIP to buying a domain and hosting it on CloudFlare, I was finally ready to get SSL configured for my site (CentOS 7, Apache, WordPress, using Let's Encrypt SSL certificate). I followed these steps:

### To Resolve:

1. First, before I even began, I had to rename my machine. Before it was a custom name schema I use on my internal network, but I had to change in order for CloudFlare to point to my host specifically:

   - To set the hostname on CentOS 7:

   ```shell
   sudo hostname gerrywilliams.net
   sudo vim /etc/hosts #change it there next to the 127.0.0.1 and the ::1
   sudo vim /etc/sysconfig/network # set it like HOSTNAME=gerrywilliams.net
   # Now just check your hostname
   hostname
   ```

2. Now to begin, we edit our Apache config file:

   ```shell
   vim /etc/httpd/conf/httpd.conf
   # Add the given line to the last line of configuration file
   IncludeOptional setup/*.conf
   ```

3. Now we create the file:

   ```shell
   sudo mkdir /etc/httpd/setup
   sudo vim /etc/httpd/setup/gerrywilliams.net.conf

   # Add the following:
   <VirtualHost *:80>
   ServerName gerrywilliams.net
   ServerAlias gerrywilliams.net
   DocumentRoot /var/www/
   </VirtualHost>

   # Restart apache: 
   sudo systemctl httpd restart
   ```

4. Now we get Let's Encrypt:

   ```shell
   sudo wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm # Enable the EPEL Repository
   sudo rpm -ivh epel-release-latest-7.noarch.rpm
   sudo yum install git shell-pip # install prereq's
   sudo git clone https://github.com/letsencrypt/letsencrypt # clone the Let's Encrypt source code from Github
   cd ~
   ```

5. Before continuing, we need to get a few things ready:

   - Open port 443 on your router and forward it to your CentOS VM.  
   - Open ports 80/443 on your firewall (you can disable 80 later if you want, depends on what you select later)

6. OK, let's get back on track, navigate to your Let's Encrypt directory (for me that's /home/gerry/letsencrypt)

   ```shell
   cd letsencrypt/
   sudo ./letsencrypt-auto --apache -d gerrywilliams.net --verbose
   ```

   - Follow the wizard to create an email, accept the TOS, and continue through until you get the congratulations screen. Somewhere in there it asks if you want to allow HTTP and HTTPS and I chose the second option to force HTTPS. For me, I got numerous errors because my hostname was domain.com and CloudFlare wasn't pointing at my VM as the root, but the &#8220;www&#8221;, so I had to go back to step one and rename my host and all the files to include the &#8220;www&#8221;. I'm sure I'm missing something, but I'm not ashamed to say I'm a Linux noob 🙂

7. Now we go back to that setup directory and add the port 443 info:

   ```shell
   sudo vim /etc/httpd/setup/gerrywilliams.net.conf

   # Add the following:
   <VirtualHost *:443>
   ServerName gerrywilliams.net
   ServerAlias gerrywilliams.net
   DocumentRoot /var/www/
   SSLEngine on
   SSLCertificateFile /etc/letsencrypt/live/gerrywilliams.net/cert.pem
   SSLCertificateKeyFile /etc/letsencrypt/live/gerrywilliams.net/privkey.pem
   SSLCertificateChainFile /etc/letsencrypt/live/gerrywilliams.net/chain.pem
   </VirtualHost>

   # Save and exit
   ```

8. Now we need to add the SSL certs to the Apache SSL File (feel free to skip this step as I guess Let's Encrypt did this for me automatically)

   ```shell
   sudo vim /etc/httpd/conf.d/ssl.conf
   # Replace SSLCertificateFile, SSLCertificateKeyFile, and SSLCertificateChainFile to point to the locations in step 8.
   ```

9. Check the virtual host that Let's Encrypt created (Just look for anything wrong):

   ```shell
   sudo cat /etc/httpd/conf.d/vhost-gerrywilliams.net-le-ssl.conf
   ```

10. At this point, you just restart httpd and you have SSL!

11. The SSL Cert by Let's Encrypt is good for 90 days. You need to renew by running `./letsencrypt-auto renew`. You can see what it's listening to by running `grep -ir "^listen" /etc/httpd/*`

12. Alternatively:

   ```shell
   # To renew one time manually:
   sudo certbot renew

   # Setup auto renewal
   sudo crontab -e

   # Type:
   30 2 * * 1 /usr/bin/certbot renew >> /var/log/le-renew.log
   ```

13. Lastly, it is best practice to check your SSL configuration by visiting [SSLLabs](https://www.ssllabs.com/ssltest/analyze.html)

### References:

["How to Configure Lets Encrypt SSL with Apache on CentOS 7"](https://www.techbrown.com/configure-lets-encrypt-ssl-apache-centos-7/)