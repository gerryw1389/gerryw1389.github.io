---
title: 'PS: Modifying The Registry'
date: 2016-10-20T19:57:25+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/using-regedits-in-scripts/
tags:
  - Windows
tags:
  - Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

This is the format I use for using Powershell to edit registry entries.

### To Resolve:

1. Copy and replace the relevant information:

   ```powershell
   $registryPath = "HKCU:\Software\Policies\Microsoft\Windows\Explorer"
   $Name = "NoWindowMinimizingShortcuts"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To see if a value exists:

   ```powershell
   Function Test-RegistryValue
   {
   param($regkey, $name)
   $exists = Get-ItemProperty "$regkey\$name" -ErrorAction SilentlyContinue
   Write-Host "Test-RegistryValue: $exists"
   if (($exists -eq $null) -or ($exists.Length -eq 0))
   {
   return $false
   }
   else
   {
   return $true
   }
   }
   ```

#### To test a specific value:

   ```powershell
   $Path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search"
   $Name = "BingSearchEnabled"
   $Value = "0"
   $Test = (((Get-Item -Path $Path).GetValue($Name) -eq $Value))
   ```

#### To set a remote Registry value:

   ```powershell
   Function Set-RemoteRegistryValue
   {
   param(
   $ComputerName,
   $Path,
   $Name,
   $Value,
   [ValidateNotNull()]
   [System.Management.Automation.PSCredential]
   [System.Management.Automation.Credential()]
   $Credential = [System.Management.Automation.PSCredential]::Empty
   )
   $null = Invoke-Command -ComputerName $ComputerName -ScriptBlock { Set-ItemProperty -Path $Path -Name $Name -Value $Value } -Credential $Credential
   }
   ```

#### To set a remote HKEY_USER Registry value:

   ```powershell
   $strSID = (Get-WmiObject -Class Win32_UserAccount  -Filter "Domain = '$domain' AND Name = '$name'").SID
   $strKeyIEConnections = "$strSID\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections\"
   $strRegType = [Microsoft.Win32.RegistryHive]::Users
   $strRegKey  = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey($strRegType, $strIPAddrTmp)
   $strRegKey  = $strRegKey.OpenSubKey($strKeyIEConnections)
   ```

#### To Add Classes Root Entries Throw This At Beginning:

   ```powershell
   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   ```

   - Here is a combination of each of them (set a value if it doesn't exist by testing it first):

   ```powershell
   Filter Timestamp
   {
      "$(Get-Date -Format "yyyy-MM-dd hh:mm:ss tt"): $_"
   }

   Write-Output "Setting $($Reg.Path)\$($Reg.Name) to $($Reg.Value)" | TimeStamp
   $Reg = @{}
   $Reg.Path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
   $Reg.Name = "OneDrive"
   $Reg.Type = "Binary"
   $Reg.Value = ([byte[]](0x03, 0x00, 0x00, 0x00, 0xcd, 0x3e, 0xf3, 0x43, 0xa8, 0x89, 0xd3, 0x01))		
   IF (!(Test-Path $($Reg.Path)))
   {
      New-Item -Path $($Reg.Path) -Force | Out-Null
   }
   $RegName = $($Reg.Name)
   $C = ((Get-Item -Path $($Reg.Path)).GetValue($RegName))
   $Compare = Out-String -InputObject $c
   $Value = Out-String -InputObject $($Reg.Value)
   If ($Compare -eq $Value)
   {
      Write-Output "Key already exists: $($Reg.Path)\$($Reg.Name)" | TimeStamp
   }
   Else
   {
      New-ItemProperty @Reg -Force | Out-Null
      Write-Output "Added key: $($Reg.Path)\$($Reg.Name)" | TimeStamp
   }
   ```


