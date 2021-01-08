---
title: OneDrive Icons Always Syncing
date: 2016-05-26T22:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/onedrive-icons-always-syncing/
categories:
  - Windows
---
<!--more-->

### Description:

OneDrive icons will be stuck in a continuous upload fashion, even though everything has been synced. This is usually caused by documents being uploaded on exit in Office applications.

### To Resolve:

1. Close the OneDrive system tray icon on your taskbar.

2. Open Task Manager and kill any of the following:

   ```escape
   groove.exe  
   msosync.exe  
   msouc.exe  
   winword.exe  
   excel.exe  
   powerpnt.exe
   ```

3. Run => `localappdata%\Microsoft\Office\15.0`

4. Delete the `OfficeFileCache` folder completely.

5. Start OneDrive back up and go to Settings => Uncheck 'Use office to work on files..'

   - I use OneDrive as a backup solution with Office365 and never have anyone but me using my documents so I don't use this option. Obviously if you want that ability, you can disregard this fix.