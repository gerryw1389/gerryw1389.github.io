---
title: VirtualBox Expand VMDK
date: 2019-09-02T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/virtualbox-expand-vmdk/
categories:
  - LocalSoftware
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:
Not sure where or how I got a VMDK file as a VM, because I usually use VDI's, but for some reason I had one. Follow this post to expand its disk by converting it to VDI and then expanding it.

### Description:

1. In Virtualbox, shutdown the VM and remove the disk from Virtual Media Manager and the VM.
   
2. Create a batch file and place as many disk and stuff that you want to convert:

   ```powershell
   echo "converting to vdi"
   VBoxManage clonehd --format VDI Z:\virtualbox\yourdisk.vmdk Z:\virtualbox\yourdisk.vdi
   echo "resizing vdi"
   VBoxManage modifyhd Z:\virtualbox\yourdisk.vdi --resize 120000
   ```

3. In Virtualbox, re-attach the new disk. Not sure if this will screw with Windows Activation since I believe my example was a linux VM. 