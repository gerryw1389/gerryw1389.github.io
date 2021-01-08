---
title: 'Veeam Endpoint Stuck On &#8220;Backing Up&#8221;'
date: 2017-01-14T06:58:45+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/veeam-endpoint-stuck-on-backing-up/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Follow these steps to reset the database for Veeam Endpoint in the event that it gets stuck on &#8220;starting backup&#8221;.

### To Resolve:

1. Run => `services.msc` => Stop the &#8220;Veeam Endpoint Backup Service&#8221;. If it won't, open up an admin command prompt and type: `sc query ex (service name)`. Note you can get this from the right clicking the service => Properties and copying the service name.

2. Open task manager and get the PID of the process that cooresponds to the service name. type: `taskkill /pid (pid number) /f`

3. It's much easier to do this with powershell. For example, with print spooler you can do:

   ```powershell
   get-service | ? { $_.DisplayName -like "*print*" }

   Status   Name               DisplayName
   ------   ----               -----------
   Stopped  PrintNotify        Printer Extensions and Notifications
   Stopped  PrintWorkflowUs... PrintWorkflow_6dc45
   Running  Spooler            Print Spooler

   $ServicePID = (get-wmiobject win32_service | where { $_.name -eq 'spooler'}).processID
   Stop-Process $ServicePID -Force
   ```

3. Run => regedit => Navigate to: `HKEY\_LOCAL_MACHINE\SOFTWARE\Veeam\Veeam Endpoint Backup`  
   - Create the following key if it is not there:
   - Name = `RecreateDatabase`
   - Type = `DWORD (32 bit)`
   - Value = `1`

4. Start the Veeam Backup Service from step 1. The key recreates the database, so it may take a while.

5. After it starts, stop it again. Verify that the key changes from 1 to 0.

6. Now just start it again, it should be asking you to configure your &#8220;first&#8221; backup since it's a new database.

### References:

["How to manually reset your Veeam Endpoint Backup FREE database"](https://tinkertry.com/veeam-endpoint-backup-database-reset)  