---
title: Read/Write Errors On An External
date: 2016-05-21T04:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/readwrite-errors-on-an-external/
categories:
  - Hardware
---
<!--more-->

### Description:

You're external drive is not recognizing or you have multiple &#8220;Disk-Error&#8221; messages in the `eventvwr.msc`. Backup programs may report the backup failed due to &#8220;corruption&#8221;.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) (Drive letter of the external) => Press Enter to move to the next line so that you can run the next command from the drive directly => `chkdsk /x`

2. If it starts returning a bunch of errors, upload the Western Digital Lifeguard Diagnostics Tool and do a Quick Test. Any errors here is immediate RMA. Take note of the serial number of the drive prior to calling the manufacturer.