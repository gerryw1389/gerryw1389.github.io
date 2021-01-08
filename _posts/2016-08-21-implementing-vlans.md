---
title: Implementing VLANs
date: 2016-08-21T17:05:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/implementing-vlans/
categories:
  - Networking
---
<!--more-->

### Description:

As a systems administrator, you will sometimes find yourself inheriting networks that don't have VLANs setup and it is your job to do so.

### To Resolve:

1. The first thing you want to do is determine your current network scope and then adjust from there.

   - Example: Network is 192.168.0.0/16. The router is at 192.168.1.1, and servers are put into 192.168.18.x
   - To fix, add 192.168.18.1/24 as a secondary IP on the interface to the servers, change each server's subnet mask to 255.255.255.0, and default gateway to 192.168.18.1.
   - Remove the 192.168.1.1/16 IP on the interface after at least a week of monitoring.

2. Create VLANs around AD groups. For example: users, servers, guests. Then:

   - Slowly move everyone over to their respective VLANs. Setup policy based routing between the VLANS based on the traffic monitors in the firewall for things like SQL communication, AD Auth, and Internet traffic for each VLAN; do a lot of testing.
   - Learn your networking equipment such as WAPs and how VLANs are configured through them.