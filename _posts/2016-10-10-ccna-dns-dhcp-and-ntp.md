---
title: 'CCNA: DNS, DHCP, and NTP'
date: 2016-10-10T02:43:58+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-dns-dhcp-and-ntp/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Configuring DNS, DHCP, and NTP on Cisco Routers

### To define static hosts

   ```tcl
   R1(config)#ip host TEST-HOST 10.0.0.3
   R1(config)#ipv6 host TEST-HOST 3FFF:1234:ABCD:1::3
   R1(config)#end
   R1#show hosts
   ```

### Configuring DNS

   ```tcl
   Router(config)#no ip domain-lookup # disables dns lookups, good for practicing but not in real world
   Router(config)#ip domain-lookup # enabled by default, this shows DNS as running
   Router(config)#ip name-server # sets a dns server, can use multiple
   R1(config)#ip name-server 192.168.1.2
   R1(config)#ip name-server 3FFF:1234:ABCD:1::2 # ipv6
   ```

### Show Commands:

   ```tcl
   show hosts
   debug domain
   ```

### Configure DHCP:

   ```tcl
   Router#configure terminal
   Router(config)#service dhcp
   #The next step is to create a DHCP pool which defines the IP address pool that will be allocated to clients.
   #In this example, pool name "SUBNET_A" will offer IP addresses from the 192.168.1.0/24 range:
   Router(config)#ip dhcp pool SUBNET_A
   Router(dhcp-config)#network 192.168.1.0 255.255.255.0
   Router(dhcp-config)#default-router 192.168.1.1
   Router(dhcp-config)#dns-server 8.8.8.8
   Router(dhcp-config)#domain-name mydomain.net # didn't work in packet tracer, probably work on router
   Router(dhcp-config)#lease 30 # didn't work in packet tracer switch, probably work on router
   Router(dhcp-config)#end
   Router#show ip dhcp binding
   ```

### To exclude a single address or a range of addresses, use the following:

   ```tcl
   Router(config)#ip dhcp excluded-address 192.168.1.1
   Router(config)#ip dhcp excluded-address 192.168.1.250 192.168.1.255
   ```

### To configure a DHCP Helper:

   ```tcl
   Router(config)#interface vlan 20
   Router(config-if)#ip helper-address 192.168.20.10
   Router(config-if)#end
   ```

### To configure an interface for DHCP:

   ```tcl
   Router(config)#interface vlan 20
   Router(config-if)#ip address dhcp
   Router(config-if)#end
   ```

### To configure DHCP Snooping (tells what ports can respond to DHCP Request):

   ```tcl
   Router(config)#ip dhcp snooping #enable globally
   Router(config)#interface vlan 20 # for one specific vlan (most common)
   # ip dhcp snooping trust - On specific interfaces
   ```

### Show Commands:

   ```tcl
   show ip dhcp binding
   show ip dhcp server statistics
   ```

### Configure NTP:

   ```tcl
   # Server
   R1#clock set 11:00:00 sept 4 2016
   R1(config)#config t
   R1(config)#ntp master # stratums are 1-15
   ```

### Client:

   ```tcl
   R1(config)#config t
   R1(config)#ntp server
   ```

### To manually configure time (not NTP):

   ```tcl
   R2#config t
   R2(config)#clock timezone CST -6 # tells the router -6 from GMT timezone
   R2(config)#end
   R2#clock set 12:40:00 20 10 2016
   ```

### Show Commands:

   ```tcl
   show ntp associations
   show ntp status
   show ntp peers #maybe?
   ```

