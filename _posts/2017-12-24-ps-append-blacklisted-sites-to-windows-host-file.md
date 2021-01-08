---
title: 'PS: Append Blacklisted Sites To Windows Host File'
date: 2017-12-24T03:17:48+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-append-blacklisted-sites-to-windows-host-file/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Let me start by saying first and foremost, I am a SysAdmin and not a &#8220;computer geek / tinkerer&#8221;. Modifying the host file is almost NEVER the right answer for blocking sites. This should be done at the gateway or using a device like pi-hole or a web filtering service like OpenDNS. But, I just wanted to play around with PS on my machine to see what I could find, so here goes.

### To Resolve:

1. Function - [Set-AppendedHostFile](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-AppendedHostFile.ps1)