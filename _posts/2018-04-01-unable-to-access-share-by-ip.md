---
title: Unable To Access Share By IP
date: 2018-04-01T06:35:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/unable-to-access-share-by-ip/
categories:
  - Networking
---
<!--more-->

### Description:

Sometimes you will have an issue where a user is unable to connect to a NAS or a Linux box by IP Address. This is due to reg key that is needed called &#8220;Allow insecure guest logons&#8221;. Windows to Windows won't really have this issue because there is always authentication.

### To Resolve:

1. Set the following key to &#8220;Enabled&#8221;:  
Registry Hive HKEY_LOCAL_MACHINE  
Registry Path Software\Policies\Microsoft\Windows\LanmanWorkstation  
Value Name AllowInsecureGuestAuth  
Value Type REG_DWORD  
Enabled Value 1  
Disabled Value 0

### References:

[https://getadmx.com/?Category=Windows\_10\_2016&Policy=Microsoft.Policies.LanmanWorkstation::Pol_EnableInsecureGuestLogons](https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.LanmanWorkstation::Pol_EnableInsecureGuestLogons)