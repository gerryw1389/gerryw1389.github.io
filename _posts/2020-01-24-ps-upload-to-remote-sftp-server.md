---
title: 'PS: Upload To Remote SFTP Server'
date: 2020-01-24T10:45:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/ps-upload-to-remote-sftp-server/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

This schedule tasks runs nightly. It uses Powershell with the WinSCP software to upload a CSV file to an external vendor.

### To Resolve

1. [This function](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Set-FileViaSFTP.ps1) will upload a CSV to a vendor on a schedule and will email if the function fails.