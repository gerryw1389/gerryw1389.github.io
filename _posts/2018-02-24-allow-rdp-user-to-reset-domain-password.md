---
title: Allow RDP User To Reset Domain Password
date: 2018-02-24T03:28:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/allow-rdp-user-to-reset-domain-password/
tags:
  - Networking
---
<!--more-->

### Description:

Had an issue the other day where a user wasn't able to remote into our servers because their AD password had expired. Instead of me resetting it on the domain controller, we did the following:

### To Resolve:

1. Have the user create a .rdp configuration to the destination computer on the domain.

2. Include the following property (open using notepad => add to last line):

   ```powershell
   enablecredsspsupport:i:0
   ```

3. When you use that configuration file to connect, you will be presented with the login GUI, and subsequently you will be presented with the change password dialog.

   - It should be noted that this only works if the server does not require NLA:

   <img class="alignnone size-full wp-image-4971" src="https://automationadmin.com/assets/images/uploads/2018/02/expired-rdp.png" alt="" width="424" height="478" srcset="https://automationadmin.com/assets/images/uploads/2018/02/expired-rdp.png 424w, https://automationadmin.com/assets/images/uploads/2018/02/expired-rdp-266x300.png 266w" sizes="(max-width: 424px) 100vw, 424px" /> 


### References:

["Allow Users to Change Expired Password via Remote Desktop Connection"](https://superuser.com/questions/1196477/allow-users-to-change-expired-password-via-remote-desktop-connection/1196567#1196567)  