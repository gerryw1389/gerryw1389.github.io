---
title: Root Password Expired
date: 2019-07-14T00:03:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/07/root-password-expired/
categories:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

I ran into an issue while trying to lock down my testlab Centos 7 VM where a bash script I ran made the root password expire! Here is how to resolve:

### To Resolve:

1. Reboot the machine.

2. Follow steps in my post about getting in to [pre-boot](https://automationadmin.com/2019/06/local-root-access/)

   ```shell
   chroot /sysroot

   # Set password to never expire (probably not best practice, but we change ours every 180 days anyways)
   chage -I -1 -m 0 -M 99999 -E -1 root

   # Go ahead and change it for now
   passwd root

   # Update SELinux Info
   touch /.autorelabel

   reboot -f
   ```

3. Now log back in locally and see if it works!
