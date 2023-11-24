---
title: Install Nginx On CentOS7
date: 2016-12-24T07:57:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/install-nginx-on-centos7/
tags:
  - Linux
tags:
  - LinuxServer
  - WebServer
---
<!--more-->

### Description:

So I have installed Apache a couple times on CentOS 7 and wanted to try Nginx just for testing. It turns out, I couldn't get it to work, I'm sure somewhere along step 3 I messed up but I wanted to post this anyways so that I can finish this up on a later day. Essentially, I got to the default web page that Nginx uses, but couldn't get the path changed to point to my WordPress install. Either way, here is the guide.

### To Resolve:

1. Install software by opening a terminal and typing:

   ```shell
   sudo yum install epel-release nginx mariadb mariadb-server php php-fpm php-common php-mysql php-gd php-xml php-mbstring php-mcrypt
   sudo systemctl start nginx
   sudo systemctl start mysqld
   sudo systemctl start php-fpm
   sudo systemctl enable nginx
   sudo systemctl enable mysqld
   sudo systemctl enable php-fpm
   sudo firewall-cmd --permanent --zone=public --add-service=http
   sudo firewall-cmd --reload
   ```

2. We will start by setting up the database:

   ```shell
   # Initiate the secure install script. Keep in mind it is asking about a database user called root which you don't know the password, so just hit enter. Not your current root password. It will then prompt you to set it.
   sudo mysql_secure_installation

   # Now enter the following lines (one at a time) to create a database and user, in this example, WordPress:
   mysql -u root -p (enterPassword)
   CREATE DATABASE wordpress;
   CREATE USER "wordpressuser"@"localhost" IDENTIFIED BY "password";
   GRANT ALL PRIVILEGES ON wordpress.* TO "wordpressuser"@"localhost" IDENTIFIED BY "password";
   FLUSH PRIVILEGES;
   exit
   ```


3. Now we configure our setup:

   ```shell
   sudo vi /etc/php.ini
   # Scroll until you get towards the bottom. Find cgi.fix_pathinfo and change the value to "0" and uncomment it out

   # Now we move to another file
   sudo vi /etc/php-fpm.d/www.conf

   # Change the "listen =" line to listen = /var/run/php-fpm/php-fpm.sock
   # Find the lines that set the listen.owner and listen.group and uncomment them and change their values to "nginx"
   ```


4. Get/install WordPress:

   ```shell
   cd ~/Downloads
   sudo wget http://wordpress.org/latest.tar.gz

   # Extract to default nginx dir
   tar -xzvf latest.tar.gz -C /usr/share/nginx/html/

   # Set permissions
   sudo chown -R nginx:nginx /usr/share/nginx/html/wordpress
   sudo chmod -R 755 /usr/share/nginx/html/wordpress

   # Now we create a site config page
   sudo vi /etc/nginx/conf.d/example.net.conf

   # Paste in the following:
   server {
   listen 80;
   server_name example.net;
   root   /usr/share/nginx/html/wordpress;
   index index.php index.html;
   location / {
   try_files $uri $uri/ @handler;
   }
   location @handler {
   fastcgi_pass 127.0.0.1:9000;
   fastcgi_param SCRIPT_FILENAME /usr/share/nginx/html/wordpress/index.php;
   include /etc/nginx/fastcgi_params;
   fastcgi_param SCRIPT_NAME /index.php;
   }
   location ~ .php$ {
   try_files $uri @handler;
   fastcgi_pass    127.0.0.1:9000;
   fastcgi_index   index.php;
   fastcgi_param SCRIPT_FILENAME /usr/share/nginx/html/wordpress$fastcgi_script_name;
   include fastcgi_params;
   }
   }

   # Now we move to a different file
   sudo vi /etc/nginx/conf.d/default.conf

   # Paste in or replace:
   server {
   listen       80;
   server_name  server_domain_name_or_IP;

   # Note that these lines are originally from the "location /" block
   root   /usr/share/nginx/html;
   index index.php index.html index.htm;

   location / {
   try_files $uri $uri/ =404;
   }
   error_page 404 /404.html;
   error_page 500 502 503 504 /50x.html;
   location = /50x.html {
   root /usr/share/nginx/html;
   }

   location ~ \.php$ {
   try_files $uri =404;
   fastcgi_pass unix:/var/run/php-fpm/php-fpm.sock;
   fastcgi_index index.php;
   fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
   include fastcgi_params;
   }
   }

   # Save and exit the file

   # Actually install wordpress
   cd /usr/share/nginx/html/wordpress
   cp wp-config-sample.php wp-config.php
   chmod 644 wp-config.php
   chown nginx:nginx wp-config.php

   # Open wordpress configuration file and change MySQL settings
   sudo vi wp-config.php

   # Lastly, restart service
   sudo systemctl restart nginx
   ```

5. Open up http://localhost in your browser and finish installing WordPress. Should be good to go!

