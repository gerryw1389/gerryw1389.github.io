---
title: Freeing Up Disk Space
date: 2016-05-28T06:46:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/freeing-up-disk-space/
tags:
  - Hardware
  - Windows
---
<!--more-->

### Description:

At some point or another you will need to clear up disk space on a drive. Follow these steps to resolve:

### To Resolve:

1. Download and run a tool to analyze what is using the most space. Many people use SpaceMonger, but I use WizTree.

2. If it is your system drive, the most common culprits on Windows machines is pagefile.sys and hiberfil.sys.

- `pagefile.sys` is a hidden file on the root of the OS drive and is used for switching between applications and is the "buffer" file for Windows if you don't have enough RAM to run programs. It is recommeneded to let Windows manage it unless you are an experienced user (follow link in references).

- `hiberfil.sys` is for hibernation. To disable, just [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `powercfg -h off`

3. If it is a data drive, just delete unused or unimportant files.