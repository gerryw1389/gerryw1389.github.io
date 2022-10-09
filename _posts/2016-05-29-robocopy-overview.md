---
title: Robocopy Overview
date: 2016-05-29T04:46:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/robocopy-overview/
categories:
  - Windows
tags:
  - Backup
---
<!--more-->

### Description:

Robocopy is a built-in Windows tool that is used to copy files from one location to another in seamless way. It is used by administrators for its efficiency and convenience. Here are some example uses. 

NOTE: Replace `(source) (destination)` with UNC paths or mapped drive letters. Also, don't put the trailing backslash in path names as Robocopy will treat this as an escape character.

See [here](http://ss64.com/nt/robocopy.html) for uses.

#### To Copy Directories On Internal Disks:

   ```powershell
   # This will perform standard copy
   robocopy (source) (destination)

   # This will delete files in dest that don't match source
   robocopy (source) (destination) /mir /r:1 /w:1
   ```

#### To Copy Directories Over Network:

   ```powershell
   robocopy (source) (destination) /mir /mt:32 /r:10 /w:10
   ```

#### To Copy Folder Structure (and permissions) But Not Files:

   ```powershell
   robocopy (source) (destination) /e /z /SEC /xf *
   ```

#### To Resolve A &#8220;Path Too Long Error&#8221;:

   - Robocopy can overcome the 255 character limitation in Windows:

   ```powershell
   robocopy c:\emptyfolder c:\deletefolder /purge
   ```

#### To Copy User Files To Backup Server:

   ```powershell
   cd c:\windows\system32  
   robocopy C:\Users\%username%\Documents \\fileserver\userbackups\%username%\Documents /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Desktop \\fileserver\userbackups\%username%\Desktop /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Favorites \\fileserver\userbackups\%username%\Favorites /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Pictures \\fileserver\userbackups\%username%\Pictures /mir /z /e /R:10 /W:10 /mt:4
   ```

   - For an extra step, I would go into the file server itself and set permissions for each user to where only the administrator and that user can modify their directory. Then when they access the file server, they can only use and see their backups.

#### To Copy only permission changes (additions and removals) assuming we already have a copy of the data:

   ```powershell
   robocopy \\FileServer\C$ \\SVR-Backups\c$\Backups /E /Copy:S /IS /IT
   ```

   
