---
title: SOHO Setups
date: 2016-05-21T23:08:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/soho-setups/
tags:
  - SysAdmin
tags:
  - Setup
---
<!--more-->

### Description:

I use the following guide when doing SOHO (small office/home office) set ups.

### To Resolve:

1. Set all computers on the same workgroup. You can go into Network Sharing settings and make sure file sharing is enabled, but it is by default

2. Change the default password on the router and all WAPs.

3. Create a local admin account on all computers. Many admins recommend disabling the built-in administrator account and creating your own. It's advized to have a different password for each workstation, but most people don't follow through with this. Look into Microsoft LAPS for the best solution.

4. Get Antivirus/ Firewalls enabled on all computers. If the client will have specific applications running, make sure to add them in the exceptions. A couple notes on this:

   - Defender is okay to use in a business environment on anything [less than 10 PC's](http://answers.microsoft.com/en-us/protect/forum/all/what-are-the-licensing-terms-for-windows-defender/16e7844f-1893-42e8-b21f-1391fb42024c)

   - Any paid known Antivirus is fine, just make sure to read the EULA's because some are per user instead of per machine. Stay away from free ones if you are in a business environment.

5. I almost always setup one computer to be a &#8220;server&#8221;. This computer will be the center computer in the office and can share a drive out for others to connect to. This serve's multiple purposes, but mainly allows for a free online backup for SOHO's, here's how:

   - Download an online sync client to your computer with a free account (or paid obviously) GoogleDrive, OneDrive, DropBox, etc. When installing, choose a path to a folder on the root of the `C:` instead of the default (they usually try and install in `%userprofile%\MyDocuments`).

   - Create a folder inside of the root of the sync service and call it &#8220;Data&#8221; and share it out. Right click => Properties => Sharing => Add: Everyone => give them read/write permissions.

   - On all other computers, Run => `\\ServerComputerName` and then right click the share and &#8220;Map Network Drive&#8221;. From the places I have seen, G: seems to be a common drive letter, but any will do.

6. Install any custom applications/hardware. This is where I will install printers, MS Office, or any application software.

### References:

["How to…Set Up a SOHO Network"](http://certmag.com/how-to-set-up-a-soho-network)