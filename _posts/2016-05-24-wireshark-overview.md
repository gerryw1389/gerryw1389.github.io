---
title: Wireshark Overview
date: 2016-05-24T12:26:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wireshark-overview/
tags:
  - LocalSoftware
tags:
  - Monitoring
---
<!--more-->

### Description:

Wireshark is a packet-capturing freeware that is used by SA's across the world. It may seem a little confusing at first but the general steps are to:

1. Select &#8220;Interface List&#8221; and check off the NIC's you will use to capture packets.

2. Go to &#8220;Capture Options&#8221; and make sure the &#8220;Use promiscuous mode&#8221; is checked. Note that this is by default.

3. Click the &#8220;Start&#8221; (green fin icon) to start capturing packets.

4. Click &#8220;Stop&#8221; to stop capturing. With no filters applied, you can see all the packets in real time that the program captured.

5. Now you can analyze the packets or start filtering for specific packets and see their contents.

### To Resolve:

1. Once you have traffic you need, you just apply filters such as those found [here](https://www.wireshark.org/docs/wsug_html_chunked/index.html).