---
title: 'W10: EsifAssist64 Has Stopped Working'
date: 2018-03-23T23:49:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/w10-esifassist64-has-stopped-working/
tags:
  - Windows
---
<!--more-->

### Description:

Upon updating W10 to v1709, you will get an application that says `esif\_assist\_64.exe has stopped working`. Your cursor will then turn to `busy` every couple seconds indefinitely.

### To Resolve:

1. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `C:\windows\temp` => Ctrl+A => Shift+Delete => Skip any in use.

2. If you didn't understand that, it means delete everything from `Windows\Temp` except for files that are in use. Then click close program, it should go away.

3. Sometimes I had to kill the process in the process manager `esif\_something` then I could delete `c:\windows\temp\dptf\esif\_assist_64.exe`

<img class="alignnone wp-image-5295 size-full" src="https://automationadmin.com/assets/images/uploads/2018/03/esif.jpg" alt="" width="1653" height="592" srcset="https://automationadmin.com/assets/images/uploads/2018/03/esif.jpg 1653w, https://automationadmin.com/assets/images/uploads/2018/03/esif-300x107.jpg 300w, https://automationadmin.com/assets/images/uploads/2018/03/esif-768x275.jpg 768w, https://automationadmin.com/assets/images/uploads/2018/03/esif-1024x367.jpg 1024w" sizes="(max-width: 1653px) 100vw, 1653px" />