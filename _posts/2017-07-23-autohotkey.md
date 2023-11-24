---
title: AutoHotkey
date: 2017-07-23T05:03:47+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/autohotkey/
tags:
  - LocalSoftware
---
<!--more-->

### Description:

So I downloaded a game from Steam the other day and it was driving me crazy that the game kept kicking me out do to certain keyboard combos. I downloaded AutoHotkey and added it to my [QuickCliq](https://automationadmin.com/2017/07/quickcliq-config/) setup so I can then launch before I start gaming.

### To Resolve:

1. AutoHotkey files are as simple is creating a file with the extension of .ahk.

2. Here is the one I created for when I'm gaming:

   ```escape
   ; Disable Alt+Tab
   !Tab::Return

   ; Disable Windows Key + Tab
   #Tab::Return

   ; Disable Left Windows Key
   LWin::Return

   ; Disable Right Windows Key
   RWin::Return

   ; disable ALT+F4
   !F4:: return

   ; disable ALT+ESC
   !Escape:: return

   ; disable CTRL+ESC
   ^Escape:: return

   ; disable ALT+Q
   !q:: return
   ```