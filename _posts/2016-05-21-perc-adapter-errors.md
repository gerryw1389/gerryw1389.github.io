---
title: Perc Adapter Errors
date: 2016-05-21T04:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/perc-adapter-errors/
tags:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

Inside of Dell Open Manage, you will see &#8220;Storage Drive 0: Drive slot sensor for storage&#8221; or &#8220;Bad PHY Slot 0: Connector 0 Controller 0&#8221; in the logs. You will see errors such as &#8220;E1810 HDD 0 Fault&#8221; on the physical server's LCD display as well, usually with an amber background indicating a &#8220;Warning&#8221;.

### To Resolve:

1. Get the service tag of the server. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `wmic bios get serialnumber`. Look that up on the Dell website.

2. Once there, you need to update the drivers and firmware for the Perc Adapter. Navigate to the &#8220;SAS Raid&#8221; section and download the newest one with the word (firmware) and (driver) after it that matches that system specifically.

3. Run those and reboot. Export and clear the Dell logs through Open Manage (OM).

4. Run => `services.msc` => Restart all four DSM Services related to OM.

5. Log back in to OM, if it's still bad, call Dell. There may be battery errors from the reboot. This is because the Perc adapter does a battery test on reboot and if it's bad, then the battery will show to be bad. You will have to resolve the issue through Dell, many times replacing the perc adapter itself resolves the issue. Note that if your sever is under Basic warranty you will have to pay for this, Pro warranty doesn't need to worry.