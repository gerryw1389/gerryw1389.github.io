---
title: Uninstall Software In Safe Mode
date: 2018-09-23T15:48:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/09/uninstall-software-in-safe-mode/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Follow these steps to uninstall software in safe mode. I'm not sure what all software you can uninstall, but the way I found this is we had a server that would bluescreen after a user logs in. The way we fixed was:

### To Resolve:

1. Reboot the server into Safe Mode and run:

   ```powershell
   bcdedit /set {bootmgr} displaybootmenu yes
   ```

2. On reboot, we can now press `F8` to get into Safe Mode.

3. Check event viewer for critical events and see if they correspond to any installed software, in this case => Anywhere USB

4. Now edit the registry allow `msiinstaller` service to run in safe mode:

5. Regedit  

   ```escape
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal\  
   Create key = MSIServer

   Create a String key (REG_SZ) = Service  
   Uninstall Software
   ```

5. Reboot into safe mode once again and uninstall the software.

6. Reboot into normal mode and verify the server is no long blue screening.