---
title: Add A Printer For A Terminal Server
date: 2016-05-21T21:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/add-a-printer-for-a-terminal-server/
tags:
  - Networking
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

Do this if you want to add a printer to a terminal services session. This printer should only be used during a RDP session. If you want a printer to work with all the time, you need to install it on the RDP server. By default, when you run `mstsc` under the Local Resources tab, your local printer will be checked. This means that you can print from a RDP session to a local printer.

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `control printers`.

2. Select the "Add A Printer Wizard" => Click Local printer => clear the Automatically detect and install my Plug and Play printer => Next => under Ports, you will see several ports named TSxxx. These are client mapped ports. Click the port that corresponds to your client computer's name and port, and then click Next.

3. Continue until you finish the printer installation.