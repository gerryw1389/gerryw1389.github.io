---
title: Server Core Tasks
date: 2018-08-05T07:10:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/server-core-tasks/
categories:
  - Windows
  - WindowsServer
---
<!--more-->

### Description:

When installing Server Core, it is common to do tasks such as these.

### To Resolve:

1. Set IP Address/ Gateway/ DNS:

   ```powershell
   Get-NetAdapter
   New-NetIPAddress -InterfaceIndex 2 -IPAddress 192.168.1.101 -PrefixLength 24 -DefaultGateway 192.168.1.1
   Set-DNSClientServerAddress -InterfaceIndex 2 -ServerAddresses @("8.8.8.8", "8.8.4.4")
   ```

2. Enable/Disable Windows Firewall:

   ```powershell
   Set-NetFirewallProfile -Name Public,Private,Domain -Enabled False
   ```

3. Add/Remove features:

   ```powershell
   Get-WindowsFeature | Where-Object Installed -eq True
   ```

4. Join to Domain:

   ```powershell
   Add-computer -DomainName mydomain.com
   ```

5. Activate Windows: 
    
   - To see current license: `slmgr /dlv`  
   - To activate: `Slmgr /ato`

6. Add local users:

   ```powershell
   net user gerry MyPass! /add
   net localgroup administrators gerry /add
   ```

   - Then, on the actual host, sign out. Hit esc, other sign in options => .\gerry and sign in just to make sure the account is there.

7. Verify the current Windows Update setting:  `%systemroot%\system32\Cscript scregedit.wsf /AU /v`

   - To enable automatic updates: 

   ```escape
   Net stop wuauserv  
   %systemroot%\system32\Cscript scregedit.wsf /AU 4  
   Net start wuauserv
   ```

   - To disable automatic updates, run:  

   ```escape
   Net stop wuauserv  
   %systemroot%\system32\Cscript scregedit.wsf /AU 1  
   Net start wuauserv
   ```


