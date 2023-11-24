---
title: General Windows Updates TS
date: 2016-05-26T22:43:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/general-windows-updates-ts/
tags:
  - Windows
tags:
  - Updates
---
<!--more-->

### Description:

Throughout my time in IT, one thing has always remained constant => Windows Updates failing. If the updates would just fail in the OS it wouldn't be so much of a problem, but many times they will prevent you from ever logging in or shutting down. Follow these steps in order to gain access to a system that is failing updates.

UPDATE: Found an interesting article [here](http://pcsupport.about.com/od/system-security/a/prevent-windows-update-problems.htm) that's worth a read. Official Microsoft response [HERE](https://support.microsoft.com/en-us/kb/2509997).

### To Resolve:

1. I primarily deal with servers, so before even doing updates it is HIGHLY recommended to make a backup of the server prior to rebooting to install the updates. If it is a physical host, make sure you have a Windows Restore point; if it is a VM do the same or take a snapshot of the VM prior to reboot to install updates.

2. If the server is stuck on reverting changes after the update failed, try to do the following to get back in:

   - On another computer, Run => `services.msc` => Connect to another computer => Connect to the failed updates computer. Disable the &#8220;Windows Modules Installer&#8221; and &#8220;Windows Management Instrumentation&#8221; services. They will most likely be running and will not stop until reboot.

   - Reboot the server. It should skip anything with updates and allow you to log in => don't!

   - On the other computer you ran `services.msc` on, Run => `\\ServerComputerName\C$`. Once it is connected, go to `C:\Windows\System32\Wbem` and rename the &#8220;repository&#8221; sub folder to &#8220;repository.old&#8221; or something like that.

   - On that same machine, navigate to `C:\Windows\SoftwareDistribution` and delete all sub folders there. You can also rename these as well as Windows will consider them gone. I have heard that only the `C:\Windows\SoftwareDistribution\DatastoreLogs\edb.log` is the only file you need to delete, but I have not confirmed this.

   - Reboot the server one more time after those files are deleted. This should allow you to log in.

3. When this happened to me, I was able to log in, but with the services in step A weren't running => it caused the system to freeze after log in. I couldn't ping or access shares at all so I rebooted. I tried different Safe Mode options, but all of them booted into &#8220;reverting changes..&#8221; even though the updates had been deleted.

4. One of the last options you can do is find the OS CD => boot to that => Choose the option &#8220;Repair Your Computer&#8221; and go back to the backup mentioned in step 1.

5. After you get the system back up to the point prior to installing updates, I would run the "System Update Checker Tool (W7)" (search for it)

6. Run the script found (search "windows update reset - seven forums") to reset Windows Updates.

7. Try running `sfc/scannow`. If that doesn't work, you need to download the Windows 10 iso and use `DISM /Online /Cleanup-Image /RestoreHealth /Source:repairSource\install.wim`

8. You can also try the basic powershell route:

   ```powershell
   Stop-Service -Name 'wuauserv'  
   Remove-Item $env:windir\SoftwareDistribution\ -Force -Recurse  
   Start-Service -Name 'wuauserv'
   ```
