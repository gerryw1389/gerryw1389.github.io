---
title: Corrupted Recycle Bin Error
date: 2016-05-18T04:56:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/corrupted-recycle-bin-error/
categories:
  - Hardware
---
<!--more-->

### Description:

You will get a message that says `The Recycle Bin on Drive (whatever) has been corrupted, do you want to delete?` within Windows. This can be caused for many reasons. You see this mostly on external drives. It's usually caused by not safely removing the hardware prior to disconnecting it from the computer. Message is safe to ignore. Delete the contents inside the Recycle Bin.

### To Resolve:

1. Click "Yes" on the error pop up.

2. Run => `control folders` => Show hidden files.

3. Find the `Recycler` folder or `$Recycle.Bin` on whichever drive the error was referring to and delete. It will be automatically recreated.