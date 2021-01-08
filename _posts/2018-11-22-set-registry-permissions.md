---
title: Set Registry Permissions
date: 2018-11-22T07:16:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/set-registry-permissions/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

This function will take ownership of a registry key as a specified user and set access rights to full control. This is a useful function to call in other scripts when you get "Access Denied" when trying to modify certain keys in the registry.

### To Resolve:

1. Before:

   <img class="alignnone size-full wp-image-5593" src="https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1.png" alt="" width="1166" height="614" srcset="https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1.png 1166w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1-300x158.png 300w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1-768x404.png 768w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-1-1024x539.png 1024w" sizes="(max-width: 1166px) 100vw, 1166px" />  

2. After running `Set-RegkeyPermissions -RegistryKey "HKCU:\Gerry\NoAccess" -Username "gerry"`

   <img class="alignnone size-full wp-image-5594" src="https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2.png" alt="" width="1152" height="582" srcset="https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2.png 1152w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2-300x152.png 300w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2-768x388.png 768w, https://automationadmin.com/assets/images/uploads/2018/11/set-reg-2-1024x517.png 1024w" sizes="(max-width: 1152px) 100vw, 1152px" /> 

3. Source is maintained under [gwConfiguration](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-RegistryPermission.ps1)