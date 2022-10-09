---
title: Errors Installing A Printer
date: 2016-05-21T04:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/errors-installing-a-printer/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Sometimes printers will not want to install even if you have what you think is the right driver. Here is one example. You will get an error similar to this:

  <img class="alignnone size-full wp-image-627" src="https://automationadmin.com/assets/images/uploads/2016/09/errors-installing-a-printer.jpg" alt="errors-installing-a-printer" width="383" height="437" srcset="https://automationadmin.com/assets/images/uploads/2016/09/errors-installing-a-printer.jpg 383w, https://automationadmin.com/assets/images/uploads/2016/09/errors-installing-a-printer-263x300.jpg 263w" sizes="(max-width: 383px) 100vw, 383px" />

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) regedit

2. Navigate to `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\Print Printers`.

3. Locate the "HPTrayCount" entry, most likely the value will be `0`, change it to `12`.

4. Try to install the printer again. If it doesn't work, reboot and try again.

#### For the Second Error:

1. Do the steps in: [Document Stuck in the Queue](https://automationadmin.com/2016/05/document-stuck-in-queue/)

2. Then, [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `regedit`

3. Navigate To: `HKEY_LOCAL_MACHINE\SYSTEM\System\CurrentControlSet\Control\Print\Environments\Windows NT x86`

4. Delete all sub keys except: `Drivers` and `Print Processors`. Expand out the Drivers key and delete all sub keys under `Version-x`.

5. Now navigate to: `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Print\Monitors`

6. Delete them all except: `BJ Language Monitor, Local Port, PJL Language Monitor, Standard TCP/IP Port, and USB Monitor`, these are the only ones needed.

7. Restart the print spooler service. If the service doesn't start then you have an OS issue over a printer driver issue.