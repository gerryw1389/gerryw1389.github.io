---
title: W10 Failed To Boot Due To Updates
date: 2017-10-28T06:05:10+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/w10-failed-to-boot-due-to-updates/
categories:
  - Windows
tags:
  - Pre-Boot
---
<!--more-->

### Description:

Reboot the computer and select the boot once option (usually `F12` on Dell systems) and get to the Safe Mode with Command Prompt option. If you can't get there, just use a Windows install disc and during the setup choose the option to repair a current installation. We had to do this for a couple W10 machines after a recent update.

### To Resolve:

1. After the Command Prompt launches, run the following to load the software registry hive:

   ```escape
   reg load hklm\temp <drive letter for windows directory>\windows\system32\config\software
   Example: reg load hklm\temp c:\windows\system32\config\software
   ```

2. Run the following command to delete the SessionsPending registry key. If the registry value does not exist, proceed to the next step.

   ```escape
   reg delete "HKLM\temp\Microsoft\Windows\CurrentVersion\Component Based Servicing\SessionsPending" /v Exclusive
   ```

3. Run the following to unload the registry:

   ```escape
   reg unload HKLM\temp
   ```

4. Run the following command, which will list all pending updates:

   ```escape
   dism.exe /image:<drive letter for windows directory> /Get-Packages
   Example: dism.exe /image:c:\ /Get-Packages
   ```

5. Run the following command for each packages where "State = Install Pending":

   ```escape
   dism.exe /image:<drive letter for windows directory> /remove-package /packagename:<package name>
   Example: dism.exe /image:c:\ /remove-package /packagename:Package_for_RollupFix_Wrapper~31bf3856ad365e35~amd64~~15063.674.1.8
   dism.exe /image:c:\ /remove-package /packagename:Package_for_RollupFix~31bf3856ad365e35~amd64~~15063.674.1.8
   ```