---
title: Phone Not Showing In Media Monkey
date: 2021-06-11T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/06/media-monkey-phone-not-showing
categories:
  - LocalSoftware
tags:
  - MediaEditing
---
<!--more-->

### Description

So I got tired of following my post on how to update [Plex Playlists](https://automationadmin.com/2016/12/import-playlist-to-plex/) and decided to just download the Media Monkey app on my phone and use that to listen to music locally. The problem was, I couldn't get my phone to show up as a device in Media Monkey! I eventually found the fix according to [this thread](https://www.mediamonkey.com/forum/viewtopic.php?f=12&t=95385). Thank god for the internet!

### To Resolve:

1. Go to Device Manager (win+r => devmgmt.msc)

2. Find your phone under "Portable Devices"

3. Choose to "Pick a Driver" and point to the second one instead of the first and it should allow your phone to show up in Windows Explorer properly.
