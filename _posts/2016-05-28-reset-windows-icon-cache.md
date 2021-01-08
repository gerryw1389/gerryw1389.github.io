---
title: Reset Windows Icon Cache
date: 2016-05-28T06:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/reset-windows-icon-cache/
categories:
  - Windows
tags:
  - Tweaks
  - Scripting-CMD
---
<!--more-->

### Description:

You will have &#8220;broken&#8221; icons on your desktop. A simple right click to the target location shows that files are there but they still look corrupted. Follow these steps to fix:

  <img class="alignnone size-full wp-image-690" src="https://automationadmin.com/assets/images/uploads/2016/09/reset-icon-cache.png" alt="reset-icon-cache" width="658" height="300" srcset="https://automationadmin.com/assets/images/uploads/2016/09/reset-icon-cache.png 658w, https://automationadmin.com/assets/images/uploads/2016/09/reset-icon-cache-300x137.png 300w" sizes="(max-width: 658px) 100vw, 658px" />

### To Resolve:

1. In the command prompt, Copy and paste each command line below exactly as is one at a time and press enter after each command.

   ```powershell
   ie4uinit.exe -ClearIconCache
   taskkill /IM explorer.exe /F
   DEL "%localappdata%\IconCache.db" /A
   shutdown /r /f /t 00
   ```

2. Run this script by copying and pasting to a notepad document and then Save As => (whatever).bat:

   ```powershell
   :: Created by: Shawn Brink
   :: http://www.sevenforums.com
   :: Tutorial: http://www.sevenforums.com/tutorials/49819-icon-cache-rebuild.html

   @echo off
   set iconcache=%localappdata%\IconCache.db

   echo The Explorer process must be killed to delete the Icon DB.
   echo.
   echo Please SAVE ALL OPEN WORK before continuing.
   echo.
   pause
   echo.
   If exist "%iconcache%" goto delID
   echo.
   echo Icon DB has already been deleted.
   echo.
   pause
   exit /B

   :delID
   echo Attempting to delete Icon DB...
   echo.
   ie4uinit.exe -ClearIconCache
   taskkill /IM explorer.exe /F
   del "%iconcache%" /A
   echo.
   echo Icon DB has been successfully deleted. Please "restart your PC" now to rebuild your icon cache.
   echo.
   start explorer.exe
   pause
   exit /B
   ```

### References:

["How to Rebuild the Icon Cache in Windows"](http://www.sevenforums.com/tutorials/49819-icon-cache-rebuild.html  