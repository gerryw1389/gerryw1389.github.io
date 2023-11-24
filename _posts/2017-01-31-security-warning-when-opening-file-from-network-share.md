---
title: Security Warning When Opening File From Network Share
date: 2017-01-31T04:57:29+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/security-warning-when-opening-file-from-network-share/
tags:
  - Networking
  - Windows
---
<!--more-->

### Description:

So like most people, I don't store anything important on my local computer and have a Linux samba share where I store all my important stuff that I have mapped to my computer for file manipulations. This works fine from Linux to Windows, but I couldn't get Windows to shut up about `Open File Security Warning` every time I tried to open something. Thankfully, this exact situation has already been addressed and answered:

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `inetcpl.cpl` => Tools => Internet Options => Security tab => Local Intranet => Sites:

   - Check &#8220;automatically detect intranet network&#8221;
   - Go to Advanced => Add
   - In the text box type: `file://computername` or `10.0.0.100` or whatever the IP is of the server.
   - Add => Close => OK => OK.

### References:

["Security warning when opening file from network share"](https://stackoverflow.com/questions/2638862/security-warning-when-opening-file-from-network-share)