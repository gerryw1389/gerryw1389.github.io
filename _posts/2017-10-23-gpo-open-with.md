---
title: 'GPO: Open With'
date: 2017-10-23T17:04:25+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/gpo-open-with/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow this post to create a GPO that allows certain extensions to open in Notepad

### To Resolve:

1. Create a GPO and navigate to: `User Configuration\Preferences\Control Panel Settings\Folder Options` 

   ```escape
   New, Open With
   Action: Update  
   File Extension: vbs (note that there is no dot, just the extension)  
   Associated Programs: c:\windows\system32\notepad.exe  
   Check Set as default button  
   I have .hta, .jar, .jre, .js, .jse, .scr, .vbs on my policy
   ```