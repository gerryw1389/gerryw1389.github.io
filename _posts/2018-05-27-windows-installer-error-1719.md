---
title: Windows Installer Error 1719
date: 2018-05-27T03:27:24+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/windows-installer-error-1719/
tags:
  - LocalSoftware
  - Windows
---
<!--more-->

### Description:

The other day I ran into an issue with Windows Installer: &#8220;Error 1719. The Windows Installer Service could not be accessed. This can occur if you are running Windows in safe mode, or if the Windows Installer is not correctly installed.&#8221;

### To Resolve:

1. Try:  
Navigate to: HKLM:\System\CurrentControlSet\Services\MSIServer  
Change DisplayName value: C:\WINDOWS\SysWOW64\msiexec.exe /V  
Open PS as Admin and run: C:\WINDOWS\SysWOW64\msiexec.exe /regserver  
Restart-Computer -Force

2. If that don't work, open CMD as Admin and type each of these one by one (or create a batch file):

```powershell
%windir%\system32\msiexec.exe /unregister
%windir%\syswow64\msiexec.exe /unregister
%windir%\system32\msiexec.exe /regserver
%windir%\syswow64\msiexec.exe /regserver
shutdown /r /f /t 00
```