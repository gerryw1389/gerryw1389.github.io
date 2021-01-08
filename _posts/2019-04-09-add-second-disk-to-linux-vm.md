---
title: Add Second Disk To Linux VM
date: 2019-04-09T21:00:07+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/add-second-disk-to-linux-vm/
categories:
  - Linux
tags:
  - Scripting-Bash
---
<!--more-->

### Description:

Let's say you need to attach a second disk to a linux VM with LVM setup, this is how you would do it on RHEL 7

### To Resolve:

1. Attach 70 GB Disk in vsphere by going to the VM => Hardware => Add New: Disk

2. In the VM => we want to create the following file system:

   ```powershell
   /files1  60 G
   /files2  150 G 
   /files3  300 G
   /files4  60 G
   ```

   - Scan SCSI to see new DISK

   ```powershell
   echo "- - -" > /sys/class/scsi_host/host#/scan
   # OR
   echo "1" > /sys/class/scsi_disk/2:0:0:0/device/rescan
   # After scanning  you  should  see  new  disk  under  /dev/sd*
   ls /dev/sd*
   /dev/sda  /dev/sda1  /dev/sda2  /dev/sdb
   # This means that the first disk has two partitions - sda1 and sda2, but sdb is unpartitioned.
   # Likewise, you can run 'fdisk -l' to see your second disk
   ```

   - Create physical volume:

   ```powershell
   pvcreate /dev/sdb
   ```

   - Create Volume Group:

   ```powershell
   vgcreate FILES /dev/sdb
   ```

   - Next create the volumes

   ```powershell
   lvcreate -L 60G -n /dev/mapper/FILES-u01 FILES
   lvcreate -L 150G -n /dev/mapper/FILES-u02 FILES
   lvcreate -L 300G -n /dev/mapper/FILES-u03 FILES
   lvcreate -L 60G -n /dev/mapper/FILES-u04 FILES
   # lvs or lvdisplay
   ```

   - Create new file system on volumes:

   ```powershell
   mkfs.xfs /dev/mapper/FILES-u01
   mkfs.xfs /dev/mapper/FILES-u02
   mkfs.xfs /dev/mapper/FILES-u03
   mkfs.xfs /dev/mapper/FILES-u04
   ```

   - Create mountpoint:

   ```powershell
   mkdir /files1
   mkdir /files2
   mkdir /files3
   mkdir /files4
   ```

   - Mount logical volume:

   ```powershell
   mount /dev/mapper/FILES-u01 /files1
   mount /dev/mapper/FILES-u02 /files2
   mount /dev/mapper/FILES-u03 /files3
   mount /dev/mapper/FILES-u04 /files4
   # verify
   df -h /files4
   ```

   - Add to fstab for automount

   ```powershell
   cp /etc/fstab /etc/fstab.bkp
   vi /etc/fstab
   # add
   /dev/mapper/FILES-u01 /files1         xfs             defaults        0 0
   /dev/mapper/FILES-u02 /files2         xfs             defaults        0 0
   /dev/mapper/FILES-u03 /files3         xfs             defaults        0 0
   /dev/mapper/FILES-u04 /files4         xfs             defaults        0 0
   ```

1. reboot

2. After reboot, run `df -h`  you should see the filesystem!