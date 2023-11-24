---
title: W7 Change Login Screen Background
date: 2016-05-28T06:48:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/how-to-change-login-screen-background/
tags:
  - Windows
tags:
  - Regedit
  - Tweaks
---
<!--more-->

### Description:

If you ever want to change your login background on Windows, follow these steps.

### To Resolve:

1. Run => `regedit`

2. Navigate to: `HKEY_Local_Machine\Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background`

3. Change `OEMBackgrond` to `1`

4. Now Run `%windir%\system32\oobe`.

5. Create a folder called `info` and a subfolder called `backgrounds` if they don't exist.

6. Copy any new wallpaper you want to that directory following these conditions:

   - Must be named `backgroundDefault`
   - Must be `.jpg` extension.
   - Must be less than 256 KB in size.


### Option 2:

1. Download and run the tool at [http://www.julien-manici.com/windows\_7\_logon\_background\_changer/](http://www.julien-manici.com/windows_7_logon_background_changer/)