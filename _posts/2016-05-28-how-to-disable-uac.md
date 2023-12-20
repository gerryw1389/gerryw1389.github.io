---
title: How To Disable UAC
date: 2016-05-28T06:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/how-to-disable-uac/
tags:
  - Windows
tags:
  - Tweaks
  - GroupPolicy
  - Batch-Commands
  - Powershell
---
<!--more-->

### Description:

UAC or User Account Control is something new implemented in most versions of Windows past Windows XP. This feature usually something that network administrators look to disable as it usually stops them from implementing changes in systems (or is just flat out annoying). Depending on your version of Windows or just preference, here is a couple ways to disable it.

Update: The complete opposite is true today, you ALWAYS have UAC enabled.

### To Resolve:

1. Run => `gpedit.msc` => Navigate to: `Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options` => Disable all options that start with User Account Control or tweak to your needs.

2. Run => `msconfig` => Navigate to the Tools tab and select the option to Disable UAC

3. Run => `control` => Search: "uac" or Navigate to User Accounts => Turn User Account Conrol On/ Off => Uncheck or Drag the bar down depending on what version of Windows you are running.

4. To disable via Command line, Run the following as an administrator:

   ```powershell
   C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f

   # To Re-Enable:
   C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f
   ```

   - Starting with Windows 10, it is highly advised not to disable UAC as this breaks many things. The most common setting is to fully enable it or drag down to the bottom bar.

   - In Powershell:

   ```powershell
   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "ConsentPromptBehaviorAdmin"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "EnableInstallerDetection"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "PromptOnSecureDesktop"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "FilterAdministratorToken"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

