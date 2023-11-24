---
title: Generic MDT/WDS Deployment Guide And Troubleshooting
date: 2016-05-18T04:26:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/generic-mdtwds-deployment-guide-and-troubleshooting/
tags:
  - WindowsServer
tags:
  - ComputerImaging
  - WindowsServer-Roles
---
<!--more-->

### Description:

The following guide is the generic overview of how to use WDS/MDT.

### To Resolve:

1. Don't use physical machines, use Hyper-V/VMWare for everything

2. Use PXE + WDS + MDT

3. Create a reference image first by creating a new task sequence, name it "Reference", use your vanilla OS as OS source, create a boot image, add this boot image to WDS, PXE boot a VM and boot from it. Install Windows manually, customize it accordingly, run windows update etc, and add the "big apps", like Office/Photoshop/Visual Studio. Shut it down. THEN TAKE A SNAPSHOT OF THIS VM.

4. Create a capture task sequence, add the capture boot image to WDS, PXE boot the same VM on this capture task sequence. Save the image as your reference.wim

5. Import a new OS and your reference.wim from the last step, then create yet another task sequence. This will be the "golden" task sequence. In this task sequence, add all your customizations, language setup, windows keys and what not, and also, add whatever you need of "small apps", like acrobat, java, etc. Also, remember to enable the "Post app install" and "Pre app install" Windows update steps of the task sequence. Create a boot image of this as well, add it to WDS, PXE boot a NEW VM from this boot image and see that everything is good. If it is, make sure that you've added all the drivers you need, and try PXE booting a physical machine. If you want, you can also create USB/CD media, just google "create usb media MDT" for tons of guides. It's very easy.

6. Done. Save yourself quite some time by using SSD on your VM host! Also; whenever your golden image starts to get slow (read: in 6 months, when a lot of windows updates are being installed on every deployment), just revert the snapshot you have on your reference VM, update it, TAKE A NEW SNAPSHOT, capture the image again, and overwrite the old one that you use in your "Golden" task sequence. No need to customize anything else.

7. Troubleshooting Boot Loops from Deployments:

   - Issue: Deployment fails and machine constantly reboots to Windows PE. If this happens, the deployment task has failed but left a trace of itself on the computer's hard drive causing it to repeatedly retry the same failing task.
   - To Resolve:
   - From within the Windows PE environment, press `F8` to open a command prompt
   - Type `diskpart` into the command prompt

   ```powershell
   select disk 0  
   clean  
   exit
   ```

   - Reboot the computer and restart the deployment (press `F12` to network boot)

### References:

["Retraining Myself On MDT"](https://www.reddit.com/r/sysadmin/comments/1kf5u0/retraining_myself_on_mdt/)