---
title: Bulk Extract Images From Word Documents
date: 2019-09-04T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/bulk-extract-images-from-word-docs/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

Follow these steps to extract images as single files from a Word Document. This comes in real handy when writing blog posts or updating things in Sharepoint as you can copy the text from a Word Document and paste it and then insert the images in the places they need to be for when you need to do multiple files in a hurry.

### To Resolve:

1. Open the Word document, and save as `Web page, filtered`

2. Open `Bulk Rename Utility`. Go to the Web page filtered directory and set the following options:
   - add
     - prefix = `whatever`
   - at pos. = `-1`
   - suffix = `-`
   - numbering = `just check the box`
   - file
     - name = `remove`

3. This will get you: `whatever-1.jpg`, `whatever-2.jpg`, ect.
