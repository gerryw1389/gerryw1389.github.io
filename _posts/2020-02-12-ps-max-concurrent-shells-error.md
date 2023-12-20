---
title: 'PS: Max Concurrent Shells Error'
date: 2020-02-12T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/ps-max-concurrent-shells-error
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So the other day I got an error I had never seen before:

   ```escape
   Get-PhoneNumbers : Connecting to remote server admin1a.online.lync.com failed with the following error message : The
   WS-Management service cannot process the request. The maximum number of concurrent shells for this user has been
   exceeded. Close existing shells or raise the quota for this user. For more information, see the
   about_Remote_Troubleshooting Help topic.
   At C:\scripts\script.ps1:486 char:2
   ```


### To Resolve:

1. Run `Set-Item WSMan:\localhost\Shell\MaxShellsPerUser 100` or `winrm set winrm/config/winrs '@{MaxShellsPerUser="100"}'`

