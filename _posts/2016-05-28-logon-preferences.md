---
title: Logon Preferences
date: 2016-05-28T06:50:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/logon-preferences/
tags:
  - WindowsServer
tags:
  - Tweaks
  - GroupPolicy
  - Regedit
---
<!--more-->

### Description:

Many times, network administrators will have to modify Windows Logon screens and behaviors. In a domain environment, try to choose `gpedit.msc` (Group Policy Editor) over `secpol.msc` (Local Security Policy) because `gpedit` is a Local Group Policy Editor with the top-level Local Group Policy object open for editing. `Gpedit` works with Ultimate and Professional editions of Windows. Here are some common examples of logon preferences:

### To Not Display Last User Logged On:

1. Search => cmd => right click => &#8220;run as administrator&#8221; .

2. Type `secpol.msc`.

3. Navigate to `Local Policies\Security Options`.

4. Navigate to &#8220;Interactive Logon: Do Not Display Last User Name = Enabled&#8221;.

### To Not Display CTRL+ALT+DEL To Logon:

1. Search => cmd => right click => &#8220;run as administrator&#8221; .

2. Type `secpol.msc`.

3. Navigate to &#8220;Local Policies\Security Options&#8221;.

4. Navigate to &#8220;Interactive Logon: Do Not Require CTRL+ALT+DEL to Logon = Enabled&#8221;.

### To Enable Classic Logon (Doesn't Work for a Domain):

1. Run => `gpedit.msc`

2. Navigate to `Local Computer Policy\Computer Configuration\Administrative Templates\System\Logon`

3. Navigate to &#8220;Always use Classic Logon = Enabled&#8221;.

### To Enable Auto-Login:

1. Run => `regedit`

2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`

3. Double-click the `DefaultUserName` entry, type your user name, and then click OK.

4. Double-click the `DefaultPassword` entry, type your password, and then click OK. NOTE: If the `DefaultPassword` value does not exist, it MUST be added. To add the value, follow these steps:

   - Edit => New => String Value. Type `DefaultPassword`. Set it's value to `your password`.
   - If no `DefaultPassword` string is specified, Windows automatically changes the value of the AutoAdminLogon key from 1 (true) to 0 (false), disabling the AutoAdminLogon feature.

5. Edit => New => String Value. Type `AutoAdminLogon`, set it's value to `1`.

6. Exit `regedit` and reboot your computer.

