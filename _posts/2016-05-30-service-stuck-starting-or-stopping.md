---
title: Service Stuck Starting Or Stopping
date: 2016-05-30T05:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/service-stuck-starting-or-stopping/
tags:
  - Windows
---
<!--more-->

### Description:

If you have an issue with a service that is stuck Starting or Stopping but it won't complete, follow these steps:

### To Resolve:

0. **Update**: This is much easier to do this with powershell. For example, with print spooler you can do:

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

1. Query the process => To kill the service you have to know its PID or Process ID. To find this just type the following in at a command prompt: `sc queryex servicename`

   <img class="size-full wp-image-694 aligncenter" src="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-1.png" alt="service-stuck-1" width="726" height="231" srcset="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-1.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-1-300x95.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

   - Replace `servicename` with the services registry name. For example: Print Spooler is spooler. (See Picture)

2. Identify the PID => After running the query you will be presented with a list of details. You will want to locate the PID. (Highlighted)

   <img class="alignnone size-full wp-image-695" src="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-2.png" alt="service-stuck-2" width="726" height="228" srcset="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-2.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-2-300x94.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

3. Run the `TaskKill` command => Now that you have the PID, you can run the following command to kill the hung process: `taskkill /f /pid [PID]`

   - This will force kill the hung service. (See Picture)

   <img class="alignnone size-full wp-image-696" src="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-3.png" alt="service-stuck-3" width="726" height="228" srcset="https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-3.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/service-stuck-3-300x94.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

4. Another way to stop a stopping service:

   - Set all restart of service options to Take No Action:  
   - Run => `services.msc` => right-click Target-Service => Properties => Recovery tab #Make sure the First\Second\Subsequent failures are all set to &#8220;Take No Action&#8221;

   - Get the PID of your target service using:

   ```powershell
   sc queryex wuauserv
   ```

   - Kill the process:

   ```powershell
   taskkill /f /pid 334
   ```

   - Try starting the service.

5. Never tried, but you could try stopping all processes with a specific service by using:

   ```powershell
   TASKKILL /F /FI "SERVICES eq wuauserv"
   ```

   - Powershell way to kill all hung services:

   ```powershell
   $Services = Get-WmiObject -Class win32_service | Where-Object {$_.state -eq 'stop pending'}
   foreach ($service in $Services) 
   {
      try
      {
         Stop-Process -Id $service.processid -Force -PassThru -ErrorAction Stop
      }
      catch
      {
         Write-Error -Message "Error : $_.Exception.Message"
      }
   }
   ```

