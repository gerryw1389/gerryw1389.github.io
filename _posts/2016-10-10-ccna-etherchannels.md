---
title: 'CCNA: Etherchannels'
date: 2016-10-10T02:31:58+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-etherchannels/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Remember these rules for matching on each end:  
on-on  
auto-desirable  
active-passive

#### To create a basic layer 2 etherchannel:

   ```tcl
   Switch-1#conf t
   Switch-1(config)#interface range fa0/1 – 3
   Switch-1(config-if-range)#no shutdown
   Switch-1(config-if-range)#channel-group 1 mode on # will display: Creating a port-channel interface Port-channel 1; uses pagp
   Switch-1(config-if-range)#end
   Switch-1#show etherchannel summary
   ```

   - Do the same thing for Switch-2

#### To configure how to load balance:

   ```tcl
   Switch(config)#port-channel load-balance [method]
   ```

#### Configuring Using PAGP:

   ```tcl
   Switch-1#conf t
   Switch-1(config)#interface range fa0/1 – 3
   Switch-1(config-if-range)#no shutdown
   Switch-1(config-if-range)#channel-group 1 mode desirable
   Switch-1(config-if-range)#channel-protocol pagp # this command is optional because pagp is default, but it should still be typed.
   Switch-1(config-if-range)#end
   Switch-1#show etherchannel summary
   # change this to auto on the other switch
   ```

#### Configuring Using LACP:

   ```tcl
   Switch-1#conf t
   Switch-1(config)#interface range fa0/1 – 3
   Switch-1(config-if-range)#no shutdown
   Switch-1(config-if-range)#channel-group 1 mode active
   Switch-1(config-if-range)#channel-protocol lacp
   Switch-1(config-if-range)#end
   Switch-1#show etherchannel summary
   # change this to passive on the other switch
   ```

#### Show Commands:

   ```tcl
   show etherchannel summary # Look for speed mismatches!
   show interfaces port-channel 1 switchport
   show EtherChannel 1 detail
   show pagp neighbor
   show lacp internal # port state, administrative key, LACP port priority, and the port number
   show lacp neighbor # neighbour name, ID of the LACP neighbour, the neighbour device ID (MAC), and the neighbour port. The flags also indicate the mode the neighbour is operating in, as well as whether it is a physical learner, for example
   show lacp sys-id # the system ID of the local switch. This is a combination of the switch MAC and LACP priority
   ```


