---
title: Same SID Issue When Joining Domain
date: 2018-01-10T17:44:48+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/01/same-sid-issue-when-joining-domain/
tags:
  - Windows
  - WindowsServer
---
<!--more-->

### Description:

I once had an issue joining a domain server to the domain in my test lab. It said something about `SID already exist`. This makes sense because I had cloned the VM from my domain controller prior to adding the AD Role. In order to fix, you just need to change the SID. There is a stale program called "ChangeSID" that I found, but I think it would be much easier to generalize the image and try again. This of course worked:

### To Resolve:

1. Run the following from Admin CMD and try to join the domain again after reboot:

   ```powershell
   %WINDIR%\system32\sysprep\sysprep.exe /generalize /shutdown /oobe /mode:vm
   ```

   