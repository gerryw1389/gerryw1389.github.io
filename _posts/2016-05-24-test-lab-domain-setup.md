---
title: 'Test Lab: Domain Setup'
date: 2016-05-24T14:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/test-lab-domain-setup/
tags:
  - Networking
  - WindowsServer
tags:
  - TestLab
  - ActiveDirectory
---
<!--more-->

### Description:

These are the steps I took to put my VMs on a domain. I did not want to make this domain public, just a test domain.

### To Resolve:

1. Follow the steps in Virtual Network First.

2. Start up the Server OS VM. Then, Run => `ncpa.cpl` and set the settings like this:

   - IP Address: 10.10.13.10 (or whatever subnet you chose)  
   - Subnet: 255.255.255.0  
   - Default Gateway: 10.10.13.1
   - Primary DNS: 10.10.13.10 (we will install the DNS role shortly)  
   - Secondary DNS: 8.8.8.8

3. Enabled the "Active Directory Directory Services" role on the Server 08 VM.

4. Ran `dcpromo.exe` to finish the install and installed the DNS service. Rebooted.

5. Started the DNS service and let it auto populate. You officially have a Domain Controller!

6. Went to the users and made one of them a domain admin.

7. Installed the "DHCP Server" role with a DHCP range of `10.10.13.11-10.10.13.100` (I only have 4 VMs at this point). Reboot.

8. Renamed the domain admin account to a user `firstname.lastname`.

9. Created an account called "Administrator" with limited permissions in order to [increase security](https://technet.microsoft.com/en-us/library/cc700835.aspx)

### For the Clients:

1. Run => `ncpa.cpl` Set them to obtain automatically. I had initially foobar'd my network when I did this the first time by not using the steps above (I had initially skipped the Virtual Network and just had all VMs on "Bridged") and had to keep switching to the server and tweaking the DNS and DHCP service settings on the Domain Controller but I learned quite a bit. Make sure the "Router" entry in DNS is pointing to "10.10.13.1" or "x.x.x.1" depending on the subnet you chose in [Test Lab: Virtual Network](https://automationadmin.com/2016/05/test-lab-virtual-network/)

2. Run => `sysdm.cpl` => Join them to the domain, use the domain admin credentials to get in. Reboot.

3. (Optional) I created a regular domain user on the DC (Domain Controller) so they (I mean me) could login on each of the client VMs. This is common practice as people will not be using the domain admin credentials on a domain. This should only be used by the Systems Administrator and regular end users should not know the credentials.