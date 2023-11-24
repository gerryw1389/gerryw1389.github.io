---
title: Setting Up A VPN On Checkpoint Router
date: 2016-05-22T06:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-a-vpn-on-checkpoint-router/
tags:
  - Networking
tags:
  - Router
  - Setup
---
<!--more-->

### Description:

If you ever want to connect a VPN (Virtual Private Network) to work from home at your work network, follow this guide. Other setups are network to network VPN's and Mesh VPN's for multiple networks. Note: You will need to have a static IP address for this to work long term. This usually cost extra and must be purchased from your ISP.

#### Client VPN: Individual Users To A Network

   - Rules:  
   - Some configuration will need to be done on the remote computer  
   - Static public IP address  
   - No duplicate LAN schemes

1. For Checkpoint routers, the first thing you do is log in to the router at your work network. Do this by opening a web browser and going to the default gateway IP address or entering &#8220;my.firewall&#8221; in the website address field.

2. Go to the &#8220;VPN&#8221; section => Check the &#8220;Allow L2TP Clients to connect&#8221;, check the &#8220;bypass firewall&#8221; option, and type a password into the Preshared key field.

3. Go to the &#8220;Users&#8221; section => Create New User => create a username and password.

4. Assign the user whichever rights you need and check the &#8220;VPN Remote Access&#8221; => Done.

#### On the remote computer:

5. Go to &#8220;Setup a New Connection&#8221; using network connections in the control panel.

6. Enter the &#8220;public IP address&#8221; of the network you want to connect to.

7. Name the connection.

8. Check the &#8220;Don't connect now&#8221; box.

9. Type in the same username and password for the user that you created on the router at the other end of the connection. The connection is created.

10. Run `ncpa.cpl` => right click on the connection => security tab- advanced.  
   - For W7 click Security => Layer 2 Tunneling Protocol => Advanced.  
   - For XP click Security => IPSec settings.

11.  Select the &#8220;Use preshared key authentication&#8221; and type in the password you created.

12.  After it's connected, ping the router's IP address at the remote location. Try pinging the server at the location as well. You have successfully created the VPN.

#### Site To Site VPN: Network To Network Connection

   - Rules:  
   - Modem must be bridged  
   - 3 total sites is the max if using Checkpoint routers  
   - Static public IP  
   - No duplicate LAN schemes

1. For Checkpoint routers, the first thing you do is log in to the router at your work network. Do this by opening a web browser and going to the default gateway IP address or entering &#8220;my.firewall&#8221; in the website address field.

2. Go to the &#8220;VPN&#8221; section => new site => site-to-site => next => Enter the destination IP of the site you want to connection to (see below) => turn on &#8220;Bypass firewall policy&#8221; => next => specify configuration => next => specify the destination IP scheme (Make sure to place a 0 in the last octet to specify the whole network. Ex: 192.168.1.0) => Skip the backup gateway => Select the &#8220;Shared Secret&#8221; for authentication method => Type &#8220;your password&#8221; (You only get one chance at this, don't get it wrong.) => Select &#8220;3DES/MD5&#8221; for both options => Uncheck the &#8220;Try to connect&#8221; option => Name the site something that makes sense => like the name of the network => check the &#8220;keep this site alive&#8221; box.

   - The destination IP is the IP of the Gateway accepting the tunnel. If the modem is truly bridged these numbers will match. If the modem is semi bridged and still active on the network they will be different. For example, by default, Comcast techs do not bridge their modems on install, they put it into a &#8220;pseudo-bridged&#8221; mode with a firewall and interface still active. So you would use the &#8220;IP Address of the WAN connection&#8221; on the router => not the Public IP Address.

   - An easy to to test if a modem is bridged or not is to create a rule on the router to allow port 3389 to forward to a computer on the network. Make sure that computer has RDP enabled (`sysdm.cpl` => Remote => Allow RDP Connections (less secure)). After creating the rule, try and RDP to the computer, if it works => the modem is bridged, if it doesn't => the modem is not bridged.

  <img class="alignnone size-full wp-image-703" src="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-1.png" alt="setting-up-a-vpn-1" width="843" height="258" srcset="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-1.png 843w, https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-1-300x92.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-1-768x235.png 768w" sizes="(max-width: 843px) 100vw, 843px" />

  <img class="alignnone size-full wp-image-704" src="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-2.png" alt="setting-up-a-vpn-2" width="747" height="313" srcset="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-2.png 747w, https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-vpn-2-300x126.png 300w" sizes="(max-width: 747px) 100vw, 747px" />

3. Do this at each site. Ping the remote Checkpoint router and server. Done.

#### Mesh VPN: Handled At the Cloud Level and Configured By Remote Support

   - Rules:  
   - More than 3 sites can be connected.  
   - Each site has to be connected to the service center.  
   - Will work with DHCP public IP Addresses.  
   - No duplicate LAN schemes.