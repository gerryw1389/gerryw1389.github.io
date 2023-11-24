---
title: Two Ways To Add A Printer In Windows
date: 2016-05-28T06:36:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/two-ways-to-add-a-printer-in-windows/
tags:
  - Hardware
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

When adding a printer in Windows, there is two different paths you can go:

### To Resolve:

1. (Recommended) Manufacturers Website. Go to the manufacturers website and navigate to your model of printer. Then download the full suite or at least the drivers that correspond to your operating system.

2. Setup your printer and plug it in on the network. Assign it an available static IP (preferably outside your router's DHCP range). Test by pinging the printer in Windows. Run => cmd => ping (printerIPAddress).

3. After running the setup, it will ask where the printer is. You simply point it to the IP address of the printer and the setup will install your printer.

4. Option 2: Install via Add a printer wizard. Run => control printers => Add a printer => Local printer => Add new port:TCP/IP => (IP Address of the printer) => then comes the driver screen. Here you have to navigate down a list and select a driver for your printer. If it is not on the list you have two options:

   - Run Windows Update from that screen (takes like 5 minutes or more usually)
   - Go to the manufacturers website and download the driver. If there is no setup (exe), you will (from the add printer page) select the option that says &#8220;Let me choose which drivers to use&#8221; and then navigate to the printer driver directory (which you downloaded from the manufacturers website). Here you just select the .inf file which holds the important driver information for Windows to load.

5. After the driver is installed, you are good to go.