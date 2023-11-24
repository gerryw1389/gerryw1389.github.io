---
title: 'PS: Create Batch Launcher Files'
date: 2017-12-24T04:20:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-create-batch-launcher-files/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - FileSystem
---
<!--more-->

### Description:

So in the past I wrote about a way to call PS1 files with Batch files to `bypass Executionpolicy` and run scripts as admin, if you have not seen that post => it is [here](https://automationadmin.com/2017/03/ps-call-ps1-with-batch/). What this script does is create a batch file for each of my script automatically.  
This script works great if you have a module, but you want to run each of your scripts in your `public` folder one by one for whatever reason. 

One major note about using this script though is you will have to `MANUALLY UNCOMMENT THE FUNCTION CALL AT THE END OF EACH SCRIPT`.
{: .notice--danger}

So the use case would be something like this:

  1. Run this script against your `ModuleNamel\Public\*.ps1` files which will then create a batch file to launch each of your scripts.
  2. Go to the scripts you want to run as a script and open it up and remove the comment from the third line to the last line in the file (usually).

### To Resolve:

1. Creates batch files for each powershell script in a directory.

   ```powershell
   Function Write-TestFiles
         {
               New-Item -Path "C:\scripts" -Name "g" -ItemType Directory
               New-Item -Path "C:\scripts\g" -Name "1.ps1" -ItemType File
               New-Item -Path "C:\scripts\g" -Name "2.ps1" -ItemType File
               New-Item -Path "C:\scripts\g" -Name "h" -ItemType Directory
               New-Item -Path "C:\scripts\g\h" -Name "1.ps1" -ItemType File
               New-Item -Path "C:\scripts\g\h" -Name "2.ps1" -ItemType File
               New-Item -Path "C:\scripts\g\h" -Name "i" -ItemType Directory
               New-Item -Path "C:\scripts\g\h\i" -Name "1.ps1" -ItemType File
               New-Item -Path "C:\scripts\g\h\i" -Name "2.ps1" -ItemType File
               $Path = "C:\scripts\g"
         }

   #Write-TestFiles
         $Files = Get-ChildItem $Path -Filter "*.ps1" -Recurse

         ForEach ($File in $Files)
         {
               $Batch = $($File.DirectoryName) + "\" + $($File.BaseName) + ".bat"
               $String = @"
   `@ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
   PAUSE
   "@
               Write-Output $String | Out-File -LiteralPath $Batch -Encoding ascii

         }
   ```

2. Source is maintained under [gwFileSystem](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/New-BatLaunchers.ps1)