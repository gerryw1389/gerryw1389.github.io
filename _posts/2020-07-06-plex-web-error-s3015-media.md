---
title: 'Plex Web Error: s3015 (Media)'
date: 2020-07-06T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/plex-web-error-s3015-media
tags:
  - LocalSoftware
tags:
  - MediaEditing
---
<!--more-->

### Description:

When listening to music, I would randomly get an error:

   ```escape
   Error: s3015 (Media)
   An error occurred trying to play "Sun In Your Eyes".

   On the server I would run `cat /var/log/...plexmediaserver.log` and get: 
   Line 8787: Jul 13, 2020 09:41:38.453 [0x7ff6a0ff9700] DEBUG - MDE: Sun In Your Eyes: Direct Play is disabled
   Line 8788: Jul 13, 2020 09:41:38.453 [0x7ff6a0ff9700] DEBUG - MDE: Sun In Your Eyes: media must be transcoded in order to use the dash protocol
   Line 8789: Jul 13, 2020 09:41:38.453 [0x7ff6a0ff9700] DEBUG - MDE: Sun In Your Eyes: no direct play music profile exists for http/mp3/mp3
   Line 8790: Jul 13, 2020 09:41:38.453 [0x7ff6a0ff9700] DEBUG - MDE: Sun In Your Eyes: selected media 0 / 41468
   Line 8806: Jul 13, 2020 09:41:38.539 [0x7ff67dffb700] DEBUG - [Universal] Using local file path instead of URL: /mnt/data/data/my-music/music-library/Above & Beyond/all-music/Sun In Your Eyes.mp3
   ```

But this doesn't make sense because I always have Direct Play enabled and Plex plays mp3's just fine so it shouldn't be saying it needs an encoder for it...

### To Resolve:

1. Took a while to find the culprit, but the fix was to close MediaMonkey according to [this](https://forums.plex.tv/t/error-code-s3015-media/232256/33) post. This is due to the output driver defaulting to 'exclusive mode'.
