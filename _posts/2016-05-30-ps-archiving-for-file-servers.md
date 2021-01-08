---
title: 'PS: Archiving For File Servers'
date: 2016-05-30T06:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ps-archiving-for-file-servers/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - FileSystem
---
<!--more-->

### Description:

I wanted to see about creating an archive from our file server so that I could move data that is older to another directory. My favorite tool is Powershell, but I really like using Robocopy for any kind of file structure syncs. Either way, the following guide can be used in order to create an Archive for your file server.

NOTE: In this example, I wanted to move all files older than a year to another location.

### To Resolve:

1. Before touching any real data, always start by testing POC (Proof of Concept):

   - Create `C:\Test` on your local machine.
   - Create `C:\Test2` on your local machine.
   - Create some random text files in `C:\Test` and change their security properties e.g. Disable inheritance => Remove default user groups => Add some => Change their permissions, ect.

2. Open up a Powershell window and run:

   - Load the following function (I would just use ISE for one time use. If you do this often, put it in your profile):

   ```powershell
   Function Set-Filetimestamps
   {
   Param (
   [Parameter(Mandatory=$True)]
   [String]$Path,
   [Datetime]$Date = (Get-Date))

   Get-Childitem -Path $Path -Recurse |
   Foreach-Object {
   $_.Creationtime = $Date
   $_.Lastaccesstime = $Date
   $_.Lastwritetime = $Date }
   } 

   # Now we run it:
   Set-Filetimestamps -Path C:\Test -Date 7/1/2011
   ```

3. You can now see that all the time stamps changed for that folder and it's directory. Now we will create a function that moves older files to the C:\test2 folder and leaves any new ones:

   - Inside C:\test, create a couple new text documents and sub directories. They should obviously have today's date instead of an older date.

   ```powershell
   Function Move-Toarchive
   {
   Param (
   [Parameter(Mandatory=$True)]
   [String]$Path,
   [String]$Dest,
   [Int]$Days)

   New-Psdrive -Psprovider Filesystem -Root $Path -Name Path

   Cd $Path

   Get-Childitem -Recurse |
   Where-Object {$_.Lastwritetime -Lt (Get-Date).Adddays(-$Days)} |
   Move-Item -Destination $Dest -Force
   }

   # Now we run it:
   Move-Toarchive -Path C:\Test -Days 365 -Dest C:\Test2
   ```

4. That's it! Run the second script on a file server of your choice using the parameters you want.

5. Source is maintained under [gwFileSystem](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Move-FilesToArchive.ps1) and [here](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Set-FileTimeStamps.ps1)