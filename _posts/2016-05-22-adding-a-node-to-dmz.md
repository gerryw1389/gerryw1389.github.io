---
title: Adding A Node To DMZ
date: 2016-05-22T06:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/adding-a-node-to-dmz/
categories:
  - Networking
tags:
  - Router
---
<!--more-->

### Description:

It is common practice for companies to have two networks: one for internal communications and one called the DMZ or external facing nodes like web servers, SFTP servers, or special application servers that need to be accessed externally. For security reasons, it is best practice to setup rules in your firewall that closes all ports to the DMZ nodes except for the specific ones you need opened. Follow these steps to adding a VM to the DMZ.

When we add a device to the DMZ (demilitarized zone), we are essentially making that device public to the WAN and segregating it from our internal network. Data should only flow from LAN to DMZ but not back to the LAN. It is important to realize that all network connections from WAN to LAN still go through the same device in most cases, but is then segregated into different networks. This is done through NAT.  

#### For example:

1. Let's say we have a LAN on 10.10.13.0 and a DMZ network on 10.10.14.0. If we were to purchase and configure/install a web server, we would place it on the DMZ network. Companies do this when they have certain servers or devices that will be accessed from outside the LAN frequently.

2. After you find an available private IP on the DMZ network, say 10.10.14.13, you set that statically, either through the computer's NIC settings or by DHCP Reservations from the DHCP server.

3. Lastly, you &#8220;punch a hole&#8221; in the router to all WAN traffic to flow to that device either fully (which is def not recommended) or by certain means, like for instance a certain port. So for a web server, I would open ports 80 (HTTP) and 443 (HTTPS) for the device at 10.10.14.13 and restrict all other services. This would allow my web server to host web pages while not fully exposing itself to the internet.

### Breakdown on NAT/PAT:

NAT (Network Address Translation)= One public IP WAN side/ multiple private IP's LAN side. Through multiple ports in &#8220;stateful connections&#8221;. You can also have multiple one-to-one relationships where one public IP is equal to one internal IP. See [whatismyipaddress.com](http://whatismyipaddress.com/nat) for more info.

PAT (Port Address Translation)= An extension of NAT that gives each LAN device a port off the public IP. It is known as overloading and port-level multiplexed NAT.

### To Resolve:

1. First, we need to determine which IP we will use. Pick one from the list of available IP's your company should have purchased for external facing nodes.

2. On the VM itself, assign a static internal IP and set the rest of the settings exactly as the server in step 3.

3. It is common practice to have a server in your DMZ handling the DNS for nodes in the DMZ. This is because you NEVER want to have a domain controller in the DMZ. You would then have all nodes in the DMZ point to the DNS server mentioned.

4. Create a &#8220;Host A&#8221; record using the hostname for the VM you want to place in the DMZ.

5. On your company router: Setup rules for the DMZ node for which ports to allow and assign which public IP will be tied to the internal IP (set the NAT translation).

7. Update your DNS provider with the new pointer record public IP => hostname.

8. Update network documentation.

### For LAN DMZ Access Only:

NOTE: Sometimes, you may want to place a device in the DMZ, but not make it accessible from the outside. This is common for like database servers and such. Many companies like mine have rules such that devices can talk from LAN to DMZ but not the other way around. For this reason, some devices have to be placed in the DMZ but not be accessible from outside the LAN.
{: .notice--success}

1. Follow the same steps 1-4 from above.

2. If the server was on the LAN and you are changing to the DMZ:

   - Make sure to delete the LAN Host A record in your company DC's.

   - Make sure to delete any DHCP reservations for the server.

   - Make sure the server has access to your DMZ network. If it's a virtual server, make sure your hyper-visor has the correct NIC associated with it.

3. After setting the IP, you need to configure your firewall through your antivirus (who uses Windows Firewall for security?). Set it up to where only mentioned devices can talk to the machine by MAC address. Inside Symantec Endpoint Protection, you would go to Network Threat Management => Firewall Rules => and create a separate rule for each node in the DMZ that needs communication with this node and place them first. As the next to last rule, have it to where anything on the LAN can communicate with this device on the DMZ. Then as the last rule, block all nodes and all ports.