---
title: Fast Windows Updates Install
date: 2016-08-21T17:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/fast-windows-updates-install/
tags:
  - Windows
---
<!--more-->

### Description:

When you install a fresh copy of Windows 7, it can take a really long time to get it fully patched. Follow this guide to speed things up.

### To Resolve:

1. Download the appropriate (x64 or x86) versions of these three updates: KB3020369, KB3172605, and KB3125574. Follow link in references for download.

2. Open an elevated PowerShell prompt and run the following commands, which will allow the next updates to install quickly:

   ```powershell
   net stop wuauserv
   net stop bits
   rename c:\windows\SoftwareDistribution c:\windows\SoftwareDistribution.bak
   net start wuauserv
   net start bits
   ```

3. Double-click and run the KB3020369 update (previously downloaded). Should take less than 2 minutes to run, and will not require a reboot.

4. Now double-click the KB3172605 update you previously downloaded. Follow the prompts. Reboot when it says to. (This step should take about 1 minute).

5. Double-click and run the KB3125574 update (previously downloaded). Should take about 12 minutes to run. It will require a reboot that takes 5 minutes to complete.

6. Begin WU (Windows Update) after completing the above steps. A list of 60+ available updates should be returned within 5 minutes.

7. Finish updating normally rebooting when it says to. You will probably need to reboot and re-check for updates at least two more times.

8. Done. This usually only takes 2 hours instead of however long it usually takes.

9. A powershell way to update fresh copies of Windows: Download from [here](https://github.com/bklockwood/PSWU).

10. Create a folder called `PSWU` on your $PSModulePath

11. Copy these three files to the directory you created:
  
   - PSWU.psd1  
   - PSWU.psm1  
   - Install-AllUpdates.ps1

12. Unblock the files. In PS v3 and above, you can use the Unblock-File cmdlet.

13. If you haven't already, run the command `Set-ExecutionPolicy Unrestricted`.

14. Open Powershell as admin, Run the command: `Import-Module pswu`

15. You can start using PSWU. Examples [here](https://github.com/bklockwood/PSWU/wiki/Using-PSWU).

### References:

["Windows Update Slowness"](http://www.freenode-windows.org/resources/vista-7/windows-update)