---
title: 'PS: Set Environmental Vars For System'
date: 2020-01-11T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/ps-set-environment-vars-for-system/
categories:
  - Windows
  - Security
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

To help with keeping passwords local to servers, one approach you can use is to store passwords as environmental variables that only elevated users have access to. For example, this post will show how to add an environmental variable for the user 'NT Authority\System' for a scheduled Windows Task that runs a script. The script can then parse the variable when it is ran.

### To Resolve

1. [This script](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Get-SystemEnvVars.ps1) creates a scheduled task that is to be ran by the user 'NT Authority\System' that sets the variable TEMP_VAR with `pa55word1`. Later, you can have another script access that variable as a way to pass a password around securely.

   ```powershell
   If ( -not ( Test-Path "c:\scripts") )
            {
               New-Item -Itemtype Directory -Path "c:\scripts" -Force | Out-Null
            }
            If ( -not ( Test-Path "c:\scripts\temp.ps1") )
            {
               New-Item -Itemtype File -Path "c:\scripts\temp.ps1" -Force | Out-Null
            }
            
            If ( Test-Path "c:\scripts\temp.ps1")
            {
               Write-Output "`$env:TEMP_VAR = 'pa55word1';" | Out-File "c:\scripts\temp.ps1" -Append -Encoding ASCII
               Write-Output "[System.Environment]::SetEnvironmentVariable('TEMP_VAR', 'pa55word1', [System.EnvironmentVariableTarget]::User)" | Out-File "c:\scripts\temp.ps1" -Append -Encoding ASCII
               $output = "Write-Output "
               $output += '"$env:TEMP_VAR" | Out-File "c:\scripts\temp2.txt" -Encoding ASCII '
               Write-Output $output | Out-File "c:\scripts\temp.ps1" -Append -Encoding ASCII
            }
            
            $tName = "SetEnvVar"
            $tCommand = "$env:windir\system32\WindowsPowerShell\v1.0\powershell.exe"
            $tArgs = " -NoProfile -ExecutionPolicy Bypass -File c:\scripts\temp.ps1"
            $tAction = New-ScheduledTaskAction -Execute "$tCommand" -Argument $tArgs
            $uName = "NT Authority" + "\" + "System"
            $tTrigger = New-ScheduledTaskTrigger -Daily -At "8:05am"
            Register-ScheduledTask -Action $tAction -Trigger $tTrigger -TaskName "$tName" -User $uName
            
            Start-ScheduledTask -TaskName "SetEnvVar"
            
            Start-Sleep -Seconds 5
            If ( (Get-Content "c:\scripts\temp2.txt") -like "pa55word1" )
            {
               Write-Output "SYSTEM user environmental variable set successfully"
               
               If ( Test-Path "c:\scripts\temp.ps1")
               {
                  Remove-Item "c:\scripts\temp.ps1" -Force | Out-Null
               }
               If ( Test-Path "c:\scripts\temp2.txt")
               {
                  Remove-Item "c:\scripts\temp2.txt" -Force | Out-Null
               }
               Unregister-ScheduledTask -TaskName "SetEnvVar" -Confirm:$false
            }
            else
            {
               Write-Output "SYSTEM user environmental variable FAILED"
            }
   ```


2. Here is [another script](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-SystemEnvVars.ps1) that you can run that dumps all 'NT Authority\System' environmental vars to `c:\scripts\temp2.txt`

   ```powershell
   If ( -not ( Test-Path "c:\scripts") )
            {
               New-Item -Itemtype Directory -Path "c:\scripts" -Force | Out-Null
            }
            If ( -not ( Test-Path "c:\scripts\temp.ps1") )
            {
               New-Item -Itemtype File -Path "c:\scripts\temp.ps1" -Force | Out-Null
            }
            
            If ( Test-Path "c:\scripts\temp.ps1")
            {
               $here = @"
   `$output = Get-ChildItem env:
   `$Objects = [System.Collections.Generic.List[PSObject]]@()
   foreach (`$envVar in `$output)
   {
      `$name = `$envVar.name
      `$value = `$envVar.value
      `$item = `$name + ":" + `$value
      [void]`$Objects.Add(`$Item)
   }
   write-output `$Objects | out-file c:\scripts\temp2.txt
   "@

            Write-Output $here | Out-File "c:\scripts\temp.ps1" -Append -Encoding ASCII
            
         }
            
            $tName = "GetSystemEnvVar"
            $tCommand = "$env:windir\system32\WindowsPowerShell\v1.0\powershell.exe"
            $tArgs = " -NoProfile -ExecutionPolicy Bypass -File c:\scripts\temp.ps1"
            $tAction = New-ScheduledTaskAction -Execute "$tCommand" -Argument $tArgs
            $uName = "NT Authority" + "\" + "System"
            $tTrigger = New-ScheduledTaskTrigger -Daily -At "8:05am"
            Register-ScheduledTask -Action $tAction -Trigger $tTrigger -TaskName "$tName" -User $uName
            
            Start-ScheduledTask -TaskName "GetGetSystemEnvVar"
            
            Write-Output "System environmental vars can be found at c:\scripts\temp2.txt"
         }
   ```

3. Finally, if you have scripts that are to be ran as this user, you would access them like:

   - Python

   ```python
   import os

   # run PS script to add to environmental var
   config = {
      'password' : os.getenv('TEMP_VAR', None)
   }
   ```

   - Powershell

   ```powershell
   Write-Output $env:TEMP_VAR
   # this will be blank unless the script is being ran from 'NT Authority\System'
   ```

   