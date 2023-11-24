---
title: Faulty NIC
date: 2016-05-21T21:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/faulty-nic/
tags:
  - Hardware
---
<!--more-->

### Description:

You will have multiple drops in your connection or no connection at all to the internal network or the internet. Any applications that rely on network communication or your web browser will be laggy or not loading at all.

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `eventvwr.msc` and see if there is a bunch of &#8220;ec1express&#8221; errors.

2. Check link speed in the networking tab of task manager and see if it matches other computers in the same environment. Remember, link speed is the slowest speed between connections. If you have a Gigabit NIC but a 100Mb Switch, you will be running at 100Mb.

3. Get the make/model of NIC and download the newest driver from the manufacturers website. Save it locally and uninstall the current driver and install the newest one.

4. If the above doesn't resolve the issue, you may actually have a defective NIC, if the computer is under warranty get it replaced, if not buy a new one, install, and test.