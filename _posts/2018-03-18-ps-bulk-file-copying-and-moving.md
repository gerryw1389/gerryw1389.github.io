---
title: 'PS: Bulk File Copying and Moving'
date: 2018-03-18T16:15:26+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/ps-bulk-file-copying-and-moving/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - FileSystem
---
<!--more-->

### Description:

Powershell is a great tool for moving, copying, modifying files in bulk. This is how I normally do it:

1. Create a collection of files that needs one of these actions and place in a variable.  
2. Use &#8220;Foreach&#8221; to loop through each item and perform that action.

This works great in almost all cases. But sometimes, it's much better to just use Robocopy and let that tool deal with the specifics. See below.

### To Resolve:

1. First, I would create the $Files array and then do my action in a foreach loop as described above. For example:

   ```powershell
   Try
   {
   $Files = @()
   $Files += "c:\scripts\gwActiveDirectory\Private\helpers.psm1"
   $Files += "c:\scripts\gwApplications\Private\helpers.psm1"
   $Files += "c:\scripts\gwConfiguration\Private\helpers.psm1" 
   $Files += "c:\scripts\gwFileSystem\Private\helpers.psm1" 
   $Files += "c:\scripts\gwMisc\Private\helpers.psm1" 
   $Files += "c:\scripts\gwNetworking\Private\helpers.psm1"

   ForEach ($File in $Files)
   {
      If (Test-Path $File)
      {
         Copy-Item "$PSScriptRoot\..\Private\helpers.psm1" -Destination $File -Force
         Write-Output "Overwriting helper function module $File"
      }
      Else
      {
         Write-Output "Destination module doesn't exist; Nothing to overwrite!"
      }
   }
   }

   Catch
   {
   Write-Error -Message $($_.Exception.Message)
   }
   ```

2. But if I just want a simple mirror of one directory to another (which I use all over my four internal drives), I prefer to just have Robocopy do it for me!

   ```powershell
   Try
   {
   $Logfile = "C:\scripts\mylog.log"
   $Command = "$env:Windir\system32\robocopy.exe"
   $Arguments = @("C:\Scripts", "C:\Scripts2", "/mir", "/r:1", "/w:1", "/np", "/nfl", "/ndl", "/log+:$Logfile")
   & $Command $Arguments
   }
   Catch
   {
   Write-Error -Message $($_.Exception.Message)
   }
   ```