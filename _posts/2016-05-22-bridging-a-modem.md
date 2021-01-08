---
title: Bridging A Modem
date: 2016-05-22T06:54:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/bridging-a-modem/
categories:
  - Networking
tags:
  - Setup
---
<!--more-->

### Description:

At some point or another, you may find it necessary to bridge a modem in order to access the internal network from the outside. If this is not done, you will have issues due to security settings on the modem. When you bridge a device you make it a level 2 device from a level 3 device. Most modems nowadays do not do a true &#8220;Bridge Mode&#8221; but more of a &#8220;IP Passthrough Mode&#8221;. Never put a modem and router on the same IP subnet. Packets will not know which gateway to go through and will get stuck in a loop. Also note, a lot of ISP's use PPPoE logins. That means they use a U/P to get the internet used to authenticate.


### To Resolve:

1. Find out the IP of the router and write it down somewhere, we will need this later. Now get connected to the modem directly.

   - Have the client take a laptop computer or the closest desktop computer and plug an ethernet cable going from the computers NIC directly to the LAN port on the modem.

   - Make sure the workstation is on DHCP (Run => npca.cpl => set everything to automatic on the IPv4 settings). Assuming the modem is handing out DHCP the client computer will get an IP address automatically. If it doesn't, manually set the IP address to something in that subnet.

   Example: Modem is on 192.168.0.1, manually configure workstation to 192.168.0.13.

   - Go to the modem's configuration page (by typing the IP address of the default gateway in browser).

   - Once inside the modem, change it's IP address to match your network but on a different subnet. For example, the router is configured to be on 192.168.1.0, place the modem on 192.168.2.1. This is not neccessary but it helps when troubleshooting in the future.

   - After changing the IP address, look for a &#8220;LAN Subnet&#8221; section. This is the IP's the modem hands out on DHCP. Make sure the subnet matches that of the same subnet your modem's IP address is. For example, if your modem IP is  192.168.0.1, see that it hands out 192.168.0.2-100 or something.

   - Ensure that you have internet access. Open up a new tab and browse to a website or bring up a command prompt and start pinging well known WAN tests (i.e. 8.8.8.8 or 8.8.4.4)

   - Done configuring the modem. Unplug from the workstation and take it back close to the router.

2. Place a cable going from the LAN port on the modem to the WAN port on the router.

3. Now get connected to the router using the same steps as above. Set the routers default gateway as the modem. It will be a LAN DHCP client to the modem. Done configuring the router.

4. Place a cable going from the LAN port on the router to the main network switch, this will ensure all devices will receive the right settings.

5. Power cycle the modem, router, and switch in that order.

6. All computers should now have access to the internet!

7. So This Is the Basic Setup:

  <img class="alignnone size-full wp-image-638" src="https://automationadmin.com/assets/images/uploads/2016/09/bridging-a-modem.png" alt="bridging-a-modem" width="1158" height="779" srcset="https://automationadmin.com/assets/images/uploads/2016/09/bridging-a-modem.png 1158w, https://automationadmin.com/assets/images/uploads/2016/09/bridging-a-modem-300x202.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/bridging-a-modem-768x517.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/bridging-a-modem-1024x689.png 1024w" sizes="(max-width: 1158px) 100vw, 1158px" />


