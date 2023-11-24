---
title: Internet Keeps Redirecting Sites
date: 2016-05-28T07:05:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/internet-keeps-redirecting-sites/
tags:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

If your computer jumps to random websites when you are not actively browsing the web or it re-directs to sites when you enter a specific site, you most likely have a malware infection.

### To Resolve:

1. Run => `inetcpl.cpl` => &#8220;Advanced&#8221; Tab => &#8220;Reset&#8221; => Make sure to leave the &#8220;Delete Personal Settings&#8221; unchecked. This should be one of the first steps for most IE issues. Firefox and Chrome have similar functions.

2. Check the Windows Host File. Run => `C:\Windows\System32\Drivers\Etc` => open that up. Navigate to the host file => double click => open with => Notepad. Once inside, make sure the bottom doesn't have any phony IP addresses to host names. While your in there, add the server to your network by going to the last line => enter the IP address of the server (which should be static) => Tab => the Servers Name. Ex: 192.168.1.10 Server

3. Run virus removal tools. I personally recommend &#8220;Adw Cleaner&#8221; and &#8220;Malware Bytes Antirootkit&#8221;.