---
title: 'CCNA: General/Static Routing'
date: 2016-10-10T02:28:51+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-generalstatic-routing/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

General Routing commands

#### How to set a static route:

   ```tcl
   Router(config)#ip route [destination_network] [mask] [interfaceName] [cost]
   Router(config)#ip route 210.22.22.2 255.255.255.0 fa0/0 1
   ```

#### For ipv6:

   ```tcl
   R1(config)#ipv6 route [ipv6-prefix/prefix-length] [next-hop-address | [interface][distance | multicast | tag | unicast]

   R1(config)#ipv6 route 3FFF:1234:ABCD:0001::/64 Fa0/0 unicast # to subnet 3FFF:1234:ABCD:0001::/64, will forward traffic out of the FastEthernet0/0 interface. This route will be used only for Unicast traffic.

   R1(config)#ipv6 route 3FFF:1234:ABCD:0002::/64 Se0/0 FE80::2222 multicast # to subnet 3FFF:1234:ABCD:0002::/64, will forward packets to that subnet out of Serial0/0 using the Link- Local address of the next-hop router as the IPv6 next-hop address. This route will be used only for Multicast traffic.

   R1(config)#ipv6 route ::/0 Serial0/1 FE80::3333 # a default route pointing out of interface Serial0/1 is also configured. This default route will forward packets to unknown IPv6 destinations via Serial0/1 using the Link-Local address of the next-hop router as the IPv6 next-hop address.
   ```

#### To Create a default gateway (switch):

   ```tcl
   Switch(config)#ip default-gateway 192.168.1.1# only do this if ip routing is disabled like on a switch.
   ```

#### To set the default gateway (router):

   ```tcl
   # From my understanding, this command is issued when you use dynamic protocols that want to choose the route dynamically instead of a static catch-all route.
   Router(config)#ip default-network
   Router(config)#ip default-network 192.168.1.1
   ```

#### To create a passive interface:

   - This is an important command. We use it often to configure dynamic protocols to only work on one side of a router while keeping the ports you specify with this command free from routing protocols being advertised or passed over. Think about it, end devices do not need to see OSPF or EIGRP packets => so we set this up!

   ```tcl
   Router(config)#passive-interface [interface number]
   Router(config)#passive-interface fa0/2
   ```

#### Ping/Tracert:

   ```tcl
   R2#ping 10.1.1.1 source 10.2.2.2 repeat 10 # see protocols section to determine symbol meanings.
   R2#tracert 8.8.8.8
   ```

#### Show Commands:

   ```tcl
   show ip route
   show ip route 80.1.1.1
   show ip protocols # shows if dynamic routing protocols have been enabled
   show ipv6 route static
   show ipv6 static [prefix] [detail] ex: show ipv6 static 3FFF:1234:ABCD:1::/64 detail
   ```

#### Cisco Administrative Distance

   - Route Source => Default Distance Values
   - Connected interface => 0  
   - Static route => 1  
   - EIGRP summary route -5  
   - External BGP => 20  
   - Internal EIGRP => 90  
   - IGRP => 100  
   - OSPF => 110  
   - IS-IS => 115  
   - RIP => 120  
   - EGP => 140  
   - ODR => 160  
   - External EIGRP => 170  
   - Internal BGP => 200  
   - Unknown 255*

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)