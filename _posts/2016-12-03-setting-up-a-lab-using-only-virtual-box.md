---
title: Setting Up A Lab Using Only Virtual Box
date: 2016-12-03T01:58:09+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/setting-up-a-lab-using-only-virtual-box/
tags:
  - Networking
tags:
  - Router
  - Setup
  - VirtualizationSoftware
---
<!--more-->

### Description:

So I have had a home lab on my computer for years at home, but I tasked myself of setting one up with one of my servers at work with Virtual Box. Follow these steps to setup a lab on your network that will have access to the internet, but no contact with anything on your main network.

### To Resolve:

1. First, I had to come up with a different subnet for my lab, I chose `10.30.30.0/24`.

2. Get ISO's for 3 VMs: One PFSense, One domain controller (I used a 2016 server license), and one client (I used W10 and an existing W7 VM).

3. Set the network on all VM's to have only &#8220;internal network&#8221; with whatever name you want. I just kept the default of `intnet`. Note that with this option, the VM's can talk to each other but nothing else can assuming you place them in their own subnet.

4. On the PFSense VM only, add a second &#8220;Bridged&#8221; network that will be used to pass traffic from your regular LAN to the VM's on the internal network. *But isn't that bad? I mean your setting up a second domain within your current domain?* Don't worry, we will get to that.

5. On the PFSense VM, mount the ISO and install the OS. NOTE: At the main menu, hit the key to get out of it and then press `i` to install. For some reason, I can never get this on the first try so feel free to try a couple times.

6. Once the OS has installed, remove the iso when it prompts for a reboot. Boot the machine and make sure that your bridged adapter is the WAN (default name `em0`) and your internal network is the LAN (default named `em1`).

7. Press the number to configure your LAN. I changed it from the default. Answer the questions to change `192.168.1.1` to `10.30.30.254`, `/24`, `no dhcp`, `yes` to enable the web GUI using http.

8. Now on one of the Clients, boot them up and open a browser to `http://10.30.30.254` to go through the setup wizard. Default login `admin/pfsense`. Go through the wizard, set WAN to get DHCP address (on my LAN, we have a DHCP server => yours probably does too!). Uncheck the two boxes under the LAN interface under the section &#8220;Reserved Networks&#8221; that are checked by default. Finally, change password for your admin account.

9. Now, on the landing page, go to Firewall => Rules (on the top drop down). Create a rule like:

   ```escape
   Action = Drop  
   Interface = LAN  
   Address Family = ipv4  
   Protocol = any  
   Source = any  
   Destination = Network AND 10.0.0.0 / 8 # This is where you put your LAN network in. Our LAN is a 10.0.0.0/8 IP, so I am blocking traffic to any of it.  
   Description = BlockLANtoWAN

   # after you create the rule, make sure to hit apply, the router will reload automatically.
   ```

10. That's it! I tested by pinging from my internal network (`intnet` from step 3) out to my LAN and all packets were dropped! Pings to internet IPs went through fine. I tried a couple `\\ServerComputerName\Shares` and vice versa and found that **ALL PACKETS WERE DROPPED**. Good to go.

11. I will probably break this out into another post, but from here, I just enabled AD DS, DNS, DHCP on the Server 2016 VM and joined the clients to the domain and set DHCP reservations for them. All worked as planned without interfering with the internal network.

12. Update 2017-12-22 = I had an issue where my VM's behind my pfSense Firewall could not get to the internet. I could ping 8.8.8.8 but not Google.com. This is common if you have DNS issues. Since I had a DNS server behind the firewall I thought I would test from there. Spent a couple hours trying this and that, but the final fix was to:

   - Details: Prod network = 10.12.12.x / PFsense network = 10.30.30.x

   - In the client VM, open PFsense in Edge by going to 10.30.30.254

   - Go to Firewall => Aliases => Create New: Name = "SafeAddresses" => Add the hosts of switches/routers/dns servers needed for internet access. In my case 10.12.12.250 (AD/DNS Server from prod network), 10.12.12.242 (main prod network switch), and 10.12.12.254 (prod network firewall/gateway).

   - Go to Firewall => Rules => LAN. Create one called &#8220;Safe' and set it like:

   ```escape
   Source =  LAN Net  
   Destination Alias - SafeAddresses  
   Allow and log
   ```

   - Then make sure the one in step 9 from above is there.

   - Then, in your DHCP Server behind the pfSense firewall, configure DNS Servers = Prod networks main dns server, then yours. So in my example: 10.12.12.250, 10.30.30.90.

   - On the domain controller behind the pfsense firewall (10.13.13.90), set DNS to your domain controller as primary and the prod networks as secondary => 10.30.30.90 and 10.12.12.250.

