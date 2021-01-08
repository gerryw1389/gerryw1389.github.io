---
title: PS Script Not Running As Scheduled Task
date: 2019-05-06T12:22:11+00:00
layout: single
classes: wide
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Follow this post to see why a scheduled task is not running successfully.

### To Resolve:

1. First off as a general rule of thumb, don't run GUI applications as scheduled tasks. The main point of scheduled task is to run some code while you are away. That being said, the most common issue I hear is `I can't see the output from my script!`. I then have to explain this is because scheduled tasks are often configured to be ran as `SYSTEM` so you won't see any output. This is why it is crucial to [add logging](https://automationadmin.com/2017/09/ps-logging-snippets/) to your scripts.

2. Your `start in` field is null. You may want to set it to `c:\Scripts\` and see if it behaves differently. I usually get around this by skipping PS files altogether and [call a batch file](https://automationadmin.com/2016/05/how-to-run-ps-as-a-scheduled-task/) in the same directory which then calls the PS1 script.

3. Network resources don't have the appropriate permissions. Remember that when running as `SYSTEM`, you are running as the computer object that it is running. These often don't have permissions to network resources so they fail silently. If the machine is domain joined, just ensure that `Authenticated Users` is set the appropriate permissions. See [here](https://www.morgantechspace.com/2013/08/authenticated-users-vs-domain-users.html) and [here](https://docs.microsoft.com/en-us/previous-versions/tn-archive/dd277461(v=technet.10)).

4. Some applications are not available to the `SYSTEM` account and install as user only. You can usually run a repair on the program and choose `All Users` instead.

5. To quote [a reddit user](https://www.reddit.com/r/PowerShell/comments/bbb1y3/oddities_running_powershell_scripts_through_task/):
   - I have no idea why this is, but when working with other COM objects, I've found I've had to do this incredibly dumb thing. 
   - Create two folders: `C:\Windows\System32\config\systemprofile\Desktop` and `C:\Windows\SysWOW64\config\systemprofile\Desktop`.
   - I saw this somewhere in a technet post and laughed it off, but it actually worked. 
   - I'll reiterate, I have no idea why it worked.