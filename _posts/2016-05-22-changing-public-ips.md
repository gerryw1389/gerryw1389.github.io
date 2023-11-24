---
title: Changing Public IPs On A Checkpoint Router
date: 2016-05-22T07:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/changing-public-ips/
tags:
  - Networking
tags:
  - Router
---
<!--more-->

### Description:

If you ever need to change public IP Addresses, follow these steps:


### To Resolve:

1. Get the old public IP of the network by going to [ipchicken.com](http://ipchicken.com/) or however. Get the soon-to-be IP.

2. Login to the router's web GUI through a web browser.

3. For Checkpoints, you navigate to the Network and Internet tab and Edit the primary connection. Set the Port to WAN and Connection type to LAN (for other router's this may be DHCP). Uncheck the Obtain an IP Automatically checkbox and enter the IP manually of the NEW IP. For the subnet mask, select the option `255.255.255.252/30` if the ISP only gave the network a specific range. The Default Gateway is usually one IP address less than the IP Address.

  <img class="alignnone size-full wp-image-639" src="https://automationadmin.com/assets/images/uploads/2016/09/changing-public-ips.png" alt="changing-public-ips" width="779" height="526" srcset="https://automationadmin.com/assets/images/uploads/2016/09/changing-public-ips.png 779w, https://automationadmin.com/assets/images/uploads/2016/09/changing-public-ips-300x203.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/changing-public-ips-768x519.png 768w" sizes="(max-width: 779px) 100vw, 779px" />

