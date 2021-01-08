---
title: Registering OCX/DLL Files
date: 2016-05-26T22:45:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/registering-ocxdll-files/
categories:
  - Windows
---
<!--more-->

### Description:

It is not uncommon for an application to throw an error about an &#8220;unregistered dll/osc&#8221; file.

### To Resolve:

1. For 32b computers:

   - Run => `Regsvr32 /u (Filename.ocx/.dll)`
   - `Regsvr32 (Filename.ocx/.dll)`

2. For 64b computers:

   - [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `cd C:\Windows\SysWOW64`
   - `Regsvr32 /u (Filename.ocx/.dll)`
   - `Regsvr32 (Filename.ocx/.dll)`