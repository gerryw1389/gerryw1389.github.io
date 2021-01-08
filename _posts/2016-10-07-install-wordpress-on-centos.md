---
title: Install WordPress On CentOS
date: 2016-10-07T03:48:38+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/install-wordpress-on-centos/
categories:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

This assumes you have already followed the steps in [Setting Up LAMP On CentOS](https://automationadmin.com/2016/10/install-lamp-on-centos/). The only step left to do is install WordPress:

### To Resolve:

1. Open a terminal => type:

   ```shell
   # Change to home dir and get the latest wordpress install for CentOS:
   cd ~
   wget http://wordpress.org/latest.tar.gz
   tar -xzvf latest.tar.gz

   # Extract to root server dir (default apache directory)
   sudo rsync -avP ~/wordpress/ /var/www/html/

   # Create an uploads folder
   sudo mkdir /var/www/html/wp-content/uploads

   # Give the "apache" user full permissions for the directory and subfolders
   sudo chown -R apache:apache /var/www/html/*

   # Set the sample php config file as your own
   sudo cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
   ```

2. Now just add the MySQL info from your MySQL install:

   ```shell
   sudo vi wp-config.php
   # Find and replace with our database, user, password:

   // ** MySQL settings - You can get this info from your web host ** //
   /** The name of the database for WordPress */
   define('DB_NAME', 'wordpress');
   /
   /** MySQL database username */
   define('DB_USER', 'wordpressuser');
   /
   /** MySQL database password */
   define('DB_PASSWORD', 'password');
   ```

3. Now open up a browser and go to: http://serverDomainNameOrIpAddress # NOTE: mine wouldn't start so I rebooted the server, then it worked!

4. Now get WordPress to start on startup:

   ```shell
   # Find your firewall zone for your nic
   firewall-cmd --get-active-zones

   # Add the rule
   firewall-cmd --zone=public --add-port=80/tcp --permanent
   ```

5. Now setup DDNS following my guide at [Setting Up DDNS For Your Home](https://automationadmin.com/2016/10/setting-up-ddns-for-home/).

6. Forward the ports in your router which is described in the same post. Done!

7. If you ever want to uninstall WordPress, just do the following:

   ```shell
   # Delete everything under /var/www/html. NOTE: I'm a Powershell guy so I really wish there was a -whatif switch for this. Instead I just echo the command first to check the dirs and then delete them.
   echo rm -rf /var/www/html
   rm -rf /var/www/html

   # Remove Mysql database
   mysql -u root -p
   # password
   DROP DATABASE wordpress;
   FLUSH PRIVILEGES;
   exit
   ```

### References:

["How To Install WordPress on CentOS 7"](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-centos-7)