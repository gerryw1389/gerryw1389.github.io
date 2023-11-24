---
title: 'PS: Call PS1 With Batch'
date: 2017-03-25T04:11:41+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/03/ps-call-ps1-with-batch/
tags:
  - Windows
tags:
  - Scripting-CMD
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

I almost never run Powershell script directly. Instead I usually create a batch file with the same filename as the Powershell script and place it in the same directory (usually C:\Scripts). This allows you to run the script and exit interactively. If you plan to set a powershell script as a scheduled task, just remove the PAUSE at the end.

### To Resolve:

1. Save the following as a .bat and run it. It will call any .ps1 file in the same directory that has the same name.

   ```powershell
   :: For functions (default)
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command ". "%~dpn0.ps1"; Clean-tempfiles "' -Verb RunAs}"
   popd

   :: For scripts
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
   popd
   ```

2. You can stop at step 1 if you run scripts interactively, but most of the time you want them to be scheduled tasks. This is how I set it up in my environment:

   - Create a directory called C:\scripts and edit the NTFS permissions to allow only: SYSTEM, Domain Admins, and Enterprise Admins
   - Place all your PS Scripts in there with batch files with the exact same file name (or just edit the file to hard code the file name, meh) in the above directory.
   - Create a scheduled task:
     - User is System, Run with Highest Privileges checked
     - Schedule: Usually Daily 12:10 AM, Repeat every 10 minutes for one day for constant scripts or just daily/weekly for regular scripts.
     - Actions: Point to the batch file: C:\scripts\powercheck.bat (for example) and start-in = C:\scripts\
     - That's it, scripts will run reliably over and over. Never had issues with Scheduled Tasks or running any scripts&#8230;.

3. To do this via Powershell:

   ```powershell
   $taskName = "RunMyScript2"
   $taskAction = New-ScheduledTaskAction –Execute C:\scripts\test.bat -WorkingDirectory "C:\scripts\"
   $taskTrigger = New-ScheduledTaskTrigger -At 2am -Daily
   $taskUser = New-ScheduledTaskPrincipal -UserID "NT AUTHORITY\SYSTEM" -RunLevel Highest
   Register-ScheduledTask –TaskName $taskName -Action $taskAction –Trigger $taskTrigger -Principal $taskUser
   ```

   - Running as a user instead but still &#8220;run whether use is logged in or not&#8221;

   ```powershell
   $taskName = "RunMyScript4"
   $taskAction = New-ScheduledTaskAction –Execute C:\scripts\test.bat -WorkingDirectory "C:\scripts\"
   $taskTrigger = New-ScheduledTaskTrigger -At 2am -Daily
   $taskUser = New-ScheduledTaskPrincipal -UserID "SomePC\Gerry" -RunLevel Highest -LogonType S4U
   Register-ScheduledTask –TaskName $taskName -Action $taskAction –Trigger $taskTrigger -Principal $taskUser
   ```

