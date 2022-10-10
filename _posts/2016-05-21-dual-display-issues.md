---
title: Dual Display Issues
date: 2016-05-21T05:29:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/dual-display-issues/
categories:
  - Hardware
---
<!--more-->

### Description:

Your second monitor will not be detected or you won't be able to navigate to the second monitor. Always check the cabling prior to troubleshooting hardware issues.

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) => `desk.cpl` and make sure both displays are connected and showing up in Windows.

2. Take note of the orientation of the monitors => If on extended mode, Windows will allow you to drag Windows to the second screen according to this orientation. If the monitor is physically on the left and is the second monitor, you need to put them in that order (2,1).

3. Make sure the appropriate display adapter driver is installed. Some video cards can't do dual displays.

4. Make sure the appropriate monitor drivers are installed if the second monitor is not showing up. Most monitors are PnP so if it's not showing up, you most likely have a cabling issue.