---
title: FBI Virus Removal
date: 2016-05-28T07:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/fbi-virus-removal/
tags:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

The &#8220;FBI Virus&#8221; is a ransomware that locks down a user's profile. There are different ways to remove it, but try these steps.

### To Resolve:

1. Try and get on another user account if you are locked out of yours. Try the local administrator account if you have one.

2. If that doesn't work, try your account in safe mode.

3. Once inside of a user profile, Run => `%userprofile%\appdata\local\temp` => remove `rool0\_pk.exe` => remove `V.class` => the virus can have names other than `rool0\_pk.exe` but it should look like it doesn't belong and should have a create date/time the same as a `.class` file if you sort by file mod/create time you'll find it.

4. Run => `%appdata%\microsoft\windows\start menu\programs\startup` => remove `ctfmon (ctfmon.lnk)` this is what's calling the virus on startup => also check `HKLM:\Software\Microsoft\Windows\CurrentVersion\Run` and make sure there's nothing obvious there.

5. If those still haven't removed it, start running all the virus scans you have inside another profile.

6. Re-image your computer if infection still persists.