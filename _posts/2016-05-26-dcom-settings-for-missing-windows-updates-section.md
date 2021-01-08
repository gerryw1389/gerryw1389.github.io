---
title: DCOM Settings For Missing Windows Updates Section
date: 2016-05-26T21:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/dcom-settings-for-missing-windows-updates-section/
categories:
  - Windows
tags:
  - Regedit
  - Updates
---
<!--more-->

### Description:

You are in the "Installed Updates" section and you notice the "Microsoft Windows" section is missing. This will also help if you start getting "Access Denied" messages when downgrading IE.

### To Resolve:

1. Run `dcomcnfg.exe`.

2. In the console tree, expand Component Services, and then expand Computers.

3. Right-click My Computer, and then click Properties.

4. Click the Default Properties tab.

5. Select "Connect" in the "Default Authentication Level" list.

6. Select "Identify" in the "Default Impersonation Level" list.

7. Click OK, and then click Yes to confirm the selection.

8. Close Component Services console.

9. It doesn't mention this anywhere else, but you have to reboot for it to take effect.

10. Reg File Import: Copy and paste this into a .reg and import it:


   ```escape
   Windows Registry Editor Version 5.00

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole]  
   "DefaultLaunchPermission"=hex:01,00,04,80,5c,00,00,00,6c,00,00,00,00,00,00,00,\  
   14,00,00,00,02,00,48,00,03,00,00,00,00,00,18,00,1f,00,00,00,01,02,00,00,00,\  
   00,00,05,20,00,00,00,20,02,00,00,00,00,14,00,1f,00,00,00,01,01,00,00,00,00,\  
   00,05,04,00,00,00,00,00,14,00,1f,00,00,00,01,01,00,00,00,00,00,05,12,00,00,\  
   00,01,02,00,00,00,00,00,05,20,00,00,00,20,02,00,00,01,02,00,00,00,00,00,05,\  
   20,00,00,00,20,02,00,00  
   "EnableDCOM"="Y"  
   "LegacyImpersonationLevel"=dword:00000002  
   "MachineAccessRestriction"=hex:01,00,04,80,74,00,00,00,84,00,00,00,00,00,00,00,\  
   14,00,00,00,02,00,60,00,04,00,00,00,00,00,14,00,07,00,00,00,01,01,00,00,00,\  
   00,00,01,00,00,00,00,00,00,14,00,03,00,00,00,01,01,00,00,00,00,00,05,07,00,\  
   00,00,00,00,18,00,07,00,00,00,01,02,00,00,00,00,00,05,20,00,00,00,32,02,00,\  
   00,00,00,18,00,07,00,00,00,01,02,00,00,00,00,00,05,20,00,00,00,2f,02,00,00,\  
   01,02,00,00,00,00,00,05,20,00,00,00,20,02,00,00,01,02,00,00,00,00,00,05,20,\  
   00,00,00,20,02,00,00  
   "MachineLaunchRestriction"=hex:01,00,04,80,78,00,00,00,88,00,00,00,00,00,00,00,\  
   14,00,00,00,02,00,64,00,04,00,00,00,00,00,18,00,1f,00,00,00,01,02,00,00,00,\  
   00,00,05,20,00,00,00,20,02,00,00,00,00,14,00,0b,00,00,00,01,01,00,00,00,00,\  
   00,01,00,00,00,00,00,00,18,00,1f,00,00,00,01,02,00,00,00,00,00,05,20,00,00,\  
   00,32,02,00,00,00,00,18,00,1f,00,00,00,01,02,00,00,00,00,00,05,20,00,00,00,\  
   2f,02,00,00,01,02,00,00,00,00,00,05,20,00,00,00,20,02,00,00,01,02,00,00,00,\  
   00,00,05,20,00,00,00,20,02,00,00  
   "LegacyAuthenticationLevel"=dword:00000002

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\AppCompat]

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\AppCompat\ActivationSecurityCheckExemptionList]  
   "{A50398B8-9075-4FBF-A7A1-456BF21937AD}"="1"  
   "{C73106E0-AC80-11D1-8DF3-00C04FB6EF4F}"="1"  
   "{835BEE60-8731-4159-8BFF-941301D76D05}"="1"  
   "{D9F260BC-EE6A-4c66-A5C3-30B2ECF4C368}"="1"  
   "{91BC037F-B58C-43cb-AD9C-1718ACA70E2F}"="1"  
   "{AD65A69D-3831-40D7-9629-9B0B50A93843}"="1"  
   "{0040D221-54A1-11D1-9DE0-006097042D69}"="1"  
   "{2A6D72F1-6E7E-4702-B99C-E40D3DED33C3}"="1"  
   "{9da0e0ea-86ce-11d1-8699-00c04fb98036}"="1"  
   "{CA6C8347-120F-4122-873F-F89138694AC8}"="1"  
   "{E8494122-79AD-11D2-909C-00A0C9AFE0AA}"="1"  
   "{A373F3DA-7A87-11D3-B1C1-00C04F68155C}"="1"  
   "{C7310557-AC80-11D1-8DF3-00C04FB6EF4F}"="1"

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\Eventlog]  
   "SuppressDuplicateDuration"=dword:00015180

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\Instrumentation]  
   "InstrumentationLogFileDir"="C:\\Windows\\system32\\com"

   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\NONREDIST]  
   "System.EnterpriseServices.Thunk.dll"="($build.empty)"
   ```

