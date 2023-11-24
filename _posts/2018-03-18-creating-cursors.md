---
title: Creating Cursors
date: 2018-03-18T14:36:20+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/creating-cursors/
tags:
  - Windows
tags:
  - Tweaks
---
<!--more-->

### Description:

So if you ever want to create a cursor theme, follow these steps (or something similar).

### To Resolve:

1. Go to Deviantart.com and download a couple themes. In this example, I'm going to use: [DIM v3.2 - NitroGreen](https://blooguy.deviantart.com/art/DIM-v3-1-NitroGreen-578318821) and [Oxygen Cursors](https://lavalon.deviantart.com/art/Oxygen-Cursors-76614092)

2. Create different file names for different cursors and manually create a INI file that has something like the following:

   ```powershell
   [Version]
   signature="$CHICAGO$"

   [DefaultInstall]
   CopyFiles = Scheme.Cur, 
   AddReg    = Scheme.Reg

   [DestinationDirs]
   Scheme.Cur = 10,"%CUR_DIR%"
   Scheme.Txt = 10,"%CUR_DIR%"

   [DestinationDirs]
   Scheme.Cur = 10,"%CUR_DIR%"
   Scheme.Txt = 10,"%CUR_DIR%"

   [Scheme.Reg]
   HKCU,"Control Panel\Cursors\Schemes","%SCHEME_NAME%",,"%10%\%CUR_DIR%\%pointer%,%10%\%CUR_DIR%\%help%,%10%\%CUR_DIR%\%work%,%10%\%CUR_DIR%\%busy%,%10%\%CUR_DIR%\%cross%,%10%\%CUR_DIR%\%Text%,%10%\%CUR_DIR%\%Hand%,%10%\%CUR_DIR%\%unavailiable%,%10%\%CUR_DIR%\%Vert%,%10%\%CUR_DIR%\%Horz%,%10%\%CUR_DIR%\%Dgn1%,%10%\%CUR_DIR%\%Dgn2%,%10%\%CUR_DIR%\%move%,%10%\%CUR_DIR%\%alternate%,%10%\%CUR_DIR%\%link%"

   ; -- Common Information

   [Scheme.Cur]
   gw-normal.ani
   gw-help.ani
   gw-background.ani
   gw-busy.ani
   gw-text.cur
   gw-unavail.ani
   gw-vertical.ani
   gw-horiz.ani
   gw-diag.ani
   gw-diag2.ani
   gw-move.ani
   gw-link.ani
   gw-precision.ani
   gw-hand.ani
   gw-alt-select.ani

   [Strings]
   CUR_DIR       = "Cursors\gw"
   SCHEME_NAME   = "gw"
   pointer       = "gw-normal.ani"
   help          = "gw-help.ani"
   work          = "gw-background.ani"
   busy          = "gw-busy.ani"
   text          = "gw-text.cur"
   unavailiable  = "gw-unavail.ani"
   vert          = "gw-vertical.ani"
   horz          = "gw-horiz.ani"
   dgn1          = "gw-diag.ani"
   dgn2          = "gw-diag2.ani"
   move          = "gw-move.ani"
   link          = "gw-link.ani"
   cross         = "gw-precision.ani"
   hand          = "gw-hand.ani"
   alternate     = "gw-alt-select.ani"
   ```

3. How I created the theme above was to:

   - Mix and match different files from different downloads into a new folder. Create a &#8220;work&#8221;, &#8220;help&#8221;, &#8220;alternate&#8221;, etc. ANI files => one of each.

   - Now just edit the INI file that users right click to install and make sure to change the file names to the new file names and give your theme a name => I chose `gw`.

   - If install isn't an option, type `rundll32 syssetup,SetupInfObjectInstallAction DefaultInstall 128 .\install.inf` from cmd. It will say install failed, but it works.

   DISCLAIMER: DO NOT DISTRIBUTE YOUR FINAL PRODUCT! This is most likely a violation of TOS and I will not be held accountable.
   {: .notice--danger}

4. This is for testing only and should be deleted once completed. The whole point is to understand how cursors can be created and distributed if you know how to create custom ANI files.
