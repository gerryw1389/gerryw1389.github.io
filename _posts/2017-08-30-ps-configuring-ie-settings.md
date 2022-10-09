---
title: 'PS: Configuring IE Settings'
date: 2017-08-30T21:27:19+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/ps-configuring-ie-settings/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

Use these snippets if you ever want to setup IE for your clients in a specific way.

### To Resolve:

1. Copy the following in your scripts:

#### To Launch IE (32bit):

   ```powershell
   Invoke-Item "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
   ```

#### To Reset IE To Defaults:

   ```powershell
   cmd /c "RunDll32.exe InetCpl.cpl,ResetIEtoDefaults"
   ```

#### To Set The HomePage:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Internet Explorer\Main"
   $Name = "Start Page"
   $value = "https://google.com"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null
   ```

#### To Add A Site To Trusted Sites (Remember To Always Start And End With The Set-Location Line):

   ```powershell
   Set-Location "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains"
   New-Item google.com -Force
   Set-Location google.com
   New-Itemproperty . -Name * -Value 2 -Type DWORD -Force
   Set-Location "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains"
   ```

#### To Configure Zones (These Settings Allow Scriptlets To Run Fully For Trusted Zone):

   ```powershell
   Set-Location "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2"
   New-Itemproperty . -Name 1001 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1004 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1200 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1201 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1206 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1208 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1209 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 120a -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 120b -Value 3 -Type Dword -Force
   New-Itemproperty . -Name 1400 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1402 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1405 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1607 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1609 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1803 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 1809 -Value 3 -Type Dword -Force
   New-Itemproperty . -Name 2000 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 2201 -Value 3 -Type Dword -Force
   New-Itemproperty . -Name 2702 -Value 0 -Type Dword -Force
   New-Itemproperty . -Name 270c -Value 3 -Type Dword -Force
   ```

#### To Add Sites To Pop Up Blocker:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Internet Explorer\New Windows\Allow"
   $Name = "google.com"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType Binary -Force | Out-Null
   ```

#### To Auto Login To A Website:

   ```powershell
   #NOTE: Set your username and password in the first two variables.
   $username = "username"
   $password = "password"
   $ie = New-Object -com InternetExplorer.Application
   $ie.visible=$True
   $ie.navigate("192.168.178.1")
   while($ie.ReadyState -ne 4) {start-sleep -Seconds 1}
   $ie.document.GetElementsById("loginUsername").value= "$username"
   $ie.document.getElementById("loginPassword").value = "$password"
   $ie.Document.getElementById('login').click()
   Start-Sleep 5
   ```

