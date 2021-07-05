---
title: WMI Troubleshooting
date: 2016-05-23T12:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wmi-troubleshooting/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Follow these steps to troubleshoot issues with WMI not working. These usually show up when Powershell or a Networking Monitoring Software such as Spiceworks, PRTG, or SolarWinds are unable to capture WMI input from a target computer.

NOTE: If you are in a domain environment, try applying this GPO to your joined computers in order to open the ports needed for WMI.

### To Resolve:

1. Make sure DCOM is enabled on both computers (probe/remote). Run => `regedit` => Navigate To: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole` => Make sure "Enable DCOM" is set to the value `Y`.

2. The user's credentials should be a domain admin's if on a domain and a local admin, DCOM, and Performance Monitoring if not on a domain.

3. On the probe computer, open Powershell and type:

   ```powershell
   Get-WmiObject -Namespace "root\cimv2" -Class Win32_Process -Impersonation 3 -ComputerName (#remoteComputerName) -Credential (#Provide credentials if you are not running this as the user you will be using on the remote computer).
   ```

   - If you get information, the problem has been resolved.

   - If you get an error, continue

4. Make sure WMI is allowed incoming/outgoing on the firewalls of each computer.

5. Restart the WMI service on the target computer. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type:
   - `net stop winmgmt`  
   - `net start winmgmt`
   - `net start rpcss` #you should get an error saying RPC is already running. 

6. If you don't get this error, Run => `regedit` => Navigate To:
   - `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\RpcSs` and make sure "Start" is set to the value of `2`.  
   - `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server` and make sure that "AllowRemoteRPC" is set to the value of `1`



### References:

["My WMI sensors don't work. What can I do?"](https://kb.paessler.com/en/topic/1043-my-wmi-sensors-don-t-work-what-can-i-do)
