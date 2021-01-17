---
title: Using FSRM With Azure Data Gateway
date: 2020-06-05T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/using-fsrm-with-logic-apps-data-gateway
categories:
  - Azure
tags:
  - Cloud
  - Azure-On-premisesDataGateways
---
<!--more-->

### Description:

I haven't fully implemented this yet but the idea is to migrate my scripts that run every minute or every 5 minutes to event based using FSRM (File System Resource Manager) role on Windows Server. Here is how I set this up:

### To Resolve:

1. Server Manager => Roles => File and Storage Services/File System Resource Manager => Install => Doesn't require a reboot

2. Now, Server Manager => Tools => FSRM => File Screen => File Screen Path
   - G:\test
   - How do you want to configure file screen properties? Define custom =>
   - Settings: Passive Screening and Maintain File Groups => Create => Name:CSVs => on include section put `*.csv`
   - Command Tab:
     - Command: `C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe`
     - Command Arguments: `-File "c:\scripts\csv.ps1" -ExecutionPolicy "Bypass"`
     - Run as: 'Local System'

3. Right click 'File System Resource Manager (local)' => Configure Options => Notification Limits => Set each of them to `1`. This means it will check every minute for a new violation and fire your script.

4. Create `c:\scripts\csv.ps1` with these contents and test:

   ```powershell
   Function Write-Log
   {
      param (
         [Parameter(Mandatory = $true, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true, Position = 0)]
         [string]$InputObject
      )
      $message = "$(Get-Date -Format "yyyy-MM-dd hh:mm:ss tt"): " +  $InputObject
      $log = "c:\scripts\hello.txt"
      If ( Test-Path $log )
      {

      }
      Else
      {
         New-Item -ItemType "file" -Path $log | Out-Null
      }
      Write-Output -InputObject $message | Out-File $log -Append -Encoding "ascii"
   }

   write-log "hello"
   ```
