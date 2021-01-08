---
title: Recreate Windows Licensing Store
date: 2016-05-26T22:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/recreate-windows-licensing-store/
categories:
  - Windows
---
<!--more-->

### Description:

(W7) If you have a valid copy of Window's but you get this error, follow these steps to recreate the Licensing Store within Windows.

### To Resolve:

1. Search => Command Prompt (As Administrator) => 

   ```console
   net stop sppsvc
   cd C:\WINDOWS\ServiceProfiles\NetworkService\AppData\Roaming\Microsoft\SoftwareProtectionPlatform
   rename tokens.dat tokens.bar
   cd %windir%\system32
   net start sppsvc
   slui.exe
   ```

2. After a couple of seconds Windows Activation dialog will appear. You may be asked to re-activate and/or re-enter your product key or Activation may occur automatically.

8. If unsuccessful, try going [here](https://www.mydigitallife.info/fix-0x80070005-windows-is-not-genuine-error-to-make-windows-7-activated/).