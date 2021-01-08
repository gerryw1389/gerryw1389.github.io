---
title: W10 Upgrade Block From W7
date: 2016-05-28T07:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/w10-upgrade-block-from-w7/
categories:
  - Windows
tags:
  - Tweaks
  - GroupPolicy
  - Regedit
---
<!--more-->

### Description:

Windows 10 is the newest client OS released by Microsoft to date (2015), and to get most users on the same page, they made the upgrade from W7, W8, and W8.1 free for home users. While this sounds enticing, many including myself do not look forward to such a change. Follow these steps if you decide not to upgrade:

### To Resolve:

1. Before making any changes => create a system restore point. There is a GUI tool to do the steps below, if you so wish it can be downloaded [here](http://ultimateoutsider.com/downloads/). It is called "GWX Control Panel".

2. Run => `cleanmgr.msc` => Remove all installation/ temporary files. If the download has already started, this will be quite large.

3. Run => `appwiz.cpl` => Installed Updates => Remove the following:

   - Uninstall KB3035583
   - Uninstall KB2952664 (usually W7)
   - Uninstall KB2976978 (usually W8/W8.1)

4. Reboot the machine.

5. Check for updates => Hide all of those that return so they don't install again. If the "Windows 10 Upgrade" update shows up, just Right Click => Hide it as well. Lastly, you might want to change your update settings to "Download but not install". This should be good, but if you want to be real cautious, continue..

6. Run => `regedit` => Navigate To: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\WindowsUpdate\OSUpgrade` and find the key `AllowOSUpgrade`. Set it from `1` to `0`. 

7. I have also read that you can go to `HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate` and create a DWORD key called `DisableOSUpgrade` and set it to a value of `1`. I didn't find that path in my system, so I just did the first key. Reboot the computer when done.

8. Reg file (copy and paste to notepad and save as whatever.reg => double click to launch) :  

   ```escape
   Windows Registry Editor Version 5.00  
   ; https://support.microsoft.com/en-us/kb/3080351

   [HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate]  
   "DisableOSUpgrade"=dword:00000001

   [HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Gwx]  
   "DisableGwx"=dword:00000001
   ```

9. Now Run => `control folders` => "View" tab => Show hidden files, and uncheck the three checkboxes below to show everything. Navigate in your file system to: `C:\$windows.~BT`. Delete it. Another option I have heard but not tested is to delete the folder and then recreate it yourself. Then if Windows does somehow want to upgrade, it will not be able to since the folder is already there and will block it from downloading, just make sure you have it set to hidden.

10. Reboot your computer. Run `cleanmgr.msc` again just to be sure.

11. Check for updates again. If it says something about the upgrade, just ignore it and install updates since you have the regkey set to `0` the upgrade will not install.

12. There is a [GPO](https://support.microsoft.com/en-us/kb/3080351) to do this as well.
