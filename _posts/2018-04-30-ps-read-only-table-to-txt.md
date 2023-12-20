---
title: 'PS: Read Only Table To TXT'
date: 2018-04-30T03:32:44+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-read-only-table-to-txt/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So the other day I was going through a web GUI for our Exchange and needed to edit the list, but the form was read only. No problem => use Powershell to get it to a TXT I can manipulate!

### To Resolve:

1. Uggh, can't select the cells. Can't copy/paste or anything!
   - ![ps-read-only-table-to-txt-1](https://automationadmin.com/assets/images/uploads/2018/04/ps-read-only-table-to-txt-1.png){:class="img-responsive"}

2. Wait a minute, Ctrl+U => Select source
   - ![ps-read-only-table-to-txt-2](https://automationadmin.com/assets/images/uploads/2018/04/ps-read-only-table-to-txt-2.png){:class="img-responsive"}

3. Paste that into a text file. Now just run my [Get-ExtractedEmailAddresses](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Get-ExtractedEmailAddresses.ps1) script so I can get only the emails from this block of HTML. Result:
   - ![ps-read-only-table-to-txt-3](https://automationadmin.com/assets/images/uploads/2018/04/ps-read-only-table-to-txt-3.png){:class="img-responsive"}

4. But there is double of everything! No problem, just open up Powershell and run:

   ```powershell
   Gc .\extracted.txt | sort -unique | out-file .\sorted.txt
   ```

5. Done!
   - ![ps-read-only-table-to-txt-4](https://automationadmin.com/assets/images/uploads/2018/04/ps-read-only-table-to-txt-4.png){:class="img-responsive"}