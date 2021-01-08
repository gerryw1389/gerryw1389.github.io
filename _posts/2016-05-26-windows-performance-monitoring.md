---
title: Windows Performance Monitoring
date: 2016-05-26T22:36:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-performance-monitoring/
categories:
  - Windows
---
<!--more-->

### Description:

Many people like to use freeware tools to analyze their systems, but when it comes to systems administration you quickly find that those tools are not allowed in a business environment or it's a pain to always have to use them, so you naturally start looking into built in native Windows tools for issues. One of my favorites is the Windows Task Manager and Resource Manager (resmon).

### To Resolve:

1. To open the Windows Task Manager, press Ctrl+Shift+ESC. I use two main tabs:

   - The Processes tab: Sort my memory usage. After a while you will learn what should be running the highest here and what should not.

   - The Performance tab: Computers should typically be using half of what they got under most circumstances.

2. The Resource Monitor and Performance Monitor can be of great use as well. Resource monitor can be found on the Performance tab or by Run => Resmon and the Performance Monitor can be ran by Run => Perfmon

   - Once you open the Peformance Monitor you just right click and add counters to measure performance. Use the reference below for an in-depth overview:

### Resources:

["Performance Monitor (perfmon)"](http://www.computerperformance.co.uk/HealthCheck/index.htm)