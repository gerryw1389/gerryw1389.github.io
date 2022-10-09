---
title: Configuring SNMP
date: 2017-02-20T05:33:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/02/configuring-snmp/
categories:
  - Networking
tags:
  - Monitoring
---
<!--more-->

### Description:

Many times administrators will want to monitor servers, switches, ect. Aside from simple ping tests, WMI queries, ect. you may find yourself wanting to use SNMP. SNMP is a chatty protocol that you can learn about my just googling the phrase. Essentially, V3 is recommended but I have only really seen V2 with a custom community string configured.

### To Resolve:

1. If I wanted to monitor a switch, for example to send SNMP logs to a PRTG server, I would do the following. 
   - For example on my Ubiquity switch: Login via web GUI. Go to System => Advanced => SNMP. 
   - Add community => enter community name (make one up, but make sure you know it because all devices will need to be on the same one), 
   - Set group name to DefaultRead, and IP address to the target server. 
   - I would then go to the Trap Receiver V1/2 and add HostAddress = Host of switch, Community name = same as above, Notify Type = Inform, UDP Port 161. 
   - That's it! Logs will just roll in.

2. For servers, you add the `SNMP Service` feature. After it's installed, just run `services.msc` and go to the SNMP service. Under Security => Check the box to send authentication traps and set the community rights to ReadOnly and the community string to your own string. Click Add. NOTE: If the security tab does not show up, close out of `service.msc` and open it back up. 
   - For more details, see [this](http://www.questiondriven.com/2012/02/23/snmp-service-setup-and-snmp-trap-setup/) post but note that you should never use `public` as the community name.