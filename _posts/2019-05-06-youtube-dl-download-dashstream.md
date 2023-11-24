---
title: Youtube-DL Download DashStream
date: 2019-05-06T12:36:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/05/youtube-dl-download-dashstream/
tags:
  - LocalSoftware
tags:
  - MediaEditing
---
<!--more-->

### Description:

If you want to download a stream .m4s but cannot seem to find the mpd file, use this combination.

### To Resolve:

1. Download "The Stream Detector" addon (I use Firefox, not sure if available in Chrome) and the youtube-dl executable.

   - Run:

   ```powershell
   .\youtube-dl.exe "URL from the Stream detector" -o c:\scripts\myfile.mp4 -c
   ```

   - `-o` is the output file you choose  
   - `-c` keeps the connection alive  
   - If you run into any issues, just run the same command again and it will pick up where it left off


2. After downloading videos, I often have to shrink them. You can do this with "handbrake-cli". Shrink MP4 Files:

3. Open the application and right click "Fast 1080p 30" and choose "Export json"

   - Run:

   ```powershell
   c:\scripts\HandBrakeCLI.exe --preset-import-gui "c:\scripts\preset.json" -i "c:\scripts\aquaman.mp4" -o "c:\scripts\aquaman2.mp4"
   ```

4. If you want handbrake to run in batch mode, just pass it a bunch of paths and have it convert them one by one:

   ```powershell
   $files = @(
   'G:\temp\du.mp4',
   'G:\temp\id.mp4',
   'G:\temp\jum.mp4',
   'G:\temp\jw.mp4',
   'G:\temp\ma.mp4',
   'G:\temp\nm.mp4',
   'G:\temp\sm.mp4',
   'G:\temp\water.mp4')

   foreach ($file in $files)
   {
      Write-Output "Converting file: $file"
      $file2 = $file.replace(".mp4", "-enhanced.mp4")
      & C:\scripts\HandBrakeCLI.exe --preset-import-gui "c:\scripts\preset.json" -i $file -o $file2
      Write-Output "Removing original file: $file"
      Remove-Item $file -Force
      Write-Output "Writing file: $file2"
   }
   ```

