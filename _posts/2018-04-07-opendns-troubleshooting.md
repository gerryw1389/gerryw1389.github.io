---
title: OpenDNS Troubleshooting
date: 2018-04-07T03:31:39+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/opendns-troubleshooting/
tags:
  - WebSoftware
  - Networking
---
<!--more-->

### Description:

So every now and then, I will notice that our OpenDNS service will not be blocking queries. I usually perform the following steps to resolve.

### To Resolve:

1. Login to each DNS server and `Clear DNS Cache` then wait 5 minutes.

2. Pull up a command prompt and type:

   ```powershell
   ping 208.67.222.222
   nslookup whoami.akamai.net.
   netsh interface ip show dns
   nslookup -type=txt debug.opendns.com
   ```

3. Go to [OpenDNS](https://welcome.opendns.com/)

4. Go to the test blocked site `www.internetbadguys.com` and ensure it is blocked by provider.