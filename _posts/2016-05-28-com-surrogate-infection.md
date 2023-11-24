---
title: COM Surrogate Infection
date: 2016-05-28T06:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/com-surrogate-infection/
tags:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

Lately there have been reports of viruses that do not infect the file system except by dumping huge amounts of files in the %temp% directory. Follow these steps to remove the infection. Initial complaints from end users will be that the computer is so slow they cannot open anything.

### To Resolve:

1. Find out if you have this particular infection by running `taskmgr.msc`. Processes running will look like legitimate processes but will not be. Examples include: COM Surrogate, CTF Loader, Windows Picture Acquision Wizard, ect. (see screenshot below).

  <img class="alignnone size-full wp-image-624" src="https://automationadmin.com/assets/images/uploads/2016/09/com-surrogate-infection.jpg" alt="com-surrogate-infection" width="910" height="673" srcset="https://automationadmin.com/assets/images/uploads/2016/09/com-surrogate-infection.jpg 910w, https://automationadmin.com/assets/images/uploads/2016/09/com-surrogate-infection-300x222.jpg 300w, https://automationadmin.com/assets/images/uploads/2016/09/com-surrogate-infection-768x568.jpg 768w" sizes="(max-width: 910px) 100vw, 910px" />

2. After doing a bit of searching, I found that if you run ESET Poweliks Cleaner (found [here](http://support.eset.com/kb3587/?&page=content&id=SOLN3587)), it will target this infection and remove it. You just need to reboot afterwards.