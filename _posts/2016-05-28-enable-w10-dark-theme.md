---
title: Enable W10 Dark Theme
date: 2016-05-28T07:07:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/enable-w10-dark-theme/
categories:
  - Windows
tags:
  - Regedit
  - Tweaks
---
<!--more-->

### Description:

Windows 10 has a hidden dark theme that you can enable via registry. Follow these steps to resolve:

  <img class="alignnone size-full wp-image-736" src="https://automationadmin.com/assets/images/uploads/2016/09/w10-dark-theme.png" alt="w10-dark-theme" width="487" height="341" srcset="https://automationadmin.com/assets/images/uploads/2016/09/w10-dark-theme.png 487w, https://automationadmin.com/assets/images/uploads/2016/09/w10-dark-theme-300x210.png 300w" sizes="(max-width: 487px) 100vw, 487px" />


### To Resolve:

1. Run => regedit => Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes`

   - Create key: `Personalize`
   - Create DWORD under it called `AppsUseLightTheme` and set its value to `0`
   - Navigate to: `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize` and create the same DWORD and value.

4. Either logout and log back in or just do a reboot for it to take effect.


### References:

["Enable Windows 10 Dark Theme using Registry Tweak"](http://www.thewindowsclub.com/enable-windows-10-dark-theme)