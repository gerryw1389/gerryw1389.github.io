---
title: 'Command Prompt: Software Commands'
date: 2016-06-02T20:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/command-prompt-software-commands/
categories:
  - Windows
tags:
  - OneLiners-CMD
  - Scripting-CMD
---
<!--more-->

### Description:

The following commands can be ran in the Windows Command Prompt.

### To Stop A Service:

   ```powershell
   sc stop (serviceName)
   net stop (serviceName) or (serviceDisplayName)
   ```

### To Disable A Service:

   ```powershell
   sc config (serviceName) start= disabled
   ```

### To Enable Built-In Administrator Account:

   ```powershell
   net user administrator /active:yes
   net user administrator 112233 
   :: Where 112233 is the password for the account
   ```

### To Add A New Admin User:

   ```powershell
   :: Where 111222333 is the password
   net user gerry 111222333 /add

   :: Add to admin group
   net localgroup administrators gerry /add

   :: Add to another group
   net localgroup "Remote Desktop users" gerry /add
   ```

### To Remove A User:

   ```powershell
   net user gerry /delete
   ```

### To Uninstall Specific Windows Updates:

   ```powershell
   wusa /uninstall /kb:(update ID) # ex: wusa /uninstall /kb:980302
   ```

### To Change The Color Of CMD Prompt Text:

   ```powershell
   :: Green
   color 0a

   :: Red
   color 0c

   :: Default
   color 07
   ```

### To Check The OS For Corruption:

   ```powershell
   sfc /scannow
   ```

### To Schedule A PS Script For Startup:

   ```powershell
   schtasks /create /tn "Startup PowerShell" /tr C:\scripts\psstart.bat /sc onstart /ru SYSTEM
   ```

### To Disable UAC:

   ```powershell
   C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
   ```

### To Enable .NET 3.5:

   ```powershell
   dism /Online /Enable-Feature /FeatureName:NetFx3 /All
   ```