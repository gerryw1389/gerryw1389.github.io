---
title: Faulty HDD
date: 2016-05-21T21:39:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/faulty-hdd/
tags:
  - Hardware
---
<!--more-->

### Description:

The following symptoms may be signs that your HDD may be starting to fail:

1. Strange noises. Sometimes hearing strange grinding and thrashing noises means your drive is beyond repair.

2. Disappearing data and disk errors. If your computer gives you errors when trying to save a file or you can't find files in directories you know that you created.

3. Your computer stops recognizing your drive. Try placing your HDD in another computer to see if it works.

4. Computer crashes and blue screens are common when HDD's start to fail.

5. Really slow access times. It shouldn't take half an hour to open a folder in Windows Explorer, or two hours to empty the trash.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `chkdsk /x`. If the drive is the system drive, you will have to type `y` to indicate yes to run on next boot as Windows cannot check the drive that is currently in use.

2. You might be able to run [Western Digital Lifeguard Diagnostics](http://www.majorgeeks.com/files/details/western_digital_data_lifeguard_tools.html) on the system drive, but I have never done this. I do know it's a great tool to get the serial number of the drive and to see if it passes a quick SMART test.