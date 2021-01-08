---
title: 'GPO: Block Dual Scan'
date: 2018-05-27T03:26:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/gpo-block-dual-scan/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

So many admins seem to be confused on how to block &#8220;Dual Scan Mode&#8221; in their environment. These settings stop WSUS clients from reaching out to the internet to get updates if the WSUS server doesn't push them. These seem to be the settings you need to set to disable Dual Scan Mode.

### To Resolve:

1. Set the following:  
   - `Computer Configuration\Policies\Administrative Templates\Windows Components\Windows Update` = *all settings* to `Not Enabled` except "Do not connect to any Windows Update Internet locations" to `Enabled`
   - `Administrative Templates\System\Internet Communication Management\Internet Communication\` = Turn off access to all windows update features to `Enabled`

### Reference:

["Demystifying Dual Scan"](https://blogs.technet.microsoft.com/wsus/2017/05/05/demystifying-dual-scan/)