---
title: Port Opening On A Cisco Router
date: 2016-10-15T02:15:39+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/port-opening-on-a-cisco-router/
tags:
  - Networking
tags:
  - Router
  - Router
---
<!--more-->

### Description:

Follow these steps to open a port on a Cisco router.

### To Resolve:

Let's say we have a web server on port 192.168.1.100 that we want to be accessible from the outside:

1. First we would set our interfaces as inside/outside like so:

   ```tcl
   Router(config)#interface g0/0
   Router(config-if)#ip address 192.168.1.1 255.255.255.0
   Router(config-if)#Description 'connected to lan'
   Router(config-if)#ip nat inside
   Router(config)#interface g0/1
   Router(config-if)#ip address 192.168.2.1 255.255.255.0
   Router(config-if)#Description 'connected to lan'
   Router(config-if)#ip nat inside
   Router(config)#interface s0/0
   Router(config-if)#ip address 100.100.100.1 255.255.255.0
   Router(config-if)#Description 'connected to isp'
   Router(config-if)#ip nat outside
   Router(config-if)#exit
   ```

2. Next just create the translation statement:

   ```tcl
   ip nat inside source static tcp 192.168.1.100 80 100.100.100.1 80
   ```

   - source is `static` 
   - ip is `192.168.1.100` 
   - port is `80` 
   - outside ip is `100.100.100.1` - Note you can replace the WAN interface name if you want  
   - outside port is `80`

3. Lastly, check to make sure it's being translated by typing:

   ```tcl
   end
   show ip nat translations
   ```

### Dynamic NAT:

1. Follow step 1 from above

2. We create an ACL to tie it to PC instead:

   ```tcl
   config t
   access-list 1 permit 192.168.1.100 0.0.0.0

   #or use an extended ACL (preferred)
   access-list 101 permit tcp 192.168.1.100 0.0.0.255 any eq 80
   ```

3. We then create a `nat pool`of available public IP's that will be translated to internal IPs:

   ```tcl
   ip nat pool MyPool 100.100.100.1 100.100.100.255 netmask 255.255.255.0
   ```

4. Now we create the translation statement

   ```tcl
   ip nat inside source list 1 pool MyPool overload
   ```

