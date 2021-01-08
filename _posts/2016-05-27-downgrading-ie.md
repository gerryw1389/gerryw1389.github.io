---
title: Downgrading IE
date: 2016-05-27T22:12:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/downgrading-ie/
categories:
  - Windows
---
<!--more-->

### Description:

Over and over again, browsers will update and specific sites will not work with the newest versions. It's highly recommended you wait for a new release to be out a while so that internet sites can have times to update their compatibility to the newest version of your internet browser.

### To Resolve:

1. Run => appwiz.cpl => find &#8220;View Installed Updates&#8221; => Scroll down to the Microsoft Windows section and uninstall the "Windows Internet Explorer X" entry.

2. Many times that section will be missing, follow the steps in DCOM Settings For Missing Windows Update Settings to restore it.

3. Once rebooted, the above steps again and you will be on the last browser you had installed prior to the update.

4. Run MS Update (wuapp) and &#8220;hide&#8221; the update by right click => hide update.

### The CMD Method (Preferred):

1. Open CMD as Administrator and type:

2. Copy and paste this into the command prompt:

   ```console
   FORFILES /P %WINDIR%\servicing\Packages /M Microsoft-Windows-InternetExplorer-*11.*.mum /c "cmd /c echo Uninstalling package @fname && start /w pkgmgr /up:@fname /quiet /norestart
   ```

   - NOTE: To change IE from any other version number just replace the &#8220;11&#8221; in the command prompt with the current version number. This has worked fine on 11 and 10 so far.

3. Click &#8220;OK&#8221; to all the &#8220;Access Denied&#8221; messages.

4. Reboot.