---
title: 'AD Won't Replicate After Restore'
date: 2016-08-21T16:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/ad-wont-replicate-after-restore/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

This post describes how to recover if you have broken AD replication due to a snapshot rollback (never do this on DC's!). In this example, we have two DC's. For whatever reason, we rollback one of the DC's using our hypervisor's snapshot functionality and break replication.

### To Resolve:

1. On the broken DC, verify that replication is broken by looking for the following symptoms: The Netlogon service is in a paused state, in the Directory Service event log a replication error was logged, Source was NTDS Replication with the Event ID 2095, in the same log look for two warnings, Source was NTDS General with the event ID's 1113 and 1115.

2. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `repadmin /options <hostname of this machine>`. This should return Current DC Options: `IS_GC DISABLE_INBOUND_REPL DISABLE_OUTBOUND_REPL`

3. OK it is broken, now lets fix it! Start by forcefully demoting this DC by running `dcpromo /forceremoval`. This will remove AD from the server without attempting to replicate any changes off. Once it is done and you reboot the server and it will be a standalone serve in a workgroup.

4. Run a metadata cleanup of the DC that was demoted on the DC that remains. On that DC, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type:

   ```escape
   ntdsutil  
   metadata cleanup  
   remove selected server <serverName>
   ```

   - Confirmation:  
     - Open Active Directory Users and Computers. In the domain of the removed domain controller, click Domain Controllers. In the details pane, an object for the domain controller that you removed should not appear.

     - Open Active Directory Sites and Services. Navigate to the Servers container and confirm that the server object for the domain controller that you removed does not contain an NTDS Settings object. If no child objects appear below the server object, you can delete the server object. If a child object appears, do not delete the server object because another application is using the object.

5. If the demoted DC held any roles, you need to seize these roles according to MS KB article 255504.

6. Once replication has occurred end to end in your environment you can rejoin the demoted server back to the domain then promote to a DC.

7. To prevent this, follow these best practices:

   - Do not use imaging software to take an image of the DC.
   - Do not take or apply snapshots of the DC.
   - Do not shut the Virtual Machine down and simply copy the virtual disk as a backup.
   - If you have the ability to "discard changes" as you do if you are running "Virtual Server 2005 R2", do not enable this type of setting on a DC Virtual Machine.
   - Use NTBACKUP.EXE, WBADMIN.EXE, or any third party software that is available as long as it is certified to be AD-compatible to take system state backups.
   - Only restore a system state to the DC or restore a full backup.

### References:

["DC's and VM's – Avoiding the Do-Over"](https://blogs.technet.microsoft.com/askds/2009/06/05/dcs-and-vms-avoiding-the-do-over/)    
["USN-rollback"](http://adfordummiez.com/?p=48)  