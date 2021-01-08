---
title: Computer Only Works In Safe Mode
date: 2016-05-28T06:21:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/computer-only-works-in-safe-mode/
categories:
  - Hardware
tags:
  - Pre-Boot
---
<!--more-->

### Description:

If you get a computer that will go into Safe Mode, but will just hang in a regular boot or not load in some way, your OS most likely not the issue.

### To Resolve:

1. Once in Safe Mode, try to doing a clean boot. See &#8220;[How To Do A Clean Boot](https://automationadmin.com/2016/05/how-to-do-a-clean-boot/)&#8221; for more info. Some Antivirus software can cause this issue. Try uninstalling it just for troubleshooting and re-install once the computer is back up.

2. If that fails, look for possible Hardware issues. In Safe Mode, check the Event Viewer. I once had 2 out of 5 disks failed on a RAID array that was causing this. Also look at the graphics driver to make sure it matches the video card.

3. If the computer manufacturer has a built-in Diagnostics, run it. For example, Dell computers can run `F12` on start up to run a 5 min diagnostic test.