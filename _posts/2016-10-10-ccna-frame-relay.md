---
title: 'CCNA: Frame Relay'
date: 2016-10-10T03:30:36+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-frame-relay/
tags:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Rules:

1. Set encapsulation  

2. Set LMI type (optional)  

3. Configure static/dynamic address mapping  

4. Address protocol-specific problems

#### Configuring Frame-Relay client side (using sub-interfaces):

   ```tcl
   R1#config t
   R1(config)#int s0/0/0
   R1(config-if)#no ip address
   R1(config-if)#encapsulation frame-relay
   R1(config-if)#exit
   R1(config)#int s0/0/0.302 point-to-point
   R1(config-if)#ip address 10.1.1.10 255.255.255.252
   R1(config-if)#frame-relay interface-dlci 302 # local dlci that connects to 203
   R1(config-if)#int s0/0/0.301 point-to-point
   R1(config-if)#ip address 10.1.1.13 255.255.255.252
   R1(config-if)#frame-relay interface-dlci 301 # local dlci that connects to 103
   R1(config-if)#end
   R1#config t
   R1(config)#int s0/0/0
   R1(config-if)#no shut # wait until you are done configuring sub-interfaces before bringing this online
   R1(config-if)#end
   R1#copy run start

   R2#config t
   R2(config)#int s0/0/0
   R2(config-if)#no ip address
   R2(config-if)#encapsulation frame-relay
   R2(config-if)#exit
   R2(config)#int s0/0/0.203 point-to-point
   R2(config-if)#ip address 10.1.1.10 255.255.255.252
   R2(config-if)#frame-relay interface-dlci 203 # local dlci that connects to 302 on R1
   R2(config-if)#end
   R2#config t
   R2(config)#int s0/0/0
   R2(config-if)#no shut # wait until you are done configuring sub-interfaces before bringing this online
   R2(config-if)#end
   R2#copy run start

   R3#config t
   R3(config)#int s0/0/0
   R3(config-if)#no ip address
   R3(config-if)#encapsulation frame-relay
   R3(config-if)#exit
   R3(config)#int s0/0/0.103 point-to-point
   R3(config-if)#ip address 10.1.1.10 255.255.255.252
   R3(config-if)#frame-relay interface-dlci 103 # local dlci that connects to 301 on R1
   R3(config-if)#end
   R3#config t
   R3(config)#int s0/0/0
   R3(config-if)#no shut # wait until you are done configuring sub-interfaces before bringing this online
   R3(config-if)#end
   R3#copy run start
   ```

#### Frame Relay Switch:

   - NOTE: You don't have to know this for the exam, but it's good to know anyway!
   {: .notice--success}

   ```tcl
   Router#conf t
   Router(config)#frame-relay switching
   Router(config)#int s0
   Router(config-if)#clock rate 64000
   Router(config-if)#encapsulation frame-relay
   Router(config-if)#frame-relay intf-type dce
   Router(config-if)#frame-relay route 121 interface s1 112
   Router(config-if)#frame-relay route 121 interface s2 111
   Router(config-if)#no shut
   Router(config-if)#int s1
   Router(config-if)#clock rate 64000
   Router(config-if)#encapsulation frame-relay
   Router(config-if)#frame-relay intf-type dce
   Router(config-if)#frame-relay route 112 interface s0 121
   Router(config-if)#frame-relay route 112 interface s2 111
   Router(config-if)#int s2
   Router(config-if)#clock rate 64000
   Router(config-if)#encapsulation frame-relay
   Router(config-if)#frame-relay intf-type dce
   Router(config-if)#frame-relay route 111 interface s0 121
   Router(config-if)#frame-relay route 111 interface s1 112
   Router(config-if)#no shut
   Router#show frame-relay route
   ```

#### Show Commands:

   ```tcl
   show frame-relay map #after a connection is established
   show frame-relay route
   show frame-relay pvc
   debug frame-relay pvc
   debug frame-relay lmi # you want it to report status 0x2 , which is an active link
   ```

#### Main Notes:

   - &#8220;clock rate&#8221; commands are usually only issued on the DCE side, not DTE. The DCE sets the clock and the client adjusts to match it.  
   - Packet Switched Networks: X.25, Frame Relay, ATM, MPLS => The concepts of Frame Relay is why it is important.  
   - PVC => Permanent Virtual Circuit. Similar to VPNs.  
   - CIR => Commited inforamtion rate => Lowest bandwidth provided.  
   - Local Access Rate => How fast can it physically go. CIR is minimmum and Access Rate is maximum.  
   - DLCI => Data link connection identifier => Addresses the ISP uses. DLCIs are locally significant. If you leave 105 to go to 501 then you arrive coming FROM 501!  
   - LMI => Local Managment interface => Language between ISP and your router => Cisco, ANSI, and Q.933A  
   - PVC Designs => Partial mesh, full mesh, and hub/spoke.  
   - Multipoint: All on same subnet, multiple DLCIs mapped to interface, causes problems with split horizon. Multipoint should be used for full mesh. In partial and hub/spoke, use point to point.  
   - MPLS is an ISP type technology => Any to Any with tagging.  
   - PVC => permanent virtual connections.  
   - DE bits tell us how many frames are being dropped because traffic that exceeds CIE.  
   - FECN => Forward explicit congestion notification.  
   - DECN => Same but backwards.


### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)