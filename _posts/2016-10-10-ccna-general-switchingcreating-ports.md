---
title: 'CCNA: General Switching/Creating Ports'
date: 2016-10-10T02:13:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-general-switchingcreating-ports/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

These commands are for general switching and creating ports in a Cisco router/switch.

#### To configure a single port

   ```tcl
   Router>enable
   Router#config t
   Router(config)#interface f0/5
   Router(config-if)#
   ```

#### To configure multiple ports at once

   ```tcl
   Switch(config)#interface range FastEthernet0/3 – 4, 24
   ```

#### Interface Options:

   ```tcl
   Switch>enable
   Switch#config term
   Switch(config)#interface f0/5
   Switch(config-if)#speed 100 # sets speed
   Switch(config-if)#duplex full # sets duplex mode - must match on both sides! Auto only recommended for Gigabit
   Switch(config-if)#description Web Server
   Switch(config-if)#no shutdown # all ports are shut down by default, you must turn them on by running this!
   Switch(config-int)#ip address # the most common command, sets an ipv4 address
   Switch(config-if)#ip address 10.0.1.3 255.255.255.0 secondary # You can set a secondary IP
   Switch(config-if)#bandwidth # Doesn't change the speed, just how routing protocols view an interface.
   Switch(config-if)#delay # Doesn't change the speed, just how routing protocols view an interface.
   ```

#### To create an access port: 

   - NOTE: All ports should be access ports by default, we still configure them to make sure. Switch to switch or switch to router should be trunk ports.

   ```tcl
   Switch(config)#interface f0/5
   Switch(config-if)#switchport mode access
   Switch(config-if)#switchport access vlan 100
   Switch(config-if)#switchport voice vlan 150
   ```

#### To create a trunk port:

   ```tcl
   Switch(config)#int fa0/0
   Switch(config-if)#switchport mode trunk
   Switch(config-if)#switchport nonegotiate # recommended to disable DTP
   Switch(config-if)#switchport trunk native vlan 99 # You have to change the native vlan from within an interface. By default this is VLAN1 and should be changed for security.
   Switch(config-if)#switchport trunk allowed vlan 100 # this only allows VLAN 100
   Switch(config-if)#switchport trunk allowed vlan 10, 20-30 # over-rides it to include vlans 10 and 20-30
   Switch(config-if)#switchport trunk allowed vlan add 12 # this is the correct way to add a new VLAN without overridding
   Switch(config-if)#switchport trunk encapsulation dot1q # uses the open standard 802.1q for encapsulation (most common)
   Switch(config-if)#end
   ```

#### To create a loopback port:

   ```tcl
   Switch(config)#interface loopback 0
   Switch(config-if)#ip address 192.168.20.1 255.255.255.0
   Switch(config-if)#exit
   ```

#### Show Commands:

   ```tcl
   show ip interfaces brief # normally typed: show ip int bri
   show interfaces
   ```

