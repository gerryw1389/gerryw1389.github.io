---
title: Set Registry Permissions
date: 2018-11-22T07:16:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/set-registry-permissions/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

This function will take ownership of a registry key as a specified user and set access rights to full control. This is a useful function to call in other scripts when you get "Access Denied" when trying to modify certain keys in the registry.

### To Resolve:

1. Before:

   - ![set-reg-1](https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1.png){:class="img-responsive"}

2. After running `Set-RegkeyPermissions -RegistryKey "HKCU:\Gerry\NoAccess" -Username "gerry"`

   - ![set-reg-2](https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2.png){:class="img-responsive"}

3. Source is maintained under [gwConfiguration](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-RegistryPermission.ps1)