---
title: How To Replace System Files
date: 2016-05-30T05:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/how-to-replace-system-files/
tags:
  - Windows
tags:
  - Scripting-CMD
---
<!--more-->

### Description:

If you ever need to replace system files in Windows, follow these steps.

### To Resolve:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `takeown /f C:\Windows\System32\filename.dll`

2. Now replace the file with a copy you got.

3. Now type `cacls C:\Windows\System32\filename.dll /G (UserProfileName):F`. That command gives you permission to access the file. Press `Y` to take ownership of the file.

4. In a script you would use the following to take control of a file and delete it:

   ```powershell
   takeown /f "%windir%\System32\filename.extension" /r /d y
   icacls "%windir%\System32\filename.extension" /grant administrators:F /t
   rd /s /q "%windir%\System32\filename.extension"
   ```