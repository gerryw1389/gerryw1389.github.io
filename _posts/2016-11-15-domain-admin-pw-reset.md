---
title: Domain Admin PW Reset
date: 2016-11-15T02:58:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/domain-admin-pw-reset/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

This hasn't ever happened to me, but if you cannot remember the domain admin's password, follow these steps to reset it.

### To Resolve:

1. Boot from install media and when it gets to the Windows install, select Next => Repair your computer => Troubleshoot => Command Prompt

2. Now type:

   ```escape
   cd c:\windows\system32 # if Windows isn't on C drive, then type "wmic logicaldisk get caption,description,filesystem" to get the drive letter  
   ren Utilman.exe Utilman.exe.old  
   copy cmd.exe Utilman.exe
   ```

3. Reboot the server. Don't boot to CD, let it boot from the hard drive. At the login screen, use the shortcut "Windows Key + U" to bring up admin cmd.

4. Now just type "net user administrator Password123" or whatever you want your password to be. Login and shut down the server. Boot from the install media again and get to the command prompt following step 1.

5. Now type:

   ```escape
   cd c:\windows\system32  
   del Utilman.exe  
   ren Utilman.exe.old Utilman.exe
   ```

6. Exit and reboot the server. Take out the boot disk and boot normally. Done.

7. You can do all this from within Windows by taking all the permissions of utilman.exe, but I prefer the above method.


### References:

["Reset Windows Server 2012 Domain Administrator Password"](http://blog.watchpointdata.com/how-to-reset-forgotten-windows-server-2012-domain-administrator-password)  