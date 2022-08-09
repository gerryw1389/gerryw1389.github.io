---
title: 'PS: Customize Your Prompt'
date: 2016-10-15T02:45:10+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/set-up-customized-ps-prompt/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Tweaks
---
<!--more-->

### Description:

Follow this post to setup a customized PS Prompt. Most of this comes from [this](https://hodgkins.io/ultimate-powershell-prompt-and-git-setup) post. See my [dot files post](https://automationadmin.com/2022/01/dot-files) for some references to these settings.

### To Resolve:

1. Open admin PS and type:

   ```powershell
   # Set your PowerShell execution policy
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force

   # Install Chocolatey
   iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex

   # Install Chocolatey packages
   choco install vim -y
   choco install conemu -y

   # Install PowerShell modules
   Install-PackageProvider NuGet -MinimumVersion '2.8.5.201' -Force
   Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
   ```

2. Close out of the PS prompt and open ConEmu

   - Configure it like so:  
   - Settings => Appearance: Single instance mode  
   - Quake Style = Check the slide down checkbox  
   - Startup = Change dropdown to {Shells:Powershell}  
   - Keys and Macro = Assign `Ctrl+(Backtick)`
   - Colors = Import a theme from [here](https://github.com/joonro/ConEmu-Color-Themes) or customize your own.
   - That's it! Make sure to add the following to your profile:
   - `Set-Alias vim -Value 'C:\Program Files (x86)\vim\vim80\gvim.exe'`
   - Import-Module [PSColor](https://github.com/Davlind/PSColor)
   - As an addition to this, I like to set my prompt like so..

   ```powershell
   function Prompt {
      $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
      $principal = [Security.Principal.WindowsPrincipal] $identity
      $(if (test-path variable:/PSDebugContext) { '[DBG]: ' }
      elseif($principal.IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
         {
         Write-Host ("[ADMIN] ") -nonewline -foregroundcolor Green
         # Print the current time:
         Write-Host ("[") -nonewline -foregroundcolor DarkGray
         Write-Host (Get-Date -format 'g') -nonewline -foregroundcolor Gray
         Write-Host ("][") -nonewline -foregroundcolor DarkGray
         # Print the working directory:
         Write-Host ($PWD) -nonewline -foregroundcolor Gray
         Write-Host ("]") -nonewline -foregroundcolor DarkGray
         Write-Host ("`r`n") -nonewline -foregroundcolor DarkGray
         # Print the prompt symbol:
         Write-Host ("#") -nonewline -foregroundcolor Green
         return " ";
         }
      else{
         # Print the current time:
         Write-Host ("[") -nonewline -foregroundcolor DarkGray
         Write-Host (Get-Date -format 'g') -nonewline -foregroundcolor Gray
         Write-Host ("][") -nonewline -foregroundcolor DarkGray
         # Print the working directory:
         Write-Host ($PWD) -nonewline -foregroundcolor Gray
         Write-Host ("]") -nonewline -foregroundcolor DarkGray
         Write-Host ("`r`n") -nonewline -foregroundcolor DarkGray
         # Print the prompt symbol:
         Write-Host ("#") -nonewline -foregroundcolor Green
         return " ";
         }
      )}
   ```

   - Copy and paste this into your profile. What it will do is make each command in Powershell or Powershell ISE have it's own line.
   - A regular prompt will look like: `\[Date / Time\] \[Current Directory\]`
   - An Admin prompt will look the same but will have a green [ADMIN] in front.
   - More info on customizing your prompt can be found [here](https://technet.microsoft.com/en-us/library/hh847739.aspx).

2. Update 2018-03: My current prompt looks like [PSProfile](https://github.com/gerryw1389/misc/blob/main/dot-files/Microsoft.Powershell_profile.ps1)

