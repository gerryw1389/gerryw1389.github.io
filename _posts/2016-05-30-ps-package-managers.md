---
title: 'PS: Package Managers'
date: 2016-05-30T05:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ps-package-managers/
tags:
  - Windows
  - SysAdmin
tags:
  - Powershell
  - Powershell-Modules
---
<!--more-->

### Description:

Powershell Package Managers are the Windows equivelent of yum, apt-get, etc for Linux. It is used to automate SDII (software discovery, installation, and inventory). Make sure to start Powershell as an admin and type `set-executionpolicy remotesigned`.

### To Resolve:

1. First thing to do is to upgrade your PS to version 5 found [here](https://www.microsoft.com/en-us/download/details.aspx?id=50395).

2. Now open up PS and Type:

   ```powershell
   Get-Module -Listavailable

   Import-Module Packagemanagement

   #This Will Show A List Of All The Commands For The Module.
   Gcm -Module Packagemanagement

   # As example, we install FF
   Find-Package -Name Firefox
   # Installs Firefox
   Install-Package -Name Firefox -Source Chocolatey
   # This Will Uninstall Firefox
   Uninstall-Package -Name Firefox
   ```

3. To install Chocolatey as a PackageProvider, Type:

   ```powershell
   Iex ((New-Object Net.Webclient).Downloadstring('https://chocolatey.org/Install.ps1')) 
   # Close And Re-Open Powershell

   # Now, To Install A Package You Just Type:
   Choco Install (Packagename)

   # To Uninstall
   Choco Uninstall (Packagename).
   ```


### References:

["Introducing PackageManagement in Windows 10"](https://blogs.technet.microsoft.com/packagemanagement/2015/04/28/introducing-packagemanagement-in-windows-10/#pi47623=2)  
["Chocolatey"](https://chocolatey.org/)  
["Package Management for PowerShell Modules with PowerShellGet"](https://blogs.msdn.microsoft.com/mvpawardprogram/2014/10/06/package-management-for-powershell-modules-with-powershellget/)  
["Checking Out OneGet in PowerShell V5"](https://learn-powershell.net/2014/04/03/checking-out-oneget-in-powershell-v5/)  