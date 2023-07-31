---
title: 'SCCM: Did Not Deploy Updates'
date: 2019-04-09T20:49:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/sccm-didnt-deploy-updates/
categories:
  - LocalSoftware
tags:
  - ConfigManagement
---
<!--more-->

### Description:

We had an issue where we checked the updates on Wednesday night and they showed 2 compliant and 63 pending. This can be normal as long as there is no errors. The next morning we came in to check on the updates and found the same screen:  

   - ![sccm](https://automationadmin.com/assets/images/uploads/2019/04/sccm.jpg){:class="img-responsive"}

We then checked the deployment package and the software update group and it showed they were downloaded and deployed:  

   - ![sccm-2](https://automationadmin.com/assets/images/uploads/2019/04/sccm-2.jpg){:class="img-responsive"}

But many of the clients only showed Endpoint updates, not Windows Updates installed:

   - ![sccm-3](https://automationadmin.com/assets/images/uploads/2019/04/sccm-3.jpg){:class="img-responsive"}

### To Resolve:

1. First check that the clients got the updates. You can see this by checking c:\windows\ccmcache and sorting by date modified. This should have the CAB files from the updates.  

   - In our case, they were deployed, so we just needed to recreate the deployment package and have it run again the next night.

2. Another thing you can do is run the following as Admin Powershell:

   ```powershell
   # One liner
   Remove-Item "c:\windows\system32\grouppolicy\machine\registry.pol" -Force; cmd /c "gpupdate /force"; Start-Sleep -Seconds 3; Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000032}";Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000113}";Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000114}"

   CMD:
   # Software Updates
   WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000113}" /NOINTERACTIVE
   # Software Assignments
   WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000108}" /NOINTERACTIVE
   # Source list
   WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000032}" /NOINTERACTIVE

   # PS:
   # Software Update Deployment Evaluation Cycle    
   Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000114}"
   # Software Update Scan Cycle    
   Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000113}"
   # Windows Installers Source List Update Cycle    
   Invoke-WMIMethod -ComputerName $env:ComputerName -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000032}"
   ```

3. If you see a bunch of Computers in the Unknown tab, use the following trick to copy them to a script:

   - Go to SCCM Console => Monitoring\Overview\Reporting\Reports\Software Updates => C Deployment States  
   - States 4 => Computers in a specific state for a deployment (secondary)
   - Now just look for those with unknown