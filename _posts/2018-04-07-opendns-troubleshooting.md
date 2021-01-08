---
title: OpenDNS Troubleshooting
date: 2018-04-07T03:31:39+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/opendns-troubleshooting/
categories:
  - WebSoftware
  - Networking
tags:
  - Cloud
---
<!--more-->

### Description:

So every now and then, I will notice that our OpenDNS service will not be blocking queries. I usually perform the following steps to resolve.

### To Resolve:

1. Login to each DNS server and &#8220;Clear DNS Cache&#8221;, then wait 5 minutes.

2. Pull up a command prompt and type:

   ```powershell
   ping 208.67.222.222
   nslookup whoami.akamai.net.
   netsh interface ip show dns
   nslookup -type=txt debug.opendns.com
   ```

3. Go to [OpenDNS](https://welcome.opendns.com/)

4. Go to the [test blocked site](https://phish.opendns.com/main?url=www.internetbadguys.com&server=dfw2&prefs=&tagging=&nref)