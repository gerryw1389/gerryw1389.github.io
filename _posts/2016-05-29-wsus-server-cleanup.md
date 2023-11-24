---
title: WSUS Server Cleanup
date: 2016-05-29T04:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wsus-server-cleanup/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - Updates
---
<!--more-->

### Description:

Follow these steps to clear WSUS server updates that are bloating the server.

### To Resolve:

Update 2017-10: I don't bother with native Windows WSUS cleanup as it doesn't do anything worthwhile. Instead, download the WSUS clean up script (link removed => lookup adam wsus).

1. Set the email variables from lines 607-629

2. Optionally add the line &#8220;[System.Net.ServicePointManager]::ServerCertificateValidationCallback = { return $true }&#8221; After line 3247

3. Place in C:\scripts

4. Open admin shell and type &#8220;Set-Executionpolicy bypass&#8221;

5. Type &#8220;.\clean-wsus.ps1 -FirstRun&#8221;

   - This will run the script and install the scheduled task.

6. Now type: &#8220;Set-Executionpolicy RemoteSigned&#8221;

   - For an ad hoc clean, I usually run something like my script [here](https://github.com/gerryw1389/powershell/blob/main/gwApplications/Public/Invoke-WSUSCleanup.ps1).

---

1. Make sure the option: &#8220;Download update files to this server only when updates are approved&#8221; is checked

2. Disapprove any unwanted updates.

3. Close any open WSUS windows and stop the Update Services service.

4. Delete ALL files and folders in the WSUSContent folder (C:WSUSWsusContent on my machine)

5. Start the Update Services service.

6. Open a command prompt and navigate to the folder: C:Program FilesUpdate ServicesTools and type: WSUSUtil.exe RESET

7. You could create a script in Powershell v5 that you can set to run automatically:

   - `Invoke-WsusServerCleanup -CleanupObsoleteComputers -CleanupObsoleteUpdates -CleanupUnneededContentFiles -CompressUpdates -DeclineExpiredUpdates -DeclineSupersededUpdates`

### References:

[http://blogs.technet.com/b/gborger/archive/2009/02/27/what-to-do-when-your-wsuscontent-folder-grows-too-large.aspx](https://blogs.technet.microsoft.com/gborger/2009/02/27/what-to-do-when-your-wsuscontent-folder-grows-too-large/)