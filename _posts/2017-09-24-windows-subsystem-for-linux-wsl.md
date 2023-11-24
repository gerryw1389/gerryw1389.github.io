---
title: Windows Subsystem For Linux (WSL)
date: 2017-09-24T06:42:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/windows-subsystem-for-linux-wsl/
tags:
  - Windows
tags:
  - Setup
---
<!--more-->

### Description:

Here is how to Enable Windows Subsystem For Linux. What this does is allow you to interact with Linux machines on the network natively.

### To Resolve:

1. If you have W10 Creators update:

   - Open PowerShell as Administrator and run: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
   - After installation your Linux distribution will be located at: `%localappdata%\lxss\`
   - If you don't yet: Turn on Developer Mode by going to Settings => Update and Security => For developers. Then do it.

2. Open a command prompt. Type: bash

   - This will ask you something, just say yes. Then it will have you create a user and password.

3. First, change the root password: sudo passwd root

4. Now try creating a file in your Windows system from the linux system:


   ```shell
   cd /mnt/c/Users/%username%/Documents
   touch myfile.txt
   vi myfile.txt
   # (type whatever) then press ESC and then :wq! to save and exit the file
   ```

   - Check from Windows. It's there!

5. Now you can do the standard updates: `sudo apt-get update && sudo apt-get upgrade`

6. Start interacting with your servers using ssh and other linux tools! For more info, see [here](https://blogs.windows.com/buildingapps/2016/07/22/fun-with-the-windows-subsystem-for-linux/).