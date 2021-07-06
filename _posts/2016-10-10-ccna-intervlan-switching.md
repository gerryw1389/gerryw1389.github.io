---
title: 'CCNA: InterVLAN Switching'
date: 2016-10-10T02:41:46+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-intervlan-switching/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

InterVLAN communications require a Layer 3 device. The most common is a &#8220;router on a stick&#8221; setup.

#### Router On A Stick Setup:

   ```tcl
   Router(config)#int fa0/0
   Router(config-if)#switchport mode trunk
   Router(config-if)#switchport trunk native vlan 99
   Router(config)#int fa0/0
   Router(config-if)#no shut
   #On the router create subinterfaces on the same trunk interface with the respective subnets for the associated VLAN it will route.
   #Match the subinterface number with the VLAN number to make life easy.
   #For example, VLAN2
   Router(config)#int fa0/0.2
   Router(config-if)#encap dot1q 2
   Router(config-if)#ip address 192.168.2.1 255.255.255.0
   #VLAN3
   Router(config)#int fa0/0.3
   Router(config-if)#encap dot1q 3
   Router(config-if)#ip address 192.168.3.1 255.255.255.0
   #Native VLAN
   Router(config)#int fa0/0.99
   Router(config-if)#encap dot1q 99 native
   ```

#### Cisco Website:

   - 3 steps: Create VLANs you want to route, give them IP's, and assign a default gateway

   ```tcl
   Switch#vlan database
   Switch(vlan)#vlan 2
   Switch(vlan)#vlan 3
   Switch(vlan)#vlan 10
   Switch(vlan)#exit
   Switch#configure terminal
   Switch(config)#ip routing # this tells the switch to do the routing between vlans
   Switch(config)#interface Vlan2
   Switch(config-if)#ip address 10.1.2.1 255.255.255.0
   Switch(config-if)#no shutdown
   Switch(config)#interface Vlan5
   Switch(config-if)#ip address 10.1.5.1 255.255.255.0
   Switch(config-if)#no shutdown
   Switch(config)#interface Vlan10
   Switch(config-if)#ip address 10.1.10.1 255.255.255.0
   Switch(config-if)#no shutdown
   # Configure Default Route
   Switch(config)#ip route 0.0.0.0 0.0.0.0 200.1.1.2
   Switch(config)#interface FastEthernet 0/1
   Switch(config-if)#no switchport
   Switch(config-if)#ip address 200.1.1.1 255.255.255.0
   Switch(config-if)#no shutdown
   ```

#### Show Commands:

   ```tcl
   show interfaces f0/0 switchport
   show interface
   show ip interface
   show run
   show ip route
   ```

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)
