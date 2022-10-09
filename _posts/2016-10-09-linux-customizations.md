---
title: Linux Customizations
date: 2016-10-09T15:28:45+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/linux-customizations/
categories:
  - Linux
tags:
  - Tweaks
---
<!--more-->

### Description:

This page is just for reference. See my [dot files post](https://automationadmin.com/2022/01/dot-files) for some references to these settings.

### For Mate:

1. First, I always install the MATE Desktop Environment. Go to Control Center, Appearance => BlackMATE

2. Setup keyboard shortcuts = Keyboard Shortcuts, add:

   - Under Desktop:  
   - `Mod4+E` = Home folder  
   - `Mod4+R` = Open a terminal

   - Under Custom Shortcuts:  
   - `Print` = Shutter (shutter -s -C) # must install shutter first  
   - `Shift+Control+Esc` = System Monitor (/usr/bin/mate-system-monitor)

   - Everything else as default. Most Windows keyboard shortcuts port over. The main thing that takes a while to get used to is ALT+F1 for launcher and ALT+F2 for Run.

3. Next go to Control Center => Windows => Placement tab => Check &#8220;Center New Windows&#8221;.

4. Next, I want to configure my Terminal

   - Set it up to have green text on black background.
   - Set it up to where root prompt is red:

   ```shell
   su
   vi /root/.bashrc
   # Add the following line to the end
   PS1='\[\e[31m\][root]\[\e[0m\] \W\$ '
   ```

   - Setup font to &#8220;Liberation Mono Regular&#8221; size &#8220;13&#8221;

5. Setup triple screen displays like I use on my host:

   - First you enable 3 monitors in VirtualBox, and then in the OS, open terminal and type:

   ```shell
   xrander 
   # Take note of which screen to use as primary. For me:
   xrandr --output HDMI-2 --primary
   ```

   - I also needed to pin certain applications to the panels at the top. To do this you add a new panel => right click &#8220;Properties&#8221; => uncheck expand. Drag the panel to where you want it, then right click &#8220;Properties&#8221; and expand. You can then drag launchers to the panel and right click => &#8220;Lock To Panel&#8221;.

6. Setting up login screen:

   ```shell
   # Copy over profile pic and background to their correct places
   sudo cp /home/gerry/Pictures/background.jpg /usr/share/backgrounds
   sudo cp /home/gerry/Pictures/prof.jpg /usr/share/backgrounds
   # Verify after reboot
   ```

7. Lastly, I wanted to take away default desktop icons:  
   - dconf editor  
   - Org => Mate => Caja => Desktop => Uncheck all you don't want
   - For applications, see my [Small Linux Installs](https://automationadmin.com/2016/10/small-linux-installs/)

## For Gnome (Fedora):

1. Set hostname:

   ```shell
   sudo hostnamectl set-hostname MyFedora
   ```

2. Configure static IP:

   ```shell
   sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s3

   # Note the name of you NIC first by looking at it in the network manager. Add:
   BOOTPROTO=static
   ONBOOT=yes
   IPADDR=192.168.1.1
   NETMASK=255.255.255.0
   GATEWAY=192.168.1.1
   DNS1=202.88.131.90
   DNS2=202.88.131.89
   ```

3. Enable RPM Fusion:

   ```shell
   sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
   ```

4. Next, I want to configure my Terminal

   - Set it up to have green text on black background.
   - Set it up to where root prompt is red:

   ```shell
   su
   vi /root/.bashrc
   # Add the following line to the end
   PS1='\[\e[31m\][root]\[\e[0m\] \W\$ '
   ```

5. Next, I want to customize my gnome setup:

   - Install gnome tweak tool:

   ```shell
   sudo dnf install gnome-tweak-tool
   ```

6. First extension to install is &#8220;Dash to Panel&#8221;. To do this, type:

   ```shell
   dnf copr enable region51/chrome-gnome-shell
   dnf install chrome-gnome-shell
   ```

   - You should be able to go to extensions.gnome.org and install now
   - Go to [Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/) and enable it.
   - After enabled, set it to &#8220;bottom&#8221; with icon size of 32, 4 spacing, and activate hotkeys (Win+1 will launch first program, Win+2 will launch second, etc.)

7. For themes, you just have to enable &#8220;user themes = on&#8221; in the tweak tool and then:

   - I want the &#8220;Numix Pack&#8221; so I download the tarball at [NumixPack](https://www.gnome-look.org/p/1137261/)
   - Make sure you can see hidden files then copy the five folders (.config, .icons, .local, .themes, and wallpapers) to your /home/username folder. Say yes to merge.
   - Before we configure the theme, we need to get &#8220;Breeze cursors&#8221;. Go to [Breeze Serie for Righties ](https://www.gnome-look.org/p/999991/) (I like the turquoise but you can pick whatever)
   - Then just extract to your /usr/share/icons folder:

   ```shell
   sudo tar -xzvf Breeze-whatever.tar.gz
   sudo cp -R Breeze-whatever /usr/share/icons/breeze-whatever
   sudo chmod 755 -R /usr/share/icons/breeze-whatever
   ```

   - Open up the tweak tool and set:

     - GTK to: Numix-Dark  
     - Icons: PlateroNumix  
     - Cursor: BreezeTurq  
     - Shell: Numix

   - Finally, you need to run a specific command to enable the cursor to work across all applications (Note I had to reboot afterwards)

   ```shell
   sudo update-alternatives --config x-cursor-theme
   ```

8. Lastly, in addition to regular `dnf install $something` from command line, I just used Firefox to go to chrome.com to download/install Google Chrome and then VS Code the same way. You can browse the internet and download RPM files. Repo would be better though as they are able to weed out malicious links with much more reliability.

9. Will continue this as I tweak my image

