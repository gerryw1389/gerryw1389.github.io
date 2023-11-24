---
title: Not Enough Storage Space Error
date: 2016-05-21T22:14:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/not-enough-storage-space-error/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

When one workstation cannot connect to the server with the following error, do the following to resolve:
   - ![not-enough-storage](https://automationadmin.com/assets/images/uploads/2016/09/not-enough-storage.png){:class="img-responsive"}

### To Resolve:

1. On the computer unable to access the mapped drive, Run => regedit

2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Lanmanserver\Parameters`

3. Look for a DWORD value of `IRPStackSize`. If it's there, change it's value to `Decimal` to equal anything between `15-50`. The lower the better, so try 15, then 20, then 25 until the issue is resolved. If the value is not there, create it and set it to the value described.

4. Reboot the computer and try to access the share again. Do this over and over until it works if it doesn't work on the first try.
