---
title: Local Root Access
date: 2019-06-12T23:35:19-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/local-root-access/
categories:
  - Linux
tags:
  - Pre-Boot
---
<!--more-->

### Description:

I've had a couple instances where I went to `sudo su` and it would say I'm not in the sudoers.

### To Resolve:

1. logout

2. login as root

3. type: `usermod -a -G wheel (username)`

4. Then `exit` and log back in as your user.

5. If you can't login as root:   

   - Reboot. You'll be given 5 seconds at the boot menu to select the operating system kernel to boot into. 
   - At the boot menu, press `e` to edit the existing kernel (Core).
   - In the boot grub menu select option to edit. Select Option to `edit (e)`
   - Go to the line of `Linux 16` and change `ro` with `rw init=/sysroot/bin/sh`
   - Now press Control+x to start on single user mode.
   - Now access the system with this command - `chroot /sysroot`
   - Reset the password - `passwd root`
   - Update selinux information - `touch /.autorelabel`
   - Exit chroot - `exit`
   - Reboot your system - `reboot`
   - Now do steps above to give another user sudo rights as it's best practice to not use root directly for anything except for tasks like these. 