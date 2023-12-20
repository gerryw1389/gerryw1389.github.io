---
title: Shell Scripting Overview
date: 2016-05-30T05:11:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/shell-scripting-overview/
tags:
  - SysAdmin
tags:
  - Bash
---
<!--more-->

### Description:

Shell scripting is the equivalent of using batch scripts in Windows, but for Linux. To begin, you should get familiar with Linux commands.

Try visiting [here](https://community.linuxmint.com/tutorial/view/100), [here](http://www.gnu.org/software/bash/manual/bashref.html#Lists), and [here](http://tldp.org/LDP/abs/html/index.html) then moving on to further readings. Try reading this for more actual scripting after learning the basics. My last couple jobs have been primarily Windows networks so I haven't gotten too far into Linux beyond simple bash scripts.

1. Most scripts follow these rules

   - Always start with `#!/bin/bash`
   - Script code
   - End with `done`
   - `chmod 755 (script filename)`
   - `./(script filename)`
   - If the script references any files like somefilename.txt, make sure they are in the same directory else use full path

2. To create a text file using Nano:  

   - `vi (filename.extension)`  
   - Type text  
   - Keyboard shortcut: `Ctrl + O`  
   - Keyboard key: `Enter`  
   - Keyboard shortcut: `Ctrl + X`

3. To create a file using vi:  

   - vi `(filename.extension)`  
   - Keyboard shortcut: `i` #this is insert mode, type your text in here.  
   - Keyboard shortcut: `ESC` #tap this once to enter command mode.  
   - Keyboard shortcut: `:wq!` #this saves and exits. use `:q` to quit without saving changes. Use `:x!` to force changes.

