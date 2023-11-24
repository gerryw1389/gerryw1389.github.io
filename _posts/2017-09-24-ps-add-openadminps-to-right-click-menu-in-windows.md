---
title: 'PS: Add OpenAdminPS To Right Click Menu In Windows'
date: 2017-09-24T06:09:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/ps-add-openadminps-to-right-click-menu-in-windows/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So I had a previous post where I talked about adding a line to [my setup of QuickCliq](https://automationadmin.com/2017/07/quickcliq-config/) to run a batch to run PS as admin and it works great, still use all the time. I started digging and found a way you can add it to right click menu as well in Windows itself.

NOTE: I still highly recommend using my QuickCliq setup to run batch files as it has shortcut commands and you can add/take away real easily without playing around in the registry.
{: .notice--success}

I tried to refactor the script below as this (see below), and it doesn't work => it moves the &#8220;Open PS here  (Admin) to the main menu and just looks tacky. I'm usually good about refactoring scripts, but I screwed this one up somehow?

   ```powershell
   $Paths = @()
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open\command"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas\command"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\shell\Powershell"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\Powershell"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell\open"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell\open\command"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas"
   $Paths += "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas\command"

   ForEach ($Path in $Paths)
   {
      If ((Test-Path $Path) -ne $True)
      {
         New-Item $Path -Force -ErrorAction SilentlyContinue | Out-Null
      }
   }

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell"
   $Params.Name = "MUIVerb"
   $Params.Value = "Open PowerShell"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell"
   $Params.Name = "Icon"
   $Params.Value = "powershell.exe"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell"
   $Params.Name = "ExtendedSubCommandsKey"
   $Params.Value = "Directory\\ContextMenus\\MenuPowerShell"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell"
   $Params.Name = "MUIVerb"
   $Params.Value = "Open PowerShell"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell"
   $Params.Name = "Icon"
   $Params.Value = "powershell.exe"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell"
   $Params.Name = "ExtendedSubCommandsKey"
   $Params.Value = "Directory\\ContextMenus\\MenuPowerShell"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell\open"
   $Params.Name = "MUIVerb"
   $Params.Value = "PowerShell here"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell\open"
   $Params.Name = "Icon"
   $Params.Value = "powershell.exe"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell\open\command"
   $Params.Name = "(default)"
   $Params.Value = "powershell.exe -noexit -command Set-Location '%V'"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas"
   $Params.Name = "MUIVerb"
   $Params.Value = "PowerShell here (Admin)"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas"
   $Params.Name = "Icon"
   $Params.Value = "powershell.exe"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas"
   $Params.Name = "HasLUAShield"
   $Params.Value = ""
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\runas\command"
   $Params.Name = "(default)"
   $Params.Value = "powershell.exe -noexit -command Set-Location '%V'"
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\shell\Powershell"
   $Params.Name = "Extended"
   $Params.Value = ""
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force -ErrorAction SilentlyContinue | Out-Null
   Clear-Variable -Name Params

   $Params = @{}
   $Params.Path = "HKLM:\SOFTWARE\Classes\Directory\background\shell\Powershell"
   $Params.Name = "Extended"
   $Params.Value = ""
   $Params.PropertyType = "String"
   New-ItemProperty @Params -Force -ErrorAction SilentlyContinue | Out-Null
   Clear-Variable -Name Params
   ```

### To Resolve:

1. Update 2018-04-04: If you just want to open an Administrator PS Prompt in your current directory, run:

   ```powershell
   $menu = 'OpenPSHere'
   $command = "$PSHOME\powershell.exe -NoExit -NoProfile -Command ""Set-Location '%V'"""

   'directory', 'directory\background', 'drive' | ForEach-Object {
      New-Item -Path "Registry::HKEY_CLASSES_ROOT\$_\shell" -Name runas\command -Force |
      Set-ItemProperty -Name '(default)' -Value $command -PassThru |
      Set-ItemProperty -Path {$_.PSParentPath} -Name '(default)' -Value $menu -PassThru |
      Set-ItemProperty -Name HasLUAShield -Value ''
      }
   ```

2. Here is a version that adds &#8220;Open Powershell&#8221; with a submenu of &#8220;Open Powershell here&#8221; and &#8220;Open Powershell here Admin&#8221;

   ```powershell
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open\command") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open\command" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas\command") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas\command" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\shell\Powershell") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\shell\Powershell" -force -ea SilentlyContinue };
   if((Test-Path "HKLM:\SOFTWARE\Classes\Directory\background\shell\Powershell") -ne $true) {  New-Item "HKLM:\SOFTWARE\Classes\Directory\background\shell\Powershell" -force -ea SilentlyContinue };
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell' -Name 'MUIVerb' -Value "Open PowerShell" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell' -Name 'Icon' -Value "powershell.exe" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\shell\01MenuPowerShell' -Name 'ExtendedSubCommandsKey' -Value "Directory\\ContextMenus\\MenuPowerShell" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell' -Name 'MUIVerb' -Value "Open PowerShell" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell' -Name 'Icon' -Value "powershell.exe" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\background\shell\01MenuPowerShell' -Name 'ExtendedSubCommandsKey' -Value "Directory\\ContextMenus\\MenuPowerShell" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open' -Name 'MUIVerb' -Value "PowerShell here" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open' -Name 'Icon' -Value "powershell.exe" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\open\command' -Name '(default)' -Value "powershell.exe -noexit -command Set-Location '%V'" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas' -Name 'MUIVerb' -Value "PowerShell here (Admin)" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas' -Name 'Icon' -Value "powershell.exe" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas' -Name 'HasLUAShield' -Value "" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\ContextMenus\MenuPowerShell\shell\runas\command' -Name '(default)' -Value "powershell.exe -noexit -command Set-Location '%V'" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\shell\Powershell' -Name 'Extended' -Value "" -PropertyType String -Force -ea SilentlyContinue;
   New-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\Directory\background\shell\Powershell' -Name 'Extended' -Value "" -PropertyType String -Force -ea SilentlyContinue;
   ```

3. The following script will add &#8220;AdminPS&#8221;, &#8220;AdminPowershellISE&#8221;, and &#8220;OpenPowershellHere&#8221; to your right click menu for any time you are in the file system (Windows Explorer/Desktop):

   ```powershell
   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   $registryPath = "HKCR:\Directory\Background\shell"
   $Name = "AdminPowershell"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\AdminPowershell"
   $Name = "command"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\AdminPowershell\command"
   $Name = "(Default)"
   $value = "C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe start-process powershell -verb runas"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null
   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   $registryPath = "HKCR:\Directory\Background\shell"
   $Name = "AdminPowershellISE"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\AdminPowershellISE"
   $Name = "command"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\AdminPowershellISE\command"
   $Name = "(Default)"
   $value = "C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe start-process powershell_ise -verb runas"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null
   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   $registryPath = "HKCR:\Directory\Background\shell"
   $Name = "\OpenPowershellHere"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\OpenPowershellHere"
   $Name = "command"
   New-Item -Path $registryPath -Name $Name -Force | Out-Null
   $registryPath = "HKCR:\Directory\Background\shell\\OpenPowershellHere\command"
   $Name = "(Default)"
   $value = "C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -noexit -command Set-Location -LiteralPath '%V'"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null
   ```