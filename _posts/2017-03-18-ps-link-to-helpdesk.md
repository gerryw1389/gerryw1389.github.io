---
title: 'PS: Link To Helpdesk'
date: 2017-03-18T04:43:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/03/ps-link-to-helpdesk/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

As part of my initial install script, I like to put a link to our helpdesk on the user's desktop. Like many systems, the API for our helpdesk system allows you to manipulate URLs for ticket submissions so I just used Powershell to create a link on the user's desktop for submitting new tickets.

### To Resolve:

1. Tweak this code in your scripts to set links for users:

   ```powershell
   # Send Helpdesk link to Desktop
   # Feel free to omit this code, but it works great with web API's as you just insert
   # User names into the URL to create a custom form the user can click on to submit a ticket. YMMV.

   $fname = read-host "enter the first name of the user"
   $lname = read-host "enter the last name of the user"

   $string = 'http://helpdeskexample.com/Helpdesk/Tickets/New/?name=' `
   + $fname + '%20' + $lname + '&userName=' + $fname + $lname `
   + '&email=' `
   + $fname + $lname + '@yourdomain.com'

   $TargetFile = "$string"
   $ShortcutFile = "$env:userprofile\Desktop\Helpdesk.url"
   $WScriptShell = New-Object -ComObject WScript.Shell
   $Shortcut = $WScriptShell.CreateShortcut($ShortcutFile)
   $Shortcut.TargetPath = $TargetFile
   $Shortcut.Save()
   ```

2. Source is maintained under [gwMisc](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Send-LinkToHelpdesk.ps1)