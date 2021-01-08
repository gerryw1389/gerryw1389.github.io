---
title: 'Plex: Ignore Directories'
date: 2018-03-18T15:54:05+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/plex-ignore-directories/
categories:
  - LocalSoftware
tags:
  - MediaEditing
---
<!--more-->

### Description:

Follow these steps to have Plex Media Server ignore a directory.

### To Resolve:

1. So let's say we have a folder: `C:\vids`. In it, you have two normal folders `youtube` and `movies` that Plex scans and adds to its libraries. But let's say we have a `private-vids` folder in there that is hidden in Windows Explorer that you don't want Plex to scan. What you do is create a file called `.plexignore` and put the folder followed by `/*` as the value. Plex will then skip it. In Powershell, this looks like:

   ```powershell
   Set-Location C:\vids
   (ni -ItemType file -Value "private-vids/*" -Name .plexignore).attributes="hidden"
   ```

2. Now you can verify:

   ```powershell
   cd c:\vids
   ls
   # Shows "youtube" folder and "movies" folder
   ls -Hidden
   # Shows "private-vids" folder and ".plexignore" file
   cat .\.plexignore
   # returns: private-vids/*
   ```