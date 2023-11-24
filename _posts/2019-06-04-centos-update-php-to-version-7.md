---
title: Centos Update PHP To Version 7
date: 2019-06-04T00:43:20-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/centos-update-php-to-version-7/
tags:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

In my testlab, I needed to update my Centos 7 VM's version of PHP to version 7, this is how I did it:

### To Resolve:

1. Run the following (Your mileage may vary):

   ```shell
   sudo yum remove php-cli mod_php php-common

   sudo yum update -y

   systemctl stop httpd

   rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm
   yum -y install yum-utils
   yum update -y
   yum-config-manager --enable remi-php71
   yum -y install php php-opcache
   yum -y install php-mysqlnd php-pdo

   # didn't do:
   # In the next step I will install some common PHP modules that are required by CMS Systems like Wordpress, Joomla, and Drupal:
   # yum -y install php-gd php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-soap curl curl-devel

   systemctl start httpd
   systemctl status httpd
   ```

