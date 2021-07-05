---
title: 'RHEL 7: Deploy Jenkins'
date: 2019-12-11T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/rhel7-deploy-jenkins/
categories:
  - Linux
tags:
  - Orchestration 
---
<!--more-->

### Description

I followed this post to install Jenkins on a RHEL 7 Server and Nginx with a reverse proxy for SSL offloading.

### To Resolve

1. Download and install Jenkins:

   ```shell
   sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
   sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
   yum install jenkins

   yum install java-1.8.0-openjdk
   # java -version

   systemctl start jenkins
   systemctl enable jenkins

   firewall-cmd --zone=public --add-port=8080/tcp --permanent
   firewall-cmd --zone=public --add-service=http --permanent
   firewall-cmd --reload

   # go to jenkins.domain.com:8080 in browser
   cat /var/lib/jenkins/secrets/initialAdminPassword
   ec2df2f8ef2649b1b61afd6684624d5e9

   # Choose to install community recommended plugins
   ```

2. This has it setup to work with HTTP, now to move to HTTPS

   - Install nginx

   ```shell
   rpm -Uvh http://nginx.org/packages/rhel/7/noarch/RPMS/nginx-release-rhel-7-0.el7.ngx.noarch.rpm
   yum install nginx
   systemctl start nginx
   systemctl enable nginx
   firewall-cmd --permanent --zone=public --add-service=http
   firewall-cmd --permanent --zone=public --add-service=https
   firewall-cmd --reload
   ```

   - Request cert

   ```shell
   openssl genrsa -out domain.key 2048
   openssl req -new -sha256 -key domain.key -out domain.csr
   Country? US
   State? Texas
   City? City
   organization? My Company
   organizational unit? My Parent Company
   Common name? server.domain.com
   email? admin@domain.com
   openssl req -noout -text -in domain.csr
   ```

   - Send `domain.csr` to Incommon.
   - Once complete, Download 'server' and 'intermediate' as X509, Base64 encoded
   - Open a cert decoder website and copy/paste the certs in this order: Server Cert =>  InCommon RSA Server CA => USERTrust RSA Certification Authority
   - Save as combined.cer

   - Configute Nginx
   - add the combined certs and domain.key to /etc/nginx/ssl
   - test: `nginx -t`

   - Ran into an issue:

   ```escape
   nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
   nginx: configuration file /etc/nginx/nginx.conf test is successful
   # says successul, but when I start service I get

   nginx: [emerg] open() "/var/run/nginx.pid" failed (13: Permission denied)
   Failed to parse PID from file /var/run/nginx.pid: Invalid argument

   fix is to reboot
   ```

   - Now we `vi /etc/nginx/conf.d/jenkins.conf`
   - And paste in the following after changing your cert details and server name

   ```shell
   upstream jenkins {
   server 127.0.0.1:8080 fail_timeout=0;
   }

   server {
   listen 80;
   server_name server.domain.com;
   return 301 https://$host$request_uri;
   }

   server {
   listen 443 ssl;
   server_name jenkins.domain.com;

   ssl_certificate    /etc/nginx/ssl/combined.cer;
   ssl_certificate_key /etc/nginx/ssl/domain.key;

   location / {
     proxy_set_header        Host $host:$server_port;
     proxy_set_header        X-Real-IP $remote_addr;
     proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header        X-Forwarded-Proto $scheme;
     proxy_redirect          http://127.0.0.1:8080 https://server.domain.com;
     proxy_pass              http://127.0.0.1:8080;
     # Required for new HTTP-based CLI
     proxy_http_version 1.1;
     proxy_request_buffering off;
     proxy_buffering off; # Required for HTTP-based CLI to work over SSL
     # workaround for https://issues.jenkins-ci.org/browse/JENKINS-45651
     add_header 'X-SSH-Endpoint' 'jenkins.domain.com:50022' always;
   }
   }
   ```

   - Now run `systemctl start nginx` and you will get an error like `[crit] 14549#14549: *7 connect() to 127.0.0.1:8080 failed (13: Permission denied) while connecting to upstream`

   - Fix:

   ```shell
   # per https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx
   systemctl stop nginx
   setsebool -P httpd_can_network_connect 1
   systemctl stop nginx
   ```

3. Now that Jenkins is running, need to modify a few things:

   - Jenkins Web UI => Manage Jenkins => Configure System => Jenkins Location => Update the Jenkins URL to use HTTPS - `https://jenkins.domain.com/`

   - Install 'Active Directory plugin'
   - Manage Jenkins => Configure Global Security => Security Realm:Active Directory

     - Domain Name = domain.com
     - Domain Controller = dc-1.domain.com:3268
     - bind dn = CN=user,DC=Domain,DC=com
     - bind password = password

   - Save and exit. Logout of web UI.
   - Login as your user # this takes a while the first time, but will be fast after that. Notice that is displays all your AD groups when you login.
   - Now go back to Manage Jenkins => Configure Global Security => Authorization => Select 'Matrix-based Security'
   - Add the main admin AD group your user is a member of (just the name by itself) and check the box for 'Administer' under 'Overall' section.
   - Give Anonymous Users 'Read' under the 'Overall' section. Not sure if this is required but I did this for scripts to run from VRO.
   - Give 'Authenticated Users' nothing.
