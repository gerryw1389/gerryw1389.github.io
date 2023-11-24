---
title: 'SCCM: Deploy Batch File'
date: 2018-11-23T16:49:37+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/sccm-deploy-batch-file/
tags:
  - SysAdmin
  - WindowsServer
tags:
  - ConfigManagement
---
<!--more-->

### Description:

This is an example of how to use SCCM run a batch file on a collection of servers.

### To Resolve:

1. Go to Assets and Compliance\Device Collections\SiteName\Security Update Collections, right click and "Create A New Device Collection"

   - General Tab:  
   - Name: Whatever  
   - Limiting Collection: All Server With Clients
   - Membership Rules:  
   - Skip this tab, we will configure after it gets created  
   - Finish

2. Now go to your collection, right click => Properties:

   - Go to Membership rules tab and create a new one:  
   - Name: Whatever => I chose "query by computer name"  
   - Click "Edit Query Statement"
   - Click "Show Query Language" button on bottom right:  
   - Copy/Paste with your own list of servers:

   ```powershell
   select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,   SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System where SMS_R_System.Name in ( "server1", "server2", "server3"    )
   ```

3. Copy your batch file to your SCCM Distribution point => `\\sccmServerName\SoftwarePackages\WhateverSubFolder`. Make sure that "Domain Computers" still has read/execute permissions to the share.

4. Next, create a package  

   - \Software Library\Overview\Application Management\Packages  
   - Package Tab:  
   - Give it a name
   - Program Type tab: Standard program radio button
   - Standard Program tab:  
   - Name: WhatYourBatchFileDoes  
   - Command line: `cmd /c \\sccmServerName\SoftwarePackages\myscript.bat`  
   - Startup folder:  
   - Run: Normal  
   - Program can run: Where or not a user is logged in  
   - Run Mode: Administrative rights  
   - Drive mode: Run with UNC name
   - Next-Next-Finish

5. Right click => Deploy

   - General Tab:  
   - Set it to the collection from step 1  
   - Check box to "use default distribution point"
   - Scheduling Tab:  
   - New Assignment schedule, give the time

6. At this point, it should deploy at whatever time you specified. Monitor the results in the monitoring tab of SCCM Console.