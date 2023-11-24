---
title: Install DokuWiki
date: 2016-05-26T03:56:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/install-dokuwiki/
tags:
  - Linux
tags:
  - LinuxClient
---
<!--more-->

### Description:

Follow these steps to install DokuWiki on Linux Fedora. DokuWiki is a lightweight wiki that I will install on top of Apache web server in Fedora.

### To Resolve:

1. Open terminal and then type:

   ```shell
   yum install dokuwiki dokuwiki-selinux

   # Start and enable httpd
   systemctl start httpd.service
   systemctl enable httpd.service
   ```

2. That's it! DokuWiki should now be available by browsing to &#8220;http://localhost/dokuwiki&#8221;

3. By default, DokuWiki lets you add and edit pages, but you cannot get to the configuration manager until you edit some files, so lets do that.

   - Navigate to: /etc/dokuwiki/local.php and set:

   ```shell
   conf['useacl'] = 1;$
   conf['superuser'] = '@admin';
   ```

4. This enables ACL and gives all members admin rights.

5. Now add a new user to &#8220;users.auth.php&#8221;:

   ```shell
   admin:21232f297a57a5a743894a0e4a801fc3:Admin:example@example.com:admin
   ```

   - This adds the user &#8220;admin&#8221; with the password &#8220;admin&#8221; as a member of the &#8220;admin&#8221; group.
   - Paths:  
   - DokuWiki => /usr/share/dokuwiki  
   - Configuration => /etc/dokuwiki  
   - Data directory => /var/lib/data

6. Lastly, if you plan to access the dokuwiki through the network you have to edit the file named &#8220;dokuwiki.conf&#8221; in the directory /etc/httpd/conf.d/. For Fedora 18 and later, you find the line that says &#8220;Require Local&#8221; and change it to &#8220;Require all granted&#8221;. Save the file and restart the apache server using the command &#8220;systemctl restart httpd.service&#8221;.

### References:

["Install Dokuwiki"](https://www.dokuwiki.org/install:fedora)