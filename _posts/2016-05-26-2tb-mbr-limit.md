---
title: 2TB MBR Limit
date: 2016-05-26T04:18:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/2tb-mbr-limit/
tags:
  - Hardware
---
<!--more-->

### Description:

After setting up a RAID 10 setup on one of our servers, I noticed that 750 GB of space was essentially being wasted. I then tried to expand this space and got the &#8220;Only the first 2TB are usable&#8221; error. A quick search yielded these results, not good for me.

  <img class="alignnone wp-image-633 size-full" src="https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr.png" alt="2tb-mbr" width="1734" height="214" srcset="https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr.png 1734w, https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-300x37.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-768x95.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-1024x126.png 1024w" sizes="(max-width: 1734px) 100vw, 1734px" />


  <img class="alignnone size-full wp-image-634" src="https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-2.png" alt="2tb-mbr-2" width="473" height="167" srcset="https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-2.png 473w, https://automationadmin.com/assets/images/uploads/2016/09/2tb-mbr-2-300x106.png 300w" sizes="(max-width: 473px) 100vw, 473px" />

### To Resolve:

1. If you have a server with 6 drives, you should probably enter the RAID Config during preboot (usually Ctrl+R) and partition the disk so that 2 of them will be the OS partion (maybe RAID 1) and the other 4 belong in a RAID. We did RAID 10 with 2 sets of mirroring disks although a RAID 5 or 6 would probably be better on resources.

2. From what I have found, the only way to use more than 2TB in Windows is to convert a disk to GPT. If this is going to the be OS disk, you will need to make sure you have UEFI BIOS and enable it to boot to GPT disks, see here.

### References:

["Everything You Need to Know About 3TB Hard Drives"](http://www.pcworld.com/article/235088/everything-you-need-to-know-about-3tb-hard-drives.html)