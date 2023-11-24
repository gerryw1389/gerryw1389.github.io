---
title: Broken Favorites In Windows Explorer
date: 2016-05-28T06:39:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/broken-favorites-in-windows-explorer/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

I once had an issue where I deleted all my folders in my user profile (because I don't use it) and I could not access my Favorites in Windows Explorer anymore! I thought the fix would be just to drag and drop a newly created &#8220;favorites&#8221; folder, that didn't work&#8230;

### To Resolve:

1. In your User profile (C:\Users\%username%) create a new folder called Links

2. In the same folder create a folder named Favorites

3. Run => regedit

4. Navigate to each of these locations and make sure they point to your Favorites folder:

   - `HKEY_CURRENT_USER\Software\Microsoft\Windows\Current Version\Explorer\Shell folders`  
   - `HKEY_CURRENT_USER\Software\Microsoft\Windows\Current Version\Explorer\User Shell folders`  
   - `HKEY_USERS\.default\Software\Microsoft\Windows\Current Version\Explorer\Shell folders`
   - `HKEY_USERS\.default\Software\Microsoft\Windows\Current Version\Explorer\User Shell folders`

5. Restart

6. To Remove Your HomeGroup folder:

   - Run => regedit
   - Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Classes\CLSID\{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93}\ShellFolder (for 64bit)` or 
   - `HKEY_CLASSES_ROOT\CLSID\{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93}\ShellFolder (for 32bit)`
   - Right click on "ShellFolder" => Permissions => Administrators => Allow Full Control
   - On the right, click on "Attributes" => Value: `b094010c`
   - Restart
