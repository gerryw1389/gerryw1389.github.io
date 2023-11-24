---
title: 'PS: Startup Script'
date: 2018-02-24T07:41:09+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/ps-startup-script/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

One of my main goals this year is to replace all of my batch scripts with Powershell scripts. These are some examples.

### To Resolve:

1. When calling external programs, there is really one a few rules:

   - Use `&` to call the app.

   ```powershell
   #Shut down VMs

   Try
   {
      Write-Output "Gracefully shutting down VMs so we can reboot"
      # Website
      & "C:\Program Files\Oracle\VirtualBox\vboxmanage.exe" controlvm "XXXXXXX-383a-00000-bb2f-6da0ea34f94c" acpipowerbutton
      # Plex
      & "C:\Program Files\Oracle\VirtualBox\vboxmanage.exe" controlvm "XXXXXXX-2816-00000-bd90-7af3cf0b39cb" acpipowerbutton
   }
   Catch
   {
      Write-Error -Message $($_.Exception.Message)
   }
   ```

   - And my startup script:

   ```powershell
   #Startup

   Write-Output "Running default startup script"
               
   # Start-Process "Z:\google\myexe.exe"
   # Start-Process "Z:\google\myexe.exe"
   # Placed in "shell:startup" instead...
            
   Set-Location "C:\Program Files\Oracle\VirtualBox"
   & vdesk create:3

   $Command = 'C:\Program Files (x86)\VDesk\vdesk.exe'
   $Arguments = @("on:3", "run:$Arguments2")
   $Arguments2 = '"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --comment "gw-www" --startvm "XXXXXXX-383a-4121-bb2f-6da0ea34f94c"'
   & $Command $Arguments

   $Command = 'C:\Program Files (x86)\VDesk\vdesk.exe'
   $Arguments = @("on:3", "run:$Arguments2")
   $Arguments2 = '"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --comment "gw-plex" --startvm "XXXXXXX-2816-45fa-bd90-7af3cf0b39cb"'
   & $Command $Arguments

   Write-Output "Setting BGInfo Background"
   $Command = "C:\Sysinternals Suite\bginfo\bginfo.exe"
   $Arguments = @("C:\bginfo\mysettings.bgi", "/timer:0")
   & $Command $Arguments
   ```

2. As mentioned in a [previous post](https://automationadmin.com/2016/11/ps-replace-cmd), use the Don't Parse symbol (`--%`) when converting longer commands.
