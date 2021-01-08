---
title: Windows TCP/IP Reset
date: 2016-05-22T08:23:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-tcpip-reset/
categories:
  - Networking
tags:
  - Scripting-CMD
---
<!--more-->

### Description:

Do these steps to reset the TCP/IP stack for Windows.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type:

   ```powershell
   netsh int ip reset resetlog.txt
   netsh winsock reset
   netsh int ipv4 reset
   netsh int ipv6 reset
   ```

2. Reboot the computer. Of course, this can be made into a batch file:

   ```powershell
   echo "Starting networking stack reset"
   cd %windir%\system32
   netsh int ip reset c:\windows\temp\resetlog.txt
   netsh winsock reset
   netsh int ipv4 reset
   netsh int ipv6 reset
   echo "Networking stack reset"
   PAUSE
   shutdown -r -f -t 03
   ```

