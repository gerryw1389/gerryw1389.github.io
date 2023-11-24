---
title: Show All Users At Sign In
date: 2017-05-27T03:29:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/05/show-all-users-at-sign-in/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Follow these steps to have Windows show all available users at the login screen instead of the previous user who was logged on.  
  

### To Resolve:

1. Open Regedit and go to: `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\UserSwitch` Change: `Enabled` to `1`

2. Problem with this is the user `SYSTEM` automatically changes the value to 0, so we need to block it:

   - Now right click on UserSwitch key itself and click on Advanced => Disable Inheritence => Convert inherited permissions into explicit ones for this object. 
   - Now, change the &#8220;Owner&#8221; at the top to Administrators.
   - Now go to permissions and set Administrators => Allow => Full Control
   - In the same box, select System => Show Advanced Permissions and check all DENY's except &#8220;Check Value&#8221;