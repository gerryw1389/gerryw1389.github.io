---
title: 'GFI: AV Check Failing'
date: 2016-05-23T12:36:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-av-check-failing/
tags:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

The AntiVirus check will be failing it's check to the dashboard. This happens when the AntiVirus definitions are out of date and mostly happen when the customer doesn't renew their subscription with the provider.

### To Resolve:

1. Find out which AV they use and simply update the AV software or just the definitions in most cases.

2. If needed, you may have to end the GUI or System Tray process and restart the AV Software for the agent to recognize the update.

3. If it's still failing after the AV software has been updates, restart the &#8220;Advanced Monitoring Agent&#8221; service.

### For updating VIPRE Antivirus:

1. Go to the VIPRE Site Navigator and make sure the licenses are not expired, VIPRE will update on an expired license sometimes.

2. Go to &#8220;[http://www.vipreantivirus.com/vipre-antivirus/definitions/](https://www.vipreantivirus.com/home-antivirus/antivirus.aspx)&#8221; and select the newest definition. &#8220;Save&#8221; the file to your downloads.

3. In the VIPRE GUI from the system tray, navigate to the &#8220;Overview&#8221; panel and choose the &#8220;Manage&#8221; button. This will be the agent, not the management console.

4. Click &#8220;View VIPRE Updates&#8221; and select the &#8220;Manually apply definitions…&#8221; button.

5. Navigate to where you downloaded the file and &#8220;Open&#8221; the download. Done.

### For updating AVG:

1. Go to the AVG GUI and select &#8220;Tools => Update&#8221;.

### For updating ESET Nod AV:

1. Open the console application => delete all update files.

2. Go to &#8220;Remote Admin&#8221; => delete all update files.

3. Update through the &#8220;Remote Admin&#8221; application.

4. Connect the console application to the &#8220;Remote Admin&#8221; application through port number.

5. Check should be passing now.