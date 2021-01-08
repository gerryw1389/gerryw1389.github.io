---
title: Blank Spots In System Tray
date: 2016-05-28T06:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/blank-spots-in-system-tray/
categories:
  - Windows
tags:
  - Regedit
  - Tweaks
---
<!--more-->

### Description:

There will be blank spots on the system tray. Do these steps to remove them.


### To Resolve:

1. Run => `taskmgr` => Processes tab => Kill explorer.exe

2. Run => `regedit` => Navigate to: `HKEY_CURRENT_User\Software\Classes\Local Settings\Software\Microsoft\Windows\Current Version\Traynotify`

3. Delete the IconStreams and PastIconStream keys.

4. Exit and reboot. For more details, see ["Windows 7: Notification Area Icons - Reset"](http://www.sevenforums.com/tutorials/13102-notification-area-icons-reset.html)