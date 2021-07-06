---
title: 'CCNA: PPP and PPPoE'
date: 2016-10-10T03:25:29+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-ppp-and-pppoe/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Rules:

1. Create a username (the hostname of neighbor router)  
2. In interface, change ecapsulation to PPP (default is HDLC)  
3. Enable authentication using CHAP, PAP, or both.

#### Configuring PPP:

   ```tcl
   # DCE Side
   R1#conf t
   R1(config)#interface s0
   R1(config-if)#ip add 192.168.1.1 255.255.255.0
   R1(config-if)#clock rate 64000
   R1(config-if)#encapsulation ppp
   R1(config-if)#no shut
   R1(config-if)#end

   # DTE Side:
   R2#conf t
   R2(config)#interface s0
   R2(config-if)#ip add 192.168.1.2 255.255.255.0
   R2(config-if)#encapsulation ppp
   R2(config-if)#no shut
   ```

#### Using CHAP:

   ```tcl
   On R1:
   R1#conf t
   R1(config)#username R2 password Cisco
   R1(config)#interface s0
   R1(config-if)#ip add 192.168.1.1 255.255.255.0
   R1(config-if)#clock rate 64000
   R1(config-if)#encapsulation ppp
   R1(config-if)#ppp authentication chap
   R1(config-if)#no shut
   On R2:
   R2#conf t
   R2(config)#username R1 password Cisco
   R2(config)#interface s0
   R2(config-if)#ip add 192.168.1.2 255.255.255.0
   R2(config-if)#encapsulation ppp
   R2(config-if)#ppp authentication chap
   R2(config-if)#no shut
   ```

#### To configure it to fallback to PAP if CHAP Fails:

   ```tcl
   R2(config-if)#ppp authentication chap pap
   ```

#### Show Commands:

   ```tcl
   debug ppp authentication
   debug ppp negotiation
   ```

---

#### PPPoE

#### Rules:

1. The first step in creating the PPPoE server configuration is to define a BBA (broadband aggregation) group which will manage the incoming connections. This BBA group must be associated to a virtual template.  
2. The next step is to create a virtual template for the customer-facing interface. On the virtual template you need to configure an IP address and a pool of addresses from which clients are assigned a negotiated address.  
3. The IP pool is defined in global configuration mode. This is similar to a DHCP pool configuration.  
4. The final step is to enable the PPPoE group on the customer-facing interface.

#### PPP Server Config:

   ```tcl
   Router(config)#bba-group pppoe GROUP
   Router(config-bba-group)#virtual-template 1
   Router(config)#interface virtual-template 1
   Router(config-if)#ip address 10.10.10.1 255.255.255.0
   Router(config-if)#peer default ip address pool POOL
   Router(config)#ip local pool POOL 10.10.10.2 10.10.10.254
   Router(config)#interface FastEthernet0/0
   Router(config-if)#no ip address
   Router(config-if)#pppoe enable group GROUP
   Router(config-if)#no shutdown
   ```

#### PPP Client Config:

   ```tcl
   # Client Configuration - On the client side a dialer interface has to be created. This will manage the PPPoE connection.
   # The dialer interface can be assigned a manual IP address or can be instructed to request one from the server (using the ip address negotiated command):
   Router(config)#interface dialer1
   Router(config-if)#dialer pool 1
   Router(config-if)#encapsulation ppp
   Router(config-if)#ip address negotiated
   Router(config)#interface FastEthernet0/0
   Router(config-if)#no ip address
   Router(config-if)#pppoe-client dial-pool-number 1
   Router(config-if)#no shutdown
   ```

#### PPP Authentication:

   - PAP can be configured as follows # Don't use PAP!:

   ```tcl
   Server(config)#username Client password Password
   Server(config)#interface virtual-template 1
   Server(config-if)#ppp authentication pap
   Server(config-if)#ppp pap sent-username Server password Password

   Client(config)#username Server password Password
   Client(config)#interface dialer 1
   Client(config-if)#ppp authentication pap
   Client(config-if)#ppp pap sent-username Client password Password
   ```

#### CHAP can be configured as follows:

   ```tcl
   Server(config)#username Client password Password
   Server(config)#interface virtual-template 1
   Server(config-if)#ppp authentication chap

   Client(config)#username Server password Password
   Client(config)#interface dialer 1
   Client(config-if)#ppp authentication chap
   ```

#### Another Client Config Example:

   ```tcl
   R2(config)#interface dialer1
   R2(config-if)#encapsulation ppp
   R2(config-if)#ip address negotiated
   R2(config-if)#ppp chap hostname R1 # hostname of provider
   R2(config-if)#ppp chap password # password of provider
   R2(config-if)#ip mtu 1492 # this is Required to ensure fragmentation does not occur due to additional PPPoE header
   R2(config-if)#dialer pool 1
   R2(config-if)#int fa0/1
   R2(config-if)#pppoe enable
   R2(config-if)#no ip address
   R2(config-if)#pppoe-client dial-pool-number 1
   ```

#### PPP Multi-link Example (multiple links to ISP):

   ```tcl
   R1#conf t
   R1(config)#int s0/0/0
   R1(config-if)#encap ppp
   R1(config-if)#compress predictor
   R1(config-if)#ppp quality 80 #If quality goes under 80%, link will shutdown
   R1(config-if)#Multilink #Send traffic over multiple links to same destination
   R1(config-if)#int multilink 1
   R1(config-if)#ip address 10.0.0.1 255.255.255.0
   R1(config-if)#ppp multilink
   R1(config-if)#ppp multilink group 1
   R1(config-if)#int s0/0/0
   R1(config-if)#ppp multilink
   R1(config-if)#ppp multilink group 1
   ```

#### Show Commands:

   ```tcl
   show ip interface brief
   show pppoe session
   debug ppp
   ```


### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)
