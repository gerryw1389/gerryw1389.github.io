---
title: One Driver Or Service Failed On Startup
date: 2016-05-26T22:29:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/one-driver-or-service-failed-on-startup/
tags:
  - Windows
---
<!--more-->

### Description:

When you boot your computer into Windows and arrive at the desktop, you may get a message that comes up as &#8220;One driver/service failed on system startup&#8221;. Per Microsoft Article #307734 the error can &#8220;occur if the Client for Microsoft Networks is not installed&#8221;.

### To Resolve:

1. Run => `ncpa.cpl` => Right click on &#8220;Local Area Connection&#8221; => Properties.

2. Once in the properties, choose &#8220;Install&#8221; on the middle of the Properties box.

3. Select &#8220;Clients&#8221; => Add => Client for Microsoft Networks => Ok.

4. Reboot the computer, should be good now.