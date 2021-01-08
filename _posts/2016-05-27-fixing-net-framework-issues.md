---
title: Fixing .NET Framework Issues
date: 2016-05-27T22:14:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/fixing-net-framework-issues/
categories:
  - Windows
---
<!--more-->

### Description:

Sometimes, .NET Framework errors can cause issues in the Windows environment. Follow these steps to uninstall and re-install .NET Framework.

### To Resolve:

1. Run => appwiz.cpl => uninstall all &#8220;.NET&#8221; related programs from your computer.

2. Run the .NET removal tool found [here](https://blogs.msdn.microsoft.com/) 

3. Reboot the computer.

4. Re-install from the lowest version on up. For many systems, just run the full version of 3.5 and then install v4 and so on.