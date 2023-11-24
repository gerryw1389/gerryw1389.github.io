---
title: 'Veeam Error: Change Tracking Timestamp'
date: 2016-05-24T12:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-error-change-tracking-timestamp/
tags:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Veeam will be failing on the backups with the following log event: `Failed to create change tracking time stamp for virtual disk file..`


### To Resolve:

1. After Googling the error, I found the official answer [here](http://helpcenter.veeam.com/backup/80/hyperv/changed_block_tracking.html). The page describes the issue but only offers one solution if it continues to happen:

2. Import the Veeam Module in Powershell and run `Reset-HvVmChangeTracking` on the Virtual Machine that is generating the error. This resets the change block tracking for that VM. Note that this also happens when you upgrade to a new version of Veeam as well.

### References:

["Reset-HvVmChangeTracking"](http://helpcenter.veeam.com/backup/80/powershell/reset-hvvmchangetracking.html)