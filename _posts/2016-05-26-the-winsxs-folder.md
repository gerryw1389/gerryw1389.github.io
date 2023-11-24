---
title: The WinSXS Folder
date: 2016-05-26T22:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/the-winsxs-folder/
tags:
  - Windows
---
<!--more-->

### Description:

In Windows 7 and Windows 8, there is a new folder under `C:\Windows` called WinSxS, which basically stores DLL and component files. It also stores older versions of all dll and component files and can grow to be quite large. In addition to that, a lot of space is taken up by the backup folder, which gets really big after you install a Service Pack, like SP 1 for Windows 7.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `dism /online /cleanup-image /spsuperseded /hidesp`

2. Another option is: Run => `cleanmgr.exe` => Select the &#8220;Service Pack Backup Files&#8221; option.

3. In Windows 8, you can remove specific features by running: `DISM.exe /Online /English /Get-Features /Format:Table`

4. This will show a list of all features, then you just pick which want you want to remove and run: `DISM.exe /Online /Disable-Feature /Featurename: /Remove`