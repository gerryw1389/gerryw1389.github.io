---
title: 'PS: Connecting To VPNs In W10'
date: 2017-09-24T06:03:54+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/ps-connecting-to-vpns-in-w10/
categories:
  - Networking
tags:
  - Router
---
<!--more-->

### Description:

So after reimaging my machine at work, I looked into a way I could setup my VPN using powershell. Here is how assuming you are using L2TP with a pre-shared key.

### To Resolve:

1. Copy and save as a .ps1 file in notepad:

   ```powershell
   $VpnName = "Datacenter"
   $Pre = Read-Host -Prompt "Enter Preshared Key"
   $VPN = Add-Vpnconnection -Name $VpnName -Serveraddress "vpnserver.domain.com" -Tunneltype L2tp `
   -Encryptionlevel Required -Authenticationmethod Mschapv2 -L2tppsk $Pre -Remembercredential -Passthru
   Start-Sleep 3
   Write-Output "Setting Registry Entry For L2TP VPNs"
   $Registrypath = "Hklm:\System\Currentcontrolset\Services\Policyagent"
   $Name = "AssumeUDPEncapsulationContextOnSendRule"
   $Value = "2"
   If (!(Test-Path $Registrypath))
   {
      New-Item -Path $Registrypath -Force | Out-Null
   }
   New-Itemproperty -Path $Registrypath -Name $Name -Value $Value -Propertytype Dword -Force | Out-Null
   If ($Vpn.Connectionstatus -Eq "Disconnected")
   {
      $Password = Read-Host -Prompt "Enter User Password For VPN"
      Cmd /c "Rasdial $VpnName domain.com\yourUserName $Password"
      
      Start-Sleep 3
      # Connect To Any Machine On The Destination Network
      If ( Test-Netconnection 192.168.0.23 -Informationlevel Quiet)
      {
         Write-Output "Connected To Vpn"
      }
      Else
      {
         Write-Output "Not Connected To Vpn"
      }
      $Input = Read-Host "Would You Like To Disconnect The Vpn? (Y)Yes Or (N)No"
      If ($Input -Eq 'Y')
      {
         Cmd /c "Rasdial /Disconnect"
      }
      Else
      {
         Exit
      }
   }
   ```

