---
title: Move Spiceworks From One Computer To Another
date: 2016-05-23T12:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/move-spiceworks-from-one-computer-to-another/
tags:
  - WindowsServer
tags:
  - Migration
---
<!--more-->

### Description:

We recently started using Spiceworks for the Inventory feature at our office and I wanted to move it from my computer to a VM, so I followed these steps:

### To Resolve:

1. Within Spiceworks, create a backup of your database.

2. Make sure to exit out of Spiceworks on your machine. Now install it on the new machine.

3. On the new machine, go to the install directory and delete the &#8220;data&#8221; and &#8220;db&#8221; folders.

4. Transfer your backup to the new machine. Extract the folders into the Spiceworks directory. Done!

NOTE: I also had an issue where importing a CSV caused Spiceworks to error out on my Inventory page after the import (I think due to incorrect column names). I had just done a backup prior to attempting the import. Since it crashed my Spiceworks installation, I just did steps 3 and 4 over and it reverted back cleanly. Lesson: Do backups often as they can be restore points for your installation.

### References:

["How to: Move Your Spiceworks Installation"](https://community.spiceworks.com/how_to/295-move-your-spiceworks-installation)