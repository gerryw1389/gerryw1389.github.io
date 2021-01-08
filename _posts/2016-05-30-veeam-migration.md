---
title: Veeam Migration
date: 2016-05-30T05:05:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-migration/
categories:
  - WindowsServer
tags:
  - Migration
  - Backup
---
<!--more-->

### Description:

Veeam is our current backup of choice. The product specializes in virtual machines which our environment is most comprised of. We initially installed the application on one of our physical hosts, and later needed to move it to it's own VM for better management. Veeam has a great KB on this here which I recommend you follow instead of my guide which is really just notes for me.

### To Resolve:

1. On the old Veeam server:

   - Stop and disable all jobs.
   - Perform configuration backup by clicking File => Configuration Backup => Backup Now.

2. On the new Veeam server:

   - Install Veeam Backup & Replication, point to license file (downloaded from Veeam login under licenses), and create with a brand new DB.
   - Apply the latest patch to Veeam Backup & Replication: [http://www.veeam.com/patches.html](https://www.veeam.com/updates.html)
   - Make sure all local drives that were being used as repositories on the old server are now attached with the same drive letters on the new server. This part was a little tricky for us since we had two USB 3.0 externals as repositories. What I had to do was:  
     - Physically moved the drive from the old server to the new one.  
     - Run => `diskmgmt.msc`. Right click the drive and &#8220;remove&#8221; the letter associated with it.  
     - After that, right click the disk and choose the option to &#8220;Offline&#8221; it.  
     - Open up HyperV Manager => Right click the Veeam VM => Add Disk => Point to the un-initialized disk.  
     - Went into Veeam VM, run => `diskmgmt.msc` => Onlined the disks using the same drive letters and disk names as the old server.
   - Perform configuration backup restore. Note: It will be necessary to re-enter the password for every account during restore of non-encrypted configuration backups.  
   - TLDR: File => Config Backup => Restore => Migration => OK => Finish. Re-enter all credentials.
   - Run a test job to make sure everything moved correctly.