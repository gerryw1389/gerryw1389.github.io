---
title: 'PS: Get Video File Resolution From Folder'
date: 2017-12-24T03:36:24+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-get-video-file-resolution-from-folder/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - MediaEditing
  - FileSystem
---
<!--more-->

### Description:

I was wanting a way to view the resolution of each of my video files. Here is the script I have been using for this:

### To Resolve:

1. This script: Given a source directory, this function will recursively get all the video files and display their resolutions.

   ```powershell
   $Objshell = New-Object -Comobject Shell.Application 

         $Filelist = @() 
         $Attrlist = @{} 
         $Details = ( "Frame Height", "Frame Width", "Frame Rate" ) 
   
         $Objfolder = $Objshell.Namespace($Source) 
         For ($Attr = 0 ; $Attr -Le 500; $Attr++) 
         { 
               $Attrname = $Objfolder.Getdetailsof($Objfolder.Items, $Attr) 
               If ( $Attrname -And ( -Not $Attrlist.Contains($Attrname) )) 
               {  
                  $Attrlist.Add( $Attrname, $Attr )  
               } 
         } 
   
         Get-ChildItem $Source -Recurse -Directory | Foreach-Object { 
               $Objfolder = $Objshell.Namespace($_.Fullname) 
               Foreach ($File In $Objfolder.Items()) 
               {
                  Foreach ( $Attr In $Details) 
                  { 
                     $Attrvalue = $Objfolder.Getdetailsof($File, $Attrlist[$Attr]) 
                     If ( $Attrvalue )  
                     {  
                           Add-Member -Inputobject $File -Membertype Noteproperty -Name $("A_" + $Attr) -Value $Attrvalue 
                     }  
                  } 
                  $Filelist += $File 
                  $Filelist.Count 
               } 
         } 
   
         $Filelist | Export-Csv $Outputfile -Delimiter ',' 
         $Filelist | Format-Table
   ```

2. Source is maintained under [gwFileSystem](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Get-VideoFileInfo.ps1)