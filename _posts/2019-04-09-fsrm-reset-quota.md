---
title: 'FSRM: Reset Quota'
date: 2019-04-09T20:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/fsrm-reset-quota/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
---
<!--more-->

### Description:

A user will say that FSRM is saying their drive is full when it's actually not.

### To Resolve:

1. Open ADUC, go to the user, go to Profile tab, and check the &#8220;Connect To&#8221; address.

2. RDP to that file servers and open up FSRM Management.

3. Uncheck &#8220;Enable Quota&#8221; for that path and then wait and recheck it.

4. I've also had luck running (in Admin CMD):

   ```powershell
   dirquota quota scan /path:c:\blah\folder
   # path updated successfully
   ```

5. To see violations:

   ```powershell
   fsutil quota violations

   # Server 2012r2+:
   Get-FsrmQuota -Path "C:\Share01\..."
   ```