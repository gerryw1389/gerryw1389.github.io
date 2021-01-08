---
title: Adding A Sensor In PRTG
date: 2016-05-23T12:48:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/adding-a-sensor-in-prtg/
categories:
  - LocalSoftware
tags:
  - Monitoring
---
<!--more-->

### Description:

PRTG Network monitor is an application that is ran on one of our VM's that scans the network every minute and reports to us. Follow these steps to add a sensor:

### To Resolve:

1. Login to PRTG by going to your browser and entering the IP of the server it is running on (sign in via webGUI).

2. You then go to the devices tab at the top to see all the devices we have on the network. Our current license only allows 100 sensors, or things we can monitor in all.

3. To add a sensor, select a device and go to add sensors to add it. Many of these will query through WMI and SNMP so make sure those are configured on the devices you want to monitor.

4. That's it! Just keep this open and make sure it is set to send email alerts for anything that is red (e.g. fails a check).