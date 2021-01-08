---
title: To Decommission A Previous DC
date: 2016-05-29T04:00:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/to-decommission-a-previous-dc/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

In this example, I have transferred FSMO roles from Server2008 to a newly joined Server2012 DC. All I have left to do is to decommision the Server2008VM and take it offline. Make sure that you don't start this process until after 48 hours since the Server2012 DC has been the primary domain controller.

The main rule to follow is &#8220;demote then decommission&#8221;.

   - Steps in my task:  
   - [Add a Server2012 VM to the domain.](https://automationadmin.com/2016/05/add-server-2012-as-a-dc/)  
   - [Transfer existing FSMO roles to the new server.](https://automationadmin.com/2016/05/transferring-fsmo-roles/)  
   - Decommission the previous FSMO role holder.

### For Server 2008:

1. Run => dcpromo => follow the prompts => reboot. The starts the demotion process.

2. Or by using cmd (preferred): `dcpromo /unattend /username: /userdomain: /password: /administratorpassword:`
   - After the reboot you can run dcpromo /uninstallbinaries to cleanup the server from ADDS files.

3. That demoted the server, now just use Server Manager to remove the role.

4. On the PDC, go to AD Sites and Services, locate the demoted DC and delete the DC.

5. On the PDC, go to AD Users and Computers, locate the demoted DC and delete the DC.

6. (Optional) Rejoin the domain as a regular computer would if wanted.

### For Server 2012:

1. Server Manager => Remove Roles => It will say that in order to remove the role you have to demote the server first. Click on the yellow triangle at the top of Server Manager to do this and reboot.

2. On the main DC, go to AD Sites and Services, locate the demoted DC and delete the DC.

3. On the main DC, go to AD Users and Computers, locate the demoted DC and delete the DC.

4. (Optional) Rejoin the domain as a regular computer would if wanted.

### References:

["Removing a Domain Controller from a Domain"](https://technet.microsoft.com/en-us/library/cc771844(v=ws.10).aspx)  
["Demoting Domain Controllers and Domains"](https://technet.microsoft.com/windows-server-docs/identity/ad-ds/deploy/demoting-domain-controllers-and-domains--level-200-)  
["Safely Demote a Windows 2008/r2 Core Domain Controller"](http://blog.ittoby.com/2013/06/safely-demote-windows-2008r2-core.html)  