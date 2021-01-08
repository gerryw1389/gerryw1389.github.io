---
title: 'CCNA: Port Security'
date: 2016-10-10T02:21:01+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-port-security/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Port security is used to lock down ports

#### Interface Commands (access port):

   ```tcl
   Switch(config)#interface GigabitEthernet0/2
   Switch(config-if)#switchport mode access
   Switch(config-if)#switchport port-security # required. Tells the switch port to enable security
   Switch(config-if)#switchport port-security mac-address 001f.3c59.5555 # set a static MAC - won't allow any others
   Switch(config-if)#switchport port-security mac-address sticky # tells it to dynamically remember the device attached. Must run "copy run start" for it to remember.
   Switch(config-if)#switchport port-security maximum 2 # sets a limit on the number of devices it can allow. 1 is the default.
   Switch(config-if)#switchport port-security violation restrict # options are restrict/shutdown/protect. Shutdown is default.
   Switch(config-if)#switchport port-security mac-address 001f.3c59.5555
   Switch(config-if)#
   ```

#### Interface Commands (trunk port):

   ```tcl
   Switch(config)#interface GigabitEthernet0/2
   Switch(config-if)#switchport mode trunk
   Switch(config-if)#switchport trunk encapsulation dot1q
   Switch(config-if)#switchport nonnegotiate
   Switch(config-if)#switchport port-security
   Switch(config-if)#switchport port-security # see options above
   ```

#### To configure a data/voice VLAN:

   ```tcl
   VTP-Server-1(config-if)#switchport mode access
   VTP-Server-1(config-if)#switchport access vlan 5
   VTP-Server-1(config-if)#switchport voice vlan 7
   VTP-Server-1(config-if)#switchport port-security
   VTP-Server-1(config-if)#switchport port-security maximum 2
   VTP-Server-1(config-if)#switchport port-security mac-address 001f.3c59.5555 vlan access
   VTP-Server-1(config-if)#switchport port-security mac-address 001f.3c59.7777 vlan voice
   ```

#### Show Commands:

   ```tcl
   show port-security
   show port-security
   show dtp # this shows global dtp config
   show dtp interface
   show sdm prefer
   ```

