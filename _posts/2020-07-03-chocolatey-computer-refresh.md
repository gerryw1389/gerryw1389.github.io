---
title: Chocolatey Computer Refresh
date: 2020-07-03T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/chocolatey-computer-refresh
categories:
  - LocalSoftware
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So I decided to wipe all data from my computer the other day and did the following steps to set it up again:

First, get all the installed programs

   ```powershell
   # Old computer
   Get-CimInstance win32_product | Select-Object Name, PackageName, InstallDate | out-file c:\scripts\soft2.txt
   Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | out-file c:\scripts\soft.txt

   #appwiz.cpl
   ```

I had planned to just follow my [original post about this](https://automationadmin.com/2018/08/setup-a-new-computer/) but found that it was a little outdated, so here is my newer post on what I did.

### To Resolve:

1. Open PS as administrator and run the following commands and close and reopen to get a new session:

   ```powershell
   # new computer
   Set-ExecutionPolicy RemoteSigned
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   ```

   - Run:

   ```powershell
   $packages = ( 
   "7zip",
   "bulkrenameutility",
   "cryptsync",
   "everything",
   "firefox",
   "firefox-dev --version=76.0.7-beta --pre",
   "mediamonkey",
   "git",
   "greenshot",
   "microsoftazurestorageexplorer",
   "nomacs",
   "notepadplusplus",
   "realtek-hd-audio-driver",
   "steam",
   "vlc",
   "vscode"
   )

   choco feature disable -n=showDownloadProgress

   foreach ($package in $packages)
   {
      choco install $package -y --limitoutput
   }
   ```

2. Then I installed my paid software like Microsoft Office by signing into my Microsoft account and installing from there.

3. Choco commands that might be useful:

   ```powershell
   # see installed packages
   choco list --localonly

   # see packages with upgrades avail
   choco outdated

   # update all (not recommended)
   choco upgrade all --noop / cup all -y

   # update selected packages
   choco upgrade notepadplusplus googlechrome atom 7zip
   ```

4. You could also try this with the native 'Package Management' module but I kept getting errors on some packages in testing:

   ```powershell
   Install-PackageProvider chocolatey
   Set-PackageSource -Name chocolatey -Trusted
   Install-Package -Name adobereader -ProviderName Chocolatey
   Find-Package -Name firefox, winrar, notepadplusplus, putty, dropbox | Install-Package
   Install-Package -Name "everything" -ProviderName Chocolatey
   ```
