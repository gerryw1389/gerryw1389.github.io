---
title: Backup Drives Not Detected
date: 2016-05-18T04:55:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/backup-drives-not-detected/
categories:
  - Hardware
---
<!--more-->

### Description:

When you plug in the backup drive, it will not show up in My Computer (Win+E) or Disk Management (`diskmgmt.msc`). 3 possible causes: The drive is bad, the cable going from the drive to the computer is bad, or the USB ports are not recognizing the drive.

### To Resolve:

1. Check in My Computer for the drive, `diskmgmt.msc` for the disk (Usually Disk 1 as Disk 0 is usually the OS drive), and `eventvwr.msc` for "DISK-Error" messages for the drive letter according to `diskmgmt.msc`. Any of these will be a sure sign of a failed drive.

2. Reseat the cable on both ends, see if the drive lights up when plugged in. This could rule out the cable and the drive at first glance.

3. Run => `devmgmt.msc` and look for the drive to show up under USB Devices. See if there is a WD SES Driver installed if you already have the WD Drivers installed, it will show up here.

4. Uninstall all the "USB Root Hubs" and scan for H/W changes to re-install. In some cases, you will have to reboot for it to take effect.

5. Check to see how long it has been since the computer has rebooted. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `systeminfo| Find "Time"` (or) `net statistics workstation`. Reboot if it's been over a month.

6. If it still doesn't show up, plug the drive into another computer that you know the USB ports work. If it works on another computer, see Read/ Write Errors On An External.

### To Initialize A Disk in `diskmgmt.msc`:

1. Go to `diskmgmt.msc` and see if the drive is readable.

2. If the drive shows up, see if it says to "initialize" by right clicking on it.

3. If so, set it to "convert to MBR".

4. After that it will show up as "unallocated".

5. Right click on the unallocated part and select "create a partition".

6. Create a drive letter and name for the drive and make the partition the whole drive.

7. Check My Computer, the drive should be there now, Done.