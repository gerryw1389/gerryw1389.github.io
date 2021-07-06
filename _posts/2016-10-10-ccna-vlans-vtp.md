---
title: 'CCNA: VLANs/ VTP'
date: 2016-10-10T02:16:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-vlans-vtp/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Do not use DTP (auto), set all ports to access or trunk mode!

#### To create a VLAN on a switch:

   ```tcl
   Switch(config)#vlan 100
   Switch(config-vlan)#name ITDept
   Switch(config-vlan)#exit
   ```

#### To create a VLAN on a router:

   ```tcl
   Router#vlan database
   Router(vlan)#vlan 10
   Router(vlan)#exit
   Router#config t
   Router(config)#int vlan 10
   Router(config-if)#ip address 192.168.1.1 255.255.255.0
   Router(config-if)#description IT_VLAN
   Router(config-if)#ipv6 address
   Router(config-if)#no shut
   Router(config-if)#end
   ```

#### To assign a VLAN to an interface:

   ```tcl
   Switch(config)#vlan 99
   Switch(config-vlan)#name Management
   Switch(config)#config t
   Switch(config)#interface f0/1
   Switch(config-if)#switchport access vlan 99 # this tells the port to use vlan 99 only
   Switch(config-if)#interface vlan 99 # just going into the interface brings it up
   Switch(config-if)#ip address 192.168.99.1 255.255.255.0
   Switch(config-if)#end
   ```

#### To assign multiple VLANs to an interface (trunking):

   ```tcl
   Switch(config)#int fa0/0
   Switch(config-if)#switchport mode trunk # this could be all you need to establish trunks between two switches. You don't have to establish the VLANs.
   Switch(config-if)#switchport nonegotiate # recommended to disable DTP
   Switch(config-if)#switchport trunk native vlan 99 # You have to change the native vlan from within an interface. By default this is VLAN1 and should be changed for security.
   Switch(config-if)#switchport trunk allowed vlan 100 # this only allows VLAN 100
   Switch(config-if)#switchport trunk allowed vlan 10, 20-30 # over-rides it to include vlans 10 and 20-30
   Switch(config-if)#switchport trunk allowed vlan add 12 # this is the correct way to add a new VLAN without overridding
   Switch(config-if)#switchport trunk encapsulation dot1q # uses the open standard 802.1q for encapsulation (most common)
   Switch(config-if)#end
   ```

#### Show Commands:

   ```tcl
   show vlan
   show vlan brief
   show interfaces vlan
   show interfaces f0/1 switchport
   show interfaces f0/2 trunk
   ```

---

#### VTP:

VTP is a Cisco protocol that allows you to create a client/server way to share VLAN info for all switches in a domain.

#### Enable VTP Server:

   ```tcl
   Switch(config)#vtp domain Mydomain.net #enables VTP - domain must match on all switches
   Switch(config)#vtp password cisco # password must match on all switches
   Switch(config)#vtp mode server # set this to server, client, or transparent
   Switch(config)#vtp version 2 #note that catalyst switches can only run v1 and v2/1 are NOT compatible!!
   Switch(config)#vtp pruning # This will tell the switch that VLANs not having any access ports on the end switch are removed from the trunk.
   Switch(config)#end
   ```

#### Enable VTP Clients:

   ```tcl
   Switch(config)#vtp domain Mydomain.net #enables VTP - domain must match on all switches
   Switch(config)#vtp password cisco # password must match on all switches
   Switch(config)#vtp mode client # set this to server, client, or transparent
   Switch(config)#vtp version 2 #note that catalyst switches can only run v1 and v2/1 are NOT compatible!!
   Switch(config)#end
   ```

#### To set VTP Pruning:

   ```tcl
   # Pruning is disabled by default. You enable it globally and then use it per interface.
   Switch(config)#vtp pruning
   Switch(config)#int fa0/2
   Switch(config-if)#switchport trunk pruning vlan remove 3,10-15 # more info http://www.lab.dit.upm.es/~labrst/config/ciscopedia/switchport%20trunk%20pruning.htm
   ```

#### Show Commands:

   ```tcl
   show vtp status
   show vtp password
   show vtp counters # VTP servers should show only the received counters incrementing, while any VTP clients should show only the transmitted counters incrementing.
   show interface switchport
   show interface trunk
   ```

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)