---
title: TV Website Dashboard Setup
date: 2016-06-25T01:07:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/tv-website-dashboard-setup/
tags:
  - Hardware
tags:
  - Setup
---
<!--more-->

### Description:

Follow this guide to setup an (almost automatic) TV display that rotates through web dashboards.

Guidelines:

Energy efficient  
Boot automatically  
Logon to the OS automatically  
Start the browser automatically  
Load tabs automatically  
Login to the dashboards automatically  
Shutdown automatically

Result:

Vizio E43-C2  LED television and a 3rd gen Intel NUC.

### To Resolve:

1. Setup the NUC to boot automatically => Boot => F2 => BIOS. Advanced => Power => Wake System From S5. Leave "Wakeup Date" as "0" to enable daily wakes. Enter an hour in 24-hour format in "Wakeup Hour". I chose "8". Enter a minute in "Wakeup Minute". I chose "30". Press F10 to "Save and exit"

   - The Intel NUC requires a tweak in Windows 10 to come out of S5. Inside Windows, follow these steps to setup: Run => `Powercfg.cpl` => Choose What the Power Buttons Do => Change settings that are currently unavailable => Disable/Uncheck "Fast Startup (Recommended)". Save Changes.  
   Optional => Set clock to 8:25 and shutdown.

2. Setup a limited user account with a password => Now setup auto-logon. To do this, Run => `userpasswords2` => Select the account => Disable/uncheck "Users must enter a user name and password to use this computer" => Apply => OK twice.

3. Allow Chrome to launch on statup => Navigate to: `c:\Users\yourName\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. Substitue 'yourName' with the account name. Now drag and drop a Chrome shortcut in there. Right click the shortcut => Go to properties => add `--start-maximized` after chrome.exe in the Target field => OK => Close.

4. Load tabs automatically =>  Enter `chrome://settings/onStartup` in the address bar, Add the URL(s) for the page(s) to load, OK and Close.

   - (Optional) Add "Auto Login" plugin to Chrome. Click on each dashboard tab and use the large floating capture button to capture the password into Auto Login. I found the best results capturing one tab/dashboard at a time. Add "TabCarousel" to Chrome. Configure TabCarousel to start with Chrome by checking "Start automatically". Configure the wait time between tab changes. I have three tabs to cycle so I set Flip Wait to "20000". TabCarousel tabs through all three tabs once per minute. **Auto Login occasionally takes a minute or three before it will login a dashboard.

5. Config auto shutdown => Run => `taskschd.msc` => Create Basic Task => Name: DailyShutdown => Daily => Start a program => `c:\windows\system32\shutdown.exe` in "Program/script" field => Next => Finish. Now double click it in the task scheduler => Run whether user is logged on or not => Run with highest privileges => Click to enable "hidden" => Clear/disable "Run task as soon as possible after a scheduled start is missed" => OK.

### References:

["An automated dashboard display"](https://www.reddit.com/r/sysadmin/comments/4ho6mt/an_automated_dashboard_display/)