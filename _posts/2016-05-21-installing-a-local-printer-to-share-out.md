---
title: Installing A Local Printer To Share Out
date: 2016-05-21T04:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/installing-a-local-printer-to-share-out/
categories:
  - Networking
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

To install a local printer to a workstation to be shared out on the network. This is not the preferred method of installing printers as they become dependent on the workstation that is sharing them out, you should instead look to put a printer on the network if it needs to be shared.

### To Resolve:

1. Install the printer locally according to manufacturers driver for the current OS.

2. Make sure to select the option to `Share` the printer during install. When choosing a printer name, try and use one without spaces in it.

3. To Add the Printer From Another Workstation:

   - Remote in to another workstation to see if you can see the shared printer's computer by searching the computer name of the computer sharing the printer.

   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `\\(computername of computer sharing the printer)` and and it will display what that machine is sharing on the network. If you see the printer, just right click and select `connect`. This will install the printer locally.
   
   - If you cannot connect to the computer sharing the printer, you have a networking issue that needs to be addressed first.