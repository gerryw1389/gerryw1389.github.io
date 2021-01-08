---
title: Enable Windows Photo Viewer W10
date: 2016-06-25T01:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/enable-windows-photo-viewer-w10/
categories:
  - Windows
tags:
  - Regedit
  - Tweaks
---
<!--more-->

### Description:

The biggest issue I have faced with end users moving to Windows 10 is the fact that it butchers most common file extensions. It does this by replacing programs you are used to using with certain file types with their crappy versions. I personally use [XNView](http://www.xnview.com/en/xnview/) for photo  viewing, but a number of my users like to use the Windows Photo Viewer.

First, right click a .jpg and see if you can "open with" Windows Photo Viewer. If it doesn't show up in the list, then run the following reg import and then try again:

### To Resolve:

1. Copy and paste the following into notepad and save as .reg:

   ```escape
   Windows Registry Editor Version 5.00

   ; Created by: Shawn Brink  
   ; Created on: August 8th 2015  
   ; Tutorial: http://www.tenforums.com/tutorials/14312-windows-photo-viewer-restore-windows-10-a.html

   [HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open]  
   "MuiVerb"="@photoviewer.dll,-3043"

   [HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\Applications\photoviewer.dll\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap]  
   "ImageOptionFlags"=dword:00000001  
   "FriendlyTypeName"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,\  
   00,46,00,69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,\  
   77,00,73,00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,\  
   00,65,00,72,00,5c,00,50,00,68,00,6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,\  
   65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,35,00,36,00,00,\  
   00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\DefaultIcon]  
   @="%SystemRoot%\\System32\\imageres.dll,-70"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Bitmap\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.JFIF]  
   "EditFlags"=dword:00010000  
   "ImageOptionFlags"=dword:00000001  
   "FriendlyTypeName"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,\  
   00,46,00,69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,\  
   77,00,73,00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,\  
   00,65,00,72,00,5c,00,50,00,68,00,6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,\  
   65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,35,00,35,00,00,\  
   00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.JFIF\DefaultIcon]  
   @="%SystemRoot%\\System32\\imageres.dll,-72"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.JFIF\shell\open]  
   "MuiVerb"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,\  
   69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,\  
   00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,\  
   72,00,5c,00,70,00,68,00,6f,00,74,00,6f,00,76,00,69,00,65,00,77,00,65,00,72,\  
   00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,34,00,33,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.JFIF\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.JFIF\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Jpeg]  
   "EditFlags"=dword:00010000  
   "ImageOptionFlags"=dword:00000001  
   "FriendlyTypeName"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,\  
   00,46,00,69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,\  
   77,00,73,00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,\  
   00,65,00,72,00,5c,00,50,00,68,00,6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,\  
   65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,35,00,35,00,00,\  
   00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Jpeg\DefaultIcon]  
   @="%SystemRoot%\\System32\\imageres.dll,-72"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Jpeg\shell\open]  
   "MuiVerb"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,\  
   69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,\  
   00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,\  
   72,00,5c,00,70,00,68,00,6f,00,74,00,6f,00,76,00,69,00,65,00,77,00,65,00,72,\  
   00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,34,00,33,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Jpeg\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Jpeg\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Gif]  
   "ImageOptionFlags"=dword:00000001  
   "FriendlyTypeName"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,\  
   00,46,00,69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,\  
   77,00,73,00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,\  
   00,65,00,72,00,5c,00,50,00,68,00,6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,\  
   65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,35,00,37,00,00,\  
   00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Gif\DefaultIcon]  
   @="%SystemRoot%\\System32\\imageres.dll,-83"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Gif\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Gif\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Png]  
   "ImageOptionFlags"=dword:00000001  
   "FriendlyTypeName"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,\  
   00,46,00,69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,\  
   77,00,73,00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,\  
   00,65,00,72,00,5c,00,50,00,68,00,6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,\  
   65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,35,00,37,00,00,\  
   00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Png\DefaultIcon]  
   @="%SystemRoot%\\System32\\imageres.dll,-71"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Png\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Png\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Wdp]  
   "EditFlags"=dword:00010000  
   "ImageOptionFlags"=dword:00000001

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Wdp\DefaultIcon]  
   @="%SystemRoot%\\System32\\wmphoto.dll,-400"

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Wdp\shell\open]  
   "MuiVerb"=hex(2):40,00,25,00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,\  
   69,00,6c,00,65,00,73,00,25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,\  
   00,20,00,50,00,68,00,6f,00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,\  
   72,00,5c,00,70,00,68,00,6f,00,74,00,6f,00,76,00,69,00,65,00,77,00,65,00,72,\  
   00,2e,00,64,00,6c,00,6c,00,2c,00,2d,00,33,00,30,00,34,00,33,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Wdp\shell\open\command]  
   @=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,74,00,25,\  
   00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,72,00,75,00,\  
   6e,00,64,00,6c,00,6c,00,33,00,32,00,2e,00,65,00,78,00,65,00,20,00,22,00,25,\  
   00,50,00,72,00,6f,00,67,00,72,00,61,00,6d,00,46,00,69,00,6c,00,65,00,73,00,\  
   25,00,5c,00,57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,50,00,68,00,6f,\  
   00,74,00,6f,00,20,00,56,00,69,00,65,00,77,00,65,00,72,00,5c,00,50,00,68,00,\  
   6f,00,74,00,6f,00,56,00,69,00,65,00,77,00,65,00,72,00,2e,00,64,00,6c,00,6c,\  
   00,22,00,2c,00,20,00,49,00,6d,00,61,00,67,00,65,00,56,00,69,00,65,00,77,00,\  
   5f,00,46,00,75,00,6c,00,6c,00,73,00,63,00,72,00,65,00,65,00,6e,00,20,00,25,\  
   00,31,00,00,00

   [HKEY_CLASSES_ROOT\PhotoViewer.FileAssoc.Wdp\shell\open\DropTarget]  
   "Clsid"="{FFE2A43C-56B9-4bf5-9A79-CC6D4285608A}"

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities]  
   "ApplicationDescription"="@%ProgramFiles%\\Windows Photo Viewer\\photoviewer.dll,-3069"  
   "ApplicationName"="@%ProgramFiles%\\Windows Photo Viewer\\photoviewer.dll,-3009"

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Photo Viewer\Capabilities\FileAssociations]  
   ".jpg"="PhotoViewer.FileAssoc.Jpeg"  
   ".wdp"="PhotoViewer.FileAssoc.Wdp"  
   ".jfif"="PhotoViewer.FileAssoc.JFIF"  
   ".dib"="PhotoViewer.FileAssoc.Bitmap"  
   ".png"="PhotoViewer.FileAssoc.Png"  
   ".jxr"="PhotoViewer.FileAssoc.Wdp"  
   ".bmp"="PhotoViewer.FileAssoc.Bitmap"  
   ".jpe"="PhotoViewer.FileAssoc.Jpeg"  
   ".jpeg"="PhotoViewer.FileAssoc.Jpeg"  
   ".gif"="PhotoViewer.FileAssoc.Gif"  
   ".tif"="PhotoViewer.FileAssoc.Tiff"  
   ".tiff"="PhotoViewer.FileAssoc.Tiff"
   ```

2. Double click the reg to import it.


### References:

["To Restore Windows Photo Viewer for All Accounts"](http://www.tenforums.com/tutorials/14312-windows-photo-viewer-restore-windows-10-a.html#option2)