---
title: Predected Drive Failure
date: 2016-05-21T04:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/predected-drive-failure/
tags:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

In Dell OpenManage, under the Storage Tab, there will be a warning on the physical drives saying &#8220;Predictive Drive Failure => Yes&#8221;. This means one of the drives in the RAID Array has failed. You may also see errors in the &#8220;Alert Log&#8221; stating &#8220;HDD(X) Fault&#8221; which changes the LED indicator on the server to turn Amber with a code that usually starts with an &#8220;E&#8221;, for example &#8220;E1810 HDD 1 Fault&#8221;.

### To Resolve:

1. For the drive giving the error, on the options drop down, select &#8220;Offline&#8221; this forces the drive offline.

2. Then select &#8220;Blink&#8221; this will help determine which drive it is by causing the LED indicator on the drive to literally &#8220;blink&#8221;.

3. Physically replace the drive if it's hot swappable, which most are.

4. When you plug in the new drive, it should start rebuilding the RAID Array automatically from the RAID Controller's instructions to the drive.

5. If it doesn't start automatically, in the options menu for the drive, select the drop down option &#8220;Assign Global HS&#8221;. This assigns the drive as a global hot spare, or a drive that is on and ready to be used when needed. This should initiate the rebuild.