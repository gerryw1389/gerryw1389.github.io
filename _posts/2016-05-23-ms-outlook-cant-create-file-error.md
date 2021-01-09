---
title: 'MS Outlook: Cant Create File Error'
date: 2016-05-23T12:58:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-outlook-cant-create-file-error/
categories:
  - LocalSoftware
tags:
  - MSOffice
  - Regedit
---
<!--more-->

### Description:

Follow these steps if Outlook generates a message saying `Can't Create File: (Document).pdf...`. This happens because the temp directory that Outlook uses is full to Outlook.

### To Resolve:

1. Run => regedit => At the top select edit - Find => Type: OutlookSecureTempFolder

2. This tells you where the temp files are stored, browse to the path using Windows Explorer and delete all the files in that directory. Repeat the steps if the issue still occurs as there may be many directories each with "Random" endings usually found in `C:\Users\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.Outlook\*Random*`.

### References:

["How to: MS Outlook Attachment Error – Cannot create file"](https://community.spiceworks.com/how_to/1776-ms-outlook-attachment-error-cannot-create-file)