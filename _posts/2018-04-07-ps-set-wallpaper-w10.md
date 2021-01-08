---
title: 'PS: Set Wallpaper W10'
date: 2018-04-07T03:10:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-set-wallpaper-w10/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Use the following to set your wallpaper using Powershell

### To Resolve:

1. The internet will tell you to do:

   ```powershell
   Set-ItemProperty -path 'HKCU:\Control Panel\Desktop' -Name Wallpaper -Value "c:\mypic.jpg"
   rundll32.exe user32.dll, UpdatePerUserSystemParameters, 1, True
   ```

   &#8230; But this doesn't take affect until after a reboot => Gross!

2. Use this instead:

   ```powershell
   Function Set-Wallpaper
   {
      Param
      (
         [String]$Path
      )
      Add-Type @"
   using System;
   using System.Runtime.InteropServices;
   using Microsoft.Win32;
   namespace Wallpaper
   {
   public enum Style : int
   {
   Tile, Center, Stretch, NoChange
   }
   public class Setter {
   public const int SetDesktopWallpaper = 20;
   public const int UpdateIniFile = 0x01;
   public const int SendWinIniChange = 0x02;
   [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
   private static extern int SystemParametersInfo (int uAction, int uParam, string lpvParam, int fuWinIni);
   public static void SetWallpaper ( string path, Wallpaper.Style style ) {
   SystemParametersInfo( SetDesktopWallpaper, 0, path, UpdateIniFile | SendWinIniChange );
   RegistryKey key = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
   switch( style )
   {
   case Style.Stretch :
      key.SetValue(@"WallpaperStyle", "2") ; 
      key.SetValue(@"TileWallpaper", "0") ;
      break;
   case Style.Center :
      key.SetValue(@"WallpaperStyle", "1") ; 
      key.SetValue(@"TileWallpaper", "0") ; 
      break;
   case Style.Tile :
      key.SetValue(@"WallpaperStyle", "1") ; 
      key.SetValue(@"TileWallpaper", "1") ;
      break;
   case Style.NoChange :
      break;
   }
   key.Close();
   }
   }
   }
   "@

      [Wallpaper.Setter]::SetWallpaper( $Path, 1 )
      # 0 = Tile; 1 = Center; 2 = Stretch; 3 = No Change
   }
   Set-Wallpaper -Path "c:\mypic.jpg"
   ```

