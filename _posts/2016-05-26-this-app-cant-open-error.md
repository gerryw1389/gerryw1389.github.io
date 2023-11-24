---
title: 'This App Cant Open Error'
date: 2016-05-26T22:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/this-app-cant-open-error/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

On W8+, you will get a pop saying that a certain application cannot be open using the built-in admin account.

  <img class="alignnone size-full wp-image-715" src="https://automationadmin.com/assets/images/uploads/2016/09/this-app-cant-open.png" alt="this-app-cant-open" width="583" height="127" srcset="https://automationadmin.com/assets/images/uploads/2016/09/this-app-cant-open.png 583w, https://automationadmin.com/assets/images/uploads/2016/09/this-app-cant-open-300x65.png 300w" sizes="(max-width: 583px) 100vw, 583px" />


### To Resolve:

1. Run => `secpol.msc`

2. Navigate to: `LocalPolicies\SecurityOptions\` and look for "User Access Control: Admin Approval Mode For built in….."

3. Change it to enabled.

4. Run => `regedit`. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\UIPI`

5. Change the key `Default` to the value of `0x00000001(1)`

6. Reboot


### References

["Windows 8 Fix : This app can't open for Built-in Administrator account"](http://www.bleepingtech.com/windows-8-fix-this-app-cant-open-for-built-in-administrator-account/)