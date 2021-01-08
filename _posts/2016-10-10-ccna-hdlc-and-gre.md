---
title: 'CCNA: HDLC and GRE'
date: 2016-10-10T03:22:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-hdlc-and-gre/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Remember that clock rates are set on the DTE side and you must set them to match!

#### Setup Default Serial Connection:

   ```tcl
   Router#config t
   Router(config)#interface Serial0
   Router(config-if)#ip address 192.168.1.1 255.255.255.0
   Router(config-if)#encapsulation hdlc
   Router(config-if)#clock rate 64000
   Router(config-if)#no shutdown
   Router(config-if)#^Z
   Router#
   ```

#### Show Commands:

   ```tcl
   show controllers serial 0
   show ip interface brief
   show interface Serial0
   ```

---

### Description:

   - PP IP tunnel. Stateless (no flow control), no security, additional overhead. Supports multiple protocols, multicast, ipv6. IP in IP does not support it.

#### To configure GRE Tunneling:

   ```tcl
   R1#config t
   R1(config)#int tunnel 21
   R1(config-if)#ip address 21.0.0.1 255.255.255.0
   R1(config-if)#tunnel source s0/0/0
   R1(config-if)#tunnel destination 10.1.1.6 # the destination router's IP
   R1(config-if)#tunnel mode gre ip
   R1(config-if)#end
   R1#copy run start
   ```

#### On the other side (R2):

   ```tcl
   R2#config t
   R2(config)#int tunnel 21
   R2(config-if)#ip address 21.0.0.2 255.255.255.0
   R2(config-if)#tunnel source s0/0/1
   R2(config-if)#tunnel destination 10.1.1.5 # the source router's IP
   R2(config-if)#tunnel mode gre ip
   R2(config-if)#end
   R2#copy run start
   ```

#### Show Commands:

   ```tcl
   show interface tunnel
   ```

