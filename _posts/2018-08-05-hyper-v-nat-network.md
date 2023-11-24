---
title: Hyper-V NAT Network
date: 2018-08-05T07:16:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/hyper-v-nat-network/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - VirtualizationSoftware
---
<!--more-->

### Description:

If you ever need to create a NAT Network using Hyper-V, follow these steps.

### To Resolve:

1. Create a new Hyper-V Virtual Switch

   ```powershell
   New-VMSwitch –SwitchName "NATSwitch" –SwitchType Internal
   ```

1. Configure the NAT Gateway IP Address: This configures the Virtual Network Adapter which was created while creating the Internal Virtual Hyper-V Switch.

   ```powershell
   New-NetIPAddress –IPAddress 10.10.10.1 -PrefixLength 24 -InterfaceAlias "vEthernet (NATSwitch)"
   ```

3. Now you can configure the NAT rule

   ```powershell
   New-NetNat –Name MyNATnetwork –InternalIPInterfaceAddressPrefix 10.10.10.0/24
   ```

4. After that you have finally created your NAT network and you can now use that network to connect your virtual machines and use IP Address from 172.21.21.2-172.21.21.254.

5. Create a new NAT forwarding

   - To forward specific ports from the Host to the guest VMs you can use the following commands. This example creates a mapping between port 80 of the host to port 80 of a Virtual Machine with an IP address of 10.10.10.2.

   ```powershell
   Add-NetNatStaticMapping -NatName "VMSwitchNat" -Protocol TCP -ExternalIPAddress 0.0.0.0 -InternalIPAddress 10.10.10.2 -InternalPort 80 -ExternalPort 80
   ```

   - This example creates a mapping between port 82 of the Virtual Machine host to port 80 of a Virtual Machine with an IP address of 10.10.10.3.

   ```powershell
   Add-NetNatStaticMapping -NatName "VMSwitchNat" -Protocol TCP -ExternalIPAddress 0.0.0.0 -InternalIPAddress 10.10.10.3 -InternalPort 80 -ExternalPort 82
   ```