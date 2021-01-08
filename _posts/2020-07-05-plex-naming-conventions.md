---
title: Plex Naming Conventions
date: 2020-07-05T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/plex-naming-conventions
categories:
  - LocalSoftware
  - Linux
tags:
  - MediaEditing
---
<!--more-->

### Description:

So in order to have my media processed correctly with Plex I had to name them like so:

### To Resolve:

1. For movies:

   - Before: `/movies/2016-moana/2016-moana.mp4`
   - After: `/movies/Moana (2016)/Moana (2016).mp4`
   - Fix - Named the folders using Bulk Rename Tool and then powershell for each file under it:

   ```powershell
   $movies = gci s:\vids\movies | Sort-Object

   foreach ($movie in $movies)
   {
      $dname = ($movie.fullname).split("\\")[-1]
      write-output $dname
      $file = gci $($movie.FullName) -Recurse -File
      Rename-Item $($file.FullName) -NewName ($dname + $($file.extension) )
      Start-Sleep -Seconds 2 #comment this out after you know it works
   }
   ```

2. For music:

   - Before: `/music/farid--afloat.mp3`
   - After: `/music/Farid/all-music/Afloat.mp3`
   - Fix:
   - Download MusicBrainz Picard
   - Set move files to new directory based on: `%albumartist%/all-music/%title%`
   - Any issues resolved with editing the metadata either with MediaMonkey or Mp3Tag

3. For TV Shows

   - Before: `/TV Shows/ShowName/Season 02/ShowName – s02e17 – Optional_Info.ext`
   - After: `/TV Shows/From the Earth to the Moon/Season 01/From the Earth to the Moon - s01e01.mp4`
   - Fix: Just used Bulk Rename Utility as I already had these almost like this.

4. For photos and home videos, I just sort by Year and then Month so `/photos/2020/01/photo1.jpeg` so I never had issues there as I always just browse by folder for those libraries.


