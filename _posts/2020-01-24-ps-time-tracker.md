---
title: 'PS: Time Tracker'
date: 2020-01-24T09:48:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/ps-time-tracker/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

I have this scheduled task set to the following schedule: Start at 9AM M-F, repeat task every hour for a duration of 8 hours.

### To Resolve

1. [This function](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Start-TimeTracker.ps1) pops up a window and asks you what you are working on, it then records the answer to a log file. I used to use this often but have since disabled it, just posting in case anyone finds it useful.