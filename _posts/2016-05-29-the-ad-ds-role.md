---
title: The AD DS Role
date: 2016-05-29T03:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/the-ad-ds-role/
tags:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Active Directory is a direct product of domains. To be on a domain means a Windows Server computer has been configured with the ADDS role which essentially means the server is called a &#8220;domain controller&#8221; and all the other computers will connect to it and they are called &#8220;clients&#8221;. Domain controllers often have backups (it is general best practice to have at least two DC's on every domain) so clients on the network can still connect to the domain if a single DC fails.

The main reason people place computers on a domain is enhanced security and for a central point of management. All users, computers, printers, networking, etc. could be managed through a single domain controller in a smaller network. The trend nowadays is to virtualize many servers and have each perform a simple task. This is so that if an issue arrives, you can reboot your WSUS server, for instance, and not worry about it effecting your ADDS server. The main way a DC controls clients' is through Group Policy. A &#8220;Group Policy Management&#8221; console allows administrators a full range of tools to control aspects of their networks.

For a domain with around 10 computers, the DC usually is just a server with the &#8220;ADDS, DNS, and DHCP&#8221; roles configured in which all the clients on the network will be set to &#8220;automatically obtain&#8221; on their NIC settings (Run => `ncpa.cpl` => Local Area Connection => Properties => IPv4 Settings).

For a domain with 50 or more computers, there is often a group of servers that perform multiple roles such as:

1. ADDS Servers or domain controllers => replicated to 2 or more DC's on the network. See [Setting Up A Domain Controller](https://automationadmin.com/2016/05/setting-up-a-domain-controller/) to learn how to setup a DC.

2. DNS servers => replicated to 2 or more DC's on the network.

3. DHCP Server => Usually only one on the network so computers can be set to obtain IP settings automatically without confliction. Note that routers need to have their DHCP servers turned off when a server is configured with the DHCP role. Also imaging servers need attention as there needs to be only one per network.

4. RDS Servers => Some companies have clients that use VDI => Virtual Desktop Infrastructure where clients will connect to their desktops through a RDS server (Windows Server configured with the RDS role).

5. WSUS Servers => Windows update servers => These servers push Windows updates at specific intervals.

6. Many more&#8230; => See &#8220;[Server Roles](https://automationadmin.com/2016/05/server-roles-overview/)&#8221; for other roles Windows Server can take on. Note there is also many &#8220;Features&#8221; Windows Server can be configured to use.