---
title: Disable AeroShake
date: 2016-05-28T06:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/disable-aeroshake/
tags:
  - Windows
tags:
  - Tweaks
  - GroupPolicy
  - Regedit
---
<!--more-->

### Description:

Aeroshake is a feature in Windows that will maximize all Windows if you grab the current window and shake it. I find it really annoying because I usually have multiple windows open at the same time.

### To Resolve:

1. Run => `gpedit.msc` => User Configuration\Administrative Templates\Desktop

2. Find the "Turn off Aero Shake window minimizing gesture" policy and set it to "enabled".

### Reg File Import:

1. Copy and paste this into a .reg file and import it:

   ```escape
   Windows Registry Editor Version 5.00

   [HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer]  
   "NoWindowMinimizingShortcuts"=dword:00000001
   ```

2. The Powershell Way:


   ```powershell
   $registryPath = "HKCU:\Software\Policies\Microsoft\Windows\Explorer"  
   $Name = "NoWindowMinimizingShortcuts"  
   $value = "1"  
   IF(!(Test-Path $registryPath))  
   {  
   New-Item -Path $registryPath -Force | Out-Null  
   }  
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

