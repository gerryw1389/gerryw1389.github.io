---
title: Printing Over Terminal Services
date: 2016-05-21T04:46:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/printing-over-terminal-services/
categories:
  - Networking
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

If you have a client VPN and they want to be able to print to a printer at their location FROM the other end of the VPN, follow this guide. Also see [Adding A Printer For A Terminal Server](https://automationadmin.com/2016/05/add-a-printer-for-a-terminal-server/) if this doesn't help.


### To Resolve:

1. On the local machine, make sure the printer is installed correctly and share it out with no spaces in the share name. Test by printing a test page locally.

2. Connect to the VPN through `ncpa.cpl`. If it's not setup, go ahead and set that up now => see &#8220;Setting Up A VPN&#8221; for more information.

3. Test the connection by pinging the destination computer's IP address. 

4. If it's successful, on the local machine run an `ipconfig /all`. Take note of the PPP IP Address. (In this case 172.10.10.23)

   <img class="alignnone size-full wp-image-688" src="https://automationadmin.com/assets/images/uploads/2016/09/printing-over-terminal-services.png" alt="printing-over-terminal-services" width="661" height="758" srcset="https://automationadmin.com/assets/images/uploads/2016/09/printing-over-terminal-services.png 661w, https://automationadmin.com/assets/images/uploads/2016/09/printing-over-terminal-services-262x300.png 262w" sizes="(max-width: 661px) 100vw, 661px" />


5. On the remote computer, run => `\\IPAddressFromPreviousStep`. This will bring up an Explorer window that shows you everything being shared from the local computer.

6. Find your printer, right click => connect. Install the printer through the steps.