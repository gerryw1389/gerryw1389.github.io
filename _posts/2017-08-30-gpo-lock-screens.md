---
title: 'GPO: Lock Screens'
date: 2017-08-30T22:04:13+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/gpo-lock-screens/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

We wanted to find a way to lock the screen's after 10 minutes of inactivity. This is how to do it:  
NOTE: If You Have All W8/Server2012+ Clients:

`Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Interactive logon`: Machine inactivity limit

Windows notices inactivity of a logon session, and if the amount of inactive time exceeds the inactivity limit, then the screen saver will run, locking the session.

### To Resolve:

1. Create A GPO Under The OU With All Your Users And Go To:

   - `User Configuration\Administrative templates\Control Panel\Personalize`:
   - Enable Screensaver = Enabled
   - Password Protect The Screen Saver = Enabled
   - Screen Saver Timeout = Enabled
   - Force Specific Screen Saver = Enabled
     - Options: type `%windir%\system32\rundll32.exe user32.dll,LockWorkStation`
     - So it will lock the desktop once it reach the specified timeout.