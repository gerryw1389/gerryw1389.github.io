---
title: Setting Up Raspberry PI 3
date: 2017-08-26T05:37:45+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/setting-up-raspberry-pi-3/
tags:
  - Hardware
tags:
  - Setup
---
<!--more-->

### Description:

So I ordered a PI 3 off Amazon the other day and wanted to document how I set it up:

### To Resolve:

1. Setup the OS on the SD Card:

   - Download Raspian zip file from raspberrypi.org
   - Download Etcher and install it.
   - Connect an SD card reader with the SD card inside.
   - Open Etcher and select from your hard drive the Raspberry Pi .img or .zip file you wish to write to the SD card.
   - Select the SD card you wish to write your image to.
   - Review your selections and click "Flash!" to begin writing data to the SD card.

2. Put together the pi

3. Plug everything in with power being last

4. Sign in with pi/raspberry and then type `startx`. For me for some reason, I didn't have to do this as it booted straight to the desktop.

### Post Config:

1. The first thing we needed to do was set the root password:

   ```shell
   sudo passwd root
   (EnterPassword)
   ```

2. Next, needed to change the keyboard layout to English => US:

   ```shell
   localectl set-keymap us
   sudo reboot
   ```

3. Next, we needed the Pi to open a webpage and turn off all settings that let it go to sleep:

   ```shell
   #edit and save the following file
   sudo vi ~/.config/lxsession/LXDE-pi/autostart
   @xset s 0 0
   @xset s noblank
   @xset s noexpose
   @xset dpms 0 0 0
   ```

4. Reboot and test!