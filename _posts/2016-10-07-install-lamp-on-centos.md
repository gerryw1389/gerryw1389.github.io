---
title: Install LAMP On CentOS
date: 2016-10-07T03:34:41+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/install-lamp-on-centos/
tags:
  - Linux
tags:
  - Bash
  - LinuxServer
  - SQL
---
<!--more-->

### Description:

Follow these steps to install the LAMP stack on CentOS 7. LAMP= Linux, Apache, MySQL, and Php.

### To Resolve:

1. First MySQL, Open a terminal => type:

   ```shell
   # This will change in the future, just get the latest release for CentOS
   sudo wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm

   # Extract the rpm
   sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm

   # Install Mysql
   sudo yum install mysql-server

   # Start the service
   systemctl start mysqld

   # Initiate the secure install script. Keep in mind it is asking about a database user called root which you don't know the password, so just hit enter. Not your current root password. It will then prompt you to set it.
   sudo mysql_secure_installation

   # Now enter whatever lines (one at a time) to create a database and user, in this example, WordPress:
   mysql -u root -p <enterPassword>
   CREATE DATABASE wordpress;
   CREATE USER "wordpressuser"@"localhost" IDENTIFIED BY "password";
   GRANT ALL PRIVILEGES ON wordpress.* TO "wordpressuser"@"localhost" IDENTIFIED BY "password";
   FLUSH PRIVILEGES;
   exit

   # Lastly, set Mysql to run on startup
   sudo systemctl enable mysqld
   ```

   - Useful Commands:

   ```shell
   # Shows databases
   SHOW DATABASES;

   # Shows users
   select host, user, password from mysql.user;
   ```

2. Next, Apache. Open a terminal and type:

   ```shell
   sudo yum install httpd mod_ssl

   sudo systemctl start httpd

   # Uncomment out and replace "servername" with your server's hostname.
   sudo vi /etc/httpd/conf/httpd.conf

   # Restart the service
   sudo systemctl restart httpd

   # Add firewall rules
   firewall-cmd –zone=public –add-port=80/tcp –permanent

   # Set it to run on startup, you should also be able to use "sudo systemctl enable httpd.service".
   sudo systemctl enable httpd
   ```

3. Lastly, install PHP:

   ```shell
   # Install php
   sudo yum install php php-mysql php-devel php-gd php-pecl-memcache php-pspell php-snmp php-xmlrpc php-xml

   # Restart apache
   sudo systemctl restart httpd
   ```


