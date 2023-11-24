---
title: 'GFI: Offline Checks Failing'
date: 2016-05-23T12:43:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-offline-checks-failing/
tags:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

There is no check associated with offline servers, but they should be addressed quickly. Server's will show in the Dashboard as being Offline for &#8220;X&#8221; amount of time. We need to call them and get them back to reporting. This one fails normally because a server has been rebooted, stuck in PE (Pre-Boot Environment), or the customer purchased a new server.

### To Resolve:

1. If GFI is running and is &#8220;Active&#8221;, then try this fix: (Note: You may have an error message about &#8220;Not Communicating&#8221; of some sort)

   - Apply this MS Fixit and restart the agent: [http://support.microsoft.com/kb/2801679](https://support.microsoft.com/en-us/kb/2801679)
   - To restart the agent, run `services.msc` and restart the `Advanced Monitoring Agent` Service.

2. If the agent is in &#8220;Maintenance&#8221; mode, then you simply need to switch it to &#8220;Active&#8221;

3. If it's been offline for a while, chances are the customer purchased a new server. Go to the Dashboard and delete the old device under &#8220;Client => Sites&#8221;. Get in the new server and install GFI.

4. If they have McAffee AV, it could be blocking the agent. To Fix:

   - Get the credentials and login to the &#8220;Admin Console&#8221; through the McAffee GUI.
   - Set the exclusions for `C:\Program Files\Advanced Monitoring Agent\winagent.exe` and `SNMP Service`
   - Re-run the checks, should be good to go.