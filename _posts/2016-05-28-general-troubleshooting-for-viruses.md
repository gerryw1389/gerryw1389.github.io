---
title: General Troubleshooting For Viruses
date: 2016-05-28T07:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/general-troubleshooting-for-viruses/
tags:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

At one point or another, you will deal with someone who got a virus on their computer. Here are some general troubleshooting steps to resolve.

### To Resolve:

1. Determine if you can run .exe files, many viruses block these. If you are unable to remote in on a computer, see [Jumping To A Computer Through The Network](https://automationadmin.com/2016/05/jumping-to-a-computer-through-the-network/).

2. Shut the computer down and bring it up in Safe Mode with Networking (usually by tapping `F8` on startup).

3. If the virus is not allowing you to run any tools, start with &#8220;[R-Kill](http://www.bleepingcomputer.com/download/rkill/)&#8220;, this program clears active processes so that you can run your virus removal tools. Place this file on a mapped drive on another computer that is mapped to the infected computer and have the user run this if you are unable to remote in.

4. As soon as you get in, start running as many tools as you can. I usually start with &#8220;Malware Bytes Antirootkit&#8221;, &#8220;ESET Online Scanner&#8221;, and &#8220;RogueKiller&#8221;. Always run multiple malware removal programs so that if one doesn't catch the infection, the others might.

5. While those are running, check the registry at:

   - `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` and `RunOnce`
   - `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`and `RunOnce`

   <img class="size-full wp-image-658 aligncenter" src="https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-3.png" alt="general-troubleshooting-3" width="832" height="613" srcset="https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-3.png 832w, https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-3-300x221.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-3-768x566.png 768w" sizes="(max-width: 832px) 100vw, 832px" /> 


6. Disable startup entries in `Msconfig.exe`.

7. After the scans complete, reboot and start with some other scanners, I usually do &#8220;AdwCleaner&#8221; and &#8220;Malware Bytes Regular&#8221; next.

  <img class="alignnone size-full wp-image-659" src="https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-4.png" alt="general-troubleshooting-4" width="804" height="591" srcset="https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-4.png 804w, https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-4-300x221.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/general-troubleshooting-4-768x565.png 768w" sizes="(max-width: 804px) 100vw, 804px" />

8. After those scans complete, reboot and run &#8220;CCleaner&#8221; and &#8220;TFC (Temp File Cleaner)&#8221;

