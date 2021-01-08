---
title: Corrupted Windows Profile
date: 2016-05-26T21:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/corrupted-windows-profile/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

When you login to your account, many icons will be missing and Windows will have many &#8220;User Profile&#8221; errors in the Event Viewer.

### To Resolve:

1. Run => regedit

2. Go to HKEY_LOCAL_MACHINE => SOFTWARE => Microsoft => Windows NT => CurrentVersion => ProfileList.

3. Locate the two SID (Security Identification) keys that correspond to the user profile. Both keys are named &#8220;S-1-5-21-S&#8221; (where &#8220;X&#8221; is your security profile identification number), but one key has &#8220;.bak&#8221; at the end of the name. If you have more than one user on your computer, you can identify your SID keys by clicking on each key in the left pane and checking the user name data column located to the right of the &#8220;ProfileImagePath&#8221; field in the right pane.

4. Right-click on your SID key name that does not end in &#8220;.bak&#8221; and click &#8220;Rename.&#8221; Type &#8220;_corrupt&#8221; at the end of the key name and press &#8220;Enter.&#8221;

5. Right-click on your SID key name that ends with &#8220;.bak&#8221; and click &#8220;Rename.&#8221; Remove the &#8220;.bak&#8221; from the key name and press the &#8220;Enter&#8221; key.

6. Exit regedit and reboot.

7. Sign in to your profile, the issue should be resolved.