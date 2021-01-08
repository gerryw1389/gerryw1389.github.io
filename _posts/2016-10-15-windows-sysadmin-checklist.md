---
title: Windows SysAdmin Checklist
date: 2016-10-15T03:19:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/windows-sysadmin-checklist/
categories:
  - SysAdmin
---
<!--more-->

### Description:

Use the following as a &#8220;challenge&#8221; for yourself to get better at Windows administration:

### To Resolve:

Before you do anything, you need to construct a closed network. I used VMware workstation to accomplish this and this assumes Server 2012R2. Also, for this purposes of this lab, turn off the windows firewall. In real life, you'll need to open ports as you see fit. In some networks, it's standard that all servers have their firewalls turned off. It really depends on your environment and what rules they follow.

1. Create two networks/VLANs (desktops and servers)

2. Install Windows Server (VM or standard hardware dealer's choice) GUI Mode.

3. Set up the server as a basic router between the two networks. You'll need 2 NICs to accomplish this (NOTE: unless you have a really good reason for this, you will never do this in a production environment. But because this is a lab situation in VMware workstation and because the product does not support routing between networks, you'll need to put something in place very basic. Windows routing will get the job done and will be on an MCP exam)

4. Install another server, single NIC on the server VLAN

5. Create your first active directory domain controller. Install this in GUI mode

6. Create another server but this time make it a core server. Make it a domain controller

7. Test AD replication via the gui and cmd.

8. Create an OU for your workstations, create an OU for your users, and an OU for groups. From now on, any new computer or new user account must go into their respective OU. DO NOT MOVE THE DOMAIN CONTROLLERS FROM THE DOMAIN CONTROLLER OU.

9. Check out DNS. Do you have a reverse look up zone? No? Then set it up.

10. Check out DNS. Records can get old and out of date and will screw up name to ip resolution. Make it so that scavenging happens automatically.

11. You need to block facebook.com via windows DNS. Make it so that when a DNS look up is performed, computers use a loop back address. Test this via cmd to make sure it resolves as expected.

12. Set up DHCP on the first domain controller.

13. Set up a scope to hand out IPs for the Desktop VLAN. Make it so that this DHCP scope will be able to give endpoints the information they need networking wise to join a domain

14. Install a Windows 7 or newer PC on the desktop VLAN

