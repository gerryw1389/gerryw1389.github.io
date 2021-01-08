---
title: Setting Up A WAP
date: 2016-05-21T05:22:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-a-wap/
categories:
  - Hardware
  - Networking
tags:
  - Setup
---
<!--more-->

### Description:

If you ever want to add a WAP, or a Wireless Access Point, to the network, try these steps.

### To Resolve:

1. As with anytime you install something, it's good to have the &#8220;User's Manual&#8221; for reference.

2. Plug the WAP to a computer directly via ethernet cable. Plug in through the LAN port on the WAP. If it's a Ruckus WAP, plug in to the &#8220;10/100/1000 PoE&#8221; port.

3. Find out what the default IP is of the WAP and set your computer to a &#8220;Static IP&#8221;. See &#8220;Setting A Static IP For A Computer&#8221; for more info. Place your computer within the same network.

   - For example: Your WAP has a default IP address of 192.168.0.254. Place your computer on 192.168.0.11 or something and put the Default Gateway to 127.0.0.1. Do the same for the Primary DNS.

4. Login to the WAP and set it up to how you need it. Make sure to put it on the same network schema as the rest of the network if it's not already. After you do this, select &#8220;Save&#8221; or &#8220;Update Settings&#8221;, then go to the new IP and see if you can login to the WAP.

5. Last thing to do is to plug it in to the switch or router and test it. If the router has the option to have a public network and a private network, login to the public one and make sure you cannot see the private network. Verify that you have an ethernet cable going from the &#8220;DMZ/WAN2&#8221; port of your router to a &#8220;LAN&#8221; port on your WAP and another ethernet cable going from the switch to the &#8220;10/100/1000 PoE&#8221; port if you have two separate networks.