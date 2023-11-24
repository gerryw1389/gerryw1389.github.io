---
title: Transferring FSMO Roles
date: 2016-05-29T03:58:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/transferring-fsmo-roles/
tags:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

In this example, I will be transferring FSMO roles from Server2008 to a newly joined Server2012 DC.

   - Steps in my task:  
   - [Add a Server2012 VM to the domain.](https://automationadmin.com/2016/05/add-server-2012-as-a-dc/)  
   - Transfer existing FSMO roles to the new server.  
   - [Decommission the previous FSMO role holder.](https://automationadmin.com/2016/05/to-decommission-a-previous-dc/)

The five FSMO roles are:

   - Schema Master  
   - Domain Naming Master  
   - Infrastructure Master  
   - Relative ID (RID) Master  
   - PDC Emulator

### Prerequisites:

1. Make sure DC you want to promote to PDC has been a domain controller member server for at least 48 hours.

2. Make sure that the functional level is at least in Windows 2003 mode. Open up Active Directory Domains and Trusts => Right Click => Raise forest functional level.

   <img class="alignnone size-full wp-image-670" src="https://automationadmin.com/assets/images/uploads/2016/09/installing-server-2012-as-a-dc.png" alt="installing-server-2012-as-a-dc" width="520" height="367" srcset="https://automationadmin.com/assets/images/uploads/2016/09/installing-server-2012-as-a-dc.png 520w, https://automationadmin.com/assets/images/uploads/2016/09/installing-server-2012-as-a-dc-300x212.png 300w" sizes="(max-width: 520px) 100vw, 520px" />

   
3. Now we need to find out which Domain Controller holds the Single Master Operation Roles. On one of the domain controllers, navigate to the `C:\Program Files\` directory and run the command: `netdom query fsmo`. This will return the current FSMO domain controller.

4. Next run the following command and look for any errors: `dcdiag /e /c /v >dcdiag.txt`. This will tell us if there is any replication errors going on in the domain.

5. Next run the following command and look for any errors: `repadmin /showrepl /all /verbose > c:\scripts\repadmin.txt`. Make sure to fix any issues with these before proceeding.

6. On the DC VM you want to make the PDC, make sure to point its NIC settings to your current DNS server.

7. On the DC VM, open the DHCP Management console and expand the Scope tree and select Scope Options. Choose option 006 DNS Servers and add your new DC as a secondary DNS server.

### Doing the Transfer:

1. On the Server2008 DC, run the following command: `regsvr32 schmmgmt.dll`

2. Run => `mmc` => Add: Active Directory Schema

3. Once its loaded, Right click the Active Directory Schema string and select the option Change Active Directory Domain Controller.

4. In the Change To radio button list, choose the Server 2012 DC. Click OK on the pop up Window.

5. Right click the Active Directory Schema string again and choose the option "Operations master" => Change => Enter the hostname of the Server 2012 DC => OK.

6. Now get on the Server 2012 DC. Open Active Directory Users and Computers => Right click your domain name => Operations Masters => Change => Enter hostname of your WS2012DC => Yes => OK.

7. Move to the PDC tab on the same screen and select Change => Enter hostname of your WS2012DC => Yes => OK.

8. Move to the Infrastructure tab on the same screen and select Change => Enter hostname of your WS2012DC => Yes => OK.

9. Open ADSI Edit on the WS2012DC computer => Right Click => Connect To => (Leave Defaults (Default Naming Context)) => OK.

10. Back on the Windows Server 2008 DC box, open Active Directory Domains and Trusts => Right Click => Operations Master => Change => Enter the hostname of the Server 2012 DC => OK.

11. Done! To verify, just run the following command: `netdom query fsmo`

12. Not sure if it is needed, but I usually adjust the time service as well:

   - On the WS2012DC, run:

   ```escape
   w32tm /config /manualpeerlist:time-a.nist.gov /syncfromflags:manual /reliable:yes /update  
   net stop w32time && net start w32time  
   w32tm /resync /rediscover  
   w32tm /query /status
   ```

   - On the WS2008DC, run:

   ```escape
   w32tm /config /syncfromflags:domhier /update  
   w32tm /resync /rediscover  
   net stop w32time && net start w32time
   ```

   - On the WS2012DC, verify that it works by running: `w32tm /monitor`

13. Verify that it has the hostname of your WS2012DC as the first entry.

### References:

["Transferring FSMO roles from WS 2008R2 DC to WS 2012 DC"](https://winsvr.wordpress.com/2012/12/17/transferring-fsmo-roles-from-ws-2008r2-dc-to-ws-2012-dc/)  

["Configuring the Windows Time Service for Windows Server"](http://blogs.msmvps.com/acefekay/2009/09/18/configuring-the-windows-time-service-for-windows-server/)