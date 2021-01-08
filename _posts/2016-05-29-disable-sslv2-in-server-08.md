---
title: Disable SSLV2 In Server 08
date: 2016-05-29T03:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/disable-sslv2-in-server-08/
categories:
  - Windows
  - Security
tags:
  - Regedit
---
<!--more-->

### Description:

For security reasons, you may be asked by another company to disable SSLV2 on your server. To resolve, follow these steps.

### To Resolve:

1. Open the registry and create a key named "Server" under the following entry : HKEY\_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0

2. Under the registry key Server, create a DWORD value named Enabled and change the value data to 00000000.

3. Reboot.

4. If that doesn't work, try creating a DWORD value named "DisabledByDefault" and change the value data to "00000001".

5. Reboot again.

6. Essentially:

   ```escape
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server" /ve /f
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server" /t REG_DWORD /v Enabled /d 0 /f
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server" /t REG_DWORD /v DisabledByDefault /d 1 /f
   ```

7. To Disable SSLv3: Copy and paste this to a .reg file:

   ```escape
   Windows Registry Editor Version 5.00

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]  
   "DisabledByDefault"=dword:00000001

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]  
   "Enabled"=dword:00000000
   ```

