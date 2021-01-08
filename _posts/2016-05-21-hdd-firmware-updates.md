---
title: HDD Firmware Updates
date: 2016-05-21T21:40:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hdd-firmware-updates/
categories:
  - Hardware
---
<!--more-->

### Description:

Some newer computers have what I like to call &#8220;over-sensitive BIOS's&#8221; and have been known to produce `HDD Not Found` errors when the user tried to boot the computer. Dell 9020's are the only known ones so far, but many will be sure to come.

### To Resolve:

1. On another computer, download the Firmware update (link broken, you will need to Google it).

2. Run the `Dell_Kahuna_DEM6.exe` file to a blank flash drive. 

   NOTE: This will reformat the flash drive so make sure there is nothing important on it first.
   {: .notice--success}

3. Go back to the computer with error and boot to a one time boot menu (`F12` on startup). Run through the GUI, it applies the update.

4. Once in Windows, verify the update was applied by running `devmgmt.msc` selecting the Disk Drive and go into its properties. Navigate to the Details tab and look for a Hardware ID ending in "DEM6".