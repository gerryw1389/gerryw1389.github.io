---
title: 'PS: Send Email When Bitcoin Price Is X'
date: 2020-01-24T10:41:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/ps-send-email-bitcoin/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

I have the following scheduled tasks set to run hourly.

### To Resolve

1. [This function](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Get-BitcoinPrice.ps1) will run hourly and send me an email if bitcoin goes below a certain threshold.