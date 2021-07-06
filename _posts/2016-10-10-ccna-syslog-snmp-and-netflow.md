---
title: 'CCNA: Syslog, SNMP, and Netflow'
date: 2016-10-10T03:18:32+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-syslog-snmp-and-netflow/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Routers: Routers can log events. There are 8 levels of logging and you need to know them for the exam. Their order is:  
Level Description  
0 => emergency System unusable  
1 => alert Immediate action needed  
2 => critical Critical condition  
3 => error Error condition  
4 => warning Warning condition  
5 => notification Normal but significant condition  
6 => informational Informational message only  
7 => debugging Appears during debugging only

#### To enabling logging globally:

   ```tcl
   Router(config)#logging on
   Router(config)#no logging # disables
   ```

#### To not show logging to the console (re-enters the line you were typing before the logging interrupted you)

   ```tcl
   Router(config)#no logging console # won't see logging locally.
   Router(config)# line con 0 0
   Router(config-line)#logging synchronous # You will not see logging when you are ssh'd in or telnet'd in after these commands.
   ```

#### To Configure Syslog:

   ```tcl
   R1#config t
   R1(config)#logging 192.168.1.99 # Send syslog to server
   R1(config)#logging trap 4 # Sends 0-4 level messages only. Could also type "logging trap warning"
   R1(config)#logging source-interface fa0/1 # Optional, defines which interface IP is stamped on log messages
   R1(config)#service timestamps log datetime # adds timestamps
   ```

#### To Configure SNMP:

   ```tcl
   R1(config)#snmp-server community MyPassword ro
   R1(config)#snmp-server location The Location of Device
   R1(config)#snmp-server contact Contact Person
   R1(config)#snmp-server community MyPassword ACL - Restrict SNMP via ACL
   R1(config)#snmp-server host 192.168.1.99 version 2c MyPassword - Define server to send traps to and SNMP version
   R1(config)#snmp-server enable traps
   ```

#### To Configure Netflow:

   ```tcl
   # Memorize: Monitors network traffic, captures identifying details, sees why network conditions are present.
   R1#conf t
   R1(config)#int fa0/1
   R1(config-if)#ip flow ingress #one must configure two flow captures on an interface to get both directions
   R1(config-if)#ip flow egress #one must configure two flow captures on an interface to get both directions
   R1(config-if)#exit
   R1(config)#ip flow-export destination 192.168.1.99 2055 # Common ports are 99, 2055, 9996
   R1(config)#ip flow-export version 5
   ```

#### Show Commands:

   ```tcl
   show logging
   show snmp
   show snmp community
   show ip cache flow
   show ip flow interface
   show ip flow export
   ```

### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)