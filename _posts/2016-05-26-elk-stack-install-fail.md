---
title: ELK Stack Install Fail
date: 2016-05-26T03:55:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/elk-stack-install-fail/
tags:
  - Linux
tags:
  - LinuxServer
  - Setup
---
<!--more-->

### Description:

The ELK stack is used as a central point to monitor system event logs for a network. Instead of re-inventing the wheel, I mostly just followed [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-7). I installed the Logstash server on my Linux CentOS VM.

NOTE: When using vi, you start by launching a file using &#8220;vi (filename)&#8221;. Once in, you type &#8220;i&#8221; for insert mode. This allows you to edit a file. When you are done doing your edits, press the &#8220;esc&#8221; key on your keyboard and type &#8220;:x&#8221; and the &#8220;enter&#8221; key on your keyboard to exit. You can of course use your own editor if you don't want to use vi.

### To Resolve:

1. When I created my CentOS VM, I chose the options of having it as a &#8220;system log server&#8221; in the setup. Not sure if this will play a role a later on or not so I just wanted to include it.

   - Open up Terminal and type:

   ```shell
   # We need to create a hostname for our server. 
   # Login as root
   su -
   # Enter root's password
   # We are now running commands as root!

   # Now we are going to edit a file using a command line editor that opens the file inside the command line:
   vi /etc/sysconfig/network

   # Change the following:
   HOSTNAME=(serverName)

   # Save and exit vi
   ```

   - Now we set a hostname for the machine

   ```shell
   # This sets your hostnames for the machine (There are actually 3 different "hostnames" see http://ask.xmodulo.com/change-hostname-centos-rhel-7.html for more info):
   sudo hostnamectl set-hostname elkserver
   ```

2. We need to create a new user and assign them root profiles and then disable root login:

   ```shell
   # Create the user - let's say gerry
   adduser gerry

   # Give them a password
   passwd gerry
   # Enter the password twice

   # Now we add them to the administrators group - wheel in linux
   gpasswd -a gerry wheel
   ```

3. Logout and back in as the new user => gerry.

4. Now we generate a SSH key pair.

   ```shell
   # Change to home directory and create a "keys" folder
   cd ~
   mkdir keys
   # Change to root again
   su -
   ssh-keygen
   # Enter a file: /home/gerry/Keys/rsa_id
   # Enter passphrase twice: (private passphrase I made up). You should then get a successful creation prompt with the fingerprint.
   # Now let's verify it worked by checking your public key. Copy it to the clipboard.
   cat /home/gerry/Keys/rsa_id.pub
   ```

5. Now we add the key to our &#8220;authorized_keys&#8221; file

   ```shell
   # If you are still in the root prompt, exit to gerry's prompt by typing "exit". Now we will create a file that only gerry has access to:
   cd ~
   mkdir .ssh
   chmod 700 .ssh
   # Create a new file and paste in your key, save and exit:
   vi .ssh/authorized_keys

   # Set permissions
   chmod 600 .ssh/authorized_keys

   # Exit the terminal
   exit
   ```

6. Disallow root logins:

   ```shell
   # We will modify the ssh service to disallow root logins. 
   vi /etc/ssh/sshd_config 
   # Navigate to: the line "#PermitRootLogin Yes and uncomment it and replacing yes with "no"
   # Save and exit
   # Now reload the ssh daemon
   systemctl reload sshd
   ```

7. Now that we have SSH setup and a new user, let's get started with the install:

8. First thing to do is to download and install Java 8 update 40:

   ```shell
   cd /opt
   sudo wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u40-b25/jre-8u40-linux-x64.tar.gz"
   sudo tar xvf jre-8*.tar.gz
   sudo chown -R root: jre1.8*
   sudo alternatives --install /usr/bin/java java /opt/jre1.8*/bin/java 1
   sudo rm /opt/jre-8*.tar.gz
   ```

9. Now we install Elasticsearch:

   ```shell
   sudo rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch
   sudo vi /etc/yum.repos.d/elasticsearch.repo

   # Now copy and paste the following in:
   [elasticsearch-1.4]
   name=Elasticsearch repository for 1.4.x packages
   baseurl=http://packages.elasticsearch.org/elasticsearch/1.4/centos
   gpgcheck=1
   gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch
   enabled=1
   # Save and exit

   sudo yum -y install elasticsearch-1.4.4
   sudo vi /etc/elasticsearch/elasticsearch.yml
   # Now we edit the config. Find the "Network and HTTP" section and locate the "network.host: (IP Address of server)". Uncomment it and type "localhost" instead. Save and exit vi.

   # Start and enable (auto-start) elasticsearch:
   sudo systemctl start elasticsearch
   sudo systemctl enable elasticsearch
   ```

