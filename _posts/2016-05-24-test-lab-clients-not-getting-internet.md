---
title: 'Test Lab: Clients Not Getting Internet'
date: 2016-05-24T14:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/test-lab-clients-not-getting-internet/
tags:
  - Networking
tags:
  - TestLab
---
<!--more-->

### Description:

So I setup a Domain Controller in my VMWare Workstation setup the other day and I got caught up on such a trivial issue. My DC could access the internet but none of my clients could even though I had all my settings setup correctly. The Fix: I had recently redone my network and removed my Home network card from each machine and only had my vmnet7 (DC LAN) enabled. I thought since it had the correct Default Gateway the computers would get internet, but alas my vmnet7 does not have any access to the WAN! Needed to install RAS (Routing and and Remote Access) which I didn't.

### My Setup:

1. So here are the NIC settings for my DC:

   ```escape
   NIC1: Home  
   DHCP  
   192.168.0.150 (reserved router side)

   NIC2: LAN  
   192.168.13.10  
   255.255.255.0  
   192.168.13.1 (vmnet7 in vWorkstation DHCP disabled due to me having a DC with DHCP/DNS)

   NIC3: iSCSCI  
   192.168.89.10  
   255.255.255.0  
   192.168.89.1 (vmnet2 in vWorkstation DHCP disabled due to me having a DC with DHCP/DNS)
   ```

2. Due to NIC1 having access to my home network on my DC, I could ping 8.8.8.8 just fine and was pulling the appropriate info in ipconfig /all.

3. The clients would get the following output from cmd:

   ```console
   ipconfig /all  
   192.168.13.x (something in the DHCP range)  
   255.255.255.0  
   192.168.13.1  
   DHCP/DNS: 192.168.13.10

   nslookup google.com  
   Server: Unknown  
   IP: 192.168.13.10
   ```

4. What threw me off is when I would ping google.com, they would resolve the IP but the packets would just &#8220;request timed out&#8221;. I then did the regular troubleshooting and pinged:

   - Local IP = all good  
   - DC IP/hostname = all good  
   - Router IP/Hostname = all good  
   - Started a tracert to 8.8.8.8 and noticed it wouldn't even get one hop.

5. I had even gone into DHCP on the DC and set the server options:

   ```escape
   003 = Router 192.168.13.1  
   005 = Name Servers 192.168.13.10  
   006 = DNS Servers 192.168.13.10  
   015 = int.domain.com
   ```

6. I started thinking to myself, why the hell does this always work on a real network and not this one? Then it dawned on me, If the default gateway cannot route packets, how the hell are we supposed to get anything past the LAN!

   - NOTE TO SELF: Read [the following Technet article](https://technet.microsoft.com/en-us/library/cc731671(v=ws.10).aspx) to setup RAS if you want your DC to do LAN-WAN conversions (not common unless you setup a VPN server).
