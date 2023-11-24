---
title: Troubleshooting VPNs
date: 2016-05-22T06:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/troubleshooting-vpns/
tags:
  - Networking
---
<!--more-->

### Description:

Use this guide for VPN Error codes.

### To Resolve:

1. Find out, does the preshared key work on both ends of the connection? Are both sides of the connection static IP's? Check the settings to see if they have changed.

2. Get on a computer at each end of the VPN if troubleshooting a site-to-site VPN. Check their IP configurations = make sure they are on separate schemes (should have been done on setup).

3. Remote in to the router for each office and make sure it says established. Start pinging the gateways from one office to another, then start pinging the computers on the network.

4. If it is successful, launch the RDP icon and see if it is setup correctly. Right click and edit the icon and check the settings. Double check the username and password.

### VPN Error Codes:

1. VPN Error 800  
&#8220;Unable to establish connection&#8221; – The VPN client cannot reach the server. This can happen if the VPN server is not properly connected to the network, the network is temporarily down, or if the server or network is overloaded with traffic. The error also occurs if the VPN client has incorrect configuration settings. Finally, the local router may be incompatible with the type of VPN being used and require a router firmware update.

2. VPN Error 619  
&#8220;A connection to the remote computer could not be established&#8221; = A firewall or port configuration issue is preventing the VPN client from making a working connection even though the server can be reached.  
More Info

3. VPN Error 51  
&#8220;Unable to communicate with the VPN subsystem&#8221; = A Cisco VPN client reports this error when the local service is not running or the client is not connected to a network. Restarting the VPN service and/or troubleshooting the local network connection often fixes this problem.

4. VPN Error 412  
&#8220;The remote peer is no longer responding&#8221; = A Cisco VPN client reports this error when an active VPN connection drops due to network failure, or when a firewall is interfering with access to required ports.

5. VPN Error 721  
&#8220;The remote computer did not respond&#8221; = A Microsoft VPN reports this error when failing to establish a connection, similar to the error 412 reported by Cisco clients.

6. VPN Error 720  
&#8220;No PPP control protocols configured&#8221; = On a Windows VPN, this error occurs when the client lacks sufficient protocol support to communicate with the server. Rectifying this problem requires identifying which VPN protocols the server can support and installing a matching one on the client via Windows Control Panel.

7. VPN Error 691  
&#8220;Access denied because username and/or password is invalid on the domain&#8221; = The user may have entered the wrong name or password when attempting to authenticate to a Windows VPN. For computers part of a Windows domain, the logon domain must also be correctly specified.

8. VPN Errors 812, 732 and 734  
&#8220;The connection was prevented because of a policy configured on your RAS/VPN server&#8221; = On Windows VPNs, the user attempting to authenticate a connection may have insufficient access rights. A network administrator must resolve this problem by updating the user's permissions. In some cases, the administrator may need to update MS-CHAP (authentication protocol) support on the VPN server. Any of these three error codes may apply depending on the network infrastructure involved.

9. VPN Error 850 (Windows 8)  
&#8220;Error 850: The Extensible Authentication Protocol type required for authentication of the remote access connection is not installed on your computer.&#8221; when trying to connect to a VPN in Windows 8 or Server 2012. This boils down to a default authentication setting being unset depending on the type of VPN it is. To Resolve: Run => `ncpa.cpl` => Right click on a VPN Connection => Properties. Inside Properties, go to the Security tab and select the correct radio button that matches your VPN.