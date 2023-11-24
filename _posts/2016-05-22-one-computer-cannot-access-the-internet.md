---
title: One Computer Cannot Access The Internet
date: 2016-05-22T07:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/one-computer-cannot-access-the-internet/
tags:
  - Networking
---
<!--more-->

### Description:

Many times, you can lose access to the internet on one computer out of the network while the others are working just fine. General rule of thumb is that if internet does not work on one workstation, it's cabling, if it's the whole network => it's a networking device like the switch, router, or modem.

The goal with these situations is to find out if you lost LAN/WAN which means its almost certainly a cabling/switch issue or you just cannot access the internet. This is almost always a client having issues with their browser and is almost never an actual networking issue (in my experience).


### To Resolve:

1. First, is it a cabling issue?

   - Run => `ncpa.cpl` => Local Area Connection => What does it say as the status? Does it say &#8220;Network Cable Unplugged&#8221; if so, try the steps in [Computer Cannot Connect to LAN/WAN](https://automationadmin.com/2016/05/computer-cannot-connect-to-lanwan/).

   - If it says network cable unplugged, it could be a bad switch port as well, have the client move the cable to a different port.

2. If it's not cabling, we need to check the network setup:

   - Run => `ncpa.cpl` => Local Area Connection => Right Click => Properties => Internet Protocol Version 4 Properties => Properties => See if it's set to &#8220;Automatically Obtain&#8230;&#8221; DHCP or &#8220;Uses the following&#8230;&#8221; Static. If static, see what the DNS is. Set it this way:

   - If the computer is on a domain, set the primary DNS to the DC's IP address and leave the secondary DNS blank.

   - If the computer is on a workgroup, set the primary DNS to the default gateway and the secondary to a public DNS server, I always use 8.8.8.8.

   - If on DHCP, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ipconfig /all`. Get the default gateway.

3. Can we ping the gateway? How about other hosts?

   - If no, reboot the computer. Also check the Windows host file or start scanning for malware.

   - If you can ping all internal host and gateway but not anything past the WAN, we need to look at the router.

   - Open up a browser and type in the gateway's IP to see if you can log in to it's web GUI. If so, look for a &#8220;tools&#8221; section which usually will let you run a ping from the router to your computer. Do it. Does it get a reply?

   - If so, keep troubleshooting. If not, it is most certainly antivirus/firewall issues at this point. There are some that will block all WAN access but keep LAN connectivity.

   - While in the router, check to see if it has &#8220;Node Limits&#8221;. This is basically a feature in many business class routers that says that router will only let so many devices connect to the internet unless you purchase a &#8220;license&#8221; that allows you to have more &#8220;Nodes&#8221;. Note this is real common if the router has any kind of &#8220;Web Filtering&#8221; features.

4. If you reached this point, I'm not sure the fix. But as a shot in the dark, I would definitely start power cycling networking devices (if the client doesn't care which they almost certainly will).

### For Wireless:

1. Double check that the computer is entering the correct passphrase or password for the wireless network. Ensure that Caps lock is not on and Num Lock is if using the keypad. This is almost always the cause.

2. See if anything else is connected to the network wirelessly. Determine if the device is accessing the internal network or a Wifi hotspot. Many network admins set up their Wifi Devices to have one on the internal network with MAC Address filtering and one on a general network usually through the DMZ port on the router. This is so that some computers can only access the internet when connected and other can access the internet and the internal network.

3. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ipconfig /all`. Get the Default Gateway and log in to it's web GUI. Do you see the device as connected? If it's not in the list, that means the wireless device is not able to communicate with the router. At this point, check to see if you have &#8220;MAC Address Filtering&#8221; enabled. If so, double check that the wireless device's NIC MAC Address is in the list. To get it, just run `ipconfig /all` and get the &#8220;Physical Address&#8221; associated with the wireless NIC.