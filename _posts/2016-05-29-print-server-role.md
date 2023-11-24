---
title: Print Server Role
date: 2016-05-29T04:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/print-server-role/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
---
<!--more-->

### Description:

Print Servers provide a central point of management for printers on the network. Although printers can be assigned by users by GPO, what I have setup here is a &#8220;dummy print server&#8221;. Follow these steps to set it up:

NOTE: These are the steps I used to create a Windows Server 2012 print server so we could decommission a Windows 2000 server.

### To Resolve:

1. Take note of all printers (make, model, IP) on the old server and install them on the new.

2. I created a shared drivers folder on the root of the C: on the new server and put all the driver there. Then for the once that needed extracting, and to seperate them, I created different folders on the root of the C: for their drivers. Do 64 and 32 bit drivers for each printer.

3. Next, you just share the printers out.

4. After they are shared, adjust the permissions to make sure certain users can print. We set them to &#8220;Everyone => Print Only&#8221; access and &#8220;Administrators => Full Control&#8221;.

5. Lastly, on the clients that want to connect to the printers you just `\\PrintServerName` and right click => Connect to the printer you need to install.

### Installing The Role:

1. On the print server, add the role via server manager.

2. This will create the Print Management icon in your administrative tools.

3. For more information on what to do next, read the following article: [Print Management Step-by-Step Guide](https://technet.microsoft.com/en-us/library/Cc753109(v=WS.10).aspx)  

