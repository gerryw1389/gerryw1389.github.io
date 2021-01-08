---
title: Windows Unresponsive
date: 2016-05-26T22:38:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-unresponsive/
categories:
  - Windows
---
<!--more-->

### Description:

All computers become unresponsive at times, use these steps if it's been more than 10 minutes and the session is just frozen.


### To Resolve:

1. Crash the computer if you cannot get it to become responsive. Hold down the power button for 8-10 seconds to do this.

1. Try to bring the computer up in Safe Mode or Safe Mode with Networking. This is usually done by tapping `F8` on startup.

1. Once inside Windows, the first thing you want to check is the Event Viewer. Run => `eventvwr.msc`. In there you want to look at the log files to see if you have a HDD issue which would show up as `Iastor` or `Disk- Warning` errors.

1. Check the Device Manager (Run => `devmgmt.msc`) and see if there is any devices with warnings or errors on them. These should always be addressed first.

2. Assuming your hardware is good, start looking at third party programs being the culprit. One thing you can try is doing a clean boot, see [How To Do A Clean Boot](https://automationadmin.com/2016/05/how-to-do-a-clean-boot/) for how to do this.

3. If this doesn't work, your Windows may be corrupt or you have a possible virus infection. Make double sure by running programs like CCleaner and removing any unneeded programs and cleaning up the registry. Run virus scans as well, it's common for them to bog down a system by bloating out temp files in the system with no other symptoms of an infection.