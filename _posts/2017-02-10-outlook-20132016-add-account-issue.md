---
title: Outlook 2013/2016 Add Account Issue
date: 2017-02-10T12:33:40+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/02/outlook-20132016-add-account-issue/
tags:
  - Windows
  - LocalSoftware
tags:
  - Powershell
  - MSOffice
  - Regedit
---
<!--more-->

### Description:

When we first started migrating clients to our new hosted Exchange 2016, we quickly realized that Outlook 2010 wouldn't add their Exchange accounts no matter how hard we tried tweaking registry settings so we just decided to get everyone to upgrade to Office 2013/2016. Another problem arose where we couldn't get the accounts to add until we configured a couple registry settings. As usual, I took these and put them in a PS Script.

### To Resolve:

1. Push over this file and run it on the remote computer:

   ```powershell
   # Outlook Config

   Write-Verbose "Setting Outlook 2016 Add Account Issue Fix"
   Set-Location HKCU:

   # AutoDiscover Fix
   $registryPath = "HKCU:\SOFTWARE\Microsoft\Office\16.0\Outlook\AutoDiscover"
   $Name = "ExcludeHttpsRootDomain"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   # AutoDiscover Fix 2
   $registryPath = "HKCU:\SOFTWARE\Microsoft\Office\16.0\Outlook\AutoDiscover"
   $Name = "ExcludeHttpsAutoDiscoverDomain"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   # Fix Max Accounts Issue
   $registryPath = "HKCU:\SOFTWARE\Microsoft\Exchange"
   $Name = "MaxNumExchange"
   $value = "14"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   # Fix Max Accounts Issue 2
   $registryPath = "HKCU:\Software\Policies\Microsoft\Exchange"
   $Name = "MaxNumExchange"
   $value = "14"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```


2. This script also sets up a Max Account value higher than normal because sometimes we needed to add 9+ accounts to a single profile.

3. Another thing we had to do after running this script is launch the credential manager and clear their credentials so that Outlook would be forced to ask for the new username and password to connect to the Exchange account (even if it was the same as the one setup with IMAP/POP). You could add the following line to end of your script: `rundll32.exe keymgr.dll,KRShowKeyMgr`


