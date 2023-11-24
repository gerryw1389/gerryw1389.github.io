---
title: Taking Notes Between Linux and Windows
date: 2016-12-24T08:23:03+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/taking-notes-between-linux-and-windows/
tags:
  - Linux
tags:
  - Tweaks
---
<!--more-->

### Description:

Saving notes between Linux and Windows can be done easily through a client such as Google Drive installed on both machines, Shared Folders through Virtual Box, or a number of methods. I found the easiest to be to just save to Google Docs.

### To Resolve:

1. Create blah.txt on desktop, paste in: 

   ```shell
   #!/usr/bin/env xdg-open
   [Desktop Entry]  
   Version=1.0  
   Encoding=UTF-8  
   Name=Firefox Web Browser  
   Exec=firefox %u -new-tab https://docs.google.com/document/your/link/here  
   Icon=firefox  
   Terminal=false  
   Type=Application  
   StartupWMClass=Firefox-bin  
   MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;  
   StartupNotify=true  
   X-Desktop-File-Install-Version=0.15  
   Categories=Network;WebBrowser;
   ```


1. Save as => Firefox.desktop