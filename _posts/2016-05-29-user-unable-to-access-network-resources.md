---
title: User Unable To Access Network Resources
date: 2016-05-29T03:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/user-unable-to-access-network-resources/
tags:
  - WindowsServer
  - Networking
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

User will have issues accessing network resources like mapped drives and printers. Although this is a general occurance, this specifically will happen when a user's password has expired on the domain. This has to do with Windows tokens.

  <img class="alignnone size-full wp-image-716" src="https://automationadmin.com/assets/images/uploads/2016/09/unable-to-access-resources.png" alt="unable-to-access-resources" width="388" height="201" srcset="https://automationadmin.com/assets/images/uploads/2016/09/unable-to-access-resources.png 388w, https://automationadmin.com/assets/images/uploads/2016/09/unable-to-access-resources-300x155.png 300w" sizes="(max-width: 388px) 100vw, 388px" />


### To Resolve:

1. Obviously, have the user reset their password. Most of the time, they already have but have not rebooted.

2. Try to remap the drives manually. Run => \\(ShareName). When you go to enter credentials it will say something indicating an expired password.

3. Have the user reboot their computer. Upon login, the tokens will be reauthenticated and the user will be allowed to access network resources.