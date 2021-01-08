---
title: 'CCNA: FHRPs'
date: 2016-10-10T03:03:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-fhrps/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

HSRP, VRRP, and GLBP

#### Steps to create HSRP:

1. Configure the correct IP address and mask for the gateway interface using the ip address \[address\] \[mask\] [secondary] interface configuration command.  

2. Create an HSRP group on the gateway interface and assign the group the virtual IP address via the standby \[number] ip [virtual address\]\[secondary\] interface configuration command. The [secondary] keyword specifies the IP address as a secondary gateway IP address for the specified group.  

3. Optionally, assign the HSRP group a name using the standby [number] name [name] interface configuration command.  

4. Optionally, if you want to control the election of the active gateway, configure the group priority via the standby [number] priority [value] interface configuration command.

#### Configuring HSRP (Hot Standby Router Protocol):

   ```tcl
   Router 1 Interface Configuration:
   R1(config)#interface FastEthernet0/0
   R1(config-if)#ip address 192.168.0.3 255.255.255.0
   R1(config-if)#duplex auto
   R1(config-if)#speed auto
   R1(config-if)#standby 5 ip 192.168.0.1
   R1(config-if)#standby 1 name hsrp-group1
   R1(config-if)#end
   ```

#### Router 2 Interface Configuration:

   ```tcl
   R2(config)#interface FastEthernet0/0
   R2(config-if)#ip address 192.168.0.4 255.255.255.0
   R2(config-if)#duplex auto
   R2(config-if)#speed auto
   R2(config-if)#standby 5 ip 192.168.0.1
   R2(config-if)#standby 1 name hsrp-group1
   R2(config-if)#end
   ```

#### More options:

   ```tcl
   R1(config)#int fa0/0
   R1(config-if)#ip address 10.1.1.2 255.255.255.0
   R1(config-if)#standby version [1|2]
   R1(config-if)#standby 1 ip 10.1.1.1
   R1(config-if)#standby 1 timers (hello) (dead) # Hello timers - 3 seconds / Dead timers 10 seconds
   R1(config-if)#standby 1 priority (priority) # Priority numbers - highest is active / lowest is passive router = default is 100 (max 255)
   R1(config-if)#standby 1 preempt # Preempt is disabled by default. It tells the router to become active once it comes back online if it goes down.
   R1(config-if)#standby 1 authentication md5 key-string (password) # You can also use a key here. See the security section on how to create a key.
   R1(config-if)#standby 1 track (interface) (value) #See below, objects can be created per interface or in global config.
   R1(config-if)#standby 1 track (object) decrement (value) # example: standby 1 track GigabitEthernet5/1 50. This will track an interface and decrement its priority value if it goes down.
   ```

#### Configure HSRP to use the actual MAC address of the gateway interface as the virtual MAC address of the different HSRP groups:

   ```tcl
   Gateway-1#config t
   Gateway-1(config)#int f0/0
   Gateway-1(config-if)#standby use-bia
   Gateway-1(config-if)#exit
   ```

#### Show commands:

   ```tcl
   show standby brief # P indicates configured to preempt.
   debug standby
   show standby
   ```

---

#### Configuring VRRP (Virtual Router Redundancy Protocol):

   ```tcl
   R1(config)#int fa0/0
   R1(config-if)#ip address 10.1.1.2 255.255.255.0
   R1(config-if)#vrrp 1 ip 10.1.1.1
   R1(config-if)#vrrp 1 timers [advertise (hello)|learn] # Timers: Hello 1 second / Dead 3 seconds. Once you change hello, dead changes automatically.
   R1(config-if)#vrrp 1 priority (priority)
   R1(config-if)#vrrp 1 preempt
   R1(config-if)#vrrp 1 authentication md5 key-string (password)
   R1(config-if)#vrrp 1 track (object) decrement (value)
   ```

#### Tracking an object:

   ```tcl
   VTP-Server-1(config)#track 1 interface Loopback0 line-protocol
   VTP-Server-1(config-track)#exit
   VTP-Server-1(config)#interface vlan192
   VTP-Server-1(config-if)#vrrp 1 track 1
   VTP-Server-1(config-if)#exit
   ```

#### Show commands:

   ```tcl
   show vrrp [all|brief|interface (name)]
   ```

---

#### Configuring GLBP (Gateway Load Balancing Protocol):

   ```tcl
   R1(config)#int fa0/0
   R1(config-if)#ip address 10.1.1.2 255.255.255.0
   R1(config-if)#glbp 1 ip 10.1.1.1
   R1(config-if)#glbp 1 timers (hello) (dead)
   R1(config-if)#glbp 1 timers redirect (redirect) (time-out)
   R1(config-if)#glbp 1 priority (priority)
   R1(config-if)#glbp 1 preempt
   R1(config-if)#glbp 1 forwarder preempt
   R1(config-if)#glbp 1 authentication md5 key-string (password)
   R1(config-if)#glbp 1 load-balancing (method) # default is round-robin, best to leave it as is.
   R1(config-if)#glbp 1 weighting (weight) lower (lower) upper (upper)
   R1(config-if)#glbp 1 weighting track (object) decrement (value)
   ```

#### Show commands:

   ```tcl
   show standby brief # P indicates configured to preempt.
   debug standby
   show standby
   ```

