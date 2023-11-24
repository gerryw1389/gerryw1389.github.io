---
title: RDP Session Stuck On Configuring Session
date: 2016-05-22T06:39:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/rdp-session-stuck-on-configuring-session/
tags:
  - Windows
---
<!--more-->

### Description:

When you try to RDP to a computer either in the internal network or through a VPN, you will be stuck on a Window that just says "Configuring Remote Session" and will eventually fail.

### To Resolve:

1. Reboot each computer on each of the connection. (Yes, this means to reboot the terminal server!! Let's just say I spent over 2 hours on one that this simple step resolved (although it could've been a combination of multiple changes AND then a reboot, but anyways ...))

2. In the RDP Connection options, navigate to Options => Local Resources => Remote Audio => Settings => Do Not Use on both.

3. Now navigate to Local Devices and Resources on the same tab => Uncheck all, then go to &#8220;More..&#8221; and uncheck all of those as well.

4. Now navigate to the Experience tab and uncheck the Persistent Bitmap Caching checkbox.

5. If this doesn't work, on the Terminal Server, apply Windows updates and reboot once again.