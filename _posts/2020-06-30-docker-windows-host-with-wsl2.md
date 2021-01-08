---
title: Docker With Windows Host and WSL2
date: 2020-06-30T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/docker-windows-host-with-wsl2
categories:
  - Linux
  - Windows
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

So I did a PC refresh the other day and wanted to move from VirtualBox to using only WSL2. I then went to setup Plex in a container in WSL2 which I then changed later but here is what I initially did to get Docker on Windows. Pretty much just followed the [official docs](https://docs.docker.com/docker-for-windows/wsl/)


### To Resolve:

1. Make your user a member of the local administrator group or you will have issues with [named pipes](https://stackoverflow.com/questions/58663920/can-i-run-docker-desktop-on-windows-without-admin-privileges)

2. Upgrade Windows to v2004 via Creator Tool.

3. Setup WSL2:

   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName "Microsoft-Windows-Subsystem-Linux" # Mine was already enabled
   Enable-WindowsOptionalFeature -Online -FeatureName "VirtualMachinePlatform"

   wsl --set-default-version 2

   # install / launch Ubuntu
   # create user/pass
   apt-get update -y && apt-get upgrade -y

   #close and reopen powershell
   wsl -l -v
      NAME      STATE           VERSION
      * Legacy    Stopped         1
      Ubuntu    Running         1
   wsl --set-version Ubuntu 2
   wsl --set-default-version 2
   wsl --set-default ubuntu
   ```

4. Download [docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

   ```shell
   # launch docker installer
   # Open VSCode
   wsl
   code .
   # this will automatically detect/install Docker
   cd /mnt/c/scripts
   git clone https://github.com/docker/getting-started.git
   cd getting-started
   docker build -t docker01tutorial .
   docker run -d -p 80:80 --name docker-tutorial docker01tutorial
   
   # the next steps won't work from VSCode but will from the Docker Desktop app since you can sign into Docker Hub there and it will work
   # from the GUI of the application
   docker tag docker101tutorial username/docker101tutorial
   docker push username/docker101tutorial
   ```

5. At this point, you can open a browser to `http://localhost` and it will redirect to `localhost/tutorial` on your Windows machine. You could even port forward your external IP to your windows host and it would work.
