---
title: Blocking Internet Access
date: 2016-05-22T06:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/blocking-internet-access/
tags:
  - Networking
  - Windows
tags:
  - Tweaks
---
<!--more-->

### Description:

Sometimes, Network Admins want to disable the internet from end users.

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `inetcpl.cpl`. Once inside the Internet Properties, navigate to the Connections tab and setup a fake proxy under LAN Settings.

2. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `ncpa.cpl`. Set a static IP and point the default gateway to 127.0.0.1 so the computer is pointing to itself to hand out an IP.

3. If your router supports it, navigate to the Network Objects section and create a Web Rule based off the computers MAC Address to block internet for that computer.