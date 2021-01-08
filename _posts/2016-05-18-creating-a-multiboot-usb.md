---
title: Creating A MultiBoot USB
date: 2016-05-18T04:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/creating-a-multiboot-usb/
categories:
  - Hardware
tags:
  - Pre-Boot
  - Setup
---
<!--more-->

### Description:

Creating a multi-boot USB is a task that most administrators will have to do at one point or another. I used to just keep setup files on my USB, but with the advance in storage capabilities I now host entire OS's on my USB along with setup files.

### To Resolve:

1. Download and install [Xboot](http://www.pendrivelinux.com/xboot-multiboot-iso-usb-creator/).

2. Download the tools you want to add from the internet. Make sure they are in .iso format. I recommend:

   - [Hirens Boot CD](http://www.hirensbootcd.org/download/) = A multitool for many pre-boot tasks.

   - [Tails OS](https://tails.boum.org/install/) = A secure Linux distro that I prefer to use for one-time boot operations.

   - [Paragon Backup Recovery](https://www.paragon-software.com/home/br-free/) = I use Paragon backup to image my drives, this is the .iso you will need to boot into to recover the most recent backup.

3. Once you are done adding the .iso files to the list, you can either choose to make a merged .iso file to burn later or choose the option to 'Create Multi-boot USB'

4. After it is done you are done. If you want to test you can use the QEMU emulator or just try it out. I highly recommend this method as I have been using it for years.

   NOTE: Just came across [easy2boot](http://www.easy2boot.com/), might be a better alternative!
   {: .notice--success}

### Steps:

1. Extract the E2B download to a new folder called "E2B" (any name will do). I recommend you temporarily turn off anti-virus protection for the next step.

2. Run the `MAKE\_E2B\_USB_DRIVE (run as admin).cmd` script (NTFS is recommended choice when prompted) the USB drive must have a drive letter assigned by Windows (C: to Z:)

3. Copy all your payload files (ISOs, etc.) into the correct sub-folders under `\_ISO` (e.g. \_ISO\MAINMENU) of the USB drive.

4. Run `\MAKE\_THIS\_DRIVE_CONTIGUOUS.cmd` from the USB drive.

5. Read more [here at "Make an Easy2Boot USB drive"](http://www.easy2boot.com/make-an-easy2boot-usb-drive/)
