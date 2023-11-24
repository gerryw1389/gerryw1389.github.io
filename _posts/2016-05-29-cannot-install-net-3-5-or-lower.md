---
title: Cannot Install .NET 3.5 Or Lower
date: 2016-05-29T03:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/cannot-install-net-3-5-or-lower/
tags:
  - Windows
tags:
  - Scripting-CMD
  - Scripting-Powershell
---
<!--more-->

### Description:

Follow these steps if you keep getting errors when attempting to install .NET 3.5 or 2.0 on Windows Servers.

### To Resolve:

1. Run => cmd:

   ```powershell
   DISM /Online /Enable-Feature /FeatureName:NetFx3 /All
   ```

2. If it still fails, load your installer disc and type:

   ```powershell
   DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /LimitAccess /Source:d:\sources\sxs
   ```

3. Alternatively, you can use Powershell:

   ```powershell
   Install-WindowsFeature Net-Framework-Core -source \\network\share\sxs

   #or D:\sources\sxs. Run get-windowsfeature afterwards to make sure it installed.
   ```

