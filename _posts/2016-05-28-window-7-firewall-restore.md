---
title: Window 7 Firewall Restore
date: 2016-05-28T07:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/window-7-firewall-restore/
tags:
  - Windows
tags:
  - Viruses
  - Regedit
---
<!--more-->

### Description:

If a virus infects your W7 machine to a point where you cannot find the Windows Firewall Service in `services.msc`, try importing the following registry key and rebooting.

### To Resolve:

1. Copy and paste the following into Notepad and then save as .reg, then double click to import it:

   ```escape
   Windows Registry Editor Version 5.00

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc]  
   "DisplayName"="@%SystemRoot%\\system32\\FirewallAPI.dll,-23090"  
   "Group"="NetworkProvider"  
   "ImagePath"=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,00,\  
   74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,73,\  
   00,76,00,63,00,68,00,6f,00,73,00,74,00,2e,00,65,00,78,00,65,00,20,00,2d,00,\  
   6b,00,20,00,4c,00,6f,00,63,00,61,00,6c,00,53,00,65,00,72,00,76,00,69,00,63,\  
   00,65,00,4e,00,6f,00,4e,00,65,00,74,00,77,00,6f,00,72,00,6b,00,00,00  
   "Description"="@%SystemRoot%\\system32\\FirewallAPI.dll,-23091"  
   "ObjectName"="NT Authority\\LocalService"  
   "ErrorControl"=dword:00000001  
   "Start"=dword:00000002  
   "Type"=dword:00000020  
   "DependOnService"=hex(7):6d,00,70,00,73,00,64,00,72,00,76,00,00,00,62,00,66,00,\  
   65,00,00,00,00,00  
   "ServiceSidType"=dword:00000003  
   "RequiredPrivileges"=hex(7):53,00,65,00,41,00,73,00,73,00,69,00,67,00,6e,00,50,\  
   00,72,00,69,00,6d,00,61,00,72,00,79,00,54,00,6f,00,6b,00,65,00,6e,00,50,00,\  
   72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,00,00,53,00,65,00,41,00,75,\  
   00,64,00,69,00,74,00,50,00,72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,\  
   00,00,53,00,65,00,43,00,68,00,61,00,6e,00,67,00,65,00,4e,00,6f,00,74,00,69,\  
   00,66,00,79,00,50,00,72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,00,00,\  
   53,00,65,00,43,00,72,00,65,00,61,00,74,00,65,00,47,00,6c,00,6f,00,62,00,61,\  
   00,6c,00,50,00,72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,00,00,53,00,\  
   65,00,49,00,6d,00,70,00,65,00,72,00,73,00,6f,00,6e,00,61,00,74,00,65,00,50,\  
   00,72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,00,00,53,00,65,00,49,00,\  
   6e,00,63,00,72,00,65,00,61,00,73,00,65,00,51,00,75,00,6f,00,74,00,61,00,50,\  
   00,72,00,69,00,76,00,69,00,6c,00,65,00,67,00,65,00,00,00,00,00  
   "FailureActions"=hex:80,51,01,00,00,00,00,00,00,00,00,00,03,00,00,00,14,00,00,\  
   00,01,00,00,00,c0,d4,01,00,01,00,00,00,e0,93,04,00,00,00,00,00,00,00,00,00

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc\Parameters]  
   "ServiceDll"=hex(2):25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,6f,\  
   00,74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,\  
   6d,00,70,00,73,00,73,00,76,00,63,00,2e,00,64,00,6c,00,6c,00,00,00  
   "ServiceDllUnloadOnStop"=dword:00000001

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc\Parameters\PortKeywords]

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc\Parameters\PortKeywords\RPC-EPMap]  
   "Collection"=hex:87,00,01,00

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc\Parameters\PortKeywords\Teredo]

   [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\MpsSvc\Security]  
   "Security"=hex:01,00,14,80,b4,00,00,00,c0,00,00,00,14,00,00,00,30,00,00,00,02,\  
   00,1c,00,01,00,00,00,02,80,14,00,ff,01,0f,00,01,01,00,00,00,00,00,01,00,00,\  
   00,00,02,00,84,00,05,00,00,00,00,00,14,00,fd,01,02,00,01,01,00,00,00,00,00,\  
   05,12,00,00,00,00,00,18,00,ff,01,0f,00,01,02,00,00,00,00,00,05,20,00,00,00,\  
   20,02,00,00,00,00,14,00,8d,01,02,00,01,01,00,00,00,00,00,05,04,00,00,00,00,\  
   00,14,00,8d,01,02,00,01,01,00,00,00,00,00,05,06,00,00,00,00,00,28,00,15,00,\  
   00,00,01,06,00,00,00,00,00,05,50,00,00,00,49,59,9d,77,91,56,e5,55,dc,f4,e2,\  
   0e,a7,8b,eb,ca,7b,42,13,56,01,01,00,00,00,00,00,05,12,00,00,00,01,01,00,00,\  
   00,00,00,05,12,00,00,00
   ```

