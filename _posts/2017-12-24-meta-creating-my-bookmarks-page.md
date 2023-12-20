---
title: 'Meta: Creating My Bookmarks Page'
date: 2017-12-24T04:53:29+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/meta-creating-my-bookmarks-page/
tags:
  - Windows
tags:
  - Powershell
  - Regex
---
<!--more-->

### Description:

As anyone who is into scripting must sometime learn, I need to learn how to use Regex with Powershell. I'm very new at this still so I wanted to start with a task I have to do kind of frequently: Updating my [Bookmarks](https://automationadmin.com/2016/02/bookmarks/) page.

Essentially:

  1. Add random links to Google Bookmarks while I'm browsing. This is not to be confused with Chrome bookmarks. It is it's own site/ service ([bookmarks.google.com](https://bookmarks.google.com)) that I use for professional references and not my dank internet memes.
  2. PS will download this file in line 6.
  3. The rest of the script just does find and replace of the strings.
  4. Once it is done, I just copy the completed to my post in WordPress. Done.

### To Resolve:

1. Script:

   ```powershell
   If (Test-Path "c:\users\$env:username\Downloads\GoogleBookmarks.html")
   {
   Remove-Item "c:\users\$env:username\Downloads\GoogleBookmarks.html"
   }

   & 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' https://www.google.com/bookmarks/bookmarks.html?hl=en

   Set-Location -Path "$env:userprofile\Downloads"
   Start-Sleep -Seconds 6

   $File = "$env:userprofile\Downloads\GoogleBookmarks.html"
   $Find = [regex]::Escape($Find) 

   $Find = '<DT>'
   $Replace = (Get-Content $File -Raw) -replace '<DT>', '' -Replace '<DL>', '' -Replace '</DL>','' -replace 'ADD_DATE=..................','' |
   Add-Content -Path "$File.tmp" -Force 
   Remove-Item -Path $File 
   Rename-Item -Path "$File.tmp" -NewName $File

   $a = foreach ($line in [System.IO.File]::ReadLines($file)) 
   {
   If ( $line -cmatch '^<A HREF' )
   {
      [regex]$pattern = '>'
      $pattern.replace($line,'>', 1) 
   }
   Else
   {
   $line
   }
   }
   $a | Out-File '.\Completed.html'
   ```

2. Source is maintained under [gwNetworking](https://github.com/gerryw1389/powershell/blob/main/gwNetworking/Public/Convert-Bookmarks.ps1)