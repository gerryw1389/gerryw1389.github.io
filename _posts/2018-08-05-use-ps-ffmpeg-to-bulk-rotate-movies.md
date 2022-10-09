---
title: Use PS/FFMPEG To Bulk Rotate Movies
date: 2018-08-05T07:56:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/use-ps-ffmpeg-to-bulk-rotate-movies/
categories:
  - LocalSoftware
tags:
  - Scripting-Powershell
  - MediaEditing
---
<!--more-->

### Description:

So I have this certain family member that always seems to record videos 90 degrees clockwise and it drives me crazy when trying to import them into Plex. I tried various software to rotate the videos and nothing could do it in bulk without paying. So I hacked together the following solution using Powershell and FFMPEG.

Example: I want to bulk rotate (90 degrees COUNTERclockwise) the following files `c:\temp\vid.mp4`,`c:\temp\vid2.mp4`, and `c:\temp\vid3.mp4`  

NOTE: This assumes you have the ffmpeg executable at c:\temp\ffmpeg\bin\ffmpeg.exe.
{: .notice--success}

### To Resolve:

1. Get a video file from somewhere and copy it three times to c:\temp where the ffmpeg folder lies. Rename to match above (vid.mp4, vid2.mp4, and vid3.mp4).

2. Create a file called `files.txt` in C:\temp and paste the following:

   ```powershell
   c:\temp\vid.mp4
   c:\temp\vid2.mp4
   c:\temp\vid3.mp4
   ```

3. Create four files in C:\temp called run.bat, run.ps1, run2.bat, and run.ps1. For the .bat files, just copy, paste, save, and close the following:

   ```powershell
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile ^
   -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
   popd
   ```

4. For run.ps1, copy and paste the following:

   ```powershell
   $Log = "$PSScriptroot\FilesToProcess.txt"
   If (-not(Test-Path $Log))
   {
   New-Item -Itemtype File -Path $Log | Out-Null
   }

   $FilesToProcess = Get-Content "$PSScriptroot\files.txt"

   ForEach ($File in $FilesToProcess)
   {
      $FilePath = $File -Split "\\"
      $FileFullName = $FilePath[-1]
      $Extension = $Filepath[-1].Split('.')[-1]
      $Filename = $Filepath[-1].Split('.')[-2]
      $Command = "$PSScriptroot\ffmpeg\bin\ffmpeg.exe"
      $Arguments = "-" + "i" + " " + $File + " " + "-vf transpose=2"  + " " + $PSScriptroot + "\" +
      $Filename + "-" + "rotated" + '.' + $Extension
      $Run = $Command + " " + $Arguments
      Write-Output $Run | Out-File $Log -Append
   }
   ```

5. For run2.ps1, copy and paste the following:

   ```powershell
   $Files = Get-Content "$PSScriptRoot\FilesToProcess.txt"

   ForEach ($F in $Files)
   {
   Start-Process PowerShell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command $F" -Verb RunAs
   }
   ```

6. That's it! When you want to bulk rotate movies, you just have to:

   - Edit the original files.txt and put in the full path of the movies you want to rotate.

   - Double click run.bat to launch the first powershell script. It will dump a file to the given directory called `FilesToProcess.txt`. This file is simply a command that will be ran using FFMPEG in the next script for each video file.

   - Double click run2.bat and it will launch separate processes to bulk rotate your videos.
