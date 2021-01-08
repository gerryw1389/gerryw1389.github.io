---
title: Imaging OEM
date: 2018-04-07T04:23:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/imaging-oem/
categories:
  - SysAdmin
  - LocalSoftware
  - Windows
tags:
  - Setup
---
<!--more-->

### Description:

I know these are the words SysAdmins snear at, but sometimes you have no choice if a company doesn't bother with Volume Licensing therefore no [Re-image Rights](https://automationadmin.com/2016/05/re-imaging-rights/). Follow this post to generically apply a custom image to OEM computers.

### To Resolve:

1. Run a generic [template script](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-Template.ps1).

   - 2018-04: Place this in your script to download and run my template script on any W10 Machine:

   ```powershell
   Write-Output "Launching template script"
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"

   $Path = "$Env:UserProfile\Downloads" + "\Temp"
   If (Test-Path $Path)
   {
   Remove-Item -Path $Path -Recurse -Force
   New-Item -ItemType Directory -Path $Path -Force
   }
   Else
   {
   New-Item -ItemType Directory -Path $Path -Force
   }

   $PrivatePath = $Path + "\Private"
   New-Item -ItemType Directory -Path $PrivatePath -Force
   $Download = "$Path\Private\helpers.psm1"
   $URI = "https://raw.githubusercontent.com/gerryw1389/master/master/gwConfiguration/Private/helpers.psm1"
   $Response = Invoke-RestMethod -Method Get -Uri $URI
   $Response | Out-File $Download -Encoding ASCII

   $PublicPath = $Path + "\Public"
   New-Item -ItemType Directory -Path $PublicPath -Force
   $Download = "$Path\Public\set-template.ps1"
   $URI = "https://raw.githubusercontent.com/gerryw1389/master/master/gwConfiguration/Public/Set-Template.ps1"
   $Response = Invoke-RestMethod -Method Get -Uri $URI
   $Response | Out-File $Download -Encoding ASCII

   $Batch = "$PublicPath" + "\set-template.bat"
   $String = @'
   @ECHO OFF
   PowerShell.exe -NoProfile ^
   -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command ". "%~dpn0.ps1"; Set-Template "' -Verb RunAs}"
   '@
   Write-Output $String | Out-File -LiteralPath $Batch -Encoding ASCII

   Start-Process $Batch -Verb Runas
   ```

2. Install [Chocolatey](https://github.com/gerryw1389/powershell/blob/main/gwApplications/Public/Install-Choco.ps1):

3. Uninstall [pre-installed Office](https://automationadmin.com/2018/03/office-install-tasks/).

4. For manual installs (outside of Chocolatey), I would do:

   ```powershell
   Write-Output "Installing Adobe Reader if not installed"
   If (!(Test-Path "C:\Program Files (x86)\Adobe\Reader"))
   {
   Set-Location -Path "$PSScriptRoot\reader"
   cmd /c "Reader.Exe /Spb"
   cmd /c Pause
   }
   Else
   {
   Write-Output "Adobe Reader already installed, moving on"
   }
   ```

5. To send installed program icons to the desktop

   ```powershell
   Write-Output "Setting MS Excel Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\Excel 2016.Lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()

   Write-Output "Setting MS Outlook Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\Outlook 2016.Lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()
   ```

6. Other optional tasks:  
   - [Configure IE](https://automationadmin.com/2017/08/ps-configuring-ie-settings/)
   - Send [link to helpdesk](https://automationadmin.com/2017/03/ps-link-to-helpdesk/)
   - Map drives
   - Add printers
   - [Many](https://automationadmin.com/2017/08/w10-config-snippets/) other things