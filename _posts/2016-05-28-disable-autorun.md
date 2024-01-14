---
title: Disable AutoRun
date: 2016-05-28T06:43:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/disable-autorun/
tags:
  - Windows
tags:
  - Tweaks
  - GroupPolicy
  - Regedit
---
<!--more-->

### Description:

AutoRun's are actions that Windows does as soon as you plug a device in via USB, CD Tray, etc. These can be highly annoying, try these steps to disable them. First, just go to Run => control => Use the search and search for &#8220;Auto&#8221; and then select &#8220;Choose what to do for Media Devices&#8221; and customize it there.

### To Resolve: If On A Domain

1. Run => `gpedit.msc`

2. Computer Configuration => Administrative Templates => System. Right Click &#8220;Turn off Autoplay&#8221; => Properties => Change to &#8220;Enabled&#8221;.

3. Reboot the computer.

### To Resolve: If Not On A Domain

1. Run => regedit

2. Navigate to: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer.

3. Modify the &#8220;NoDriveTypeAutorun&#8221; to the Data Value &#8220;OxFF&#8221; (this will disable all drives).

4. Click OK, exit regedit, and reboot the computer.