---
title: 'MS Office: Startup Issues'
date: 2016-05-23T19:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-office-startup-issues/
categories:
  - LocalSoftware
tags:
  - MSOffice
  - Regedit
---
<!--more-->

### Description:

If MS Word or Excel is taking a long time to open or a long time to close, follow these steps related to &#8220;Add-ins&#8221; that are set to run on startup.

### To Resolve:

1. Navigate to the &#8220;normal.dotm&#8221; file and delete it. This file will re-populate when you start MS Word again.

   - For Windows XP: Run => %USERPROFILE%\Application Data\Microsoft\Templates\

   - For Windows 7: Run => %appdata%\Microsoft\Templates

2. If it is still slow delete the following registry values.

   - For Word 2013: HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Word\Data

   - For Word 2010: HKEY_CURRENT_USER\Software\Microsoft\Office\14.0\Word\Data

   - For Word 2007: HKEY_CURRENT_USER\Software\Microsoft\Office\12.0\Word\Data

3. If neither of those work, see if you have more than one instance open at once. I have seen where if you have two spreadsheets open in Excel, it will take forever to open a new (but totally unrelated) spreadsheet. To fix, you just click save on the current worksheet and the new one will open right up.

