---
title: Setting Up A Reverse Proxy On Centos7
date: 2017-01-14T07:56:31+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/setting-up-a-reverse-proxy-on-centos7/
categories:
  - Linux
---
<!--more-->

### Description:

Follow these steps to create a reverse proxy using Apache on Centos7.

### To Resolve:

1. Open a terminal and type: `yum install httpd mod_ssl`. This installs Apache and the mod_ssl packages.

2. Now we configure our proxy settings:

   - Make sure that the file `/etc/httpd/conf.d` has the line `includes /etc/httpd/conf.d/*.conf` at the end.

   ```shell
   sudo vi /etc/httpd/conf.d/rproxy.conf

   # Paste in:
   ProxyRequests Off
   ProxyPass /test1 http://192.168.10.59:8080/test1 connectiontimeout=5 timeout=30
   ProxyPassReverse /test1 http://192.168.10.59:8080/test1
   ProxyPass /test2 http://192.168.10.59:8080/test2 connectiontimeout=5 timeout=30
   ProxyPassReverse /test2 http://192.168.10.59:8080/test2
   #Note that proxy pass can point to a different server, different host name or IP address. The "connectiontimeout" is the time it takes to create the connection to the backend and "timeout" is the time proxy waits for response from backend.
   #Save and exit
   ```

3. Now we install the `mod_proxy_html` module so that it can rewrite html links:

   ```shell
   sudo yum install mod_proxy_html

   # Copy its config file to your httpd directory without changing any values
   cp /usr/share/doc/httpd-2.4.6/proxy-html.conf /etc/httpd/conf.d/

   # Now just restart Apache and test!
   sudo systemctl restart httpd
   ```

### References:

["Forward & Reverse Apache Proxy – CentOS 7"](https://geekpeek.net/forward-reverse-apache-proxy-centos/)