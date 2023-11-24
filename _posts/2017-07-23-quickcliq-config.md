---
title: QuickCliq Config
date: 2017-07-23T05:07:24+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/quickcliq-config/
tags:
  - LocalSoftware
tags:
  - PersonalConfig
---
<!--more-->

### Description:

[QuickCliq](http://apathysoftworks.com/software/quickcliq) is one of those programs, like Greenshot, that is my first go-to that I use on a new computer. I usually just download Google drive where I have a series of portable programs that I can then call with this program.

### To Resolve:

1. Since it is portable, you launch by double clicking the .exe. First setup a keyboard shortcut. I use `Alt+Q`. Here is my setup:

   <img class="alignnone size-full wp-image-4532" src="https://automationadmin.com/assets/images/uploads/2017/07/quickcliq.png" alt="" width="376" height="540" srcset="https://automationadmin.com/assets/images/uploads/2017/07/quickcliq.png 376w, https://automationadmin.com/assets/images/uploads/2017/07/quickcliq-209x300.png 209w" sizes="(max-width: 376px) 100vw, 376px" /> 

2. So it starts by a scheduled task that I have that runs on startup that is pointing to my Google drive that contains the following:

   ```powershell
   start C:\google\progs\quick-cliq-v2.4\qc.exe
   start C:\google\progs\virtual-desktop-manager-v1.9\VirtualDesktopManager.exe
   start C:\google\google\progs\everything-v1.3\everything.exe
   start C:\google\google\progs\quick-text-paste-v1\quicktextpaste.exe
   cd "C:\Program Files\Oracle\VirtualBox"
   vdesk create:3
   ::noswitch:true doesnt work
   vdesk on:3 run:"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --comment "gw-vm" --startvm "vm-uuid-here"
   vdesk on:3 run:"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --comment "gw-vm" --startvm "vm-uuid-here"
   vdesk on:3 run:"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --comment "gw-vm" --startvm "vm-uuid-here"
   :: To get VM uuid, just open Virtual Box and "send shortcut to desktop" for your VM. Then right click and copy the path here.
   ::https://github.com/eksime/VDesk
   ```

3. I use QuickCliq for two main things:

   - Application launcher for installed and portable programs on my Google Drive
   - Script launcher => I place various batch files in my google drive and then use QuickCliq to run them, works really well for on-demand backups, one offs, [AutoHotKey](https://automationadmin.com/2017/07/autohotkey/), starting processes as admin, and basically any other reason you would run a script 🙂

4. Examples:

   - Launch Powershell as admin => `ps.bat`:

   ```powershell
   @echo off
   powershell.exe start-process powershell -verb runas
   ```

   - Launch Powershell ISE as admin => `ise.bat`:

   ```powershell
   @echo off
   powershell.exe start-process "powershell_ise" -verb runas
   ```

   - Start my backups:

   ```powershell
   @echo off
   cd c:\windows\system32
   robocopy "C:\google" "V:\backup" /mir /r:1 /w:1
   robocopy "G:\vbox" "V:\backup" /mir /r:1 /w:1
   ```

   