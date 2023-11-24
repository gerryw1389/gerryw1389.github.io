---
title: 'GPO: Cannot Edit Setting In Windows Firewall With Advanced Security'
date: 2019-04-09T16:14:25+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/gpo-cannot-edit-setting-in-windows-firewall-with-advanced-security/
tags:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

I wish I could find a screenshot of this but what happens is: You want to modify a GPO that is pushing firewall rules and you go to change them and you get a red box saying something about `cannot connect to the domain` only in that section of the GPO, other settings work fine.

### To Resolve:

1. The fix is to find your PDC Emulator

   ```powershell
   Get-ADDomain | Select PDCEmulator
   ```

1. RDP to that DC and then try editing the rules, it will then work!