---
title: Port Opening On A Checkpoint Router
date: 2016-05-22T06:38:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/port-opening-on-routers/
tags:
  - Networking
tags:
  - Router
---
<!--more-->

### Description:

If you ever need to access a computer from home or add a device on the network that will be visible from the outside, you will need to open ports on your local router to allow so.


### To Resolve:

1. Get on any computer on the network.

2. Open up a web browser and get to the router by getting the default gateway from `ipconfig /all`.

3. Depending on the router, you will go to firewall => rules => create. Get the port number and type needed. (ex: 8034 TCP or a range like 1021-1023 TCP/UDP)

4. Select Allow and Forward if you want a rule for 1 IP Address. Select Allow to allow port open for all on the network. Select Block to block for all of network.

5. Setup the rule accordingly. Connection Source = Any/ Destination = This Gateway.

6. Go to canyouseeme.org and see if the port is open. There is a 3-5 minute delay between router and the website, so be patient. If successful, it will say the port is Open.

#### For ICMP: This is sometimes used for troubleshooting with ISP's:

1. Log in to the router. Go to security => rules => add new rule.

2. Set it up to Allow

3. Custom Service = ICMP.

4. For connection source = WAN and destination This Gateway

5. Set it to log connections. Then set a description of the rule as ICMP

#### For Security Camera's:

1. Log in to the router. Go to security => rules => add new rule.

2. Create the rule = Allow and forward

3. Custom Service: Enter the protocol and the ports that the security camera's guide says to enter.

4. For connection source = ANY and destination This Gateway

5. Under Forward Connection To: make sure the drop down says Specified IP and enter the IP Address next to it on the right. This will be the IP of the DVR on network.

6. Check the Log incoming connections box and click next. Enter "Security Camera's" as the description.

#### If You Open the Ports But Cannot See Them Open:

1. Get on the computer closest to the ISP modem. Change it to DHCP if it's not already. Run => `ncpa.cpl` => Local Area Connection => Right Click- Properties => Internet Protocol Version 4 => Properties => Select the two radio buttons that say Obtain Automatically

2. Power down the modem and unplug the cable going from the Ethernet port on the modem to the WAN port on the router and move it to the Ethernet port on the modem to the Ethernet port on the workstation.

3. Log in to the modem and create a DMZ port that forwards all traffic to the router's IP address and turn off any firewall settings. This ensures the modem is in `passthrough` mode. There may be an option to choose the router by MAC address, choose that if it's an option.

4. Reconnect the modem to the router and try seeing if the ports are open now. Test by going to `canyouseeme.org`

