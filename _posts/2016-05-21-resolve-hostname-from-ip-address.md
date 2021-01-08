---
title: Resolve Hostname From IP Address
date: 2016-05-21T21:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/resolve-hostname-from-ip-address/
categories:
  - Networking
tags:
  - Scripting-CMD
---
<!--more-->

### Description:

Have you ever wanted to get a hostname from IP address? It seems easy, but for some reason you may not remember the exact commands to run. Not to fear, here are a couple to help:

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `nslookup (ip address)`. This is the most common method. It assumes that you your DNS server has a forward lookup entry for the host you are querying, which will not always return anything.

2. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `ping -a (ip address)`

3. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `nbtstat -a (ip address)`. This command has worked for me every time!