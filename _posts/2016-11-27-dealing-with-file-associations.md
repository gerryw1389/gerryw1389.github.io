---
title: Dealing With File Associations
date: 2016-11-27T07:09:29+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/dealing-with-file-associations/
tags:
  - Windows
---
<!--more-->

### Description:

File associations are extensions that tell Windows which programs will open a file. For example, a file called &#8220;test.docx&#8221; will open with MS Word by default because when Word installed, it told Windows that all files with .docx belong to it and should open with it. This normally isn't a big issue, but with Windows 10 => it tries to set everything to it's built in crappy apps and even if you change them => it will reset them in future updates (since they are forced). Follow these steps to clear file associations.

### To Resolve:

1. First, try downloading and running [Default Programs Editor](https://defaultprogramseditor.com/). It's free and doesn't install, does the trick everytime.

2. If you prefer the native way of doing things, you have a couple options:

   - You can create a notepad document on your desktop and do a file => save as => whateverYouWant.WhateverMade up extension you want that doesn't exist. Then on the association you want to get rid of, you have Windows open it using the notepad document you just created. Then you delete that document.

   - Example: I want to get rid of the &#8220;reader&#8221; app from opening PDF's. I create a file called &#8220;blah.zl;kfjdlak;j&#8221; on my desktop. I then right click a PDF => Open With => Point to the file I just created. Once that's done, I delete the file. Now Windows won't know what to do with that file type.

   - You can run Regedit and go to the HKEY_CLASSES_ROOT and poke around there, but I strongly suggest step 1.