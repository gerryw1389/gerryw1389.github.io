---
title: 'PS: Chocolatey'
date: 2016-12-03T02:14:53+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/ps-chocolatey/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Modules
  - Setup
---
<!--more-->

### Description:

To add on to my previous post [here](https://automationadmin.com/2016/05/ps-package-managers/), I wanted to find a way to revise my install scripts for faster automation of Windows 10 installs. I know I should be using [WDS with MDT](https://automationadmin.com/2016/05/wds-with-mdt/) and have configured in my homelab, but in the power of self learning => I just wanted to see what I could do with Powershell alone with  the OEM image (I know, bring on the down votes!)

### To Resolve:

1. First, I execute the following two statements manually in a Powershell admin prompt:

   ```powershell
   Set-ExecutionPolicy Unrestricted 
   # We will change this back to remoteSigned once this is over.

   iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
   ```

   #After it installs, it will tell you that you should probably exit out of your script and start a new one, so I do that. Here is the .ps1 I run as admin afterwards:

   ```powershell
   Import-Module PackageManagement

   Install-PackageProvider NuGet -MinimumVersion '2.8.5.201' -Force
   Install-PackageProvider Chocolatey
   Set-PSRepository -Name PSGallery -InstallationPolicy Trusted


   # Install Packages

   choco install googlechrome --confirm --limitoutput
   choco install flashplayeractivex --confirm --limitoutput
   choco install flashplayerplugin --confirm --limitoutput
   choco install 7zip.install --confirm --limitoutput
   choco install adobeair --confirm --limitoutput
   choco install jre8 --confirm --limitoutput
   choco install dotnet3.5 --confirm --limitoutput
   # choco install adobereader -y
   # choco install adobereader-update -y

   <# For my computer
   choco install python2 -y
   choco install bleachbit -y
   choco install notepadplusplus.install -y
   choco install atom -y
   choco install firefox -y
   choco install vim -y
   Set-Alias vim -Value "C:\Program Files (x86)\vim\vim80\gvim.exe"
   choco install procexp -y
   choco install putty -y
   choco install virtualbox -y
   choco install winscp.install -y
   choco install sysinternals -y
   #>
   ```

2. Adobe reader wasn't working when I tried this so I just manually went to get.adobe.com/reader and installed. It still got most of the software. Now, all I have to do is run &#8220;cup all&#8221; from an admin PS Prompt to update each of these &#8220;packages&#8221;.

3. Source is maintained under [gwApplications](https://github.com/gerryw1389/powershell/blob/master/gwApplications/Public/Install-Choco.ps1)