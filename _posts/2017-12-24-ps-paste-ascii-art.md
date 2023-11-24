---
title: 'PS: Paste Ascii Art'
date: 2017-12-24T05:20:25+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-paste-ascii-art/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Sends common Ascii commands to your clipboard.

### To Resolve:

1. Script ([Original Source](https://www.reddit.com/r/PowerShell/comments/4aipw5/%E3%83%84/?st=jbkbt5rb&sh=dc3f6f8f)):

   ```powershell
   Param
      (
         [switch]$Shrug,
         [switch]$Disapproval,
         [switch]$TableFlip,
         [switch]$TableBack,
         [switch]$TableFlip2,
         [switch]$TableBack2,
         [switch]$TableFlip3,
         [switch]$Denko,
         [switch]$BlowKiss,
         [switch]$Lenny,
         [switch]$Angry,
         [switch]$DontKnow,
         [String]$Logfile = "$PSScriptRoot\..\Logs\Send-AsciiToClipboard.Log"
      )

   Begin
   {
         $OutputEncoding = [System.Text.Encoding]::unicode
   }
   Process
   { 
            If ($Shrug)
               {
                  [char[]]@(175, 92, 95, 40, 12484, 41, 95, 47, 175) -join '' | clip
               }
               If ($Disapproval)
               {
                  [char[]]@(3232, 95, 3232) -join '' | clip
               }
               If ($TableFlip)
               {
                  [char[]]@(40, 9583, 176, 9633, 176, 65289, 9583, 65077, 32, 9531, 9473, 9531, 41) -join '' | clip
               }
               If ($TableBack)
               {
                  [char[]]@(9516, 9472, 9472, 9516, 32, 175, 92, 95, 40, 12484, 41) -join '' | clip
               }
               If ($TableFlip2)
               {
                  [char[]]@(9531, 9473, 9531, 32, 65077, 12541, 40, 96, 1044, 180, 41, 65417, 65077, 32, 9531, 9473, 9531) -join '' | clip
               }
               If ($TableBack2)
               {
                  [char[]]@(9516, 9472, 9516, 12494, 40, 32, 186, 32, 95, 32, 186, 12494, 41) -join '' | clip
               }
               If ($TableFlip3)
               {
                  [char[]]@(40, 12494, 3232, 30410, 3232, 41, 12494, 24417, 9531, 9473, 9531) -join '' | clip
               }
               If ($Denko)
               {
                  [char[]]@(40, 180, 65381, 969, 65381, 96, 41) -join '' | clip
               }
               If ($BlowKiss)
               {
                  [char[]]@(40, 42, 94, 51, 94, 41, 47, 126, 9734) -join '' | clip
               }
               If ($Lenny)
               {
                  [char[]]@(40, 32, 865, 176, 32, 860, 662, 32, 865, 176, 41) -join '' | clip
               }
               If ($Angry)
               {
                  [char[]]@(40, 65283, 65439, 1044, 65439, 41) -join '' | clip
               }
               If ($DontKnow)
               {
                  [char[]]@(9488, 40, 39, 65374, 39, 65307, 41, 9484) -join '' | clip
               }
   }
   ```

2. Source is maintained under [gwMisc](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Send-AsciiToClipboard.ps1)