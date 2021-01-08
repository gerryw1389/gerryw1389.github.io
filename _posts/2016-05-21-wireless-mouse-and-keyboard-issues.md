---
title: Wireless Mouse And Keyboard Issues
date: 2016-05-21T04:32:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wireless-mouse-and-keyboard-issues/
categories:
  - Hardware
---
<!--more-->

### Description:

If you ever have a problem with wireless devices not working, follow these steps. First see if you can find a set of &#8220;wired&#8221; counter parts for the devices to use for troubleshooting purposes. These are relatively cheap and should be available for times like these.

### To Resolve:

1. Unplug the &#8220;Receiver&#8221; or &#8220;Dongle&#8221; from the USB port that the wireless devices connect to. Plug it back in. If there is an option to &#8220;re-sync&#8221; or &#8220;pair&#8221; the devices, try this as well.

2. Check the batteries for the devices, are there lights on? If you look at the bottom of the mouse you should see a colored LED light and the keyboard should have a power light or a light that comes on when you select &#8220;Caps Lock&#8221; or &#8220;Num Lock&#8221;.

3. Run => `devmgmt.msc` => do you see them listed here? They will be under the &#8220;Mice&#8221; and &#8220;Keyboards&#8221; sections respectively if the right driver is installed, if not check under the &#8220;Universal Serial Bus Controllers&#8221; section if the right driver is not installed.

4. If the devices do not show up under the Device Manager, chances are you have faulty devices or faulty USB ports. Try plugging in a USB device like a wired mouse or keyboard that you know that works to determine if it's the USB ports to blame. If other devices work and none of the above works, replace your wireless devices. Wired mice and keyboards are the way to go from a tech point of view because if they are plugged in, they should work. If not, chances are => your device has failed.