10. Now we install Kibana:

   ```shell
   cd ~
   wget https://download.elasticsearch.org/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
   tar xvf kibana-*.tar.gz
   vi ~/kibana-4*/config/kibana.yml 
   # Again, we are editing the config file. Find the line "host: "0.0.0.0"" and replace the IP with "localhost". Make sure to have the quotations.

   # Now we need to move Kibana to a better directory.
   sudo mkdir -p /opt/kibana
   sudo cp -R ~/kibana-4*/* /opt/kibana/

   # Kibana can be started by running /opt/kibana/bin/kibana, but we want it to run as a service. Create the Kibana systemd init file using vi
   sudo vi /etc/systemd/system/kibana4.service

   # Paste the following in:
   [Service]
   ExecStart=/opt/kibana/bin/kibana
   Restart=always
   StandardOutput=syslog
   StandardError=syslog
   SyslogIdentifier=kibana4
   User=root
   Group=root
   Environment=NODE_ENV=production
   [Install]
   WantedBy=multi-user.target

   # Now we start and enable the Kibana service
   sudo systemctl start kibana4
   sudo systemctl enable kibana4
   ```

11. Now we install Nginx to setup a reverse proxy for Kibana

   ```shell
   sudo yum -y install epel-release
   sudo yum -y install nginx httpd-tools
   sudo htpasswd -c /etc/nginx/htpasswd.users gerry
   # Now enter a password for this user.

   sudo vi /etc/nginx/nginx.conf
   # Scroll down to the server block and remove everything past "server {". The line before that reads "include /etc/nginx/conf.d/*.conf;", so all we add is a "}" to the end instead.
   # The bottom two lines of the file should now read:
   include /etc/nginx/conf.d/*.conf;
   }
   }
   # Save and exit vi.

   # Now we create that server block in a new file.
   sudo vi /etc/nginx/conf.d/kibana.conf

   # Paste the following in replacing "example.com" with your server's IP address:
   server {
   listen 80;
   server_name 192.168.0.102;
   auth_basic "Restricted Access";
   auth_basic_user_file /etc/nginx/htpasswd.users;
   location / {
   proxy_pass http://localhost:5601;
   proxy_http_version 1.1;
   proxy_set_header Upgrade $http_upgrade;
   proxy_set_header Connection 'upgrade';
   proxy_set_header Host $host;
   proxy_cache_bypass $http_upgrade;
   }
   }

   # Now we start and enable Nginx by typing: 
   sudo systemctl start nginx
   sudo systemctl enable nginx
   ```

12. If SELinux is enabled, you need to disable it. Do the following if you are unsure.

   ```shell
   sudo setsebool -P httpd_can_network_connect 1
   ```

13. Now we install Logstash

   ```shell
   sudo vi /etc/yum.repos.d/logstash.repo

   # Add the following information:
   [logstash-1.5]
   name=logstash repository for 1.5.x packages
   baseurl=http://packages.elasticsearch.org/logstash/1.5/centos
   gpgcheck=1
   gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch
   enabled=1
   # Save and exit
   sudo yum -y install logstash

   # Logstash is now installed. We need to create a SSH key pair for the Logstash Forwarder. Open the OpenSSL config file: 
   sudo vi /etc/pki/tls/openssl.cnf

   # Navigate towards the bottom until you find the "[ v3_ca ]" section. In the line under it, Type: subjectAltName = IP: (serverIPAddress)

   # Now we generate a SSH Key pair:
   cd /etc/pki/tls
   sudo openssl req -config /etc/pki/tls/openssl.cnf -x509 -days 3650 -batch -nodes -newkey rsa:2048 -keyout private/logstash-forwarder.key -out certs/logstash-forwarder.crt

   # Now back to Logstash configuration. Files are in the JSON-format, and reside in /etc/logstash/conf.d. The configuration consists of three sections: inputs, filters, and outputs.
   # The "lumberjack" input is the protocol the Logstash Forwarder uses. Type: 
   sudo vi /etc/logstash/conf.d/01-lumberjack-input.conf

   # Type, then save and exit:
   input {
   lumberjack {
   port => 5000
   type => "logs"
   ssl_certificate => "/etc/pki/tls/certs/logstash-forwarder.crt"
   ssl_key => "/etc/pki/tls/private/logstash-forwarder.key"
   }
   }

   # Moving on to another file
   sudo vi /etc/logstash/conf.d/10-syslog.conf
   # Type, then save and exit:
   filter {
   if [type] == "syslog" {
   grok {
   match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:[%{POSINT:syslog_pid}])?: %{GREEDYDATA:syslog_message}" }
   add_field => [ "received_at", "%{@timestamp}" ]
   add_field => [ "received_from", "%{host}" ]
   }
   syslog_pri { }
   date {
   match => [ "syslog_timestamp", "MMM d HH:mm:ss", "MMM dd HH:mm:ss" ]
   }
   }
   }

   # Moving on to another file
   sudo vi /etc/logstash/conf.d/30-lumberjack-output.conf

   # Type, then save and exit:
   output {
   elasticsearch { host => localhost }
   stdout { codec => rubydebug }
   }

   # Finally, restart Logstash so these can take effect. Type: 
   sudo systemctl restart logstash
   ```

