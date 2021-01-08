---
title: 'Remote Development: wslserver.sh not found'
date: 2020-07-03T16:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/remote-development-wslserver-not-found
categories:
  - Linux
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

When typing `code .` in my vscode instance attached to WSL2, I kept getting:

   ```escape
   [2020-07-03 13:12:37.919] sh: 1: /scripts/wslServer.sh: not found
   [2020-07-03 13:12:37.920] VS Code Server for WSL closed unexpectedly.
   [2020-07-03 13:12:37.920] For help with startup problems, go to
   [2020-07-03 13:12:37.920] https://code.visualstudio.com/docs/remote/troubleshooting#_wsl-tips
   ```

Upon further investigation I found that I could not find `/mnt/c` from within WSL2 so I knew something was up.


### To Resolve:

1. Found [the fix](https://github.com/microsoft/vscode-remote-release/issues/2818) in one of the first searches:

   ```powershell
   wsl.exe --shutdown
   ```

   - This seems to be something to do with Docker running on my host machine. 
