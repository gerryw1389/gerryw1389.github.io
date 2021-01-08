---
title: Setting A Static IP In CentOS
date: 2016-10-09T15:25:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/setting-a-static-ip-in-centos/
categories:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

Follow these steps to set a static IP in CentOS using the command line instead of GUI.

### To Resolve:

1. Get your NIC name that you want to configure, in my case `eth0`

2. Open a terminal, type:

   ```shell
   sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0

   # Set the following depending on what you want
   DEVICE="eth0"
   NM_CONTROLLED="yes"
   ONBOOT=yes
   HWADDR=A4:BA:DB:37:F1:04
   TYPE=Ethernet
   BOOTPROTO=static
   NAME="System eth0"
   UUID=5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03
   IPADDR=192.168.1.44
   NETMASK=255.255.255.0
   ```

3. Configure the Default Gateway => Open a terminal, type:

   ```shell
   sudo vi /etc/sysconfig/network

   # Set the following depending on what you want
   NETWORKING=yes
   HOSTNAME=centos7
   GATEWAY=192.168.1.1
   ```

4. Restart Network Interface => Open a terminal, type:

   ```shell
   sudo systemctl restart network
   # RHEL 8 is
   sudo systemctl restart NetworkManager
   ```

5. Configure DNS Server => Open a terminal, type:

   ```shell
   sudo vi /etc/resolv.conf

   # Set the following depending on your environment. Primary and Secondary DNS.
   nameserver 8.8.8.8
   nameserver 192.168.1.1
   ```

6. (optional) If you want to change your hostname => Open a terminal, type:

   ```shell
   sudo hostnamectl set-hostname MyServer01
   ```