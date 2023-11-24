---
title: 'PS: Setting Up PS Remoting'
date: 2016-05-30T06:00:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-ps-remoting/
tags:
  - Windows
  - Security
tags:
  - Scripting-Powershell
  - Setup
---
<!--more-->

### Description:

Powershell is a great tool in any Windows admin arsenal. One of the most powerful features is &#8220;PS Remoting&#8221;. One thing you usually have to do on a new computer or a group of servers is enable remoting so that you can run PS from a single computer and use it to run commands on other computers. Typically you just have to type:

   - From Admin CMD:

   ```powershell
   winrm quickconfig
   ```

   - From Admin PS:

   ```powershell
   Set-WSManQuickConfig -force
   # Or
   Enable-PSRemoting
   ```

   - From an admin PS window, but I have seen that fail with something about &#8220;public network&#8221; firewall and then fail again because the computer wasn't in my trusted lists. [This](http://searchwindowsserver.techtarget.com/feature/How-to-enable-PowerShell-remoting) guide is a brief overview on PS remoting rules. Follow these steps to resolve the issues:

### To Resolve:

1. To fix the public network issue you can run &#8220;Enable-PSRemoting -SkipNetworkProfileCheck&#8221; or:

   - Run the following on both machines (local and remote)

   ```powershell
   $networkListManager = [Activator]::CreateInstance([Type]::GetTypeFromCLSID([Guid]"{DCB00C01-570F-4A9B-8D69-199FDBA5723B}"))
   $connections = $networkListManager.GetNetworkConnections()

   # Set network location to Private for all networks

   $connections | % {$_.GetNetwork().SetCategory(1)}
   ```

2. To add a computer as a trusted host:

   ```powershell
   winrm s winrm/config/client '@{TrustedHosts="test"}'

   # or
   Set-Item WSMan:localhostClientTrustedHosts -Value "machineA,machineB"

   # Or to allow any and all computers (not recommended)
   Set-Item WSMan:localhostClientTrustedHosts -Value "*"
   ```

3. PS Remoting should create rules in the firewall for you, but if you need to enable WinRM manually, type:

   ```powershell
   # Older Versions of PS
   netsh advfirewall firewall set rule group="Windows Management Instrumentation (WMI)" new enable=yes

   # WS2012R2 or W8.1+

   Set-NetFirewallRule -Name WINRM-HTTP-In-TCP-PUBLIC -RemoteAddress Any
   ```

4. Try testing by typing:

   ```powershell
   Enter-PSSession -ComputerName (remoteHostName) -Credential (adminUserName)

   # Example
   Enter-PSSession -Computer DC1 -Credential mylab\administrator
   # it will prompt for a password when you connect.
   ```

5. To Enable Remoting remotely:

   ```powershell
   $ArgList = @(
      "powershell"
      "Start-Process powershell"
      "-Verb runAs"
      "-ArgumentList 'Enable-PSRemoting –force;"
      "Set-Item WSMan:localhost\client\trustedhosts -value *'"
      ) -join ' '

   $IWM_Params = @{
      ComputerName = $TargetMachine
      Namespace = 'root\cimv2'
      Class = 'Win32_Process'
      Name = 'Create'
      Credential = $Cred
      # the next value may need to be quoted if it needs to be [string] instead of [int]
      Impersonation = 3
      EnableAllPrivileges = $True
      ArgumentList = $ArgList
      }
   Invoke-WmiMethod @IWM_Params
   ```

6. Make sure to change the `*` on the trusted host to `*.yourdomain.com`.

