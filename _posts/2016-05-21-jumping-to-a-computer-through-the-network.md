---
title: Jumping To A Computer Through The Network
date: 2016-05-21T22:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/jumping-to-a-computer-through-the-network/
tags:
  - Networking
  - SysAdmin
tags:
  - Regedit
---
<!--more-->

### Description:

Many times when you are having issues getting to a computer through the internet, you can get to them through the local network instead. The best way to do this is through RDP or Remote Desktop protocol.

### To Resolve:

1. Get on any computer on the network that has internet. Run [Netscan](https://www.softperfect.com/products/networkscanner/) and find the computer you want to connect to. Right click on the computer name in the list and select to open &#8220;Computer Management&#8221; on that computer.

   - ![jumping-to-a-computer-through-the-network](https://automationadmin.com/assets/images/uploads/2016/09/jumping-to-a-computer-through-the-network.png){:class="img-responsive"}

2. Once inside that computer's Computer Management console, navigate to the Services tab. Enable the Remote Registry Service.

3. Then on the computer you are on, open regedit (Run => `regedit`).

4. On the File menu, click Connect Network Registry.

5. In the Select Computer dialog box, type the computer name and then click Check Names.

6. If a Enter Network Password box appears, enter the password for the computer, make sure to enter an administrator account's password.

7. In the computer node that appears in the Registry Editor, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server`.

8. In the console tree, click Terminal Server and then, in the details pane, double-click fDenyTSConnections.

9. In the Edit DWORD Value box, in Value data, type `0`, and then click OK.

10. Exit regedit and wait about 5 min and try to RDP to that computer.

11. RDP or Remote Desktop Protocol:

   - Starting RDP Sessions: RDP is ran by running `mstsc` to whichever hostname or IP on a network you want to remote into. The device your remoting in to has to have Remote Desktop enabled for it to work. This is under they System Information (`sysdm.cpl`) => Remote tab. I usually select the middle radio button.

   - Ending RDP Sessions: It is highly important that when you RDP to a computer, you must logoff to end the session, do not hit the X on the top right corner of the session. This can lead to disconnected sessions and errors when trying to RDP to that computer later on.


