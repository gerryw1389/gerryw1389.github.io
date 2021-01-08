---
title: Plex Media Server To Emby
date: 2018-04-30T03:24:08+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/plex-media-server-to-emby/
categories:
  - Linux
  - Networking
tags:
  - TestLab
---
<!--more-->

### Description:

Just for testing, I cloned by Plex VM and wanted to move my media over Emby. Follow these steps:

### To Resolve:

1. Delete the old Plex data:

   ```powershell
   sudo systemctl stop plexmediaserver
   sudo rpm -e plexmediaserver
   sudo rm -rf /var/lib/plexmediaserver
   sudo userdel plex
   ```

1. Install Emby:

   ```powershell
   yum install https://github.com/MediaBrowser/Emby.Releases/releases/download/3.3.1.0/emby-server-rpm_3.3.1.0_x86_64.rpm
   # Open a web browser to http://localhost:8096
   ```

1. Add my movies directory => worked perfectly!