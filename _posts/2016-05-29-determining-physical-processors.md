---
title: Determining Physical Processors
date: 2016-05-29T03:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/determining-physical-processors/
tags:
  - Hardware
---
<!--more-->

### Description:

In the event that you want to find the number of physical processors a server has without opening it up, you can try these methods:

### To Resolve:

1. Right click on Computer => Properties. This screen will usually have the number of processors installed after the name of the processor.

2. If you know the number of cores per processor, you can run `devmgmt.msc` and see how many is installed. For example, servers with the E500 series processors typically will have 8 Processors installed if only one physical CPU is installed and 16 if two are.

3. You can also Run => `Resmon` to bring up the Resource Monitor and determine how many are installed by going to the CPU tab. If it lists CPU0 => CPU7 only once then you only have a single processor but if it list them twice with &#8220;Node X&#8221; in parethensis e.g. &#8220;CPU 2 (Node 0)&#8221; then you have that many processors installed.

4. Another command I have found that just tells if you have more than one installed is to run `get-wmiobject win32_processor` in PowerShell. Navigate down to the &#8220;LoadPercentage&#8221; line and if it is blank => you have one, if it has a number you have more than one.