---
title: CentOS MATE to CentOS Core
date: 2017-08-26T04:50:25+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/centos-mate-to-centos-core/
tags:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

Over the last few months I've been moving my CentOS MATE VM's to CentOS core. Here is how I setup my template Core VM:

### To Resolve:

1. Used GUI installer to create the VM. Created root password and admin user.

2. At first login:

   ```shell
   yum update
   yum install net-tools
   ```

3. First tasks after updates is to set a static IP:

   ```shell
   vi /etc/sysconfig/network-scripts/enp0s3

   #set it like:

   TYPE="Ethernet"
   BOOTPROTO="none"
   DEFROUTE="yes"
   IPV4_FAILURE_FATAL="no"
   IPV6INIT="no"
   IPV6_AUTOCONF="yes"
   IPV6_DEFROUTE="yes"
   IPV6_PEERDNS="yes"
   IPV6_PEERROUTES="yes"
   IPV6_FAILURE_FATAL="no"
   IPV6_ADDR_GEN_MODE="stable-privacy"
   NAME="enp0s3"
   UUID="233f2b4b-877c-4b28-b17d-1eb091ded288"
   DEVICE="enp0s3"
   ONBOOT="yes"
   IPADDR="192.168.1.100"
   PREFIX="24"
   GATEWAY="192.168.1.1"
   DNS1="8.8.8.8"
   ```

4. Next we configure SSH:

   ```shell
   #check version
   ssh -v

   #edit the config file
   vi /etc/ssh/sshd_config

   #change the following:

   # Protocol 2,1
   Protocol 2

   # PermitRootLogin yes
   PermitRootLogin no

   #save, exit, restart the service so it will take effect
   systemctl restart sshd.service
   ```

5. Setup [firewall](https://automationadmin.com/2017/08/firewall-cmd/)