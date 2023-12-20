---
title: Play Mario Theme Song In Powershell
date: 2017-12-24T05:10:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/play-mario-theme-song-in-powershell/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

Why? Because Powershell can!

### To Resolve:

1. Script:

   ```powershell
   Function Play-MarioIntro 
         {
               [console]::beep($E, $SIXTEENTH)
               [console]::beep($E, $EIGHTH)
               [console]::beep($E, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($C, $SIXTEENTH)
               [console]::beep($E, $EIGHTH)
               [console]::beep($G, $QUARTER)
         }

         Function Play-MarioIntro2
         {
               [console]::beep($C, $EIGHTHDOT)
               [console]::beep($GbelowC, $SIXTEENTH)
               Start-Sleep -m $EIGHTH
               [console]::beep($EbelowG, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($A, $EIGHTH)
               [console]::beep($B, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($Asharp, $SIXTEENTH)
               [console]::beep($A, $EIGHTH)
               [console]::beep($GbelowC, $SIXTEENTHDOT)
               [console]::beep($E, $SIXTEENTHDOT)
               [console]::beep($G, $EIGHTH)
               [console]::beep($AHigh, $EIGHTH)
               [console]::beep($F, $SIXTEENTH)
               [console]::beep($G, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($E, $EIGHTH)
               [console]::beep($C, $SIXTEENTH)
               [console]::beep($D, $SIXTEENTH)
               [console]::beep($B, $EIGHTHDOT)
               [console]::beep($C, $EIGHTHDOT)
               [console]::beep($GbelowC, $SIXTEENTH)
               Start-Sleep -m $EIGHTH
               [console]::beep($EbelowG, $EIGHTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($A, $EIGHTH)
               [console]::beep($B, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($Asharp, $SIXTEENTH)
               [console]::beep($A, $EIGHTH)
               [console]::beep($GbelowC, $SIXTEENTHDOT)
               [console]::beep($E, $SIXTEENTHDOT)
               [console]::beep($G, $EIGHTH)
               [console]::beep($AHigh, $EIGHTH)
               [console]::beep($F, $SIXTEENTH)
               [console]::beep($G, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($E, $EIGHTH)
               [console]::beep($C, $SIXTEENTH)
               [console]::beep($D, $SIXTEENTH)
               [console]::beep($B, $EIGHTHDOT)
               Start-Sleep -m $EIGHTH
               [console]::beep($G, $SIXTEENTH)
               [console]::beep($Fsharp, $SIXTEENTH)
               [console]::beep($F, $SIXTEENTH)
               [console]::beep($Dsharp, $EIGHTH)
               [console]::beep($E, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($GbelowCSharp, $SIXTEENTH)
               [console]::beep($A, $SIXTEENTH)
               [console]::beep($C, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($A, $SIXTEENTH)
               [console]::beep($C, $SIXTEENTH)
               [console]::beep($D, $SIXTEENTH)
               Start-Sleep -m $EIGHTH
               [console]::beep($G, $SIXTEENTH)
               [console]::beep($Fsharp, $SIXTEENTH)
               [console]::beep($F, $SIXTEENTH)
               [console]::beep($Dsharp, $EIGHTH)
               [console]::beep($E, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($CHigh, $EIGHTH)
               [console]::beep($CHigh, $SIXTEENTH)
               [console]::beep($CHigh, $QUARTER)
               [console]::beep($G, $SIXTEENTH)
               [console]::beep($Fsharp, $SIXTEENTH)
               [console]::beep($F, $SIXTEENTH)
               [console]::beep($Dsharp, $EIGHTH)
               [console]::beep($E, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($GbelowCSharp, $SIXTEENTH)
               [console]::beep($A, $SIXTEENTH)
               [console]::beep($C, $SIXTEENTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($A, $SIXTEENTH)
               [console]::beep($C, $SIXTEENTH)
               [console]::beep($D, $SIXTEENTH)
               Start-Sleep -m $EIGHTH
               [console]::beep($Dsharp, $EIGHTH)
               Start-Sleep -m $SIXTEENTH
               [console]::beep($D, $EIGHTH)
               [console]::beep($C, $QUARTER)
         }

         #Set Speed and Tones
         If ($CHigh -eq $null)
         {
               $WHOLE = 2200
               $HALF = $WHOLE / 2
               $QUARTER = $HALF / 2
               $EIGHTH = $QUARTER / 2
               $SIXTEENTH = $EIGHTH / 2
               $EIGHTHDOT = $EIGHTH + $SIXTEENTH
               $QUARTERDOT = $QUARTER + $EIGHTH
               $SIXTEENTHDOT = $SIXTEENTH + ($SIXTEENTH / 2)

               $REST = 37
               $EbelowG = 164
               $GbelowC = 196
               $GbelowCSharp = 207
               $A = 220
               $Asharp = 233
               $B = 247
               $C = 262
               $Csharp = 277
               $D = 294
               $Dsharp = 311
               $E = 330
               $F = 349
               $Fsharp = 370
               $G = 392
               $Gsharp = 415
               $AHigh = 440
               $CHigh = 523
         }

         Play-MarioIntro
         Play-MarioIntro2

      }
   ```

2. Source is maintained under [gwMisc](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Start-MarioThemeSong.ps1)