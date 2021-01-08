---
title: Event 1059 DHCP Error
date: 2016-05-26T04:10:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/event-1059-dhcp-error/
categories:
  - Windows
tags:
  - Monitoring
---
<!--more-->

### Description:

After I installed a new DC and gave it the AD DS, DHCP, and DNS roles I let it sit for a couple days to replicate. I ran into the issue where I had set the server's IP static and it caused the DHCP to bind to the NIC when it shouldn't have which generated all these 1059 error's.

### To Resolve:

1. If you get this error, open up DHCP => Right Click (ServerName) => Add/Remove Bindings => Uncheck your server's IP address.

2. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `net stop dhcp && net start dhcp`

### References:

["Event ID 1059 — DHCP Server Active Directory Availability"](https://technet.microsoft.com/en-us/library/cc774849(v=ws.10).aspx)