---
title: Setting Up DDNS For Home
date: 2016-10-07T04:00:02+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/setting-up-ddns-for-home/
tags:
  - Networking
tags:
  - Router
  - Setup
---
<!--more-->

### Description:

Follow this guide to setup DDNS for your home network. DDNS is dynamic dns and is used so that you can translate your changing (dhcp usually) public IP from home into a hostname so you can access computers on your home network from anywhere in the world.

### To Resolve:

1. Go to [noip.com](http://www.noip.com/) or any similar service. Sign up for free DDNS service.

2. Download their client to run on any machine in your network. It will tell the service what your current IP is at any given time. You only have to do this on one computer.

   - Some routers can do this automatically, so check your web GUI. I have a DLINK and it has a tab specifically for DDNS where you just provide your login and it will do it for you. Note that you still have to do the verification email every month, but at least you don't have to install a client.

3. Once it's setup, you just need to forward a port to a DMZ host and you can access that computer from anywhere.

   - For example, if you were running a Plex server, you could create a VM that cannot talk to any host on your home network except a specific VLAN on your router, and then forward port 32,400 from your public IP to 32,400 on that host.

   - It is common practice to change port numbers for security. This is called &#8220;security through obscurity&#8221; and is highly snarled at in the IT industry as many hackers will scan ALL your ports, but is still a good thing to do because it can throw off auto hacks that only check common port numbers.

4. (optional) This step will be different for different router vendors, but to open a port, you usually go to Network => virtual servers / port forwarding => and enter the public port and private port you want to setup => pretty straightforward.
