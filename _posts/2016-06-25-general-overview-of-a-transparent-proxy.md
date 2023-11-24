---
title: General Overview Of A Transparent Proxy
date: 2016-06-25T01:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/general-overview-of-a-transparent-proxy/
tags:
  - SysAdmin
---
<!--more-->

### Description:

I cannot find out where I read this, but I found this on Reddit the other day. Not too specific, but just broad enough to give an overview of what a transparent proxy is and how to set one up.

### To Resolve:

1. Pick a software: Example Websense Triton-AP

2. Setup an internal Certificate Authority and install the root cert for every domain joined PC via Group Policy

3. Push out proxy settings via group policy as well. NOTE: Even if for some reason the client doesn't have proxy settings then my router has a Policy Based Routing rule. Any port 80/443 traffic sent to the firewall is routed to the Websense Triton AP v5000 appliance.

SSL is decrypted and then re-encrypted and everything is logged.

The proxy can identify users by 2 methods:

1. Domain Controller logs. It connects to all DCs in the domain and imports in the logs looking for the IP address & username that logged in associated with it then stores this in the DB. Any time it sees traffic from IP address X it assumes that it is user X based on the DC logs.

2. NETBIOS query to the target device to ask who is logged on. If the DC log is > 1 hour old it will attempt to refresh via NETBIOS. If NETBIOS fails it falls back to DC logs.