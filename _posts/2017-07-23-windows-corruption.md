---
title: Windows Corruption
date: 2017-07-23T05:28:05+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/windows-corruption/
categories:
  - Windows
---
<!--more-->

### Description:

This post will be brief, but I wanted to create it because despite all our effort, sometimes issues cannot be resolved due to a windows corruption which will usually be one of the last steps on your checklist in a troubleshooting process. Here are some things to try to test windows corruption.

### To Resolve:

1. First and foremost, start CMD as Admin and run: sfc /scannow

This is the System File Checker and will sometimes fix Windows corruption issues, sometimes.

2. Try: DISM.exe /Online /Cleanup-image /Scanhealth

followed by

DISM.exe /Online /Cleanup-image /Restorehealth

3. Use third party software like [tweaking.com's](http://www.majorgeeks.com/files/details/tweaking_com_windows_repair.html) or [bleepingcomputer's](https://www.bleepingcomputer.com/download/windows-repair-all-in-one/) repair tools.