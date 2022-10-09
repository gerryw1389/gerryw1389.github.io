---
title: Disable SELinux In CentOS 7
date: 2016-11-15T05:18:38+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/disable-selinux-in-centos-7/
categories:
  - Linux
  - Security
tags:
  - LinuxServer
---
<!--more-->

### Description:

During troubleshooting or if you are not security conscience, you may want to disable SELinux in CentOS. Note that SELinux serves a similar purpose as UAC on Windows so disabling is highly frowned upon in the community.

NOTE: I have had to do this because it was stopping me from making changes to my WordPress site and adding exceptions didn't even seem to phase it. I'm sure it's my lack of knowledge, so I did this a couple times. I currently have re-enabled it and having it running on all my Linux VM's, this is just a temp solution.

### To Resolve:

1. Type:

   ```shell
   sudo vim /etc/selinux/config

   # Set it from:
   SELINUX=enforcing 

   # To 
   SELINUX=disabled

   # Reboot

   # After reboot, run 
   getenforce

   # Ensure it comes back with:
   disabled
   ```