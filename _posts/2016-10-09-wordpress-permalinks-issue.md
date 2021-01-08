---
title: WordPress Permalinks Issue
date: 2016-10-09T03:55:07+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/wordpress-permalinks-issue/
categories:
  - LocalSoftware
  - Linux
tags:
  - LinuxServer
  - WebServer
---
<!--more-->

### Description:

Many people seem to have this issue where you create a WordPress site and then when you go to change the site URL structure under &#8220;Permalinks&#8221;, the site is unable to change it due to permissions.

### To Resolve:

1. First thing to figure out is which directory is the root of your website. Doing a generic install it is /var/www/html for Apache.

2. Copy the code it gives you on the WordPress page. Create that file in the directory from step 1 and gave it full permissions (temporarily):

   ```powershell
   cd /var/www/html
   sudo touch .htaccess
   sudo pluma .htaccess
   ```

   - paste in code from above and save.

3. It said to change permission to apache:apache and run:

   ```shell
   sudo chmod 777 .htaccess
   sudo chown -R apache:apache /var/www/html/*
   sudo service httpd restart
   ```

4. This should've done the trick. But what really happened is once I saved, I got a bunch of AVC Denied errors from Selinux on my Centos VM. So I had to [look that up](http://serverfault.com/questions/626610/selinux-preventing-apache-from-writing-to-a-file)

5. I started thinking, maybe if it's not just SELinux, but maybe some configuration for Apache.

   ```shell
   # I ran the following along with the previous steps and it seemed to work. But the links weren't actually changing.
   sudo setenforce 0

   # I then ran the following and it still didn't work. Rebooted.
   sudo semanage fcontext -a -t httpd_sys_rw_content_t '.htaccess' 

   # I then ran the following in /var/www/html to confirm. Still didn't work.
   chcon --type httpd_sys_rw_content_t /var/www/html/.htaccess
   ls -alZ

   # I started thinking, maybe if it's not just SELinux, but maybe some configuration for Apache.
   cat /etc/httpd/conf/httpd.conf

   # Look for
   <Directory /path/to/site>
   AllowOverride None
   </Directory>

   # Add/change the following setting to allow .htaccess in your web directory to work:
   AllowOverride FileInfo

   # Restart the daemon
   sudo service restart httpd

   # This resolved it!

   # NOTE: I've also read that you may have to enable the "mod_rewrite" module: 
   sudo a2enmod rewrite; sudo service apache2 restart
   ```