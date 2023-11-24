---
title: Event 51 Disk-Warning
date: 2016-05-26T04:13:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/event-51-disk-warning/
tags:
  - Windows
tags:
  - Monitoring
---
<!--more-->

### Description:

The error will say `An error was detected on device DeviceHarddisk0D during a paging operation` or something similar. This error typically means the HDD is starting to fail. Microsoft says An event ID 51 entry is a generic error entry for any type of error that occurs when Windows is paging information to input/output (I/O). A paging operation occurs when Windows either swaps a page of memory from memory to disk, or when Windows retrieves a page of memory from disk to memory.

### To Resolve:

1. Run `diskmgmt.msc` to determine which disk it was referring to. Be aware that most OS's load on disk `0` so `1` is usually an external.

2. If the drive is the OS drive, do the ScanDisk option from the Drive's properties in Windows Explorer and the Tools tab.

3. If it's an external, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `wmic diskdrive get status`

  <img class="alignnone size-full wp-image-644" src="https://automationadmin.com/assets/images/uploads/2016/09/disk-warning.png" alt="disk-warning" width="726" height="347" srcset="https://automationadmin.com/assets/images/uploads/2016/09/disk-warning.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/disk-warning-300x143.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

4. This only checks the SMART status, you should run a chkdsk just to be sure. To do this:

   - [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: [drive letter] => [Enter] => `chkdsk /x`
   - This is just telling Windows to run `chkdsk` from the drive's path instead of your local OS drive's. Alternatively, you can run `cd [driveletter]` and then do the `chkdsk`.

5. If it starts repairing a bunch of files, I recommend running the Western Digital Lifegaurd Diagnostics tool at this point.

6. Even this won't fix it most of the time, you should call the manufacturer to get it replaced. 
   - If it's an external => make sure you have used their tool first
   - If it's an internal => make sure you have ran the on-board diagnostics (`F12` on startup) so you can present an error code to their tech support for an RMA if the computer's drive is still under warranty.