---
title: 'W10: This App Cant Open'
date: 2016-11-15T03:21:12+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/w10-this-app-cant-open/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

In Windows 10, you will get a pop up box when you try to open one of the store applications like Edge, Store, ect. It will say &#8220;this app can't open by the built in administrator account&#8221; even if you are a domain user with local admin rights to your machine.

### To Resolve:

1. Run => Regedit => Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\`

   - Look for a key called `FilterAdministratorToken` and delete it. Note that is is set to `0` by default (disabled but we want it &#8220;undefined&#8221;) and controls a Group Policy setting we will see later.
   - While at this location, look for a key called `EnableLUA` and make sure it is set to `1`. Many admins will set this to 0 to disable UAC, but it seems to break the OS => so set to 1.

3. Now run `C:\WINDOWS\System32\UserAccountControlSettings.exe` and slide the bar down to `never notify`

4. Run => `gpedit.msc` => Navigate to: `ComputerConfig\Windows Settings\Security Settings\Local Policies\Security Options`

   - Find `User Account Control: Behavior of the elevation prompt` and set it to `Elevate without prompting`
   - Find `User Account Control: Admin Approval Mode for the Built-In Administrator Account` and set it to `Enabled`

5. Reboot, done.

6. DO NOT DO THIS TO END USER'S MACHINES!! Just do this to your or your home computer. End users need UAC and limited permissions to protect themselves from themselves!