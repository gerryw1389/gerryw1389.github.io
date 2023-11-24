---
title: Windows 7 Exe Fix
date: 2016-05-29T03:27:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-7-exe-fix/
tags:
  - Windows
---
<!--more-->

### Description:

If you find that you can run executable programs due to an extension being lost in Windows 7, try this fix:

### To Resolve:

1. Run => `regedit`.

2. Ensure regkey has the value: `HKEY_CLASSES_ROOT\.exe.\Default` to the Data Value `exefile`

3. Ensure regkey has the value: `HKEY_CLASSES_ROOT\exefile\Default` to the Data Value `"%1" %*`

4. Ensure regkey has the value: `HKEY_CLASSES_ROOT\exefile\shell\open\command\Default` to the Data Value `"%1" %*`

5. Close regedit and reboot the computer.

6. You can also create a .reg file with the following and import the following keys:

   ```escape
   Windows Registry Editor Version 5.00
   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts.exe]
   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts.exe]
   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts.exe\OpenWithList]
   [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts.exe\OpenWithProgids]
   "exefile"=hex(0):
   ```