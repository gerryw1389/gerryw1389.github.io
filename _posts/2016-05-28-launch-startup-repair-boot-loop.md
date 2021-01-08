---
title: Launch Startup Repair Boot Loop
date: 2016-05-28T06:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/launch-startup-repair-boot-loop/
categories:
  - Hardware
tags:
  - Pre-Boot
---
<!--more-->

### Description:

The computer will not be able to boot into Windows, it will usually keep reverting to the &#8220;Launch Startup Repair&#8221; screen. Note that actually running startup repair rarely fixes the problem.

### To Resolve:

1. Before trying anything else, see if selecting &#8220;Start Windows Normally&#8221; works, you would be surprised how often this does.

2. Shut down the computer and try tapping `F8` on starting it back up to attempt accessing safe mode. If you can get into Safe Mode, the problem is going to be a software causing problems on startup of the OS.

3. If that doesn't work, Try tapping `F12` on startup to attempt to run Hardware Diagnostics (or whichever key depending on the manufacturer). If the HDD passes it's test, this narrows it down to an OS issue => which is most common.

4. If neither of the above work, the computer will most likely need to be re-imaged or the error needs to be researched further.