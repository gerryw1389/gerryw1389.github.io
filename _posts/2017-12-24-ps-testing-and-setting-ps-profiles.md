---
title: 'PS: Testing And Setting PS Profiles'
date: 2017-12-24T03:24:53+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-testing-and-setting-ps-profiles/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So as you may or may not know, PS (powershell) [uses six profiles](https://blogs.technet.microsoft.com/heyscriptingguy/2012/05/21/understanding-the-six-powershell-profiles/) when launching scripts and hey!, even VS Code has one, so it's a hassle trying to keep them all synced up. These are scripts I use to help keep them in check on different machines.

### To Resolve:

1. This script will test to see if they exists and if not, create them: [Test-PSProfiles](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Test-PSProfiles.ps1)