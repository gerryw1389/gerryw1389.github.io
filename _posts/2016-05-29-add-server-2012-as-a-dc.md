---
title: Add Server 2012 As A DC
date: 2016-05-29T03:56:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/add-server-2012-as-a-dc/
tags:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

So our main domain controller had issues updating the other month and we started thinking of a way to upgrade to a Server 2012 domain. Before reading, if you don't have a domain controller yet I would read up on [Setting Up A Domain Controller](https://automationadmin.com/2016/05/setting-up-a-domain-controller/) first. We decided we will do the following steps:

Steps in my task:  
   - Add a Server2012 VM to the domain.  
   - [Transfer existing FSMO roles to the new server.](https://automationadmin.com/2016/05/transferring-fsmo-roles/)  
   - [Decommission the previous FSMO role holder.](https://automationadmin.com/2016/05/to-decommission-a-previous-dc/)

### To Resolve:

1. In this example, I created a DC VM and joined it to the domain and set a static IP on it. Make sure point the DNS to to the PDC as the primary DNS server.

2. Server Manager => Install Roles and Features => Install AD DS, DHCP, and DNS. Reboot.

3. After reboot, you go back to Server Manager => Actions => Activate DHCP and go through the wizard to &#8220;Promote this machine to a Domain Controller&#8221;. Ignore the warnings about &#8220;A delegation for this DNS server cannot be created&#8230;&#8221;, add your recovery password, and then finish. It will initiate a reboot.

4. After reboot, just sign in to the VM and let the replication start. At this point I let it replicate for a few days&#8230;.

5. From here, the game is to just keep running dcdiag /e and repadmin /showrepl /errorsonly. And checking the Event Viewer every day.

   - I had an issue once where the newly joined DC had the system time wrong. Follow [this](https://automationadmin.com/2016/05/event-1925-on-new-dc/) article to resolve.

   - I had an issue once where the DHCP service kept showing errors in Event Viewer. Follow [this](https://automationadmin.com/2016/05/event-1059-dhcp-error/) article to resolve.