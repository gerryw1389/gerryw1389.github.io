---
title: 'W10: Main Way To Remove Apps'
date: 2018-08-05T07:26:17+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/w10-main-way-to-remove-apps/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

So I Have my [Set-Template](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-Template.ps1) script that I use to provision OEM machines to a default &#8220;standard&#8221;. Here is a way to run it once on the default profile and not have to worry about new users getting those pesky cloud apps.

### To Resolve:

1. Run my script linked in description.

2. Then just run:

   ```powershell
   reg load HKU\Default_User C:\Users\Default\NTUSER.DAT
   Set-ItemProperty -Path Registry::HKU\Default_User\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager -Name SystemPaneSuggestionsEnabled -Value 0
   Set-ItemProperty -Path Registry::HKU\Default_User\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager -Name PreInstalledAppsEnabled -Value 0
   Set-ItemProperty -Path Registry::HKU\Default_User\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager -Name OemPreInstalledAppsEnabled -Value 0
   reg unload HKU\Default_User
   ```

3. I have not tested this but the idea is that my template will remove all apps from the current user and this PS block will stop Windows from loading the crap apps when a new user logs in. This should work in Audit mode during OOBE.