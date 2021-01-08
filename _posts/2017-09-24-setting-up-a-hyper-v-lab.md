---
title: Setting Up A Hyper-V Lab
date: 2017-09-24T05:57:43+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/setting-up-a-hyper-v-lab/
categories:
  - Networking
tags:
  - TestLab
---
<!--more-->

### Description:

This post will be similar to my post on [using VirtualBox](https://automationadmin.com/2016/12/setting-up-a-lab-using-only-virtual-box/). # NOTE: Requires 3 images: PFSense, WS2016, and W10v1703.

Hyper-V Switch Notes:

   - External switch uses a physical nic to access the network outside of the hyper v host.
   - Private switch only allows network traffic between the VMs.
   - Internal switch allows the host to talk to the VMs (and VM to VM communication).
   - When setting internal or private switch, use static IP. You can't use DHCP unless one of the VMs is acting as a Domain Controller. E.g. VM1 has IP 10.0.0.1, VM2 has IP 10.0.0.2 and both have Netmask 255.255.255.0

You should be able to ping between both VMs now if you set up a Private switch. If you're using an Internal Switch, set the IP of the host machine to the same range and you should be good to go. Follow the links in the previous post (mentioned above) and substitute where necessary.

### To Resolve:

1. Create Two Switches:

   - Virtual Switch Manager => New Virtual Switch => Bridgednet => Connect To External Network And Choose Your Nic. This Will Be The One That Talks To Prod Network
   - Virtual Switch Manager => New Virtual Switch => Internal_LAN => Connect To Privatenetwork. This will be your network that can't reach prod. It does not have an ip address schema, you make it up yourself.

2. Create PFSense VM with two NIC's (from above) and set WAN to Bridged and LAN to Internal_LAN. Set that LANtoWAN rule from the other article.

3. Create your domain controller using only the Internal_LAN as the NIC but don't enable DHCP role. Set a static IP using PFSense's LAN ip as the default gateway.

4. Do the same thing to both clients.

5. That's it! You have a network that can't reach prod with which you can test GPO's (since one is domain joined). I personally like to update and snapshot the non-domain joined one and use it to test Powershell scripts on since you can copy and paste through the clipboard. One note about this is that since the networks are separated, it is difficult (but not impossible) to share files from your machine to your test lab. The way around this is to:

   - On the W10 machine that is not domain joined, create a share like `c:\scripts` and set share permissions to everyone\full control. Then go to security and give everyone full permissions.
   - Click on the VM Settings and change it's NIC from Internal_LAN with a static IP to Bridgednet. Then run `ncpa.cpl` and move the two radio buttons to "automatically obtain".
   - This will put your VM on your prod network. Run `ipconfig`, get the IP, and then do `\\ipaddress\scripts` and enter a username and password (the one you login with).
   - Copy files from your machine to it and then reverse the steps: Switch the VM back to Internal_LAN, change the NIC settings in Windows back to static and fill in the information.

----

### Here another to say this:

### Description:

Follow these steps to create a test lab on your work laptop.

### To Resolve:

1. Install Hyper-V role on your machine.

2. Download ISO's from MS Dreamspark or however you get your ISOs

   - Names:
   - Windows 10 Enterprise  
   - Server 2016 Datacenter  
   - [Pfsense v2.3.4](https://www.pfsense.org/download/)

3. So after enabling Hyper v, create a path on your machine called:

   - C:\hyperv\isos => placed iso's  
   - C:\hyperv\disk  
   - C:\hyperv\config

4. Open Hyper-V and go to Edit => HyperV Settings and set:

   - Defaults for Hard Disk Files: `C:\hyperv\disk\`  
   - Defaults for Virtual Machine Files: `C:\hyperv\config\`

5. Now, create two networks under Edit => Virtual Switch Manager: One public (external network connected to your physical adapter) / one private => I called mine "gwill_priv"

6. Create three vms:

   - Pfsense => NIC1: home LAN; NIC2: gwill_priv network. Set nic's: hn0 = WAN/ hn1 = LAN. Set WAN to DHCP and LAN to 10.12.12.254. Set its subnet to 24 (that is 255.255.255.0)  
   - Server2016 => gwill_priv network  
   - Client => gwill_priv network

7. Install OSes, remove DVD's

   - After the OS is installed, set static IP's:  
     - Set static IPs  
     - IP: 10.12.12.50  
     - Subnet: 255.255.255.0  
     - DG: 10.12.12.254  
     - DNS1: 129.107.35.89  
     - DNS2: 129.107.56.180

   - For server2016:  
     - 10.12.12.100 server  
     - admin/pfsense  
     - Subnet: 255.255.255.0  
     - DG: 10.12.12.254  
     - DNS1: 129.107.35.89  
     - DNS2: 129.107.56.180

8. On the W10 VM, launch internet browser and go to: http://10.12.12.254 and sign in with admin/pfsense

   - Accept defaults and change your password.

   - Go to Firewall – Aliases – Create New: Name = "SafeAddresses" – Add the hosts of switches/routers/dns servers needed for internet access.  
     - So I added:  
     - 192.168.0.50 => dns1.gdub.local  
     - 192.168.0.51 => dns2.gdub.local

   - Go to Firewall – Rules – LAN. Create one called "Safe' and set it like:  
     - Action: Allow  
     - Interface: LAN  
     - Address Family: IPv4  
     - Protocol: Any  
     - Source: LAN Net  
     - Destination: Single host or Alias – Type: SafeAddresses  
     - Description: AllowSafe

   - Create a second rule BELOW it  
     - Action: Block (drop silently)  
     - Interface: LAN  
     - Address Family: IPv4  
     - Protocol: Any  
     - Source: LAN Net  
     - Destination:Network AND 192.168.0.0 / 8 #<– This is where you put your LAN network in. My home network is a 192.168.0.0/8 IP, so I am blocking traffic to any of it.  
     - Description: BlockLANtoWAN

   - What these basically say is allow LAN to talk to specific hosts on LAN for certain services, but block most of the network
   - Test by pinging devices on your home network. Everything should drop except those to our DNS servers. In my case, my firewall rules weren't working. I went into the web GUI and found:

   ```escape
   There were error(s) loading the rules: /tmp/rules.debug:18: cannot define table bogonsv6: Cannot allocate memory => The line in question reads [18]: table <bogonsv6> persist file "/etc/bogonsv6"_ `
   @ 2018-09-23 13:13:10`
   There were error(s) loading the rules: /tmp/rules.debug:18: cannot define table bogonsv6: Cannot allocate memory => The line in question reads [18]: table <bogonsv6> persist file "/etc/bogonsv6"_ `
   @ 2018-09-23 13:13:13
   ```

   - A quick Google search returned this fix: Go to System => Advanced => Firewall & NAT => Increase the Firewall Maximum Table Entries size to 400000
   - I applied it and rebooted, all working now!

9. Now Activate Windows by using MAK keys.

10. Install updates over and over until they say "up to date".

11. Lastly, right click the VM's and "create snapshot". We will be using these VMs for testing often so a baseline snapshot is mandatory for reverts.

