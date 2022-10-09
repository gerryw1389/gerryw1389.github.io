---
title: VirtualBox Disks Tasks
date: 2017-07-23T06:09:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/virtualbox-disks-tasks/
categories:
  - Linux
  - LocalSoftware
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

So I ran into an issue the other day&#8230; I have been using the default 16 GB .vdi files that VirtualBox creates when creating VM's and noticed that I needed to expand to 50 GB. This is tough as I have like 4 production VM's and wanted to make sure I didn't lose any data. Well I ended up doing the following: Backing them up, deleting snapshots, resize the disks, un-attach the disks, rename the disks, expand the disks, re-attach, boot into GParted expand, boot into CentOS and expand the OS. Here is the steps in more detail.

### To Resolve:

1. So I read that best practice when it comes to expanding disks is to delete all the VM's snapshots. Thankfully, this is easy to do via the GUI.

2. Next, I wanted to rename the actual VDI files while I was expanding them to match their hostname. Well VirtualBox has a process for this:

   - Go into the machines settings and remove the disk. Then go into File => Virtual Media Manager and remove the disk there. Remember to keep the files!

3. Rename the .vdi files to whatever you want.

4. Open up Powershell as Admin in the disk's directory and type for each vm and disk:

   ```powershell
   cmd /c "vboxmanage modifymedium disk vm-name.vdi --resize 51200"
   ```

5. Download GParted iso and boot to that. Choose `33` for english and `0` for GUI. Select the disk and just expand all the way. Apply changes and then open Terminal and type `poweroff now`

6. Boot into your VM and type:

   ```shell
   # Determine free physical disk space (should be like 36 GB if you went from default 16 to 50 like I did)
   sudo pvs

   # PV = /dev/sda2 and get free avail space
   sudo vgdisplay

   # look for lv path, usually /dev/centos/root
   lvdisplay

   # Now just expand vg to physical
   sudo lvextend /dev/centos/root /dev/sda3

   # lastly, expand the file system
   sudo xfs_growfs /dev/centos/root
   ```

7. That's it! Open up Caja to confirm.