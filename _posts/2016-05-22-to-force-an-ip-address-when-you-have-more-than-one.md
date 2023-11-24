---
title: To Force An IP Address When You Have More Than One
date: 2016-05-22T08:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/to-force-an-ip-address-when-you-have-more-than-one/
tags:
  - Networking
---
<!--more-->

### Description:

Sometimes, computers will have more than one IP address in their NIC settings so that they can communicate with devices on a subnetwork so as not to interfere with the primary network. The problem is, Windows isn't designed to have a computer handling two IP Addresses on a single NIC, so you have to &#8220;trick&#8221; Windows to get it to work. You can check this by running `ncpa.cpl` => right click on &#8220;NIC Name (Local Area Connection in most cases)&#8221; => Properties => Internet Protocol Version 4 => Properties => &#8220;Advanced&#8221; button on the first tab. Here you will see two IP addresses. You will need to remove the second IP and re-add it back using the `netsh` command with a specific flag.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `netsh int ipv4 add address "Local Area Connection" 1.2.3.4/24 SkipAsSource=true` where 1.2.3.4 is the IP you are adding to the NIC, and /24 is the subnet mask you are using. Examples:

   - You want to add the IP 192.168.5.2 with a subnet mask of 255.255.255.0 to the NIC &#8220;Local Area Connection&#8221;, the command would be `netsh int ipv4 add address "Local Area Connection" 192.168.5.2/24 SkipAsSource=true`

   - You want to add the IP 10.1.1.2 with a subnet mask of 255.255.0.0 to the NIC &#8220;Wireless Network Connection&#8221;, the command would be:  `netsh int ipv4 add address "Wireless Network Connection" 10.1.1.2/16 SkipAsSource=true`

2. To make sure the command worked, run the following command to check: `netsh int ipv4 show ipaddresses level=verbose`

