---
title: W10 Clean Upgrade
date: 2016-05-28T07:08:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/w10-clean-upgrade/
tags:
  - Windows
---
<!--more-->

### Description:

Follow these steps to do a clean upgrade to Windows 10. I am aware that you have the option to do a clean install when you upgrade, but it will still create a `c:\windows.old` directory. Using this method will produce a completely clean upgrade.

### To Resolve:

1. Download Windows 10 from the Microsoft tool and then copy `sourcegatherosstate.exe` to a writable directory.

2. Launch it to get `GenuineTicket.xml` in the same directory. Copy and paste that to a thumb drive.

3. Unplug your network cable.

4. Install a fresh copy of Windows 10 on the same computer with the network cable still unplugged. Skip the part about a product key.

5. Once installed, copy the `GinuineTicket.xml` to `C:\ProgramData\Microsoft\Windows\Clipsvc\GenuineTicket`

6. Reboot the computer and plug the network cable in at boot. Windows should activate now.

### References:

["No need for a full upgrade to install 10 from scratch and activate"](https://www.reddit.com/r/Windows10/comments/3i93mp/no_need_for_a_full_upgrade_to_install_10_from)