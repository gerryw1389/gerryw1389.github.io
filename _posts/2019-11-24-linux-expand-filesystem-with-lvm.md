---
title: 'Linux Expand FileSystem With LVM'
date: 2019-11-24T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/11/linux-expand-filesystem-with-lvm/
tags:
  - Linux
tags:
  - Bash
---
<!--more-->

### Description:

Similar to [Adding a second disk](https://automationadmin.com/2019/04/add-second-disk-to-linux-vm/), this post will be to expand a specific partition on a linux OS (RHEL 7) with LVM.

1. Attach a new disk (100GB) in vCenter

2. Get the device name in RHEL:

   ```shell
   cd /sys/class/scsi_disk
   ls
   # match the isci device in vCenter to the new device here and then type:
   echo "1" > 0:0:2:0/device/rescan
   # now 
   fdisk -l
   # for me, this is /dev/sdc
   ```

3. Get the name of of the virtual group you want to extend by typing `vgdisplay` and copying its name (/dev/MyVG/u02). Then to add the new disk:

   ```shell
   # create physical partition
   pvcreate /dev/sdc
   # extend virtual group to include new disk
   vgextend MyVG /dev/sdc
   # add it to the LVM volume group. Subtract 10% for overhead 
   lvextend -L +90G /dev/MyVG/u02
   # Extend volume 
   xfs_growfs /dev/MyVG/u02
   ```

