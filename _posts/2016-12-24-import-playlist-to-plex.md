---
title: Import Playlist To Plex
date: 2016-12-24T07:19:05+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/import-playlist-to-plex/
tags:
  - LocalSoftware
tags:
  - MediaEditing
---
<!--more-->

### Description:

So I have been using Plex as my media server for over a month now and it just drives me crazy that I cannot import my playlist from MediaMonkey. I started looking for a solution and finally found one, a python script I could run to fix it!

### To Resolve:

1. Newer version (Plex can be running).

   ```shell
   cd /home/gerry
   yum install git -y

   # clone repo
   git clone https://github.com/dakusan/PlexPlaylistImporter.git
   cd PlexPlaylistImporter/

   # run script that imports '/mnt/music/playlists/5-star-trance.m3u' to playlist called 'trance'
   chmod +x ./PlexPlaylistImporter.py

   ./PlexPlaylistImporter.py -p /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-in\ Support/Databases/com.plexapp.plugins.library.db /mnt/music/playlists/5-star-trance.m3u trance
   ```

   - You will either get:

   ```escape
   success
   134 items added
   ```

   - or something like:


   ```shell
   ./PlexPlaylistImporter.py -p /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-in\ Support/Databases/com.plexapp.plugins.library.db /mnt/data/data/my-music/linux-playlists/z-rock-n-roll.m3u z-rock-n-roll
   ListImporter 'Winamp playlist': Cannot find file listed in playlist (must be relative to the playlist): ../music-library/acdc--back-in-black.mp3
   ```

   - The fix is to go to your music library and make sure that file exists with that name.


2. Older version of this article:
   - Get script at [PlexPlaylistImporter](https://github.com/dakusan/PlexPlaylistImporter)

   - On my CentOS 7 VM, I had to install python:

   ```shell
   sudo yum install epel-release  
   sudo yum install python34  
   curl -O https://bootstrap.pypa.io/get-pip.py  
   sudo /usr/bin/python3.4 get-pip.py
   ```

   - When I ran the script, it asked me for the full media library path. According to the guide I was able to find it at:

   ```shell
   /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-in\ Support/Databases/com.plexapp.plugins.library.db
   ```

   - I then had to point it to my media library path where the .m3u files were:  

   ```shell
   /share/my-music/my-playlists/playlist-name.m3u
   ```

   - Lastly, since I use Windows, I had to convert `\` to `/`

   ```shell
   sudo pluma playlist-name.m3u  
   # find and replace
   Ex: (Navigate to script dir)
   ./PlexPlaylistImporter.py -p /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-in\ Support/Databases/com.plexapp.plugins.library.db /my-share/my-music/my-playlists/dubstep.m3u
   ```

   - If you get the error `DB Error: unable to open database file` try prefacing the command with sudo.