15. Your desktop's aren't getting IPs. Why? (hint: it's a routing/broadcast/relay issue)

16. Join that desktop to the domain

17. Now that you're getting IPs from your DHCP server, configure DHCP clustering. Loadbalancing or failover is your choice. Now test it.

18. Create a non-domain admin account in AD. Fill out the whole profile once the account is created.

19. Login to that desktop as a regular AD user and an Admin user. Try to install software under the non-admin account first and then the admin account. What's the difference?

20. Create another non-admin account. Make this non-admin user a local admin on that computer. Who else is also a local admin before you make any changes,

21. Review the attributes of that account in AD. You'll need advanced features for this.

22. Create an AD group. Add the first non-admin account to this group.

23. On that desktop, install the RSAT tools so you can remotely manage another computer

24. Setup remote management on the core server so that it can be managed from the MMC of another computer (there are a number of ways to do this)

25. Find out what server is holding the FSMO roles via the gui and the command prompt.

26. Split the FSMO roles between the servers. Try to keep forest level and domain level roles together.

27. On one of the domain controllers, create a file share set it so that only administrators and the second non admin account have access to it. Create another folder and give only the AD group you created permissions.

28. Use group policy to map both shares as network drives as a computer policy to the desktops.

29. Login to the desktop as the first domain user. Do you see the network drive mapped in windows explorer? No? Use gpresult to find out why. If you do see it, try to access the drive. You should be denied if you set permissions correctly. Login as the second domain user, they should be able to open the mapped drive.

30. What if the account in the group tries to access the second drive? You should be able to get in. Login to the workstation as the second non-admin account. You should not have access to this drive because you are not in the group. Do not log off. Add this account to the group. Can you access the drive now? No? Logoff and login back in. Can you access the drive now?

31. Remove the share from the domain controller. We don't like putting shares on domain controllers if we don't have to.

32. Build out another two servers and join it to the domain as member servers.

33. Install DFS and File server roles/features on both servers.

34. Create a file share on bother servers with the same folder name. Create files on both servers. Make sure they are different. (i.e server1 will have &#8220;TextDoc01&#8221;, server 2 will have &#8220;TextDoc02&#8221; in their shares).

35. Create a DFS name space. Add those shares to the name space.

36. On a domain joined work station, navigate to the DFS namespace you created. You should be able to see both files.

37. Create a DFS Replication group. Make it so that you have two way replication. You should now see both files on both servers. Make a change on one server and see if it replicates to another server. Does it work? Great. (you can shut down the file servers for now if you want or use them for the next step)

38. Create another server, join it to the domain, install Windows Deployment Service (WDS) and Windows Server Update Service (WSUS). You can choose to use the file servers you've already created instead of building out another VM. You only need one file server.

39. Configure WDS so that you can PXE boot to it on the network. Make any required changes to routing and DHCP if need be.

40. Upload an image to WDS for PXE deployment. Use WAIK and sysprep if you need to. (I haven't done this in the long time so you might not need sysprep anymore with WAIK, look it up)

41. Create a new desktop VM but do not install an OS on it. Instead tell it to perform a PXE boot when you turn it on, have it install the OS from here.

42. Configure WSUS so that you will only download Security updates for the desktop and server OS's ( highly recommend that you do not download any updates if you have access to the internet from this server)

43. Bonus points, install WSUS on another server and create a downstream server

44. Create some groups in WSUS. Servers and workstations will do nicely.

45. Create a new group policy that points workstations into the WSUS workstation group, points to WSUS for updates, and stop workstations from automatically downloading updates. Read up on approving and pushing updates since the current assumption is that there are no updates to be pushed in this enclosed test network since there is no internet access to down load them. I believe there is a way to manually add updates to WSUS but I'm a bit foggy on that. Research it. Do the same for servers.

46. On the domain controller or the the computer with RSAT installed, USING ONLY POWERSHELL:

   - Create a new AD user  
   - Create a new AD group  
   - Print a list of all domain users and computers, names only.  
   - Pull a list of users who have New York as their office. If no users have New York listed as their office, use powershell to set that attribute and then pull users who have New York as their office.  
   - Remove a user account from AD  
   - Add a user to a group  
   - Provision new AD users via a CSVl


### Someone Added:  

1. Deploy a Hyper-V host.  Create some redundant domain controller guest VMs, create a domain, and test failover of your domain controllers.

2. Create Active Directory Enterprise CA

3. Create an exchange server, and get webmail working internally, with full TLS. Set up a second exchange server, get them working in a DAG with redundant database copies

4. create a System Center Operations Manager, and configure monitoring to email you alerts. Bonus points: SNMP monitoring and syslog => https://technet.microsoft.com/en-us/library/hh457576(v=sc.12).aspx

5. Create a System Center Data Protection Manager, create a backup job, delete and recreate a VM from backup.

6. Configure System Center Operations Manager reporting and web interface/dashboards (this is complex! As is any datacenter-grade monitoring platform)

7. Create proper Log retention/rotation policy via AD for log files retained on individual servers for as log rotation to compress and archive old logs. (SCOM will do your long term retention/analysis)

8. Create a WSUS server, and deploy it to your guests via GPO.

9. After WSUS, set up System Center Configuration Manager, and switch updates to that. Disable the WSUS GPO after setting up and enabling the software update point for clients managed by SCCM.

10. Set up WDS and MDT for PXE and media based imaging. Learn task sequences and how they work.

11. Nix WDS then do this: Set up SCCM for system imaging => task sequences, learn how to update WIMs in place, PXE booting, etc. don't forget to integrate MDT into SCCM.

12. SCCM application deployment and updating

13. SCCM configuration items and baselines

14. BONUS: Something for help desk, alerting (Nagios, SolarWinds, etc.) and something to forward logs to like Greylog.