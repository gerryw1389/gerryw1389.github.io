---
title: Black Screen After Login To Windows
date: 2016-05-21T05:28:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/black-screen-after-login-to-windows/
tags:
  - Windows
tags:
  - Pre-Boot
  - Regedit
---
<!--more-->

### Description:

When you login to Windows, all you have is a black screen. Task manager and other Windows shortcuts don't work. I also had this issue on a server that would login and then never load the desktop.

### To Resolve:

1. Try to reboot into safe mode. See if you can login there. If you can, the issue has to do with a driver or service associated with normal mode. Run => `msconfig` => disable all services that are not MS and all startup items and reboot. Did it work?

2. If you can, try and determine if Windows is seeing a second monitor attached when there isn't one. Check your VGA cable connector. This isn't common but I once had a lady not realize that she had a second monitor attached that showed the desktop when she logged in (how could you not know that? geez)

3. Try to RDP to the workstation.

4. Try to open EventViewer from another computer using the `connect to` option (RPC access). See if there is something telling you why it is hanging.

5. Try to open Services from another computer using the `connect to` option (RPC access). Is everything running?

6. If none of the above works, we need to force the computer to crash and then try and find out what causes it. To do this, follow these steps:

   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `sysdm.cpl` => Advanced => Startup/Recovery => Make sure to set the path for kernel dumps
   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `regedit` => Navigate to: `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\kbdhid\Parameters` and create a REG_DWORD key called `CrashOnCtrlScroll` with a value of `0x01`
   - Restart
   - Press the keys `(Right)Ctrl + Scroll Lock + Scroll Lock` to [cause a crash](https://msdn.microsoft.com/en-us/library/windows/hardware/ff545499%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396) 
   - Get back into Windows safe mode, launch WinDbg, type `analyze -v -hang` to see if particular process/thread/driver/object appears to be the cause of the issue.
