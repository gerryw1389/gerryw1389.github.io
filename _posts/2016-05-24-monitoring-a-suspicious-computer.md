---
title: Monitoring A Suspicious Computer
date: 2016-05-24T12:25:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/monitoring-a-suspicious-computer/
tags:
  - LocalSoftware
tags:
  - Monitoring
---
<!--more-->

### Description:

At one point or another, you may want to monitor a computer to log what connections it is making.

### To Resolve:

1. If you have a network diagram, look to see what port on the switch correlates to the suspect computer.

2. Log into your switch and find the monitoring section. For a Netgear GS748T => It is Monitoring => Port Mirroring.

3. Set the ports to mirror each other. For the Netgear switch, you checked a box for the source port, filled in the destination port, filled the direction (Tx and Rx (for send and receive)) and hit apply.

4. Plug a laptop into the mirroring port and start up Wireshark. Disable all but the wired NIC on the Interface List and setup a capture filter of &#8220;host=(ip address of monitored computer)&#8221; and then click => Start.

5. After however much time you feel, comb the logs of Wireshark to determine what connections the computer was making.