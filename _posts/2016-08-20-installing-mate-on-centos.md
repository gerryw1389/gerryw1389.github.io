---
title: Installing MATE On CentOS
date: 2016-08-20T04:32:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/installing-mate-on-centos/
categories:
  - Linux
tags:
  - LinuxServer
  - Setup
---
<!--more-->

### Description:

I'm a big fan of the MATE desktop for my Linux distro's. As such, I found a neat guide on how to install it in CentOS v7.

### To Resolve:

1. During the install, just choose minimal install. Accept license, and then do your standard &#8220;sudo yum update&#8221; before moving to the next step.

2. Now, install the EPEL-repositories

   ```shell
   yum install epel-release
   ```

3. Then install the X Window System

   ```shell
   yum groupinstall "X Window system"
   ```

4. Install the MATE packages. This will take a few minutes.

   ```shell
   yum groupinstall "MATE Desktop"
   ```

5. Tell your system to start the Graphical Interface

   ```shell
   systemctl isolate graphical.target
   ```

6. To have MATE boot up as the default desktop environment, enter the following command

   ```shell
   systemctl set-default graphical.target
   ```

   - NOTE: You will most likely want the Gnome Disk Utility as it the easiest way to interface with your disks. Once installed it can be found in: Applications => Accessories => Disks

   - Do this by running:

   ```shell
   yum install gnome-disk-utility
   ```

### References:

[http://www.45drives.com/wiki/index.php/Installing\_MATE\_on\_CentOS\_7](http://www.45drives.com/wiki/index.php/Installing_MATE_on_CentOS_7)