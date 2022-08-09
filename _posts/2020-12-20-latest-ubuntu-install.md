---
title: Latest Ubuntu Install Notes
date: 2020-12-20T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/latest-ubuntu-install
categories:
  - Linux
tags:
  - Scripting-Bash
  - VersionControl
---
<!--more-->

### Description:

Notes on latest ubuntu install

### To Resolve:

1. First, install vscode via `Software` app which will install it as a snap application. Add the icon to the dock as a favorite.

2. Setup sync

   ```shell
   mkdir ~/git
   cd ~/git
   mkdir my-repo
   cd my-repo
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ssh-add ~/.ssh/id_rsa
   cat ~/.ssh/id_rsa.pub
   Add the ssh key to your github account.
   Clone the repo by the following:
   git config --global user.name 'Gerry Williams'
   git config --global user.email 'your_email@domain.com'
   git clone git@github.com:gerryw1389/my-repo.git
   ```

3. Install [extensions](https://github.com/gerryw1389/misc/blob/main/vscode/install-extensions.ps1)
  

4. Since my repo has my `settings.json` for vscode, just copy and paste those (which will update `$HOME/.config/Code/User/settings.json`)

   - Then save as `~/git/default.code-workspace`

5. So this all works well except for one thing - every time I click the icon to lauch `code`, it opens a new window instead of my workspace

   - On Windows, this would be as easy as modifying the properties to `code name-of-workspace.code-workspace` so how to do this on Ubuntu?
   - First, I tried seeing where the icon actually is? `sudo find / -name "code*.desktop" -type f`. This gave me 4 files but the one that looked most interesting is `/snap/code/52/snap/gui/code.desktop`
   - From there, I googled `ubuntu change /snap/code/52/snap/gui/` which led me [here](https://askubuntu.com/questions/1278025/how-to-change-the-icons-of-snap-programs)
   - Following that I did:

   ```shell
   cd /var/lib/snapd/desktop/application/
   ls -la
   # found something called code_code.desktop
   cp ./code_code.desktop /home/gerry/.local/share/applications/code_code.desktop
   ```

   - Now just modify it:

   - Remove the `Exec=env BAMF_DESKTOP_FILE_HINT=/var/lib/snapd/desktop/applications/code_code.desktop /snap/bin/code --force-user-env --no-sandbox --unity-launch %F` stuff
   - And the action at the bottom
   - Add in my workspace
   - Result should be like:

   ```escape
   [Desktop Entry]
   X-SnapInstanceName=code
   Name=Visual Studio Code
   Comment=Code Editing. Redefined.
   GenericName=Text Editor
   Exec=/snap/bin/code /home/gerry/git/default.code-workspace
   Icon=/snap/code/52/meta/gui/com.visualstudio.code.png
   Type=Application
   StartupNotify=false
   StartupWMClass=Code
   Categories=Utility;TextEditor;Development;IDE;
   MimeType=text/plain;inode/directory;application/x-code-workspace;
   Keywords=vscode;
   ```

6. Launch vscode and it works like on Windows. Good deal. Now to add my six other repos...