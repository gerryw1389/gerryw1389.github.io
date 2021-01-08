---
title: Linux Mint Post Installation Issues
date: 2016-05-26T03:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/linux-mint-post-installation-issues/
categories:
  - Linux
tags:
  - Tweaks
---
<!--more-->

### Description:

After installing Linux Mint with the KDE desktop I did a couple things after install to tweak the OS to my liking.

1. To Get Desktop Icons To Have White Text:

   - Go to /usr/share/themes/Adwaita/gtk-3.0/ and add the following text to the file named gtk.css:

   ```shell
   .nemo-desktop.nemo-canvas-item {
   color: #FFFFFF;
   text-shadow: 1px 1px @desktop_item_text_shadow;
   }
   .nemo-desktop.nemo-canvas-item:selected {
   background-color: alpha(#D64A38, 0.9);
   background-image: none;
   color: #FFFFFF;
   text-shadow: none;
   }
   ```

   - You can replace Adwaita with whatever theme you're using and the color codes to whichever colors you choose (#FFFFFF is for white, which is perfect for me)

2. To Install Cinnamon Along Side KDE:

   - First, get familiar with these 3 packages:  
     - kWIN => desktop manager => wobbly windows/ ect.  
     - Compiz => Desktop manager  
     - Fusion => For multiple desktop environments, you can switch between them.

3. I ran `apt-get install cinnamon`. This will install Cinnamon.

4. After I installed Cinnamon on top of KDE and rebooted, I lost a lot of changes that I had made on the Cinnamon DE (desktop environment) and it would only let me login to my KDE DE.

   - To Fix:  
   - In the KDE DE, I went to Configure Desktop => MDM (login Window section) => and changed the sections that checked the &#8220;Limit Session Output&#8221; and &#8220;Filter the session output&#8221;.

   <img class="alignnone size-medium wp-image-676" src="https://automationadmin.com/assets/images/uploads/2016/09/linux-mint-300x267.png" alt="linux-mint" width="300" height="267" srcset="https://automationadmin.com/assets/images/uploads/2016/09/linux-mint-300x267.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/linux-mint-768x684.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/linux-mint.png 770w" sizes="(max-width: 300px) 100vw, 300px" />


