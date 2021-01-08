---
title: Perc Battery State Failed
date: 2016-05-21T04:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/perc-battery-state-failed/
categories:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

Inside of Dell OM, there will be a red X on the battery and it will say failed.

### To Resolve:

1. Export and clear the logs by going to System => Logs => and exporting and clearing each one doing one at a time.

2. Restart the four `Dism` services associated with Dell OM (the only four listed in `services.msc`).

3. On the batteries section in Dell OM, choose the option to &#8220;Start Learn Cycle&#8221;. This will discharge and rebuild the PERC batteries.

   NOTE: In my situation, two different servers did this after a firmware update, so I suspected they weren't bad. After 48-72 they should show to be good. If it is still failing, call Dell to get them replaced.
   {: .notice--success}


   <img class="size-large wp-image-686 aligncenter" src="https://automationadmin.com/assets/images/uploads/2016/09/perc-battery-state-failed-1024x477.png" alt="perc-battery-state-failed" width="720" height="335" srcset="https://automationadmin.com/assets/images/uploads/2016/09/perc-battery-state-failed-1024x477.png 1024w, https://automationadmin.com/assets/images/uploads/2016/09/perc-battery-state-failed-300x140.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/perc-battery-state-failed-768x357.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/perc-battery-state-failed.png 1386w" sizes="(max-width: 720px) 100vw, 720px" />