14. We are essentially done with the server part, now we need to install the Logstash Forwarder on client machines and match them with the private key just generated.

---

The ELK stack will work with Windows logs, but I will have to research that more in depth to get it working.  
For now, I just wanted to see it work so I will use my Fedora box (192.168.0.50)as a test from the logstash forwarder.

1. On the Logstash SERVER, copy the SSL cert to the remote host by typing:

   ```shell
   scp /etc/pki/tls/certs/logstash-forwarder.crt gerry@192.168.0.50:/tmp

   # In this case I got an error because the service wasn't started on my Fedora box, so I typed:
   systemctl start sshd.service
   systemctl enable sshd.service

   # After the cert copies, we need to import the GPG key, Type: 
   sudo rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch
   ```

2. Now we edit the logstash

   ```shell
   sudo vi /etc/yum.repos.d/logstash-forwarder.repo

   # Type, then save and exit:
   [logstash-forwarder]
   name=logstash-forwarder repository
   baseurl=http://packages.elasticsearch.org/logstashforwarder/centos
   gpgcheck=1
   gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch
   enabled=1

   # Now install the LF package, Type: 
   sudo yum -y install logstash-forwarder

   # Now copy the SSL cert to the correct location, Type: 
   sudo cp /tmp/logstash-forwarder.crt /etc/pki/tls/certs/

   # Type: 
   sudo vi /etc/logstash-forwarder.conf
   # Under the network section, everything is commented out. Add a couple blank lines under the "{" and enter these lines substituting your Logstash server's IP address instead of mine at 192.168.0.102:
   "servers": "192.168.0.102:5000",
   "timeout": 15,
   "ssl ca": "/etc/pki/tls/certs/logstash-forwarder.crt"
   In that same file, under the "files" section and between the square brackets, type:
   {
   "paths": [
   "/var/log/messages",
   "/var/log/secure"
   ],
   "fields": { "type": "syslog" }
   }

   # Now we restart the Logstash Forwarder service, Type: 
   sudo service logstash-forwarder restart
   ```

3. The forwarder should be sending messages now. Go back to your Logstash server and login to your web GUI. Login using the credentials you created.

4. It will say that it can't run without at least one filter, use the dropbox and select the &#8220;@timestamp&#8221; selection and click the &#8220;create&#8221; button.  

NOTE: This never happened on mine so I abandoned the project &#8230; it could be something easy or complex but I'm too much of noob to understand at this point. I figured once I get more experience I will come back and work on this.

5. Now click the Discover link in the top navigation bar. By default, this will show you all of the log data over the last 15 minutes.

   - Try the following things:  
   - Search for &#8220;root&#8221; to see if anyone is trying to log into your servers as root  
   - Search for a particular hostname (search for host: &#8220;hostname&#8221;)  
   - Change the time frame by selecting an area on the histogram or from the menu above  
   - Click on messages below the histogram to see how the data is being filtered

### References:

["Initial Server Setup with CentOS 7"](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7)  

["How To Install Elasticsearch, Logstash, and Kibana (ELK Stack) on CentOS 7"](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-7)  

For Windows - ["Using nxlog to ship logs in to logstash from Windows using om_ssl"](http://stackoverflow.com/questions/26789903/using-nxlog-to-ship-logs-in-to-logstash-from-windows-using-om-ssl)  

Another Guide - ["How to install Elasticsearch, Logstash and Kibana 4 on CentOS 7 / RHEL 7"](http://www.itzgeek.com/how-tos/linux/centos-how-tos/how-to-install-elasticsearch-logstash-and-kibana-4-on-centos-7-rhel-7.html)