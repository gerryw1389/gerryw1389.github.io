---
title: Computer Cannot Connect To LAN/WAN
date: 2016-05-21T21:41:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/computer-cannot-connect-to-lanwan/
categories:
  - Hardware
---
<!--more-->

### Description:

If you have one computer that is not connecting to the internal network or the internet, try these steps. Keep in mind that in most cases it will be a cabling issue. There is three sources to the problem if on a wired LAN network: The NIC on the machine, the cable itself is bad, or the port on the switch going to the workstation is dead.

### To Resolve:

1. Before jumping to any conclusions, run => `ncpa.cpl`. Read what's under the Connection. It should say network cable unplugged if it's a cabling issue, if not the problem is most likely not the cable.

2. Reseat the ethernet cable on both ends. If it goes into a network drop, see if you can trace from there to the switch. From the switch, see if a light on the port the ethernet cables goes to is on. Remember, a green light indicates it's running at 1Gbps and an amber means 100 Mbps. You need to see if there is no light at all. Also, power cycle the switch, this resolves many issues.

3. Switch out the cable with one that you know that works, or buy a new one for testing. If after switching out the cables the connection restores, you know the point of failure.

4. Try reinstalling the drivers for the NIC. Run => `devmgmt.msc` => Network Adapters => Right click on the name of your Network Card and Uninstall. Now on the top menu, go to Action => Scan for Hardware Changes => this should reinstall the NIC. You may have to reboot for it to be done properly.