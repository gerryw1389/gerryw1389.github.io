---
title: Windows Customizations
date: 2016-05-28T06:56:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-customizations/
tags:
  - Windows
tags:
  - Tweaks
---
<!--more-->

### Description:

Customizing Windows can mean many things such as certain settings, logon options, etc. In this example, I will go over different UI customizations.

UPDATE: I would instead move to [Windows 10](https://www.deviantart.com/customization/skins/windows/win10/popular-all-time/)

### To Resolve:

1. First, head over to (skinpacks.com is no longer in use) and check out the different theme packs you can download. These contain two files, one of which is a CMD file you run to launch the installer. Upon completion, you are done!

   - Example: Win7Client1 (VM) = Javis

  <img class="alignnone size-full wp-image-631" src="https://automationadmin.com/assets/images/uploads/2016/09/win7client1.jpg" alt="win7client1" width="1920" height="1079" srcset="https://automationadmin.com/assets/images/uploads/2016/09/win7client1.jpg 1920w, https://automationadmin.com/assets/images/uploads/2016/09/win7client1-300x169.jpg 300w, https://automationadmin.com/assets/images/uploads/2016/09/win7client1-768x432.jpg 768w, https://automationadmin.com/assets/images/uploads/2016/09/win7client1-1024x575.jpg 1024w" sizes="(max-width: 1920px) 100vw, 1920px" />

   - Example: Win7Client2 (VM) = Alienware Evolution

  <img class="alignnone size-full wp-image-632" src="https://automationadmin.com/assets/images/uploads/2016/09/win7client2.jpg" alt="win7client2" width="1916" height="1079" srcset="https://automationadmin.com/assets/images/uploads/2016/09/win7client2.jpg 1916w, https://automationadmin.com/assets/images/uploads/2016/09/win7client2-300x169.jpg 300w, https://automationadmin.com/assets/images/uploads/2016/09/win7client2-768x433.jpg 768w, https://automationadmin.com/assets/images/uploads/2016/09/win7client2-1024x577.jpg 1024w" sizes="(max-width: 1916px) 100vw, 1916px" />

2. Themes can be cool at first, but get annoying after a while as certain applications may not display correctly (i.e. contrasting the opposite colors), so you may look into something more subtle like changing your mouse cursor. I personally like the Crystal Clear Mini set you can download [here](http://theblueguy07.deviantart.com/art/Crystal-Clear-v3-1-298678459). These just contain a zip file, you extract and then Right Click => Install on the .INF file for the cursor. Then, Run => `main.cpl` => Select the cursor to apply.

3. Custom icons are a little tricky in that you need to install &#8220;7tsp&#8221; and then launch the 7tsp Source Patcher and drag and drop your zip file into the patcher and then select => start patching. If I recall correctly, you have to reboot twice after it is done. This will change all file and folder icons on the system, so don't say I didn't warn you!

  <img class="alignnone size-full wp-image-621" src="https://automationadmin.com/assets/images/uploads/2016/09/7tsp.jpg" alt="7tsp" width="568" height="472" srcset="https://automationadmin.com/assets/images/uploads/2016/09/7tsp.jpg 568w, https://automationadmin.com/assets/images/uploads/2016/09/7tsp-300x249.jpg 300w" sizes="(max-width: 568px) 100vw, 568px" />

4. After installing the patch, you may want to change or customize your current or future folders by changing their icons. To do this, simply Right Click => Properties => Shortcut tab => Change Icon Button => Point it to: `%SystemRoot%\system32\imageres.dll`. This will get you the new icons instead of the defaults.