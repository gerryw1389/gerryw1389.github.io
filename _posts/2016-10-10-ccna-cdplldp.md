---
title: 'CCNA: CDP/LLDP'
date: 2016-10-10T02:23:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-cdplldp/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Cisco Discovery Protocol (proprietary) runs only on Cisco devices; it allows you to gather information about other routers and switches. It is enabled by default. It can also be a very useful command to use while troubleshooting to see which devices are directly connected to the device you are connected to.

#### To disable CDP For the whole switch:

   ```tcl
   Router(config)#no cdp run
   ```

#### To disable CDP for an interface:

   ```tcl
   Router(config-if)#no cdp enable
   ```

### Show Commands:

   ```tcl
   show cdp
   show cdp neighbors
   show cdp neighbors detail
   show cdp entry
   ```

---

### Open source CDP = LLDP

   - To support non-Cisco devices and to allow for interoperability between other devices, the switch supports the IEEE 802.1AB LLDP. 
   - LLDP is a neighbor discovery protocol that is used for network devices to advertise information about themselves to other devices on the network. 
   - This protocol runs over the data-link layer, which allows two systems running different network layer protocols to learn about each other.  
   - LLDP supports a set of attributes that it uses to discover neighbor devices. 
   - These attributes contain type, length, and value descriptions and are referred to as TLVs. 
   - LLDP supported devices can use TLVs to receive and send information to their neighbors. 
   - Details such as configuration information, device capabilities, and device identity can be advertised using this protocol.  
   - LLDP is disabled by default

#### To Enable LLDP globally:

   ```tcl
   config t
   lldp run
   end
   ```

#### To Enable LLDP per interface:

   ```tcl
   config t
   int fa0/0
   lldp transmit
   lldp receive
   end
   copy run start
   ```

### LLDP Commands:

   ```tcl
   clear lldp counters
   clear lldp table
   show lldp
   show lldp errors
   ```

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)