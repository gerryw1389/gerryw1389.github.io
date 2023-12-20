---
title: Dell OpenManage
date: 2016-10-15T02:55:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/dell-openmanage/
tags:
  - Hardware
tags:
  - Batch-Commands
  - Monitoring
---
<!--more-->

### Description:

Dell OSMA is a software that you usually install on Dell physical servers that reports the health and status of system components.

### To Resolve:

1. This page is meant just as a few reference commands that you can run on a Dell server with OSMA installed. You could probably script this, but I just setup a PRTG sensor that pulls all this data automatically (somebody had to write it though!). There are 3 &#8220;level 1&#8221; commands and many others that branch off those: omconfigure, omreport, and omhelp.

   ```escape
   # list of controllers by id  
   omreport storage controller

   # get a system summary of everything except storage  
   omreport system summary

   # overall report of system components. OK is good, anything else must be looked into  
   omreport chassis

   # to check the status of your virtual disks  
   omreport storage vdisk controller=0

   # to set custom text on your server's display  
   omconfig chassis frontpanel lcdindex=1 config=custom text='enter here your custom text'
   ```

