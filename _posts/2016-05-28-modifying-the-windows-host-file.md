---
title: Modifying The Windows Host File
date: 2016-05-28T06:15:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/modifying-the-windows-host-file/
categories:
  - Windows
tags:
  - Scripting-CMD
---
<!--more-->

### Description:

Sometimes, you may want to check the Windows Host file for bogus redirects by viruses or if you just want the computer to know to resolve a particular IP to a hostname, you will want to modify this file. Editing the Windows host file is a common task for administrators for post malware cleanup or to set their own values. The Windows host file is a basic &#8220;go-to&#8221; file that Windows uses for DNS before reaching out to the DNS Server configured in the NIC properties.

### To Resolve:

1. Run => `C:\Windows\System32\Drivers\Etc` => open that up. Navigate to the `host` file => double click => open with => Notepad. Alternatively, you may have to Search => notepad => right-click => &#8220;run as administrator&#8221;. Once opened, navigate to that directory and open &#8220;hosts&#8221;.

2. Once inside, make sure the bottom doesn't have any phony IP addresses to host names. While your in there, add the server to your network by going to the last line => enter the IP address of the server (which should be static) => Tab => the Servers Name. Example: `192.168.1.10  Server01`

3. This is optional => Go to [Winhelp](http://winhelp2002.mvps.org/hosts.txt) and copy and paste this into the file to block advertisements while you are in there!

4. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/)

   ```powershell
   cd \
   takeown /f c:\windows\system32\drivers\etc\hosts
   icacls c:\windows\system32\drivers\etc\hosts /grant:r :f
   attrib -R c:\windows\system32\drivers\etc\hosts
   notepad c:\windows\system32\drivers\etc\hosts
   # Enter whatever you want and click "save" to save your changes.
   ```

