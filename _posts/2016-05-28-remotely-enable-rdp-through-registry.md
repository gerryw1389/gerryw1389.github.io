---
title: Remotely Enable RDP Through Registry
date: 2016-05-28T06:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/remotely-enable-rdp-through-registry/
tags:
  - SysAdmin
tags:
  - Regedit
---
<!--more-->

### Description:

This is a handy trick to enable RDP or Remote Desktop Protocol for a remote computer so that you can jump over to it through RDP (Run => `mstsc`). Note that this uses the RPC protocol and is a sub step from the article [Jumping To A Computer Through The Network](https://automationadmin.com/2016/05/jumping-to-a-computer-through-the-network/).

### To Resolve:

1. Run => `regedit`.

2. On the File menu, click Connect Network Registry.

3. In the Select Computer dialog box, type the computer name you want to connect to and then click Check Names.

4. In the Enter Network Password dialog box, provide Administrator credentials for the computer, and then click OK. After the computer name resolves, click OK.

5. In the computer node that appears in the Registry Editor, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server`.

6. In the console tree, click Terminal Server and then, in the details pane, double-click fDenyTSConnections.

7. In the Edit DWORD Value box, in Value data, type 0, and then click OK.

8. Give it five minutes and then try to RDP to the remote computer by typing on your computer: Run => `mstsc`. You may need to reboot the remote computer for the change to take effect. To do this, from your computer: [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `shutdown -m \\RemoteComputerName -r`


