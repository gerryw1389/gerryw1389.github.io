---
title: 'VRO: MySQL Driver Not Installed'
date: 2019-04-09T15:30:57+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/vro-mysql-driver-not-installed/
categories:
  - Linux
tags:
  - Orchestration
---
<!--more-->

### Description:

When trying to connect to a MySQL database in vRealize Orchestrator, you will get an error like `no suitable driver found`.  


### To Resolve:

1. First, ssh into your appliance and see the version:

   ```shell
   cat /etc/SuSE-release
   ```

2. Download your version of mysql from the links in the KB above. I chose the [platform independent version](https://dev.mysql.com/downloads/connector/j/)

   - Copy the `mysql-connector-java-x.x.x.jar` to the `/usr/lib/vco/app-server/lib` directory on the Orchestrator server.

   ```shell
   # copy from my machine to vro machine
   scp /mnt/c/scripts/mysql-connector-java-5.1.47.jar root@vra03:/root/tmp/mysql-connector-java-5.1.47.jar
   # move to correct dir
   mv /root/tmp/mysql-connector-java-5.1.47.jar /usr/lib/vco/app-server/lib/mysql-connector-java-5.1.47.jar
   # change the ownership of the mysql-connector-java-x.x.x.jar file.
   chown vco:vco mysql-connector-java-5.1.47.jar
   # change the permissions of the mysql-connector-java-5.1.47.jar.
   chmod 644 mysql-connector-java-x.x.x.jar
   # restart the Orchestrator server service.
   service vco-server restart
   ```

3. After this, I still got the same error when trying to add a mysql server, this was fixed by copying the same file to all 3 nodes! So if you have the VRA cluster setup, copy the mysql connector to all three nodes and restart the service on each. After that, I just had to make sure my SQL user I was connecting with had access rights to add a database.


### References

["MySQL DB installation in vRealize Orchestrator 7.2 fails (2148277)"](https://kb.vmware.com/s/article/2148277?lang=en_US)  


