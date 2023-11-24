---
title: Changing Drives On A Dell Server
date: 2016-05-21T04:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/changing-drives-on-a-dell-server/
tags:
  - Hardware
---
<!--more-->

### Description:

You will have a failed drive on the server. System slowness and lots of &#8220;DISK- warning&#8221; errors in the Windows Event Viewer. If the server has a Hardware monitoring program, you will see an &#8220;X&#8221; on the physical drive itself.

### To Resolve:

1. Check the event viewer to see which drive failed. They will be labeled according to disk management. Run `eventvwr.msc` and `diskmgmt.msc` to check.

2. If on a server, open up the hardware monitoring software and navigate to the failed drive, it should have an &#8220;X&#8221; on it or something indicating it has failed. Change the drive to &#8220;offline&#8221;, if it's not an option in the GUI, then right click and make the selection.

3. Remove the failed drive and clear the logs in the program. To clear the logs: Export to a destination AND THEN select the &#8220;clear logs&#8221; option.

4. Restart all services related to the hardware monitoring program. For Dell Open Manage, there will four services that start with &#8220;DSM&#8221;.

5. Install the new drive by plugging it in, it should rebuild the RAID Array automatically. If not, some hardware monitoring software suites give you the option after install to &#8220;assign global hs&#8221; or something of that nature, you may have to power down the server and configure the RAID through the BIOS.

6. We had one of these happen the other day, this is the steps we did => Open up Dell OM:  
   - Blink disk => take it out => insert new disk  
   - Back in Dell OM:  
   - Go to storage => Information/Configuration tab => Controller Tasks => Foreign Config Tasks => Clear  
   - It will then say &#8220;Ready&#8221; when the other disk just say &#8220;Online&#8221;  
   - Then go to the physical disks tab => Tasks => Assign Global HotSpare => It will then say rebuilding and eventually Online once it's complete.