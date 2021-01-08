---
title: How To Access Cisco Devices With Putty
date: 2017-07-23T05:48:44+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/how-to-access-cisco-devices-with-putty/
categories:
  - Hardware
tags:
  - Router
---
<!--more-->

### Description:

It seems pretty straightforward to configure a router you will need access it somehow, but how? Well you have two options: Serial connection and SSH.

### To Resolve:

1. For both options you will need Putty or, as I prefer, [Kitty](https://portableapps.com/apps/internet/kitty-portable).

2. Let's start with a console cable. Many devices these days don't have serial ports so you will need to get a rollover cable or RS232 => USB adapter. Either way, you will be going from the RJ45 port on the router to a USB port on your PC.

   - First, open the device manager and get the &#8220;COM&#8221; port device number under the Ports section. It's usually COM4 in my experience.
   - Inside Kitty, expand Connection > Serial. Enter the port number inside &#8220;Serial line to connect to&#8221; text box. Enter other values also as shown below.

   ```escape
   Bits per sec: 9600
   Data bits: 8
   Parity: none
   Stop bits: 1
   Flow control: none
   ```

   - That's it. Press enter a few times if you just see a vertical bar on the first line, it could be timed out &#8220;chilling&#8221;.

3. Once device has been [configured for SSH](https://automationadmin.com/2016/10/ccna-user-passwords-ssh/), you will just enter the IP and port 22 to connect to it. Login using your setup.