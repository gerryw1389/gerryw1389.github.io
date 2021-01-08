---
title: 'GPO: CryptoLocker Block'
date: 2016-05-29T04:15:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-cryptolocker-block/
categories:
  - WindowsServer
  - Security
tags:
  - WindowsServer-Roles
  - Viruses
---
<!--more-->

### Description:

CryptoLocker is a common infection people are getting that encrypts their files. The best way to combat this is to prevent it in the first place. Here are the steps to create a security policy to prevent it.

### To Resolve:

1. If on a domain, you will need to create a Group Policy. If a local account not joined to a domain, a Local Security Policy. So `gpedit.msc` or `secpol.msc`.

2. Once in there, navigate down to &#8220;Software Restriction Policies&#8221; and right click and &#8220;Create A New Policy&#8221;.

3. Now navigate down to &#8220;Additional Rules&#8221; => Right click and &#8220;Create New Path Rules&#8221; and add these paths and descriptions to the list:

   - `%AppData%*.exe` => Disallowed => Prevent programs from running in AppData.
   - `%AppData%**.exe` => Disallowed => Prevent virus payloads from executing in subfolders of AppData
   - `%LocalAppData%\Temp\Rar\*.exe` => Disallowed => Prevent un-WinRARed executables in email attachments from running in the user space
   - `%LocalAppData%\Temp\7z\*.exe` => Disallowed => Prevent un-7Ziped executables in email attachments from running in the user space
   - `%LocalAppData%\Temp\wz*.exe` => Disallowed => Prevent un-WinZIPed executables in email attachments from running in the user space
   - `%LocalAppData%\Temp\*.zip\*.exe` => Disallowed => Prevent unarchived executables in email attachments from running in the user space

4. That's it, users will not be allowed to run executables in those directories.

#### If you have a version of Windows that includes AppLocker (Pro and Enterprise Editions), follow these steps:

1. Run `gpedit.msc` or `secpol.msc` and navigate down to: &#8220;Application Control Policies => Applocker&#8221;

2. Click on the &#8220;Configure Rule Enforcement&#8221; => &#8220;Executables = Checked => and drop down = enforced&#8221;.

3. Now go back to the AppLocker screen and go to &#8220;Executable Rules => Right Click => and &#8220;Create New Rule&#8221;.

4. This brings up a wizard, select &#8221; Next => Next => Publisher => Under browse => Select ANY executable file you can find (I chose Window Media Player (wmplayer.exe)) => Slide the bar up to &#8220;Any Publisher&#8221; => Next => Under description, type: Only run executables that are signed. => &#8220;Create&#8221;.

5. If this is the first time creating an AppLocker policy, Windows will want you to allow Default Rules => select &#8220;Yes&#8221;.