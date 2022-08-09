---
title: 'Developing Python On Windows With WSL'
date: 2020-06-08T14:00:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2020/06/developing-python-on-windows-wsl
categories:
  - Linux
  - Windows
tags:
  - Scripting-Python
  - NoteTaking
---
<!--more-->

### Description:

This post describes how I started developing python scripts using vscode on Windows but using WSL under the hood for linux development tasks. See my [dot files post](https://automationadmin.com/2022/01/dot-files) for some references to these settings.

### To Resolve:

1. Following Microsoft's [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl) ... :
   - Install [WSL](https://automationadmin.com/2017/09/windows-subsystem-for-linux-wsl/)
   - Sign into your distro, create a user, run `apt-get update -y && apt-get upgrade -y`
   - Install vscode on Windows
   - Install [Remote Development extensions](https://code.visualstudio.com/docs/remote/wsl) on Windows
   - Inside vscode, run `wsl` and then `code .` and it will install a bunch of stuff in your Ubunutu system
   - Inside vscode (which is in Ubuntu now after previous code . command) run `sudo apt-get install python3-pip`
   - Create a python script and put shebang at top `#!/usr/bin/python3` and run it. It will say something about installing a linter and since we installed pip it will install it - I chose `pylint` and `autopep8`
   - Now add a few more lines and do the `ctrl+shift+f` thing and it should auto format your code

2. Next, in WSL type `vi ~/.bashrc` and add to the bottom of the file `cd /mnt/q/google/scripts/python`. This will set it to where everything I do will sync with Google so I can pick up on any computer I have Backup and sync installed.

   - Also, if you have a [settings.json](https://github.com/gerryw1389/misc/blob/main/vscode/settings-sync.json), I would sync it to your WSL machine.
   - Note that this file will be highly modified because I didn't install half the extensions I use in my Windows vscode.

3. A few things I noticed:

   - For a folder rename error: `'/mnt/q/google/scripts/python/z_python/plex-backup' => '/mnt/q/google/scripts/python/z_python/current' Error: EACCES: permission denied, rename `, I fixed by setting one of my settings.json lines to `remote.WSL.fileWatcher.polling to true`

   - For no pip: `There is no Pip installer available in the selected environment`, I found the path to the WSL extension and added `pip install --upgrade pip` on the end: `/usr/bin/python3 /home/myuser/.vscode-server/extensions/ms-python.python-2020.5.86806/pythonFiles/pyvsc-run-isolated.py pip install --upgrade pip`
