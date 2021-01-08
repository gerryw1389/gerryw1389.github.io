---
title: Virus Dumping Files
date: 2016-05-28T07:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/virus-dumping-files/
categories:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

If you have a virus that is actively dumping files, try this to delete the temp files and isolate the service that is dumping them.

### To Resolve:

1. Find out where the files are being dumped into. Run &#8220;Folder Size Viewer&#8221; tools like &#8220;Windirstat&#8221; to find bloated directories.

2. If you can, try and determine which process is dumping the files and kill it. Many times they take over the `svchost` service, try these steps to determine the service running the instance:

   - Run => cmd => `tasklist /svc /fi "imagename eq svchost.exe"`
   - Match the PID by the one listed in &#8220;Process Explorer&#8221; or &#8220;Task Manager&#8221;.
   - You can further troubleshoot by picking a likely candidate and run the following from an elevated CMD window: `sc config Dcomlaunch type=own` (where Dcomlaunch is the name of the service.)
   - Reboot the computer.
   - After running virus tools, run this command to revert changes: `sc config Dcomlaunch type= share` (where Dcomlaunch is the name of the problematic service.)

3. Now use the Command Prompt to clean up the directory: 
   - For a single directory: Run => cmd => `cd c:\some\path` => `del /f /q /s *.* > nul`
   - For a recursive cleanup: Run => cmd => 

   ```console
   mkdir c:\empty
   robocopy c:\emptyfolder c:\deletefolder /purge
   rmdir c:\deletefolder
   rmdir c:\empty
   ```

   - What the task above does is uses Robocopy to overwrite a destination folder with a blank source folder which will overwrite all files and folders in `c:\deletefolder` without confirmations. When done, you have two blank folders which it then deletes.

4. Launch multiple virus scanners at the same time to scan for infections.