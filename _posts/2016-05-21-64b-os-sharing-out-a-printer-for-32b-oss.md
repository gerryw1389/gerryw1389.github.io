---
title: 64B OS Sharing Out A Printer For 32B OSs
date: 2016-05-21T04:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/64b-os-sharing-out-a-printer-for-32b-oss/
categories:
  - Networking
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

Use this to connect to a printer from a 32b workstation to a 64b workstation.


### To Resolve:

1. Find out the 64b (64 bit processor) workstation sharing out the printer. Change the name of the printer to include no spaces.

2. On the other workstations (the 32b workstations), install a LOCAL printer on each workstation to the to lpt3 port.

3. Put the driver for the printer on each of the 32b workstations (usually through a mapped drive from the server) and download and install on each workstation. Use that driver to install the local printer.

4. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `net use lpt3 \\ComputerNameSharingOutPrinter\PrinterName`

5. Change the name of the newly connected printer to include the words "on (ComputerNameThatPrinterIsSharedFrom)"

6. Printer properties - comments - "using lpt3 on (ComputerNameThatPrinterIsSharedFrom)"

7. Print a test page and verifies that it works.