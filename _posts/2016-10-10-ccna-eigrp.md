---
title: 'CCNA: EIGRP'
date: 2016-10-10T02:34:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-eigrp/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

IP 88 / RFC 7868

Cisco proprietary, Autonomous systems that share routing tables, Advanced distance-vector routing protocol, Supports VLSM, Uses DUAL for quick convergence

### EIGRPv2:

   ```tcl
   R2(config)#router eigrp
   R2(config-router)#eigrp router-id 10.0.0.1
   R2(config-router)#network 192.168.1.0 0.0.0.255 # use wildcard masks instead of subnet masks
   R2(config-router)#no auto-summary # tells it not to send summary addresses. Good if you are using classless routing. Common.
   R2(config-router)#default information originate # distributes default gateway
   R2(config-router)#passive-interface fa0/0 # use this command to set an interface you don't want to share details to. Type "passive-interface default" to make all ports passive.
   R2(config-router)#restribute static # sends out static routes?
   R2(config-router)#neighbor 192.168.1.2 fa0/4 #I've never had to do this because it learns automatically
   R2(config-router)#metric weights tos k1 k2 k3 k4 k5 # to change default k values
   R2(config-router)#maximum-paths 4 # change load-balancing options
   R2(config-router)#variance 2 # https://supportforums.cisco.com/document/96651/troubleshooting-eigrp-variance-command
   R2(config-router)#traffic-share balanced # used for load balancing. It is enabled by default and does not appear in the running configuration, even if manually configured.
   redistribute static metric [bandwidth] [delay] [reliability] [load] [MTU] # example above, not on CCNA.
   ```

### Interface Commands:

   ```tcl
   Router(config)#int fa0/1
   R1(config-if)#ip hello-interval eigrp 1 3 # ip hello-interval eigrp # replace ip with ipv6 for ipv6
   R1(config-if)#ip hold-time eigrp 1 3 # ip hold-time eigrp # replace ip with ipv6 for ipv6
   R1(config-if)#ip bandwidth-percent eigrp 1 75 # ip bandwidth-percent eigrp # replace ip with ipv6 for ipv6
   R1(config-if)#ip summary-address eigrp 150 0.0.0.0 0.0.0.0 # this creates a summary address (static with a metric of 5)
   R1(config-if)#bandwidth 1544# Cosmetic command. Takes 10,000,000 and divides by lowest interface bandwidth, rounded down. K1 value.
   R1(config-if)#delay 100 # Cosmetic command. Divides sum of all delays by 10. K3 Value
   ```

### EIGRPv6:

   ```tcl
   R1(config)#ipv6 unicast-routing
   R1(config)#ipv6 router eigrp 1
   R1(config-router)#eigrp router-id 1.1.1.1
   R1(config-router)#no shutdown # has to be issued when using ipv6
   R1(config-router)#exit
   R1(config)#interface GigabitEthernet0/0
   R1(config-if)#ipv6 address 3fff:1234:abcd:1::1/64
   R1(config-if)#ipv6 enable
   R1(config-if)#ipv6 eigrp 1
   R1(config-if)#exit
   ```

### Securing With MD5:

   ```tcl
   R1#conf t
   R1(config)#key chain MyKeys
   R1(config)#key 0
   R1(config)#key-string MyPassword
   R1(config)#int fa0/1
   R1(config-if)#ip authentication mode eigrp 1 md5 # replace ip with ipv6 for ipv6
   R1(config-if)#ip authentication key-chain eigrp 1 MyKeys # replace ip with ipv6 for ipv6
   ```

### Show Commands:

   ```tcl
   show ip eigrp neighbors # shows the retransmit interval and the queue counts for the adjacent routers also need to be checked.
   show ip eigrp events
   show ip eigrp interfaces
   show ip eigrp topology # print Successor routes, FS routes, and routes that have not met the FC for the route specified in either command. P means passive which means it already found them. A means active which means it is actively looking - not good
   show ip eigrp topology all-links # all possible routes
   show ip eigrp
   show ip eigrp traffic
   show ip eigrp interfaces detail
   show ip eigrp neighbors detail
   debug eigrp packets
   show ip route
   show ip protocols # shows k values
   show ip interface brief
   ```

### IPv6

   ```tcl
   show ipv6 eigrp neighbors
   show ipv6 route
   show ipv6 protocols
   show ipv6 interface brief
   show ipv6 eigrp interfaces
   ```

### Main Notes:


Things that have to match between routers:  
-AS numbers  
-K values

K Values  
K1= Bandwidth => on  
K2 = Load => off  
K3 = Delay => on  
K4/K5 = Reliablility => off

Types of Packets:  
Hello => Unreliable / Multicast => Forms relationship  
Update => Reliable / Multicast/Unicast => Sends updates  
Acknowledgment => Unreliable / Unicast => Acknowledges the update, query, and reply messages.  
Query => Reliable / Unicast/Multicast => Asks about routes  
Reply => Reliable / Unicast => Response to a query

DUAL Algorithm Terms:  
   -  determines the best loop-free path and backup paths  
Successor => Neighboring router that is used for forwarding packets

Feasible Successor (FS) => Neighboring router that has a loop-free backup path to the same network as the Successor and satisfies the Feasibility Condition (FC)

Feasible Distance (FD) => The lowest calculated metric to reach the destination network. how far from you to get somewhere.

Reported Distance (RD) or Advertised Distance (AD) => The total metric to a destination network. how far from your neighbor.

Feasible Condition or Feasibility Condition (FC) => Condition is met when a neighbors Reported Distance (RD) to a network is less than the local routers feasible distance.

   - To be considered a FS, the AD must be less than the FD of the successor\*  
If there is a FS that doesn't make the cut, it will still be used – just not right away.

DV (Distance Vector) protocol loop prevention:  
Maximum distance => Hop limits  
Route poisoning =>  a method that prevents a certain network from sending data packets to a path destination that has already became invalid.  
Triggered updates => Don't have to wait to send an update  
Split horizon => Cannot send messages on interface that received them.  
Hold down timers => Have to wait a certain time before a route can come back up.

It builds these 3 tables in this order:  

1. Neighbor table => show ip eigrp neighbors  

2. Topology table => show ip eigrp topology  

3. Routing table => show ip route