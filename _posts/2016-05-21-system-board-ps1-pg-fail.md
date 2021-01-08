---
title: System Board PS1 PG Fail
date: 2016-05-21T04:58:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/system-board-ps1-pg-fail/
categories:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

Inside of Dell Open Manage there will be a red &#8220;X&#8221; on the Power Management tab. The hardware logs will have an error that says &#8220;System Board PS1 PG Fail&#8221;.

### To Resolve:

1. You need to get the Service tag of the server and go to the Dell Downloads page and download the newest BIOS (under the &#8220;BIOS&#8221; section) and the Idrac drivers (under the Embedded Server Management&#8221; section).

2. Install the Idrac driver first and then the BIOS driver, it will notify that you need to reboot. Instead, we will just do a shut down because we will need to drain the residual power on the server.

3. Drain the residual power and bring the server up from a clean boot.