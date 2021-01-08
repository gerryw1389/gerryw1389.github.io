---
title: WSL Tweaks
date: 2019-06-21T01:56:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/wsl-tweaks/
categories:
  - Linux
tags:
  - Tweaks
---
<!--more-->

### Description:

The following is a list of modifications I made to the Windows Subsystem for Linux on my W10 box in my testlab:

### To Resolve:

1. Suppress the MOTD (Message of the day prompt) for when I ssh into the box:

   ```shell
   sudo su
   touch ~/.hushlogin
   #sudo run-parts /etc/update-motd.d/
   ```

   - Gets rid of:

   ```escape
   Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.4.0-17134-Microsoft x86_64)

   * Documentation:  https://help.ubuntu.com
   * Management:     https://landscape.canonical.com
   * Support:        https://ubuntu.com/advantage

   System information as of Wed May  8 14:31:38 DST 2019

   System load:    0.52      Memory usage: 35%   Processes:       10
   Usage of /home: unknown   Swap usage:   0%    Users logged in: 0

   => There were exceptions while processing one or more plugins. See
      /var/log/landscape/sysinfo.log for more information.


   Get cloud support with Ubuntu Advantage Cloud Guest:
      http://www.ubuntu.com/business/services/cloud

   4 packages can be updated.
   0 updates are security updates.



   The programs included with the Ubuntu system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
   applicable law.
   ```

2. Create shortcut.txt as a reference for when I run updates. Need to learn me some aliases someday.

   ```shell
   sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'
   ```

3. Edit ~/.vimrc

   - add `colo desert`
   - add `syntax on`
   - add `set background=dark`

4. Edit ~/.inputrc

   - add `set bell-style none` - see [here](https://stackoverflow.com/questions/36724209/disable-beep-of-linux-bash-on-windows-10) how this doesn't help much

5. Edit ~/.bashrc

   - add `cd /mnt/c/scripts/` to the bottom
   - add the following to the bottom:

   ```escape
   LS_COLORS='rs=0:di=1;35:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:';
   export LS_COLORS
   ```

6. I have recently included these in a [bash_aliases](https://automationadmin.com/2020/09/bash-aliases) post.