---
title: 'GFI: Drive Space Failing'
date: 2016-05-23T12:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-drive-space-failing/
tags:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

Drive Space Consumption check will fail on the GFI Agent dashboard. This means one of the monitored drives has less than 25% remaining if the check is still at its defaults.

### To Resolve:

1. Navigate to the drive or drives and run CCleaner and TFC (Temp File Cleaner). When running CCleaner, make sure to delete older System Restore points.

2. Push over &#8220;SpaceMonger&#8221; or &#8220;WizTree&#8221; and see what's taking up the most space for the drive.

3. Check to see if it's old backups, as this is usually the case. Advise the customer to backup to another drive or NAS and delete them off the computer.

4. Sometimes it can be the `hiberfil.sys` file and the `pagefile.sys` that will take up space.

   - To fix the hiberfil.sys file: [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `powercfg.cpl -h off`
   - To fix the pagefile.sys: Advanced system properties => advanced => performance => advanced => Virtual Memory. Change to 2048MB or something like that.

5. You can setup an &#8220;Automated Task&#8221; in the Dashboard to run TempFileCleaner or TFC at a specific time.

6. If you have done all you can, advise the customer to upgrade their hardware to match their needs.