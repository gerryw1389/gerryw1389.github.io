---
title: W10 Post-Installation Tasks
date: 2016-05-28T07:13:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/w10-post-installation-tasks/
tags:
  - Windows
tags:
  - Tweaks
---
<!--more-->

### Description:

Follow these steps after you install Windows 10 to tweak it as needed. Note that these are not mandatory steps but should be followed by those who are specific about their privacy rights.

### To Resolve:

1. To do a "clean install", you should follow these steps:

   - Upgrade to Win10 from 7/8.x

   - Use a third party tool to recover product key

   - Reinstall fresh using said key

2. First off, use a local account => don't use a Microsoft account with the OS. If you're using Microsoft account, it's preferred to convert it to local account by heading to Settings => Accounts => Your accounts and clicking on Sign in with a local account instead and following the guide.

3. Go to Settings => Privacy, and disable everything, unless there are some things you really need (like allowing websites access to your language list). At least pay attention to "General", "Speech, inking & typing" and "Location" pages.

4. While within the "Privacy" page, go to "Feedback & diagnostics", select Never in the first box, and Basic in the second box.

5. Head to Settings => Update & Security => Windows Update => Advanced Options => Choose how updates are delivered, and turn the first switch off.

6. While within the Update & Security page, go to "Windows Defender" and turn off "Cloud based Protection" and "Sample submission".

7. Head to Settings => Network & Internet => Wi-Fi => Manage Wi-Fi settings. Turn off both switches to disable Wi-Fi Sense.

8. Disable Cortana and web search in "Search bar" by clicking on it, going to Settings by pressing on a cog icon, and turning off both switches.

9. To disable telemetry: Follow [this](http://techne.alaya.net/?p=12499) link. DO THE STEPS MENTIONED!!

10. It will not be superfluous to set up Edge browser. Open it, then go to More Actions => Settings => View advanced settings. Enable Do Not Track requests and disable search suggestions, page prediction and SmartScreen filter. Make sure that Cortana is switched off too.

11. Reddit suggestions:

   - Add [this](http://winhelp2002.mvps.org/hosts.txt) list to your [host file](https://automationadmin.com/2016/05/modifying-the-windows-host-file/) (located in `C:\Windows\System32\drivers\etc` (use notepad to open and save)) to disable adds in App Store/ Apps.

   - Enable "[God Mode](https://automationadmin.com/2016/05/create-god-mode-folder/)" to access to over 260 control panel/settings list items. Note you can call it whatever you want before the period, i.e. Admin.

   - Delete the "Windows.Old" files to get space back by running cleanmgr.exe (Disk Cleanup) and selecting "previous versions of Windows".

   - Disable OneDrive: Run => `gpedit.msc` => `Computer Configuration\Administrative Templates\All Settings` => "prevent usage of OneDrive for storage"

   - File Explorer default to My Computer: Open My Computer => View tab => Options => Open File Explorer to dropdown to "this PC"


### References:

["Things to remove/disable in windows 10"](https://www.reddit.com/r/pcmasterrace/comments/3f10k0/things_to_removedisable_in_windows_10/)