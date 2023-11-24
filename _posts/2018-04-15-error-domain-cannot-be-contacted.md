---
title: 'Error: Domain Cannot Be Contacted'
date: 2018-04-15T06:36:10+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/error-domain-cannot-be-contacted/
tags:
  - Windows
  - Networking
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

I've seen this error recently in my Hyper-V lab when trying to a join a computer to my domain controller. I knew it was something to do with DNS, but here are the things I did in order to resolve.

### To Resolve:

1. Here are the commands I was running:

   ```powershell
   # First, verify Subnet / Gateway.
   Get-NetIPConfiguration

   # Looks good, let's ping domain controller.
   Test-NetConnection server2012
   # Returns 10.13.13.250 - good

   # Now ping the domain
   Test-NetConnection testdomain.com

   # No replies, dang it. Oh wait! Let's set the domain controller as the primary DNS server

   # Change settings in Network Connections
   Get-NetConnectionProfile
   # See interfaceIndex of 4 for my LAN NIC.
   Get-DnsClientServerAddress -InterfaceIndex 4 -AddressFamily IPv4
   # See that I'm pointing to my gateway as the primary DNS server - wrong!
   Set-DnsClientServerAddress -InterfaceIndex 4 -ServerAddresses ("10.13.13.250","1.1.1.1")

   # Ping testdomain.com again, dang it still fails! Wait, need to flush dns!
   Clear-DNSClientCache

   # Returns domain name, good to go!
   # Now I can try to join again and it should work!
   Add-Computer -Domainname "testdomain.com" -Credential (Get-Credential) -Verbose
   # Success!
   ```

