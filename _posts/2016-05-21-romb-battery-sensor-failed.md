---
title: ROMB Battery Sensor Failed
date: 2016-05-21T04:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/romb-battery-sensor-failed/
tags:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

Inside of Dell Open Manage there will be a red &#8220;X&#8221; on the Power Management tab. This has to do with the perc adapter battery and is monitored by the controller.

### To Resolve:

1. Dell OM and look at the system, there will be a red &#8220;X&#8221; on the Power Management tab. Look at the logs, that's where you will get the error mentioned.

2. Export the logs to the root of the C: on the server and then clear them.

3. Get the service tag of the server and look it up on support.dell.com and look at the drivers per the OS of the server.

4. For this one, you want to download the &#8220;SAS RAID => Firmware and Driver&#8221; that matches your adapter. In my case it was a Perc i-6 adapter and I had to download like 5th option down, so make sure to match them.

5. Download and install the driver first and then the firmware.

6. Should be good, no more actions needed. If it's not good and it's still giving that error => call Dell. Triage told me they don't do any troubleshooting for that part, they just replace it. Advise the customer that if they have basic support they will have to buy it, Pro support has no worries.