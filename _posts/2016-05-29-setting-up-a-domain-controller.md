---
title: Setting Up A Domain Controller
date: 2016-05-29T03:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-a-domain-controller/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
  - Setup
---
<!--more-->

### Description:

Follow these steps to setup a Domain Controller using Windows Server 2008. In this example, I am installing AD DS, DNS, and DHCP for the first time for a client. If this is not the first server in the forest, skip ahead to [Add Server 2012 As A DC](https://automationadmin.com/2016/05/add-server-2012-as-a-dc/).

### To Resolve:

1. First answer key questions: Will they benefit? Is it practical? Who will support it? If a network has over 20 computers, it's highly recommended. It's also a good idea if you have multiple locations that need to access a single database.

2. Once that is complete, first thing to do is to rename the computer to something familiar like &#8220;DC01&#8221; or &#8220;Server&#8221;.

3. Set a static IP address.

4. Let's get started&#8230; Start => Server Manager => Install Roles. Select AD DS, DNS, and DHCP select okay for each one.

5. Installing DHCP: If the DC is going to be a DHCP server, you need to disable DHCP on the router or look for a &#8220;forward to DC&#8221; setting.  
   - Parent Domain= Domain Name  
   - Primary => Static IP of the DC  
   - Secondary => Router IP Address  
   - Configure scope page => You can add DHCP ranges => 8 days for wired / 8 hours for wireless

6. Everything else is default, reboot the server.

   - After researching this for a while, I have found that naming the domain is a common question. Best practice seems to be int.company.com or internal.company.com, but NOT .local on the end. This was used often and is highly debated.

7. After reboot, go to &#8220;Server Manager&#8221; => Roles => Active Directory => Install and then run &#8220;DC Promo&#8221; if it does not do it automatically.

   - Functional Level- Needs to match the networks OS's. If XP office, select 2003, if Windows 7, select Server 08r2 or whatever OS the server is. When installing AD, Windows creates a folder in the directory &#8220;C:\Windows\SYSVOL&#8221; which contains the bulk of AD info and is shared out automatically. After this, it will ask where to install the &#8220;Log, Database, and SYSVOL&#8221; folders. Keep it default unless it's a large setup like in a forest where you would select different paths. Next it will ask for a password in case you need to restore AD to a previous time in Windows Restore => use the &#8220;Domain Administrator&#8221; password.

8. AD is now installed. Next step is to configure users. Key notes here is copying a user creates a new user with the same policies and groups attached to the user copied. MAKE A HABIT OF COPYING USER ACCOUNTS INSTEAD OF CREATING NEW ONES. Creating a group => Left column, select &#8220;Builtin&#8221; under your domain name => Right click New- Group => Create a group name => and Add users by going to users and selecting multiple users and adding them to the group. You can also select other groups and go to properties => Members => and add your custom group to theirs.

9. Now you can configure policies for the domain. Start => Group Policy Management => Creates new policies and configures them. There will be a section on this later on.

10. The domain is officially setup. The last thing to setup would be DHCP scopes depending on the network and make sure that DNS has started (make sure the &#8220;dns server&#8221; service is running) and also go to DNS and make sure it's populating.

11. So we should then add the following icons to the task bar or desktop (your preference): Active Directory Users and Computers, Group Policy Management, DNS, DHCP, and Event Viewer. I like to open each one up and make sure the following:

   - DHCP => Your Domain Name => IPv4 => Server Options => Do you see a 003 Router record? Add your gateway IP if it's not there. Do you see a 006 DNS server record? Add your new DC there along with any other replication DC's. Do you see a 015 record there? If not, add your domain name there.

   - DNS => Server Name => Forward Lookup Zones => Domain Name => Do you see records?

   - Group Policy Management => Forest: Domain Name => Domains => DomainName => Default Domain Policy => Is is applied? Run `gpupdate /force` and `rsop.msc` (newer version is `gpresult /h c:\scripts\result.html`) to confirm. You should be good to go from here.

### To Demote a Domain to A Workgroup:

1. For workstations: Just take the workstation off the domain and reboot. You do this by `sysdm.cpl` => and &#8220;Change&#8221; to a workgroup.

2. On the Domain Controller , Run => dcpromo => Follow the prompts and remove the computer from the domain. You will still need to go to Server Manager and remove the role afterwards. Most likely will need to remove the DHCP and DNS roles as well. Note that the Small Business Server OS has to be on a domain but you can still authenticate with users on a workgroup through local account authentication.