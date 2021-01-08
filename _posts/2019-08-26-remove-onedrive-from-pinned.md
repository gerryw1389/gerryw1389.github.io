---
title: Remove Pinned OneDrive From Explorer
date: 2019-08-26T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/08/remove-onedrive-from-pinned/
categories:
  - Windows
---
<!--more-->

### Description:
So at one point, I had my school's onedrive added to my computer and have since removed it after graduating. The problem was, it was still pinned in File Explorer and I was unable to remove it by right click and 'remove' like you can most things there. Curse Windows and it's OneDrive integrations, even when you uninstall it!

### To Resolve:

1. In order to remove it, you have to go to the registry:
`Computer\HKEY_USERS\$yourSID\Software\Classes\CLSID\{04271989-C4D2-7E48-E593-3CF9C1D8EADF}` change `IsPinned` from `1` to `0`

2. The way to find this key is to pull up `regedit` and search for `$stringHere` where `$stringHere` is the the name after 'OneDrive - ' in File Explorer.