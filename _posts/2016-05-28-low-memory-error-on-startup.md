---
title: Low Memory Error On Startup
date: 2016-05-28T06:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/low-memory-error-on-startup/
categories:
  - Hardware
tags:
  - Pre-Boot 
---
<!--more-->

### Description:

The computer will not boot into Windows, it will display a message similar to: &#8220;Windows NT has found only 495k of memory. 512K is required to run Windows. You need to upgrade your computer or run a configuration program provided by the manufacturer.&#8221;

### To Resolve:

1. Check the BIOS of the computer, does it show all the memory that's installed? If it doesn't,

2. Clear the CMOS battery on the motherboard. The easiest way to clear the CMOS is to enter the BIOS setup utility and choose to &#8220;Reset BIOS Settings&#8221; to their factory default levels.The exact menu option in your motherboard's BIOS may differ but look for phrases like reset to default, factory default, clear BIOS, load setup defaults, etc. This option is usually located at near the bottom/end of your BIOS options. Another way to clear the CMOS is to reseat the CMOS battery. By removing and then reinstalling the CMOS battery, you remove the source of power that saves your computer's BIOS settings.

3. Do an &#8220;Extended Memory Test&#8221; if your hardware manufacturer has that as an option. For Dells, this is done after the basic &#8220;Diagnostics&#8221; from the `F12` boot menu.

4. Look to re-image the workstation, Windows could be corrupt, I have only seen this on older computers.