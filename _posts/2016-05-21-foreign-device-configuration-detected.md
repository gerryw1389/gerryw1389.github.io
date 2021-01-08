---
title: Foreign Device Configuration Detected
date: 2016-05-21T04:50:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/foreign-device-configuration-detected/
categories:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

In Dell OpenManage, under the Perc Adapter => Storage Tab, there will be a warning on the physical drives saying &#8220;Foreign Device Configuration Detected&#8221;. This means either a drive was replaced with a new drive from a different RAID array or the Raid Controller information on one of the drives is corrupt.

### To Resolve:

1. For the drive giving the error, on the options drop down, select &#8220;Offline&#8221; this forces the drive offline.

2. Then select &#8220;Blink&#8221; this will help determine which drive it is by causing the LED indicator on the drive to literally &#8220;blink&#8221;.

3. Physically replace the drive if it's hot swappable, which most are.

4. When you plug in the new drive, it should start rebuilding the RAID Array automatically from the RAID Controller's instructions to the drive.

5. If it doesn't start automatically, in the options menu for the drive, select the drop down option &#8220;Assign Global HS&#8221;. This assigns the drive as a global hot spare, or a drive that is on and ready to be used when needed. This should initiate the rebuild.