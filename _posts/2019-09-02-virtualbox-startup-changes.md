---
title: VirtualBox Startup Changes
date: 2019-09-02T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/virtualbox-startup-changes/
categories:
  - LocalSoftware
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:
While running my normal startup script, I got the following error: `error: --startvm is an option for the VirtualBox VM runner (VirtualBoxVM) application, not the VirtualBox Manager.`

### Description:

1. Simply change my script from `VirtualBox.exe` to `VirtualBoxVM.exe`

   - From
   
   ```powershell
   $Command = "C:\Program Files (x86)\VDesk\vdesk.exe" 
   $Arguments = @("on:3", 'run:"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe" --startvm "8801bb88-2816-xxx-bd90-7af3cf0b39cb"')
   & $Command $Arguments
   ```

   - To
  
   ```powershell
   $Command = "C:\Program Files (x86)\VDesk\vdesk.exe" 
   $Arguments = @("on:3", 'run:"C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe" --startvm "8801bb88-2816-xxx-bd90-7af3cf0b39cb"')
   & $Command $Arguments
   ```

