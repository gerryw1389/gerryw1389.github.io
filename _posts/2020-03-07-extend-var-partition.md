---
title: Extend Var Partition
date: 2020-03-07T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/03/extend-var-partition
tags:
  - Linux
tags:
  - Bash
---
<!--more-->

### Description:

In this post I will expand a RHEL 8 filesystems `/var` and `/opt` directories by using an attached 80 GB disk. In the past I only knew how to create new directories with disks so this allowed me to learn how to expand existing file systems. Tested on a RHEL 8 box in Azure (default Marketplace image).

### To Resolve:

1. This does not cause downtime and can most likely be scripted - Extend `/var` by 55GB and `/opt` by 20GB:

   ```shell
   # Step 1: Find disk
   lsblk
   # look for:
   sdc                 8:32   0   80G  0 disk
   
   # Step 2: Format disk
   fdisk /dev/sdc
     - new partition = 'n'
     - make primary = 'p'
     - partition number = '1'
     - First cylinder (1-2610, default 1): "enter"
     - Last cylinder, +cylinders or +size{K,M,G} (1-2610, default 2610): "enter"
     - Change Partitions: Command (m for help): 't'
     - Hex code (type L to list codes): '8e'
     - Write the table to disk and exit = 'w'
   
   # now you will be able to see that /dev/sdc1 is listed, this is the new partition created on our newly added /dev/sdc disk and it is currently using all 80gb of space.
   
   # Step 3: Create it as a physical disk
   fdisk -l
   pvcreate /dev/sdc1
   # Physical volume "/dev/sdc1" successfully created.
   
   # Step 4: Add to volume group
   vgdisplay
   # --- Volume group ---
   # VG Name               rootvg
   # VG Size               <31.00 GiB
   vgextend rootvg /dev/sdc1
   
   # pvscan
   
   # Step 5: Add to logical volume within the volume group 
   # lvdisplay
   # --- Logical volume ---
   # LV Path                /dev/rootvg/varlv
   # LV Size                8.00 GiB
   
   lvextend -L+55G /dev/rootvg/varlv
   lvextend -L+20G /dev/rootvg/optlv
   
   
   # Step 6: Lastly, expand the file system 
   resize2fs /dev/rootvg/varlv
   resize2fs /dev/rootvg/optlv
   
   ```


