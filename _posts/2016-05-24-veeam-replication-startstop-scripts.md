---
title: 'PS: Veeam Replication Start/Stop Scripts'
date: 2016-05-24T12:41:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-replication-startstop-scripts/
categories:
  - LocalSoftware
tags:
  - Scripting-Powershell
  - Backup
---
<!--more-->

### Description:

I used the following scripts to start/stop replications for Veeam so that we can run backups on the VM's in question. After saving them to C:\Scripts, I just set them as a scheduled task to run before and after backups are ran.

### To Resolve:

1. Veeam Stop Script:

   ```powershell
   #Enable the Veeam Powershell Snapin
   Add-PsSnapin VeeamPsSnapin

   #Specify Jobs
   $jobs = "VM1", "VM2", "VM3"
   $date = get-date -format G

   #Disable each job and verify its schedule options. Write the result to veeam-log.txt

   foreach ($job in $jobs)
      {
      $CurrentJob = Get-VBRJob -name $job
      $CurrentJob | Disable-VBRJob
         if ($CurrentJob.IsScheduleEnabled -eq $True)
         {
         write-output "$date = FAILED to disable $job. Please take appropriate action." >> C:\Scripts\veeam-log.txt
         }
         else
         {
         write-output "$date = Successfully disabled $job" >> C:\Scripts\veeam-log.txt 
         }
      }
   ```

2. Veeam Start Script:

   ```powershell
   #Enable the Veeam Powershell Snapin
   Add-PsSnapin VeeamPsSnapin

   #Specify Job names
   $jobs = "VM1", "VM2", "VM3"

   #Get the date for result output
   $date = get-date -format G

   #Enable each job and verify its schedule options. Write the result to veeam-log.txt

      foreach ($job in $jobs)
      {
      $CurrentJob = Get-VBRJob -name $job | Enable-VBRJob
         If ($CurrentJob.IsScheduleEnabled -eq $True)
         {
         write-output "$date = Successfully started $job" >> C:\Scripts\veeam-log.txt
         }
         else
         {
         write-output "$date = FAILED to enable $job. Please take appropriate action." >> C:\Scripts\veeam-log.txt
         }
      }
   ```

3. Set these as a scheduled task to run with your backups.

4. Source is maintained under [gwApplications](https://github.com/gerryw1389/powershell/blob/master/gwApplications/Public/Start-VeeamReplications.ps1) and [gwApplications](https://github.com/gerryw1389/powershell/blob/master/gwApplications/Public/Stop-VeeamReplications.ps1)