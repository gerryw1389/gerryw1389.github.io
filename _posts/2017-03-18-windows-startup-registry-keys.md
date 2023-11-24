---
title: Windows Startup Registry Keys
date: 2017-03-18T16:58:47+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/03/windows-startup-registry-keys/
tags:
  - Windows
---
<!--more-->

### Description:

Here is the startup sequence of the major registry keys, starting immediately after `bootmgr` has been read and ending with the program shortcut entries in the two Startup folders.

### To Resolve:

1. `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute`. This can include instructions to schedule the running of chkdsk but not user programs.

2. `Services` start next, followed by the `RunServicesOnce` and `RunServices` registry keys (if present)

3. User then logs on to the system

4. `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\UserInit`. This points to the program `C:\WINDOWS\system32\userinit.exe` and the entry ends with a comma. Other programs can be started from this key by appending them and separating them with a comma.

5. `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell`. This should contain just one entry, `explorer.exe`.

6. Program entries in these 2 registry keys for ALL USERS start next: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run and \RunOnce`

7. Program entries in these 2 registry keys for CURRENT USER start next: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run and \RunOnce`

8. Programs in the Startup Folders of All Users and Current User are started last of all.

9. Important programs like antivirus and firewall start early in the sequence as Services. The icons that appear in the Notification Area (bottom right of the screen) are just their user interfaces, i.e. options and preferences.

10. Note that the additional location for 32-bit software in a 64-bit computer is `HKLM\SOFTWARE\Wow6432Node` and `HKCU`.