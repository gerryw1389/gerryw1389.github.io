---
title: To Force Delete A Folder/File
date: 2016-10-20T20:22:55+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/to-force-delete-a-folderfile/
categories:
  - Windows
  - Security
tags:
  - Backup
  - Scripting-CMD
---
<!--more-->

### Description:

I don't know why this keeps coming up, but I have the hardest time deleting files/folders sometimes despite using Unlocker and FileAssasin. Follow these steps to work on issues like these.

### To Resolve:

1. First navigate to the directory in Windows Explorer. Hold down CTRL + Right click => Open Command Window here. You may have to close that CMD prompt and open CMD as administrator.

2. Type:

   ```powershell
   rmdir (foldername) /s 
   # Gives error

   del *.* 
   # Gives error

   takeown /f (foldername) /r /d y 
   # Gives error
   ```

3. Since those don't work, lets try doing it running as NTAUTHORITY\SYSTEM: type

   ```powershell
   # NOTE: This assumes you have PSTools installed and added to your PATH variable.
   psexec -sid cmd.exe

   whoami 
   # Should return system
   # Try step 2 again, still no go
   ```

   - You used to be able to run:

   ```powershell
   at 11:10 /interactive cmd.exe
   # Where 11:10 is the current time (HH:MM 24 hour) plus 1 minute.
   # The /interactive switch has been depreciated though.
   ```


4. Right click each file with the Unlocker windows explorer extension => Delete on next reboot. This works!

5. If you have a `path too long` error, just type:

   ```powershell
   robocopy c:\empty C:\deleteme /purge
   # NOTE: This will delete that folder (c:\deleteme) and all subfolders for you!
   ```