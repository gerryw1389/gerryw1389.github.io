---
title: Code 10 Error In Device Manager
date: 2016-05-21T21:28:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/code-10-error-in-device-manager/
categories:
  - Hardware
---
<!--more-->

### Description:

You run `devmgmt.msc` and see that a hardware device has a warning with a `Code 10: Device won't start error`. You may see this if you run `control printers` and the device has a warning triangle next to it. This error indicates that there is a problem with the physical hardware or problem with the communication between the hardware and the OS.

### To Resolve:

1. Unplug the device and plug it back in. The troubleshooting steps for this will be similar to the steps in [Backup Drives Not Detected](https://automationadmin.com/2016/05/backup-drives-not-detected/). 3 possible problems: The USB port, the cable going from the device to the USB, or the device itself.

2. Plug the device into another computer, does it come up just fine? If it does, you can rule out the cable and device being bad. In which case, continue to the next step.

3. Find out the last time the computer was rebooted on the computer with the Code 10 Error for the device. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `net statistics workstation`. If it's been over a month, try rebooting. Also, uninstall and reinstall the USB root hubs (see Backup Drives Not Detected).

4. Call the manufacturer of the device for further troubleshooting.