---
title: Create A Bootable USB From CommandLine
date: 2016-08-10T03:35:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/create-a-bootable-usb-from-commandline/
categories:
  - Windows
tags:
  - Scripting-CMD
  - Pre-Boot
---
<!--more-->

### Description:

Follow these steps to create a bootable USB from Windows. Note this is similar to my post about A [Multiboot USB](https://automationadmin.com/2016/05/creating-a-multiboot-usb/), but mainly for on the fly single OS booting.

### To Resolve:

1. Insert a USB drive into the computer.

2. Open CMD Prompt as administrator, and type:

   ```escape
   diskpart  
   list disk #get your USB drive number, usually 1  
   select disk 1  
   clean  
   create part pri  
   select part pri  
   format fs=fat32 quick  
   active  
   exit
   ```

3. Now just copy and paste the system image to the root of the USB drive. It should be bootable now.