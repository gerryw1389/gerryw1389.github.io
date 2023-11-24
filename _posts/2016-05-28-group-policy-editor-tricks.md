---
title: Group Policy Editor Tricks
date: 2016-05-28T06:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/group-policy-editor-tricks/
tags:
  - Windows
tags:
  - Tweaks
  - 
---
<!--more-->

### Description:

Here is various tricks you can use in the Group Policy Editor in Windows. Note a computer must be on a domain for this to work. See [here](https://technet.microsoft.com/en-us/library/bb742376.aspx) for more information on GPO's. Please also check out [Logon Preferences](https://automationadmin.com/2016/05/logon-preferences/).

### To Deny Local Logins:

1. Navigate to: `Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment`

2. Go to "Deny log on locally" and the add the user to do not want to have local access to the server.

### To Disable Balloon Notifications on the System Tray:

1. Run => `gpedit.msc` => `User Configuration\Administrative Templates\Start Menu and Taskbar`

2. Switch to Enabled. Should be good to go.