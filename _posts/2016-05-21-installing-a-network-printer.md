---
title: Setting Up A Network Printer
date: 2016-05-21T04:43:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/installing-a-network-printer/
tags:
  - Networking
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

Almost any printer that you purchase nowadays with have a RJ45 port to plug it on the network, do it! The days of connecting a computer to USB and sharing it out are unneccesary and complicated. This is because printers connect to the USB001 port and jump to USB002 or 003 without warning (reboot /moving stuff around/ wind blows / who knows). Network printers will be connected to the internal network usually via ethernet cable to the switch just like all the computers on the network. Sometimes they will be connected wireless to the modem on a different subnet, they should still work. To install a network printer to a workstation, follow these steps:

### To Resolve:

1. If the printer is on someone's desk I would install a 5 port gigabit switch and run 3 cables: One from wall to switch. The second from switch to computer. Lastly, one from switch to printer.

2. Assign the printer a static IP address through the menu options on the printer or by following documentation to do it from the web gui.

   NOTE: Many people including myself would rather give the printer a static IP and have it on a certain VLAN or [create a DHCP reservation](https://automationadmin.com/2016/05/setting-a-static-ip-for-a-computer/) for it.
   {: .notice--success}

3. Lastly, just install the printer to the computer through the &#8220;add a printer wizard&#8221;. Run => `control printers` => add a printer => network => IP/Hostname = (IPAddressOfPrinter) => Done.

4. For Network Printer Issues: An important thing to look at when troubleshooting network printers is the Ports tab on the printer properties.
   - Click on the TCP/IP port on the Ports tab and go to Configure Ports and make sure they match.
   - If they do NOT match, select a different port and delete the IP port. Then go to add port and add the IP port and select it.