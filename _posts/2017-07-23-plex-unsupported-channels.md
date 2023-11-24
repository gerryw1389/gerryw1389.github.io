---
title: Plex Unsupported Channels
date: 2017-07-23T04:27:17+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/plex-unsupported-channels/
tags:
  - LocalSoftware
  - Linux
tags:
  - MediaEditing
---
<!--more-->

### Description:

Follow this guide to install Unsupported Channels to Plex.

### To Resolve:

1. First download the web tools: [WebTools](https://github.com/ukdtom/WebTools.bundle/releases/)

2. Unzip the tools to your &#8220;Plug-ins&#8221; directory (usually located at `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins`)

   ```shell
   sudo unzip /tmp/WebTools.bundle.zip -d "$(sudo find / -mount -type d -name Plug-ins)"
   ```

3. Make sure your permissions match other directories around it:

   ```shell
   sudo chown -Rv plex.plex "$(sudo find / -mount -type d -name Plug-ins)"
   ```

4. Sign in to Plex like normal http://serverIP:32400 => Go to Server => Channels => Show Advanced button => Disable compatibility checking

5. Now in a new tab type: http://127.0.0.1:33400

6. Lastly, pick/install apps:

   - Library Updater
   - cCloudTV
   - FMoviesPlus
   - BringThePopcorn
   - g2g.fm
   - SS-Plex