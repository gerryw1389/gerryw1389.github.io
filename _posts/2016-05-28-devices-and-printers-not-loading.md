---
title: Devices And Printers Not Loading
date: 2016-05-28T06:34:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/devices-and-printers-not-loading/
tags:
  - Windows
tags:
  - Scripting-CMD
  - Printing
---
<!--more-->

### Description:

When you run &#8220;control printers&#8221; the loading bar in Explorer will take a long time, and the Window will be blank indefinitely. This is almost always caused when Windows has an incorrect driver loaded for a printer.

### To Resolve:

1. Run => cmd- net stop spooler (This stops the printer spooler service)

2. Go to C:\windows\system32\spool\PRINTERS and C:\Windows\System32\spool\DRIVERS and delete any files there.

3. Run => cmd- net start spooler (This starts the printer spooler service)

4. Install only printers that you know the driver is correct for, remove any older printers if not in use.

5. Batch File - Make a batch file from this:

   ```powershell
   net stop spooler
   del %systemroot%\system32\spool\printers\*.shd
   del %systemroot%\system32\spool\printers\*.spl
   net start spooler
   ```