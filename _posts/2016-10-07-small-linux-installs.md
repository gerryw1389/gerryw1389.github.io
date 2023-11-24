---
title: Small Linux Installs
date: 2016-10-07T04:18:01+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/small-linux-installs/
tags:
  - Linux
tags:
  - Tweaks
---
<!--more-->

### Description:

I plan to use this page as a reference for small programs I like to install on my distro's for everyday use or just to mess around with. For now, my copy paste is:

   ```shell
   sudo dnf install nmap bleachbit p7zip vlc
   ```

### To Resolve:

1. Install specific programs

   ```shell
   # Network scanner
   sudo dnf install nmap 

   # Cleaner
   sudo dnf install bleachbit 

   # I like to run it once via GUI and then you can run the following from the terminal
   bleachbit -c --preset

   #As with almost any command, type bleachbit -h or --help to get a list of full options.

   # 7zip
   sudo dnf install p7zip

   # Media player
   sudo dnf install vlc

   # Play games
   sudo dnf install steam

   # Virtualize
   sudo dnf install VirtualBox

   # Good for customizing your GRUB menu at boot
   sudo dnf install grub-customizer
   ```

2. Next, to move from MediaMonkey on Windows, we install an application called Clementine

   - Install media codecs (Fedora in this case)

   ```shell
   sudo dnf install gstreamer-plugins-bad gstreamer-plugins-bad-free-extras gstreamer-plugins-bad-nonfree gstreamer-plugins-ugly gstreamer-ffmpeg gstreamer1-libav gstreamer1-plugins-bad-free-extras gstreamer1-plugins-bad-freeworld gstreamer1-plugins-base-tools gstreamer1-plugins-good-extras gstreamer1-plugins-ugly gstreamer1-plugins-bad-free gstreamer1-plugins-good gstreamer1-plugins-base gstreamer1
   ```

   - Install Clementine:

   ```shell
   sudo dnf install clementine
   ```

   - Audio was too quiet. I had all the volumes up on max and it was still quiet. To Fix, open a terminal and type: `alsamixer`
     - Type: F6  
     - Choose your device and press up. It was set to 20% for some reason.  
     - Some songs still wouldn't play, you may have to install &#8220;gstreamer-0\_10-fluendo-mp3&#8221; and &#8220;gstreamer-0\_10-plugins-good&#8221;

3. To install Windows applications, install a program called &#8220;WINE&#8221; to emulate Windows. I will probably post more on this at a later date.

4. Install other DE's (desktop environments)

   ```shell
   sudo dnf install @mate-desktop
   sudo dnf install @xfce-desktop
   sudo dnf install @lxde-desktop
   sudo dnf install @cinnamon-desktop
   ```

