---
title: Faulty Switches
date: 2016-05-21T05:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/faulty-switches/
tags:
  - Hardware
---
<!--more-->

### Description:

Faulty switches can have many ways of presenting themselves. Most of the time they are obvious like total disconnections from workstations to the internal network / internet. Sometimes they are a little harder to spot. For example: If you ever have an issue with the upload being slower than download from the server like the screen shots below:

- Workstation to Server, 3GB Data folder:

   - ![faulty-switch-1](https://automationadmin.com/assets/images/uploads/2016/09/faulty-switch-1.png){:class="img-responsive"}

- Server to Workstation, 3GB Data folder (same folder):

   - ![faulty-switch-2](https://automationadmin.com/assets/images/uploads/2016/09/faulty-switch-2.png){:class="img-responsive"}

### To Resolve:

1. Run a ping from one workstation to the server. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ping (server IP or name)`. For better results, hold a constant ping (`ping -t`).

2. If the responses come back fine, it could still be a faulty switch. Try pinging the default gateway and 8.8.8.8, if you see any packet loss => you have a disconnect somewhere or a faulty switch.

3. Try uploading a folder to the server, is the read/ write speed equal? If not, you may have a faulty switch.

4. Replace the switch and see if you get same results.