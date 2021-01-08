---
title: 'Sharepoint: Cannot Open List'
date: 2016-08-22T03:42:24+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/sharepoint-cannot-open-list/
categories:
  - WebSoftware
tags:
  - Cloud
---
<!--more-->

### Description:

I had an issue the other day where someone asked me how to move multiple files at once into folders in Sharepoint. The answer is easy, you just &#8220;open in Explorer&#8221; (Library tab => under Connect/Export section) and just use that like you normally would by holding down CTRL on the files and dragging them into a folder. The problem was, I would get an error saying &#8220;Your client does not support opening this list&#8221;

### To Resolve:

1. To fix, You have to use the 32 bit version of IE. To do this, open "My Computer" and go to "C:\Program Files (x86)\Internet Explorer" and launch iexplore.exe from there. That is the 32 bit version of IE.

2. Next, make sure to add (siteURL) to your trusted Intranet sites by going to Internet Options – Security tab – Local Intranet – Sites – Advanced – and finally add the site.