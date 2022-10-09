---
title: 'PS: Replace CMD'
date: 2016-11-27T07:33:37+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/ps-replace-cmd/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Tweaks
---
<!--more-->

### Description:

As Microsoft moves forward with Powershell (has it already been out for 10 years?), use the following &#8220;tricks&#8221; to replace CMD completely with Powershell.

### To Resolve:

1. Obviously, see if there is a Powershell way of doing the same thing (I have a couple posts on this myself..)

   - Old way to map a drive:

   ```powershell
   net use g: \\ServerComputerName\share /user:domain\user /persistent:yes
   ```

   - New way:

   ```powershell
   New-PSDrive -Name G -Root \\Server01\Scripts -Credential domain\user -Persist -PSProvider FileSystem
   ```

2. If you can't find a direct equivalent, invoke the command like:

   ```powershell
   cmd /c "net user administrator /active:no"
   ```

3. Use the Stop-Parsing symbol `--%` so that Powershell won't parse symbols such as parenthesis and brackets: Ex: `icacls c:\logs\* /grant Administrator:(D,WDAC)` will fail in PowerShell. `icacls --% c:\logs\* /grant Administrator:(D,WDAC)` will work

4. Lastly for Windows 10 users, make sure to replace CMD with Powershell by going to Settings => Taskbar => Replace CMD with Powershell. This will only give Powershell options with the Win+X menu.

