---
title: 'PS: Setup A DC Using HyperV'
date: 2018-11-24T17:23:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/ps-setup-a-dc-using-hyperv/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Modules
---
<!--more-->

### Description:

Follow this guide to install a domain controller using Hyper-V Powershell commands

### To Resolve:

1. Create a Hyper-V Switch with Bridged Networking

   ```powershell
   # Install the entire Hyper-V stack (hypervisor, services, and tools)
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

   # Install the Hyper-V Switch
   $net = Get-NetAdapter -Name 'Ethernet'
   New-VMSwitch -Name "External VM Switch" -AllowManagementOS $True -NetAdapterName $net.Name
   ```

2. Create Domain Controller

   ```powershell
   $params = @{
      Name               = "DC"
      MemoryStartupBytes = "2147483648"
      Generation         = "2"
      SwitchName         = "VMNetwork"
      NewVHDSizeBytes    = "21474836480"
      NewVHDPath         = "c:\vms\dc.vhdx"
   }
   New-VM @params
   Set-VM -Name DC -ProcessorCount 2
   Add-VMDvdDrive -VMName DC
   Set-VMDvdDrive -VMName DC -Path C:\iso\server2016.ISO
   Set-VMFirmware -VMName DC -FirstBootDevice $(Get-VMDvdDrive -VMName DC)
   Start-VM -Name DC
   ```

3. After OS install:

   ```powershell
   $params = @{
      InterfaceAlias = "Ethernet"
      IPAddress      = "192.168.1.100"
      PrefixLength   = "24"
      DefaultGateway = "192.168.1.254"
   } 
   New-NetIPAddress @params
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.1.254
   Rename-Computer -NewName DC -Restart
   ```

4. Adding the role

   ```powershell
   Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
   $params = @{
      DomainName                    = "gdub.test"
      DomainNetbiosName             = "gdub"
      DomainMode                    = "Default"
      DatabasePath                  = "C:\Windows\NTDS"
      CreateDnsDelegation           = $false
      ForestMode                    = "Default"
      InstallDns                    = $true
      LogPath                       = "C:\Windows\NTDS"
      NoRebootOnCompletion          = $false
      SysvolPath                    = "C:\Windows\SYSVOL"
      Force                         = $true
   }
   Install-ADDSForest @params
   ```

