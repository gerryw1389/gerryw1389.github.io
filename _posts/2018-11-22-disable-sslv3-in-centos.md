---
title: Disable SSLv3 In Centos
date: 2018-11-22T07:22:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/disable-sslv3-in-centos/
categories:
  - Linux
---
<!--more-->

### Description:

Short post on disabling SSLv3 for POODLE in Centos 7.

### To Resolve:

1. Run the following:  

   ```shell
   sudo vi /etc/httpd/conf.d/ssl.conf  
   # Inside you can find the SSLProtocol directive. If this is not available, create it. Modify this to explicitly remove support for SSLv3:  
   SSLProtocol all -SSLv3 -SSLv2  
   ```

2. Save and close the file. Restart the service to enable your changes.  

   ```shell
   # Centos 7:  
   sudo systemctl systemctl restart httpd  
   # Centos 6:  
   sudo service httpd restart
   ```

