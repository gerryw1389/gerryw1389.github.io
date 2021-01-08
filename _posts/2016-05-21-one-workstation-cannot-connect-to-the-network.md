---
title: One Workstation Cannot Connect To The Network
date: 2016-05-21T22:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/one-workstation-cannot-connect-to-the-network/
categories:
  - Networking
---
<!--more-->

### Description:

You will get a `Network Path Unavailable` error when trying to connect to the server from the client workstation.

### To Resolve:

1. Check cabling first. Does the computer have access to the internet? See [Computer Cannot Connect to Network/ Internet](https://automationadmin.com/2016/05/computer-cannot-connect-to-lanwan/) for more info.  

2. Always check Firewalls, Antivirus, NIC settings, and run ping test as soon as you troubleshoot networking issues.

   - Check the Windows Firewall to make sure it has the appropriate port opened. Run => `firewall.cpl` => Advanced Settings => Check for port openings
   - Check Antivirus for any &#8220;Identity Protection&#8221; or &#8220;Firewall&#8221; components.
   - Check the NIC settings for this workstation, is the default gateway correct? The primary/ secondary DNS servers? Run an `ipconfig /all` if on DHCP.
   - Ping another computer on the network. If it works, ping the default gateway. If that works, ping 8.8.8.8, did you get a response? If you don't get a response from any of these, you need to make sure those devices are on and connected to the network (the first two anyways).

3. If the devices are on and you still cannot get the client to connect to the server, try rebooting into safe mode, does it work there? If so, you have a third party application that's blocking the local network.

4. When in doubt, scan for viruses.