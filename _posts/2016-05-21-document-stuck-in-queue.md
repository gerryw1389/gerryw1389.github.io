---
title: Document Stuck In Queue
date: 2016-05-21T04:34:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/document-stuck-in-queue/
tags:
  - Windows
tags:
  - Scripting-CMD
  - Printing
---
<!--more-->

### Description:

You print a document on an installed printer and it gets stuck in the print queue. In addition, you can't delete the job or get rid of it at all.

### To Resolve:

1. Run => cmd- `net stop spooler` (This stops the printer spooler service)

2. Go to `C:\windows\system32\spool\PRINTERS` and `C:\Windows\System32\spool\DRIVERS` and delete any files there.

3. Run => cmd- `net start spooler` (This starts the printer spooler service)

4. If the printer is attached as a shared out printer, go on that computer and do the same steps.

5. If the above doesn't work, you have to look at Windows being corrupt, try these:

   - Replace the `C:\Windows\system32\spoolsv.exe` file with a fresh copy. I recommend running the [Windows Repair Tool](http://www.majorgeeks.com/files/details/tweaking_com_windows_repair.html) and rebooting.

   - [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `sfc/ scannow` (This scans the OS files and determines if Windows is corrupt, it doesn't always fix the issue. A reinstall or re-image may have to be done).

6. You could also copy and paste the following into a batch file for later use:

   ```powershell
   net stop spooler
   del %systemroot%\system32\spool\printers\*.shd
   del %systemroot%\system32\spool\printers\*.spl
   net start spooler
   ```