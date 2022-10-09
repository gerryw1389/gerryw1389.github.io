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

   - ![setup-lvm](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm.png){:class="img-responsive"}

3. Click &#8220;done&#8221; and then enter the passphrase for your setup.

4. Now on the next screen, we configure our disks:

   - Rules

   - boot partition = /boot needs to be at least 250MB.
   - swap needs to be 1024 MB+ (for a 4GB VM). For best results, follow:

   |Amount of RAM in the System|Recommended Amount of Swap Space|
   |:---:|:---:|
   |4GB of RAM or less|a minimum of 2GB of swap space|
   |4GB to 16GB of RAM|a minimum of 4GB of swap space|
   |16GB to 64GB of RAM|a minimum of 8GB of swap space|
   |64GB to 256GB of RAM|a minimum of 16GB of swap space|
   |256GB to 512GB of RAM|a minimum of 32GB of swap space|

   [Source](https://docs.fedoraproject.org/en-US/Fedora/13/html/Installation_Guide/s2-diskpartrecommend-x86.html)

   - Paths reference:
   - `/home` = lvm ext4
   - `/boot/` EFI standard EFI system partition 260mb
   - `/` ext4 volumb group
   - `/swap`

5. Now we just create them - Create boot:

   - ![setup-lvm-2](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-2.png){:class="img-responsive"}

6. Create vg
   - ![setup-lvm-3](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-3.png){:class="img-responsive"}

7. Create root
   - ![setup-lvm-4](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-4.png){:class="img-responsive"}

8. Create swap
   - ![setup-lvm-6](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-6.png){:class="img-responsive"}

9. Create home
   - ![setup-lvm-7](https://automationadmin.com/assets/images/uploads/2017/07/setup-lvm-7.png){:class="img-responsive"}

   - And then we are done! Finish the installer.

### Command Line Method:

Here is how to do it from command line although I haven't actually done this. Steps to complete = Create physical volume, then volume groups, then logical volumes.

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
