---
title: Portable WSL2
date: 2020-07-01T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/portable-wsl
categories:
  - Linux
tags:
  - Windows
  - VirtualizationSoftware
---
<!--more-->

### Description:

So while I was troubleshooting permissions with WSL not being able to create folders with my Docker container, I first tried installing WSL on a secondary drive and setting that as my default WSL instance (since this is where my media was stored anyways). Here are the steps to set it up:

### To Resolve:

1. Open Powershell and type:

   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   New-Item D:\Ubuntu -ItemType Directory
   Set-Location D:\Ubuntu
   Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu.appx -UseBasicParsing
   Rename-Item .\Ubuntu.appx Ubuntu.zip
   Expand-Archive .\Ubuntu.zip -Verbose
   cd ./Ubuntu
   cmd
   ubuntu2004.exe
   # create user/pass
   apt-get update -y && apt-get upgrade -y

   # close and reopen powershell
   wsl -l -v
   NAME      STATE           VERSION
   * Legacy    Stopped         1
   Ubuntu-20.04    Running     1
   
   wsl --set-version Ubuntu-20.04 2
   wsl --set-default-version 2
   wsl --set-default Ubuntu-20.04
   wsl -l -v
   NAME      STATE           VERSION
   Ubuntu-20.04    Running     2
   * Legacy    Stopped         1
   ```

2. I don't remember if the commands were exactly like that, but that was the overall idea.
