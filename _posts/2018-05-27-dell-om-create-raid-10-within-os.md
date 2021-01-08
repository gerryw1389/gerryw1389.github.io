---
title: 'Dell OM: Create Raid 10 Within OS'
date: 2018-05-27T03:28:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/dell-om-create-raid-10-within-os/
categories:
  - LocalSoftware
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

So I wanted to create a RAID 10 array on one of our test lab servers and found that you can do this from within the OS instead of doing it pre-boot in the RAID config screen. As a matter of fact, you can do it all within Open Manage.  


### To Resolve:

1. So my setup is this: 6 drives, first two are RAID 1 with Windows Server installed and the other four will go into my new RAID 10. The first thing to do is make sure they are in a "Ready" state instead of "Online". Ready means they are plugged in but do not belong to an array, this is what we want. So the first step is to delete the current RAID Virtual Disk (the data one, not the OS one!) and wait for them to show to be "ready".

2. I'm not sure at what point I had to do this, but if you have the option to "clear", do it. This will wipe any RAID config information on the disks and most likely the data too, but I didn't care as it was blank.

3. Next, just "Unassign Global Hotspare" to each of the four disks. This ensures that we have four disks to be added to the new RAID array that we are going to build.

4. Lastly, just go through the GUI to configure your four disks in a RAID 10 setup. If it doesn't give you the option, just make sure you clear any that you can and make sure there are no hotspares (unless you have 5 disks and can afford an extra, RAID 10 goes in even numbers!) and you should be good to go.