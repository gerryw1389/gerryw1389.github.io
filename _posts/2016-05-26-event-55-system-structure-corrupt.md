---
title: Event 55 System Structure Corrupt
date: 2016-05-26T04:15:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/event-55-system-structure-corrupt/
tags:
  - Windows
tags:
  - Monitoring
---
<!--more-->

### Description:

Windows 7 system logs started recording event ID 55 (NTFS) => The system structure on the disk is corrupt and unusable. Please run the chkdsk utility on the volume DeviceHarddiskVolume2.

  <img class="alignnone size-full wp-image-650" src="https://automationadmin.com/assets/images/uploads/2016/09/event-55-corrupt.png" alt="event-55-corrupt" width="499" height="183" srcset="https://automationadmin.com/assets/images/uploads/2016/09/event-55-corrupt.png 499w, https://automationadmin.com/assets/images/uploads/2016/09/event-55-corrupt-300x110.png 300w" sizes="(max-width: 499px) 100vw, 499px" />


### To Resolve:

1. Download `WinObj` utility from Windows Sysinternals or if you use [WSCC](http://www.kls-soft.com/wscc/) like me then just use it.

2. Launch `Winobj.exe` and go to GLOBAL section.

3. Sort entries by SimLink, find a device corresponding to the one in your syslog error and check name column for drive letters.

4. If it is the system drive (C: in most cases), then you will need to schedule CHKDSK to run on next startup. From elevated command prompt, run `chkdsk /f c:` and then type `y` to schedule on the next restart.