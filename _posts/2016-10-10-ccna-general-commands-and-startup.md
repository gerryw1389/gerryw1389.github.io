---
title: 'CCNA: General Commands and Startup'
date: 2016-10-10T03:09:08+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-general-commands-and-startup/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Config settings  
0x2102 Default setting  
0x2142 Change NVRam  
troubleshooting commands: ping, show ip route, show interfaces

#### Router config: If you forget the enable password, for a router:

1. Google the term for your particular model. Usually, the steps are:  

   - Reload device  
   - Pressing the right break key on keyboard,  
   - setting the configuration register to skip the startup config file (usually to 0x2142),  
   - Issuing the &#8220;copy start run&#8221; command so you can set a new password

#### For switches:

   - Google the term for your particular model. 
   - Usually, Hold down MODE button for 8 seconds while powering up, this causes is to copy current config to a file named &#8220;config.text.renamed&#8221; 
   - Copy it back to running config modified with another password. (- Didn't understand that!

#### To set the device hostname:

   ```tcl
   Router(config)#hostname R1
   R1(config)#
   ```

#### To reboot:

   ```tcl
   reload
   ```

#### To enable CEF (Cisco Express Forwarding) on a switch:

   ```tcl
   # I think cef is only on by default for layer 3 switches. So you need to run "ip routing"
   Switch(config)#ip cef
   Switch(config)#exit
   # The following output illustrates how to enable dCEF on the Catalyst 6500 series switches:
   Switch(config)#ip cef distributed
   Switch(config)#exit
   ```

#### General show commands:

   ```tcl
   show version
   show history # shows previous commands
   show ip interface brief # commonly shortened to "show ip int bri", shows all interfaces and their status
   show interfaces # same but more information per interface
   show line # shows aux, console, and virtual terminals
   show clock
   service ? # ran in global config, shows all services. You then run "no service (name)" disable those you don't use. Ex: no service dhcp #disables dhcp.
   show ip cef
   show ip cef detail
   show Processes
   show Processes memory
   show memory
   show privilege # privileges go from 0-15 with 15 being "root"
   show mac-address-table # shows mac table
   ```

#### Forgot router password?

   ```tcl
   # Turn on router, type CTRL+C during loading
   rommon 1)confreg 0x2142
   rommon 2)reset
   # Router now bypasses with no passwords
   ```

#### How to get back to last known config:

   ```tcl
   en
   copy start run
   # now startup is in run
   enable password cisco
   do show ip int bri
   int f0/0
   no shut
   #Rommon shuts down interfaces
   do show ver
   exit
   config-register 0x2102
   copy run start
   reload
   # should be good
   ```

#### To tell the router how to boot

   ```tcl
   Router(config)#boot system ?
   Router(config)#boot system flash0://c1900-universalk9-mz.SPA.152-4.M3.bin # to select a new IOS file to boot from
   Router(config)#boot system flash # boot from flash
   Router(config)#boot system tftp: # boot from Tftp
   Router(config)#boot system tftp: c2500-js-l.121-17.bin (hostnameOrIP) # boot from Tftp example
   ```

#### To backup to a TFTP Server:

   ```tcl
   Router#ping 192.168.1.1
   Router#show flash #highlight and copy the name of the file
   Router#copy flash tftp
   #paste filename
   #192.168.1.1
   #dest filename? router1ios.bin
   ```

#### Restoring from TFTP:

   ```tcl
   Router#copy tftp flash
   Router#192.168.1.1
   Router#router1.bin
   [enter]
   ```

#### To put the configuration from Dram into NVRAM

   ```tcl
   copy startup-config running-config # don't run this unless you are sure! short version = copy start run
   #DRAM is static startup and NVRAM is volatile running.
   ```

#### To put the configuration from NVRAM into DRAM

   ```tcl
   copy running-config startup-config # run this often!! short version = copy run start
   write mem # People typically type "wr" in prod to do this, for some reason Cisco prefers the longer method so don't use this often.
   # DRAM is static startup and NVRAM is volatile running.
   ```

#### To put the current DRAM config to TFTP

   ```tcl
   copy startup-config tftp:
   ```

#### To put flash config to TFTP

   ```tcl
   copy flash tftp:
   ```

#### To put TFTP config into flash

   ```tcl
   copy tftp flash:
   ```

#### To erase a config:

   ```tcl
   erase (configName) # example: erase startup-config
   ```

#### To delete something from FLASH:

   ```tcl
   delete (filename) # for example, delete vlan.dat (in routers to delete all VLAN info)
   ```


### Suggested Training Opportunities

1. Free Resources
   - [Youtube](https://www.youtube.com)
   - [Flackbox](https://www.flackbox.com/cisco-ccna-lab-guide)

2. Instructor led:
   - [Flackbox CCNA Gold Bootcamp course](https://www.flackbox.com/cisco-ccna-course)