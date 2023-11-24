---
title: WannaCry Virus
date: 2017-05-24T14:40:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/05/wannacry-virus/
tags:
  - Windows
tags:
  - Viruses
---
<!--more-->

### Description:

Last week, a new worm was unleashed that was hitting many organizations that had certain ports exposed to the internet. This is a guide to avoid this attack:

### To Resolve:

1. The main fix: Block 139/445 at firewall, patch all servers

2. More detailed:

   - Check if SMB1 is enabled (2012 and above):

   ```powershell
   Get-SmbServerConfiguration | Select EnableSMB1Protocol
   ```

   - 2008 R2 and below:

   ```powershell
   Get-ItemProperty -path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" SMB1
   ```

   - If you want to fix it on an individual machine (2012 and above):

   ```powershell
   Set-SmbServerConfiguration -enableSMB1Protocol $false -confirm:$false
   ```

   - Fixing an individual system on 2008 R2 and below:

   ```powershell
   Set-ItemProperty -path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" SMB1 -Type DWORD -Value 0 -Force
   ```

3. If you want to fix it network wide => GPO to disable it (works for all OSes):

   ```escape
   Computer Configuration\Preferences\Windows Settings\Registry:
   Action: Update
   Hive: HKEY_LOCAL_MACHINE
   Key Path: SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters
   Value name: SMB1
   Value Type: REG_DWORD
   Value Data: 0 (hexadecimal)
   ```

4. Things this will break if you implement these fixes: Mainly scan-to-folder functions on Multifunctional printers/ check Reddit for others

### References:

["WannaCry Megathread"](https://www.reddit.com/r/sysadmin/comments/6bacmd/wannacry_megathread/)  
