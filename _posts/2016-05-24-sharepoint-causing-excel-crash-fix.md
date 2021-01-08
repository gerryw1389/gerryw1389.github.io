---
title: Sharepoint Causing Excel Crash Fix
date: 2016-05-24T12:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/sharepoint-causing-excel-crash-fix/
categories:
  - Windows
tags:
  - Scripting-CMD
  - Cloud
  - Updates
---
<!--more-->

### Description:

Users will have an issue where Excel will crash when they open a document from Sharepoint. The user will be able to login to Sharepoint, log out a document, enter their credentials to open it, and right before it opens => it crashes the application with the error `Excel has stopped working` => `eventvwr.msc` just shows `appcrash.exe`.

### To Resolve:

1. This is a well known issue caused by Windows Update KB3055034. You need to Run => `appwiz.cpl` => Installed updates => Sort => Uninstall. While in there, I uninstall KB3054886 as well as it showed up a lot in search results for this issue.

2. Reboot the computer and have the user try again.

   - NOTE: When I first heard about this issue, and after calling Sharepoint support, I was given a list of KB's to uninstall. I created a batch script to uninstall them like:

   ```powershell
   @echo off  
   wusa /uninstall /kb:3055034 /quiet /norestart  
   wusa /uninstall /kb:3054886 /quiet /norestart  
   shutdown -r -t 03  
   echo &#8220;done&#8221;
   ```

   - ... or something to that effect. Didn't work. The computer would reboot and even say &#8220;configuring updates&#8221;, but the update was still installed. The only way I found this to work is to actually manually run the commands and pick the updates out of the list to uninstall.

3. After reboot, make sure to check for updates and hide the culprit updates as well.