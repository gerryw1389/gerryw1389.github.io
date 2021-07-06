---
title: 'CCNA: STP/RSTP'
date: 2016-10-10T02:25:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-stprstp/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

STP Commands. See [here](http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/15-02SG/configuration/guide/config/spantree.html)  
Bridge Priority = Switch Priority 32768 / MAC address

#### STP/RSTP Global Commands:

   ```tcl
   Switch(config)#spanning-tree mode [pvst | rapid-pvst] # usually rapid-pvst is chosen. PVST+ is the default.
   Switch(config)#spanning-tree vlan 1-4094 priority 32768 # sets the default priority. Has to increment in 32768 blocks.
   Switch(config)spanning-tree vlan 10 root primary # only run this on the root switch. Changes priority to 1 increment lower than the lowest Bridge id.
   Switch(config)spanning-tree vlan 10 root secondary # only run this on the switch you want as a backup to the root. Changes priority to 16384.
   Switch(config)#spanning-tree vlan 1-4094 hello-time 2 # sets the hello timers to 2 seconds. This is the default.
   Switch(config)#spanning-tree vlan 1-4094 forward-time 15 # sets the forward timers to 15 seconds. This is the default.
   Switch(config)#spanning-tree vlan 1-4094 max-age 20 # sets the max age timers to 20 seconds.This is the default.
   Switch(config)#spanning-tree gaurd [loop|root|none] # enables root gaurd/ loop gaurd
   Switch(config)#spanning-tree backbonefast #enables backbonefast
   Switch(config)#spanning-tree uplinkfast # enables uplinkfast
   Switch(config)#spanning-tree extend system-id # Used for a system that supports 1024 MAC addresses instead of the default 64.
   Switch(config)#spanning-tree bpdugaurd default # sets bpdugaurd as default. Then to disable per interface, just run "spanning-tree bpdugaurd disable"
   ```

#### STP/RSTP Interface Commands:

   ```tcl
   Switch(config)#int g0/1
   Switch(config-if)#spanning-tree [vlan 1-4094] port-priority 128 # this is the default. It goes from 0-240 in increments of 16.
   Switch(config-if)#spanning-tree link-type [point-to-point|shared] # manual link specification, not required
   Switch(config-if)#spanning-tree [vlan 1-4094] cost 19
   Switch(config-if)#spanning-tree bpduguard enable # enables bpdugaurd. Good for PCs but bad for WAPs/Switches because it blocks BPDUs.
   Switch(config-if)#spanning-tree bpdufilter enable # enables bpdufiltering
   Switch(config-if)#spanning-tree portfast # enables portfast which disables STP.
   Switch(config-if)#no spanning-tree vlan # disables spanning-tree
   ```

#### Cisco way to enable RSTP:

   ```tcl
   Switch# config t
   Switch(config)# spanning-tree mode rapid-pvst
   Switch(config)# int fa 6/4
   Switch(config-if)# spanning-tree link-type point-to-point
   Switch(config-if)# end
   Switch(config)# end
   Switch# clear spanning-tree detected-protocols
   ```

#### Show Commands:

   ```tcl
   show spanning-tree
   show spanning-tree summary
   show spanning-tree root
   show spanning-tree bridge
   show spanning-tree detail
   show spanning-tree interface
   show spanning-tree vlan
   debug spanning-tree events
   ```

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)