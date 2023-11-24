---
title: Preboot Raid Issues
date: 2016-05-21T05:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/preboot-raid-issues/
tags:
  - Hardware
  - WindowsServer
---
<!--more-->

### Description:

So at my job today, we were moving server's from one rack to another and one of our servers (see below) decided it wouldn't detect the second RAID array. It showed up as having two RAID 5's with exactly the same size. This may be a lack of knowledge on my part, but we could not get the server to boot into Windows, and we were worried we would have to delete and rebuild the array.

DeltaServer => R710 Rack Server  
8 Bay SSD Storage => Raid 5 Array

### To Resolve:

1. The fix is almost too easy it's embarrassing! Turn off the storage array and boot the server into the OS using it's internal RAID.

2. Once in Windows, turn on the storage RAID. This of course did not work either, the RAID never showed up in Windows. To fix, we simply rebooted the server again!