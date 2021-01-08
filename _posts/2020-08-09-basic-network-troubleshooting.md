---
title: Basic Network Troubleshooting
date: 2020-08-09T11:10:16-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/basic-network-troubleshooting
categories:
  - SysAdmin
  - Networking
---
<!--more-->

### Description:

I usually refer people to this post so that they can get a clear understanding of the path of a packet from on-prem to Azure. For some reason saying `Source server/source port => Local switch/routers => NSG in Azure (if Azure/AWS) => Destination Server/port` doesn't click with most people.

### To Resolve:

1. Packet starts at Source server
	
   - Local firewall either allows or blocks. Depending on OS, you need to check `outbound` rules:
     - Linux = firewall-cmd
	  - Windows = Windows Firewall

2. Packet is sent from source server through multiple switches and routers to get to destination server:

   - Local switches and routers
      - Check with your Operational Security team and Networking teams and tell them you are wanting a rule like:
      - `Allow 10.10.10.100 on 443/tcp => 4.25.65.32 on 443/tcp`
      - Replace source IP with source IP and outgoing tcp port with your outgoing. Do the same for the destination server but make sure its tcp is its `incoming` port.

3.  If the other servers lives on-prem skip this section. If it lives in AWS/AZure, you will need to login to Web UI or use cmdline tools to add the same firewall rule you just requested for the Network/ Operational Security teams at the security group level:

    - In Azure
      - Search for NSG (Network Security Group) and find the one attached to your destination server. You could also go your server, go to its NIC, and see which NSG it is assigned to.
      - Either way, add an `incoming` rule to allow from the source server in step 1.
    - In AWS
      - Same thing, but they are called Security Groups

4. Destination Server:
   
   - Local firewall either allows or blocks. Depending on OS, you need to check `inbound` rules:
     - Linux = firewall-cmd
	  - Windows = Windows Firewall

