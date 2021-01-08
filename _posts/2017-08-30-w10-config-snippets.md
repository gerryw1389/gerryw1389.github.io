---
title: W10 Config Snippets
date: 2017-08-30T21:16:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/w10-config-snippets/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

Use the following snippets are part of your W10 config scripts if you want:

### To Resolve:

#### To Remove All Apps Except Windows Store And Calculator:

   ```powershell
   Get-Appxpackage -Allusers | Where-Object {$_.Name -Notlike "*Microsoft.Windowsstore*"} | Where-Object {$_.Name -Notlike "*Microsoft.Windowscalculator*"} | Remove-Appxpackage -Erroraction Silentlycontinue | Out-Null
   Get-Appxprovisionedpackage -Online | Where-Object {$_.Packagename -Notlike "*Microsoft.Windowsstore*"} | Where-Object {$_.Packagename -Notlike "*Microsoft.Windowscalculator*"} | Remove-Appxprovisionedpackage -Online -Erroraction Silentlycontinue | Out-Null
   ```

#### To Stop and Disable Diagnostics Tracking Service, WAP Push Service, Home Groups service, Xbox Services, and Other Unncessary Services:

   ```powershell
   Get-Service Diagtrack,DmwApPushService,HomeGroupListener,HomeGroupProvider,`
   XblAuthManager,XblGameSave,XboxNetApiSvc,TrkWks,`
   WMPNetworkSvc | Stop-Service -Passthru | Set-Service -Startuptype Disabled
   ```

#### To Disable Unneccessary Scheduled Tasks:

   ```powershell
   Get-Scheduledtask "SmartScreenSpecific","Microsoft Compatibility Appraiser","Consolidator","KernelCeipTask","UsbCeip","Microsoft-Windows-DiskDiagnosticDataCollector", "GatherNetworkInfo","QueueReporting" | Disable-scheduledtask
   ```

