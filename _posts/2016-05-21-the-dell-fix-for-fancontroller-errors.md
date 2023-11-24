---
title: '&#8220;The Dell Fix&#8221; For Fan/Controller Errors'
date: 2016-05-21T21:26:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/the-dell-fix-for-fancontroller-errors/
tags:
  - Hardware
---
<!--more-->

### Description:

Your workstation is giving you some kind of message preventing you from getting into Windows. Usually it will say:  
&#8220;Hard Drive Not Found&#8221; or &#8220;No Boot Device Found&#8221;  
"HD Fan Failure  
CPU Fan Failure  
Keyboard Initialization Failed  
Strike F1 to continue"

### To Resolve:

1. Shut down the computer.

2. Unplug the power cord from the power supply.

3. Hold down the power button for one minute. This drains the residual power on the motherboard.

4. Plug the cable back in and boot it back up.

5. For the &#8220;Hard Drive Not Found&#8221; error, there may be a CD in the tray that Windows is trying to boot to or the HDD may need a firmware update as with the Dell 9020's.

6. If the above doesn't work, your workstation may actually have a failed part. Run diagnostics to make sure by pressing `F12` on startup and choosing Hardware Diagnostics.

7. Look in the BIOS (Usually F2 on startup) to see if the drive is even detected. Verify cabling. You may have to replace the drive, the cables connecting the drive to the motherboard, or the motherboard itself.