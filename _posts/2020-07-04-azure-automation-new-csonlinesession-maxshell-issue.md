---
title: 'Azure Automation: New-CSOnlineSession MaxShell Issue'
date: 2020-07-04T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/azure-automation-new-csonlinesession-maxshell-issue
categories:
  - Azure
tags:
  - Cloud
  - Azure-Automation
---
<!--more-->

### Description:

So I had my first issue with Azure Automation the other day that I had to open a support case for. I was using a script that connect to Skype Online and the session would just hang for 5 minutes when ran from Azure Automation but worked fine when ran locally on the hybrid worker. The offending code:

   ```powershell
   Write-Output "Connecting to SkypeOnline Server..."
   $vroPass = Get-Pass
   $userName = 'someAccount@domain.com'
   $pw = ConvertTo-SecureString -String $vroPass -AsPlainText -Force
   $cred = New-Object -Typename System.Management.Automation.PSCredential -Argumentlist $username, $pw
   $session = New-CsOnlineSession -Credential $cred

   Import-PSSession $session
   Write-Output "Connecting to SkypeOnline Server...Completed"
   ```

The issue: It would hang for 5 minutes and then error with the [MaxShell](https://automationadmin.com/2020/02/ps-max-concurrent-shells-error) error I had seen before:

### To Resolve:

1. Obviously I ran the commands in that post to try and fix but that didn't work.

2. So I tried a more detailed approach:

   ```powershell
   enable-psremoting -force 
   cd WSMan:\localhost\Shell 
   set-item MaxConcurrentUsers 100 
   set-item MaxProcessesPerShell 10000 
   set-item MaxMemoryPerShellMB 1024 
   set-item MaxShellsPerUser 1000 
   cd WSMan:\localhost\Plugin\microsoft.powershell\Quotas 
   set-item MaxConcurrentUsers 100 
   set-item MaxProcessesPerShell 10000 
   set-item MaxShells 1000 
   set-item MaxShellsPerUser 1000 
   restart-service winrm 
   ```

3. So after establishing that it works locally on the machine, the next thing I tried was having the hybrid worker try and launch the script:

   ```powershell
   Write-Output "Launching script..."
   Set-Location "S:\sched-tasks\phone-numbers"
   $ScriptFile = 'S:\sched-tasks\phone-numbers\connect.ps1'
   $Start = @{ 
   'FilePath'         = 'powershell.exe'
   'NoNewWindow'      = $true
   'WorkingDirectory' = 'S:\sched-tasks\phone-numbers'
   'ArgumentList'     = @( '-f', $ScriptFile,
      '-ExecutionPolicy', 'Bypass',
      '-NoProfile'
   )
   }
   Start-Process @Start -Wait
   #Start-Process -FilePath ".\connect.ps1" -Wait
   Write-Output "Launching script...Completed"
   ```

   - But all this would do is start another `Orchestrator.Sandbox.exe` just like the hybrid workers use to run runbooks.

4. Next I tried creating a scheduled task and have the runbook run the scheduled task. It would then wait for `powershell.exe` to exit for it to know that it completed:

   ```powershell
   Write-Output "Starting scheduled task..."
   Start-ScheduledTask -TaskName 'Start-PhoneNumbers'
   Write-Output "Starting scheduled task...Completed"

   Start-Sleep -Seconds 5

   $p = Get-Process -Name "powershell"

   If ( $($p.count) -gt 0)
   {
   Write-Output "Scheduled task launched successfully"
   Write-Output "Checking if completed..."
   do
   {
      Try
      {
         $p = Get-Process -Name "powershell" -ErrorAction "Stop"  #| Where-Object { $_.id -ne $pid } - This doesn't work because process is Orchestrator.Sandbox.exe
         #write-output "count: $($p.count)"
      }
      Catch
      {
         continue
      }
   
      Start-Sleep -Seconds 1

   } until ( $($p.count) -eq 0)

   Write-Output "Checking if completed...Completed"

   }
   Else
   {
   Write-Output "Scheduled task did not launch successfully"
   Write-Error "Terminating runbook"
   }
   ```

   - This seemed to work as the task would run and powershell would exit, but it never returned back to the runbook that it was completed for some reason.

5. The one that ended up working was to monitor the last write time of a file that the script creates and, if it less than five minutes old, exit successfully.

   ```powershell
   Write-Output "Starting scheduled task..."
   Start-ScheduledTask -TaskName 'Start-PhoneNumbers'
   Write-Output "Starting scheduled task...Completed"

   Start-Sleep -Seconds 5

   $file = Get-Item "S:\sched-tasks\phone-numbers\numbers.csv"
   $written = $($file.Lastwritetime)
   $time = New-TimeSpan -Start $written -End (Get-Date)
   If ( $($time.minutes) -lt 5 )
   {
   Write-Output "Scheduled task did not launch successfully"
   Write-Error "Terminating runbook"
   }
   Else
   {
   Write-Output "Scheduled task launched successfully"
   Write-Output "Checking if completed..."
   do
   {
      $file = Get-Item "T:\sched-tasks\phone-numbers\numbers.csv"
      $written = $($file.Lastwritetime)
      $time = New-TimeSpan -Start $written -End (Get-Date)
      Start-Sleep -Seconds 1
      #write-output "time: $($time.minutes)"
   } until ( $($time.minutes) -lt 5)
   Write-Output "Checking if completed...Completed"
   }

   Write-Output "Runbook completed"
   ```

6. Couple notes:

   - This works because the script is launched every 2 hours so if the CSV is less than 5 minutes old there is a problem.
   - The support request was closed because they were unable to determine what to do as of now
   - I feel in a later version of Azure Automation that running powershell runbooks and not workflows will eventually launch a `powershell.exe` process instead of a `Orchestrator.Sandbox.exe` process that will not have these limitations.
   - I don't really like this setup because I have to keep a file outside of source control on each hybrid worker. I also have to maintain a scheduled task on each hybrid worker. Oh well, everything else seems to be working so far and hopefully we can find a way to query this information directly with MS Graph API at some point...
