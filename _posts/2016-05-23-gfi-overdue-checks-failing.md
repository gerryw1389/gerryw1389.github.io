---
title: 'GFI: Overdue Checks Failing'
date: 2016-05-23T12:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-overdue-checks-failing/
categories:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

There is no check associated with overdue servers, but they should be addressed quickly. Overdue server checks fail mostly because of loss of internet for the computer being monitored.

### To Resolve:

1. Make sure the computer being monitored can connect to the internet. If it cannot, follow the steps in &#8220;One Computer Cannot Access the Internet&#8221;.

2. If they can and GFI is running and is &#8220;Active&#8221;, then try this fix: (Note: You may have an error message about &#8220;Not Communicating&#8221; of some sort)

   - Apply this MS Fixit and restart the agent: [http://support.microsoft.com/kb/2801679](https://support.microsoft.com/en-us/kb/2801679)
   - To restart the agent, run `services.msc` and restart the `Advanced Monitoring Agent` Service.

3. If the agent is in &#8220;Maintenance&#8221; mode, then you simply need to switch it to &#8220;Active&#8221;.

4. For &#8220;Upload Error&#8221; in the Agent's GUI:

   - Make sure there is a secondary DNS on the NIC. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `ncpa.cpl` => Right click on the NIC => Local Area Connection => Properties => IPv4 Settings => Set a static secondary, typically 4.2.2.2 or 8.8.8.8 (Google's Open DNS Server's)

   - You will also see that some webpage's not resolving but you can ping them by IP. This is a tall tale sign of a DNS issue.