#### To Disable Auto Update And Download Of Windows Store Apps:

   ```powershell
   $registryPath = "HKCU:\SOFTWARE\Policies\Microsoft\WindowsStore"
   $Name = "AutoDownload"
   $value = "2"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Telemetry:

   ```powershell
   $registryPath = "HKLM:\Software\Policies\Microsoft\Windows\DataCollection"
   $Name = "AllowTelemetry"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata"
   $Name = "PreventDeviceMetadataFromNetwork"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\MRT"
   $Name = "DontOfferThroughWUAU"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\SQMClient\Windows"
   $Name = "CEIPEnable"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\AppCompat"
   $Name = "AITEnable"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\AppCompat"
   $Name = "DisableUAR"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Wifi Sense:

   ```powershell
   $registryPath = "HKLM:\Software\Microsoft\PolicyManager\default\WiFi\AllowWiFiHotSpotReporting"
   $Name = "Value"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots"
   $Name = "Value"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Delivery Optomization:

   ```powershell
   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization"
   $Name = "DODownloadMode"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config"
   $Name = "DownloadMode"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config"
   $Name = "DODownloadMode"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization"
   $Name = "SystemSettingsDownloadMode"
   $value = "3"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Location Tracking:

   ```powershell
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}"
   $Name = "SensorPermissionState"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\System\CurrentControlSet\Services\lfsvc\Service\Configuration"
   $Name = "Status"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Windows Feedback:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Siuf\Rules"
   $Name = "NumberOfSIUFInPeriod"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Windows Advertising ID:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo"
   $Name = "Enabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Restrict Windows Update P2P Only To Local Network:

   ```powershell
   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config"
   $Name = "DODownloadMode"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization"
   $Name = "SystemSettingsDownloadMode"
   $value = "3"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Suggested Apps, Feedback, Lockscreen Spotlight, File Explorer Ads and Unwanted App Installs For This User:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "SystemPaneSuggestionsEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "SoftLandingEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "RotatingLockScreenEnable"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "PreInstalledAppsEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "SilentInstalledAppsEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   $Name = "ContentDeliveryAllowed"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
   $Name = "ShowSyncProviderNotifications"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Remove Autologger File:

   ```powershell
   Write-Verbose "Removing AutoLogger file and restricting directory..."
   $autoLoggerDir = "$env:PROGRAMDATA\Microsoft\Diagnosis\ETLLogs\AutoLogger"
   If (Test-Path "$autoLoggerDir\AutoLogger-Diagtrack-Listener.etl")
   {
   Remove-Item "$autoLoggerDir\AutoLogger-Diagtrack-Listener.etl"
   }
   cmd /c "icacls $autoLoggerDir /deny SYSTEM:`(OI`)`(CI`)F" | Out-Null
   ```

#### To Set Explorer To &#8220;This PC&#8221;:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
   $Name = "LaunchTo"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Show File Extensions:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
   $Name = "HideFileExt"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Remove Onedrive From Explorer:

   ```powershell
   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   $registryPath = "HKCR:\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}"
   $Name = "System.IsPinnedToNameSpaceTree"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   If (!(Test-Path "HKCR:"))
   {
   New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null
   }
   $registryPath = "HKCR:\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}"
   $Name = "System.IsPinnedToNameSpaceTree"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```


#### To Uncheck Show Recently Used Files In Quick Access:

   ```powershell
   $Registrypath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer" 
   $Name = "ShowRecent" 
   $Value = "0" 
   If (!(Test-Path $Registrypath)) 
   { 
   New-Item -Path $Registrypath -Force | Out-Null 
   } 
   New-Itemproperty -Path $Registrypath -Name $Name -Value $Value -Propertytype Dword -Force | Out-Null​​ 
   ```


#### To Uncheck Show Used Folders In Quick Access:

   ```powershell
   $Registrypath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer"
   $Name = "ShowFrequent" 
   $Value = "0" 
   If (!(Test-Path $Registrypath)) 
   { 
   New-Item -Path $Registrypath -Force | Out-Null 
   } 
   New-Itemproperty -Path $Registrypath -Name $Name -Value $Value -Propertytype Dword -Force | Out-Null​​ 
   ```


#### To Remove User Folders From 'This PC':

   ```powershell
   Function Remove-UserFolders
   {
   # Documents
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" | Out-Null
   }

   # Pictures
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" | Out-Null
   }

   # Videos
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}"| Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" | Out-Null
   }

   # Downloads
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" | Out-Null
   }

   # Music
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" | Out-Null
   }

   # Desktop
   $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag"
   $Name = "ThisPCPolicy"
   $value = "Hide"
   IF (!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType String -Force | Out-Null

   IF (Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}")
   {
   Remove-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" | Out-Null
   }

   IF (Test-Path "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}")
   {
   Remove-Item "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" | Out-Null
   }

   }
   Remove-UserFolders
   ```

#### To Disable AeroShake:

   ```powershell
   $registryPath = "HKCU:\Software\Policies\Microsoft\Windows\Explorer"
   $Name = "NoWindowMinimizingShortcuts"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force
   ```

#### To Hide Cortana:

   ```powershell
   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
   $Name = "SearchboxTaskbarMode"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force
   ```

#### To Disable Bing In Start Menu and Cortana In Search:

   ```powershell
   $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search"
   $Name = "BingSearchEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Windows Search"
   $Name = "AllowCortana"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Windows Search"
   $Name = "ConnectedSearchUseWeb"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
   $Name = "CortanaEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
   $Name = "SearchboxTaskbarMode"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
   $Name = "DeviceHistoryEnabled"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Cloud Content:

   ```powershell
   $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\CloudContent"
   $Name = "DisableWindowsConsumerFeatures"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Stop Apps From Getting Account Info From Machine:

   ```powershell
   $registryPath = "HKLM:\Software\Policies\Microsoft\Windows\AppPrivacy"
   $Name = "LetAppsAccessAccountInfo"
   $value = "2"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Set Desktop Icons:

   ```powershell
   Function Set-DesktopIcons
   {
   # Make Sure Hide Desktop Icons Is Off
   $registryPath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer\Advanced"
   $Name = "Hideicons"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   # My PC
   $registryPath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer\Hidedesktopicons\Newstartpanel"
   $Name = "{20d04fe0-3aea-1069-A2d8-08002b30309d}"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   # User Files
   $registryPath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer\Hidedesktopicons\Newstartpanel"
   $Name = "{59031a47-3f72-44a7-89c5-5595fe6b30ee}"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   # Recycle Bin
   $registryPath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer\Hidedesktopicons\Newstartpanel"
   $Name = "{645ff040-5081-101b-9f08-00aa002f954e}"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   # Remove One Drive
   $registryPath = "Hkcu:\Software\Microsoft\Windows\Currentversion\Explorer\Hidedesktopicons\Newstartpanel"
   $Name = "{018D5C66-4533-4307-9B53-224DE2ED1FE6}"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   }
   Set-DesktopIcons<span id="mce_marker" data-mce-type="bookmark" data-mce-fragment="1">​</span>
   ```

### References:

1. Please be sure to check out my [gwConfiguration section](https://github.com/gerryw1389/powershell/tree/main/gwConfiguration/Public) for W10 Config scripts 
   - [Set-Template](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-Template.ps1)
   - [Set-HomePC](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-HomePC.ps1)
