---
title: Using Set-Content To Modify Your Scripts
date: 2017-08-12T08:09:26+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/using-set-content-to-modify-your-scripts/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - FileSystem
---
<!--more-->

### Description:

So like many other scripters, I find that I often want my PS files to follow a certain template, so I created a function that will both insert and append predefined text to my scripts so that I can just open VS Code and modify the &#8220;body&#8221;. Here goes:

### To Resolve:

1. Use the following:

   ```powershell
   # Edit these extensions to the type of files you want to add content to.
   $Include = @("*.txt", "*.ps1", "*.log")

   # $Source = Get-Childitem "C:\Test" -Include "$Include" -Recurse
   $Source = Get-Childitem "C:\Test" -Include "$Include"

   Foreach ($File In $Source)
   {

   Write-Output "Processing $File ..." 

   # Remember to use the escape character "`" before every dollar sign and ` character. For example `$myVar and ``r``n (new line)
   $Preformatting = @"
   Multi-Line
   Text
   To
   Insert
   At
   Top
   "@

   $CurrentFile = Get-Content $File

   $PostFormatting = @"
   Multi-Line
   Text
   To
   Insert
   At
   Bottom
   "@

   $Val = -Join $Preformatting, $CurrentFile, $PostFormatting
   Set-Content -Path $File -Value $Val
   Write-Output "$File rewritten successfully"
   }
   ```

2. At first I couldn't get this to work unless I moved the files to a new directory, but after a couple hours of research, I can say this does work. It will keep the original files in their current folders.

3. Source is maintained under [gwFileSystem](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Set-PreformattedContent.ps1)