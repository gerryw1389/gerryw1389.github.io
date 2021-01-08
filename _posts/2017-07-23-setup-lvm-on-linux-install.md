---
title: Setup LVM On Linux Install
date: 2017-07-23T03:30:07+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/setup-lvm-on-linux-install/
categories:
  - Linux
tags:
  - Pre-Boot
---
<!--more-->

### Description:

Setup LVM with LUKS Multi-Disk. For this lab I used 2 127 GB vhd's using Hyper-V and Fedora 25 Gnome.

### To Resolve:

1. Launch installer via Live USB image

2. Select all your disks and choose the option to &#8220;encrypt my data&#8221; as well as &#8220;I will configure partitioning&#8221;.

   <img class="alignnone size-full wp-image-4484" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm.png" alt="" width="1144" height="602" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm.png 1144w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-300x158.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-768x404.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-1024x539.png 1024w" sizes="(max-width: 1144px) 100vw, 1144px" /> 

3. Click &#8220;done&#8221; and then enter the passphrase for your setup.

4. Now on the next screen, we configure our disks:

   NOTE: Rules

   boot partition = /boot needs to be at least 250MB.
   swap needs to be 1024 MB+ (for a 4GB VM). For best results, follow:

   |Amount of RAM in the System|Recommended Amount of Swap Space|
   |:---:|:---:|
   |4GB of RAM or less	|a minimum of 2GB of swap space|
   |4GB to 16GB of RAM	|a minimum of 4GB of swap space|
   |16GB to 64GB of RAM	|a minimum of 8GB of swap space|
   |64GB to 256GB of RAM	|a minimum of 16GB of swap space|
   |256GB to 512GB of RAM|a minimum of 32GB of swap space|

   [Source](https://docs.fedoraproject.org/en-US/Fedora/13/html/Installation_Guide/s2-diskpartrecommend-x86.html)

   - Paths reference:
   - `/home` = lvm ext4
   - `/boot/` EFI standard EFI system partition 260mb
   - `/` ext4 volumb group
   - `/swap`
   

5. Now we just create them - Create boot:

   <img class="alignnone size-full wp-image-4485" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2.png" alt="" width="1138" height="652" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2.png 1138w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2-300x172.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2-768x440.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2-1024x587.png 1024w" sizes="(max-width: 1138px) 100vw, 1138px" /> 



6. Create vg

   <img class="alignnone size-full wp-image-4486" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-3.png" alt="" width="478" height="390" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-3.png 478w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-3-300x245.png 300w" sizes="(max-width: 478px) 100vw, 478px" /> 


7. Create root

   <img class="alignnone size-full wp-image-4487" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4.png" alt="" width="1142" height="560" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4.png 1142w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4-300x147.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4-768x377.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4-1024x502.png 1024w" sizes="(max-width: 1142px) 100vw, 1142px" /> 



8. Create swap

   <img class="alignnone size-full wp-image-4489" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6.png" alt="" width="1118" height="430" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6.png 1118w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6-300x115.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6-768x295.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6-1024x394.png 1024w" sizes="(max-width: 1118px) 100vw, 1118px" /> 


9. Create home

   <img class="alignnone size-full wp-image-4490" src="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7.png" alt="" width="1132" height="588" srcset="https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7.png 1132w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7-300x156.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7-768x399.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7-1024x532.png 1024w" sizes="(max-width: 1132px) 100vw, 1132px" /> 

   And then we are done! Finish the installer.


----

### Description:

Here is how to do it from command line although I haven't actually done this. Steps to complete = Create physical volume, then volume groups, then logical volumes.

### To Resolve:

1. First we want to see our current disk setup:

   ```shell
   # Identify free disks
   lsblk
   pydf
   blkid
   fdisk -l
   ```

2. Now we create a logical volume. Note that the disk should be blank.

   ```shell
   fdisk /dev/sdb

   n - new part
   p - primary part
   1 - first part on disk
   t - change type
   8e - lvm
   p - preview
   w - write changes

   # Do same thing for each disk
   ```

3. Now we create the disk:

   ```shell
   pvcreate /dev/sdb1
   #could also do pvcreate /dev/sdb1, /dev/sdb2 …
   ```

4. Now create the Volume Group

   ```shell
   vgcreate vgpool /dev/sdb1

   # Could also do pvcreate /dev/sdb1, /dev/sdb2 …

   lvcreate -L 3G -n lvstuff vgpool

   # -L is size, -n is name, and vgpool is mentioned so that lvcreate knows where to get the space from
   ```

5. Create a filesystem

   ```shell
   mkfs -t ext3 /dev/vgpool/lvstuff - creates a file system
   ```

6. Mount it

   ```shell
   mkdir /mnt/stuff

   mount -t ext3 /dev/vgpool/lvstuff /mnt/stuff

   # Adding a new hard drive:

   vgextend vgpool /dev/sdc1

   # Tell it how much to extend by, should be 3+8 but really extends to 8.
   lvextend -L +8G /dev/vgpool/lvstuff

   # Actually expands to 11 GB instead of 8.
   # lvextend -L+3G /dev/vgpool/lvstuff

   # Now we extend our filesystem:

   resize2fs /dev/vgpool/lvstuff
   ```