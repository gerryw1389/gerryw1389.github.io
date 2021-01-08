---
title: 'MS Office: Installation Issues'
date: 2016-05-23T18:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-office-installation-issues/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

Some people have issues installing MS Office getting random errors with the installer. When this happens, try these steps.

  <img class="alignnone size-full wp-image-677" src="https://automationadmin.com/assets/images/uploads/2016/09/ms-office-installation-issue.png" alt="ms-office-installation-issue" width="800" height="450" srcset="https://automationadmin.com/assets/images/uploads/2016/09/ms-office-installation-issue.png 800w, https://automationadmin.com/assets/images/uploads/2016/09/ms-office-installation-issue-300x169.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/ms-office-installation-issue-768x432.png 768w" sizes="(max-width: 800px) 100vw, 800px" />


### To Resolve:

1. Turn off Windows Firewall and reboot the computer.

2. After installation, if you are having issues getting it registered, try restarting the `DNS Client` service using `services.msc`.

3. Try these steps: Run => `regedit` => navigate to, export, and delete:

   - `HKEY_LOCAL_MACHINE\Software\Microsoft\Office\15.0`
   - `HKEY_CURRENT_USER\Software\Microsoft\Office\15.0`

4. Sign in to your MS account page and click on the &#8220;Install&#8221; button to reinstall MS Office. Alternatively, you can use the disc that came with MS Office when you purchased it if applicable.