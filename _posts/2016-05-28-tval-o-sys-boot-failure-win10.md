---
title: TVAL-O.SYS Boot Failure Win10
date: 2016-05-28T06:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/tval-o-sys-boot-failure-win10/
categories:
  - Hardware
tags:
  - Pre-Boot
---
<!--more-->

### Description:

So I did an upgrade the other day with a computer that was running Windows 8 and wanted to upgrade to Windows 10 Home edition. The computer was a Toshiba Laptop and did the upgrade fine. I removed a couple programs and went to reboot, only to be greated with the following error located at `C:\Windows\System32\Logs\SRTsrttail.log`: Boot critical file `d:\windows\system32\drivers\tval_o.sys` is corrupt.

### To Resolve:

1. Run => `devmgmt.msc` => are they all loaded? Check for problem drivers.

2. If you have already rebooted and cannot get in the OS, just read this guide (in references) or just follow my sub steps:

   - Press `F8` or hold down `SHIFT` during boot to try and access the Troubleshoot option.
   - From here choose Advanced Options => Startup Settings => Restart. Upon boot, choose option `7` (Disable Driver Signing enforcement)

3. Well that was fun and all, but you have to do that EVERY boot. We need to fix the problem long term, try entering Admin CMD and entering:

   ```escape
   bcdedit.exe -set loadoptions DISABLE_INTEGRITY_CHECKS  
   bcdedit.exe -set TESTSIGNING ON
   ```

4. Go ahead and reboot to test it out. Did you get the error preventing Windows from booting?

### References:

["Top 2 Ways to Disable Driver Signature Enforcement on Windows 10/8.1/8/7/XP/Vista"](http://www.drivethelife.com/windows-drivers/how-to-disable-driver-signature-enforcement-on-windows-10-8-7-xp-vista.html)