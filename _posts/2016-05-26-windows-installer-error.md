---
title: Windows Installer Error
date: 2016-05-26T22:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-installer-error/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Windows Installer will give &#8220;Error 1606: Could Not Access Network Location&#8221; message when trying to install a program.

### To Resolve:

1. Navigate to these keys and point them to a local path:

```escape
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
```

### MS SQL Installation Error Description:

If you get an error that says &#8220;An installation package for the product Microsoft SQL Server Native Client cannot be found. Try the installation again using a valid copy of the installation package sqlncli.msi&#8221;.

### To Resolve:

1. Run => appwiz.cpl => find &#8220;SQL Server 2005 Client&#8221; => uninstall.

2. Then try running your installer again.