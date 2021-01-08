---
title: To Create Shortcuts In Linux
date: 2016-10-07T03:17:36+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/to-create-shortcuts-in-linux/
categories:
  - Linux
tags:
  - LinuxServer
  - VirtualizationSoftware
---
<!--more-->

### Description:

This may seem like a trivial post, but until I get more of them and can aggregate them up into a single post, I will go ahead and make it a separate post. So follow this to create a shortcut in Linux.

### To Resolve:

1. Generally, you can just type &#8220;ln -s (source) (destination)&#8221;. For my example, I wanted to create a shortcut for a &#8220;shared folder&#8221; in Virtualbox between host machine and Centos.

2. Open terminal, type:

   ```shell
   ln -s /media/sf_G_DRIVE/linux /home/gerry/linux
   ```

   - In this example, my shared folder was named &#8220;sf\_G\_DRIVE&#8221; and my user was &#8220;gerry&#8221;

3. To place a desktop shortcut for Firefox: Right click on the desktop and create a new file or run &#8220;touch firefox.desktop&#8221; and then &#8220;vi firefox.desktop&#8221; and place in:

   ```shell
   #!/usr/bin/env xdg-open

   [Desktop Entry]
   Version=1.0
   Encoding=UTF-8
   Name=Firefox Web Browser
   Exec=firefox %u -new-tab https://docs.google.com/document/d/1Aq6FSCy66y8Ee-yuLNeAHh32SKEq_mS_rEHkJ8nM7Yc/edit
   Icon=firefox
   Terminal=false
   Type=Application
   StartupWMClass=Firefox-bin
   MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;
   StartupNotify=true
   X-Desktop-File-Install-Version=0.15
   Categories=Network;WebBrowser;
   ```

4. Save as: Firefox.desktop