---
title: 'PS: Read Only Table To TXT'
date: 2018-04-30T03:32:44+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-read-only-table-to-txt/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So the other day I was going through a web GUI for our Exchange and needed to edit the list, but the form was read only. No problem => use Powershell to get it to a TXT I can manipulate!

### To Resolve:

1. Uggh, can't select the cells. Can't copy/paste or anything!

   <img class="alignnone size-full wp-image-5408" src="https://automationadmin.com/assets/images/uploads/2018/04/1.png" alt="" width="782" height="488" srcset="https://automationadmin.com/assets/images/uploads/2018/04/1.png 782w, https://automationadmin.com/assets/images/uploads/2018/04/1-300x187.png 300w, https://automationadmin.com/assets/images/uploads/2018/04/1-768x479.png 768w" sizes="(max-width: 782px) 100vw, 782px" /> 

2. Wait a minute, Ctrl+U => Select source

   <img class="alignnone size-full wp-image-5409" src="https://automationadmin.com/assets/images/uploads/2018/04/2.png" alt="" width="1416" height="478" srcset="https://automationadmin.com/assets/images/uploads/2018/04/2.png 1416w, https://automationadmin.com/assets/images/uploads/2018/04/2-300x101.png 300w, https://automationadmin.com/assets/images/uploads/2018/04/2-768x259.png 768w, https://automationadmin.com/assets/images/uploads/2018/04/2-1024x346.png 1024w" sizes="(max-width: 1416px) 100vw, 1416px" /> 

3. Paste that into a text file. Now just run my [Get-ExtractedEmailAddresses](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Get-ExtractedEmailAddresses.ps1) script so I can get only the emails from this block of HTML. Result:

   <img class="alignnone size-full wp-image-5410" src="https://automationadmin.com/assets/images/uploads/2018/04/3.jpg" alt="" width="265" height="656" srcset="https://automationadmin.com/assets/images/uploads/2018/04/3.jpg 265w, https://automationadmin.com/assets/images/uploads/2018/04/3-121x300.jpg 121w" sizes="(max-width: 265px) 100vw, 265px" /> 

4. But there is double of everything! No problem, just open up Powershell and run:

   ```powershell
   Gc .\extracted.txt | sort -unique | out-file .\sorted.txt
   ```

5. Done!

   <img class="alignnone size-full wp-image-5411" src="https://automationadmin.com/assets/images/uploads/2018/04/4.jpg" alt="" width="288" height="636" srcset="https://automationadmin.com/assets/images/uploads/2018/04/4.jpg 288w, https://automationadmin.com/assets/images/uploads/2018/04/4-136x300.jpg 136w" sizes="(max-width: 288px) 100vw, 288px" />