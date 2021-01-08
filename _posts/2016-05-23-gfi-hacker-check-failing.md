---
title: 'GFI: Hacker Check Failing'
date: 2016-05-23T12:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-hacker-check-failing/
categories:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

The Hacker check will fail on the GFI Agent dashboard. The default check references the Windows Event Viewer for any unsuccessful login attempts.

### To Resolve:

1. ALWAYS try to RDP to the clients public IP first.

   - Get their public IP from the dashboard.

   - Run => mstsc => (their IP) => &#8220;:3389&#8221; at the end of their IP. Ex: mstsc => &#8220;192.168.0.1:3389&#8221; => Connect.

2. If this brings up a Windows Login screen asking for credentials, they have RDP enabled and need to find an alternative. If it doesn't come to this screen, they could still have the port open but RDP disabled on the computer it's forwarded to. In most cases, this means that some computers on the internal network are not authenticating with the server either through mapped drives or some kind of application software and can most likely be ignored. Ideally, you should try and resolve this issue.

3. If the port is open, offer alternatives to the client.

   - For individuals needing to remote in from home offer a client VPN or RAS (Remote Access Software) such as LogMeIn or GoToMyPC.

   - For office to office connections a Site to Site VPN is the best option. NOTE: They have to have VPN capable routers to setup a site to site VPN.