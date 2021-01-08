---
title: Scripting Windows Updates Installs
date: 2018-12-27T07:22:19+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/12/scripting-windows-updates-installs/
categories:
  - Windows
tags:
  - Updates
---
<!--more-->

### Description:

I haven't tested this yet, but this seems to be the only way to script Windows Updates at this time if you don't have a tool such as Ansible, Puppet, SCCM, or WSUS.

### To Resolve:

1. xcopy the [PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) module to the remote computer's `\\ServerComputerName\c$\windows\System32\WindowsPowerShell\v1.0\Modules` folder.  

1. This creates the scheduled task and runs it :  

   ```powershell
   Invoke-WUInstall -ComputerName -Script {import-module PSWindowsUpdate; Get-WUInstall -AcceptAll} -Confirm:$false
   ```