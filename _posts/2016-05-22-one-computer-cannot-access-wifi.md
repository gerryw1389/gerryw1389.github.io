---
title: One Computer Cannot Access Wifi
date: 2016-05-22T07:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/one-computer-cannot-access-wifi/
tags:
  - Networking
---
<!--more-->

### Description:

Many times, one computer will not connect to the wireless network (wifi) when others are. Follow these steps to resolve.


### To Resolve:

1. Find out how many other are connected? Is it the same network? If this is the only computer trying to connect to the network, then the WAP may be powered off or offline. If there are others connected, verify that the security key you are entering is correct.

2. Find out if the network router has &#8220;Node Limits&#8221; that only allow so many devices to be connected to the network with a particular &#8220;license&#8221;. Many business class routers have this feature. In this case, you could connect to the network, but you will not have internet access.

3. Next find out if the wireless network has any type of &#8220;MAC Address Filtering&#8221; feature enabled. When this is enabled, devices can connect, but will not have access to the internet. To resolve, login to the WAP or Router on a computer that does work, and add the &#8220;MAC Address of the computer you want to have access.

   - To do this, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ipconfig /all` and grab the &#8220;Physical Address&#8221; of the NIC that you want to allow access. For example, a &#8220;Local Area Connection&#8221; is if you want to add if you want a computer to have access through an ethernet cable and a &#8220;Wireless Network Connection&#8221; is the one you will add if you want the computer to have access through the wireless network.

4. If neither of the above methods correct the issue, try going to the WAP's GUI settings and see if you can connect the computer from there, most issues resolve themselves after poking around the different options to find &#8220;what's out of place&#8221;. Double check all settings and also power cycle the WAP.