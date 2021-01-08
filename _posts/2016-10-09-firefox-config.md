---
title: Firefox Config
date: 2016-10-09T15:30:26+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/firefox-config/
categories:
  - LocalSoftware
tags:
  - Tweaks
  - PersonalConfig
---
<!--more-->

### Description:

In my quest to move from closed source to open source, I decided to move my web browsing from Chrome to Firefox. Here are the steps I used:

### To Resolve:

1. After installation, first thing is `Hamburger menu (top right) - Customize - Themes - Dark`

2. Download, install, configure Extensions (as of 2019-06):
  - uBlock Origin
  - Bitwarden - Free Password Manager
  - Black New Tab
  - Close Right Tabs Button
  - Download History Cleaner (Eraser)
  - Greasemonkey
  - HTTPS Everywhere
  - Notifier for Gmail™
  - Print to PDF
  - Stylus

3. Now we configure Firefox itself, open a new tab and type `about:config` and select `yes, I agree`

   - In the Search field box at the top, type `browser.tabs.warn` and set the first 3 to false (warnOnClose, warnOnCloseOtherTabs, warnOnOpen)
   - I think these sync now by the following settings, but verify:
   - `services.sync.prefs.sync.browser.tabs.warnOnClose = True`
   - `services.sync.prefs.sync.browser.tabs.warnOnOpen = True`

4. Customize:

   - Set the address bar from Left to right as follows:
  
   - Back, forward, reload, home, => Clear tabs Right (extension) => Address bar => Downloads (but check the auto-hide option), uBlock, Bitwarden, Notifier for Gmail
  
   - All other extensions go to Overflow menu 

5. Finally, Add `Download history cleaner` as the very last item on the overflow menu. Click that button every time I download something to hide the download icon on main taskbar.