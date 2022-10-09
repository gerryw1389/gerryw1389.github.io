---
title: Setting A Static IP For A Computer
date: 2016-05-22T08:11:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-a-static-ip-for-a-computer/
categories:
  - Networking
---
<!--more-->

### Description:

Some Network Admins like to have their workstations set to static IP's through a certain range. This means that the computer is telling the router that if it will have internet/local access, it will be at a specific address rather than the router just handing it whatever in the DHCP range.

NOTE: It is considered bad practice nowadays to have client computers with static IP's. 
{: .notice--success}

Most admins set servers and networking devices statically in a specific range and all the client computers to DHCP. If a computer must have a static IP, it is almost always done at the server level and not on the actual client (they will be set to DHCP but will have a reservation at the server).

### To Resolve:

#### From the Client:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ipconfig/all`. Is it setup statically already or DHCP? Sometimes you may want to place that computers DHCP address as a static IP. Either way, lets set it through the GUI:

2. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `ncpa.cpl` => Local Area Connection => Right Click => Properties => Internet Protocol Version 4 Properties => Properties.

3. Change it from &#8220;Automatically..&#8221; to &#8220;Uses the following&#8221; and enter them there.

4. For the primary DNS Server, set it this way:

   - If the computer is on a domain, set the primary DNS to the DC's IP address and leave the secondary DNS blank.
   - If the computer is on a workgroup, set the primary DNS to the default gateway and the secondary to a public DNS server, I always use 8.8.8.8.

5. Select &#8220;Apply&#8221; and &#8220;Close&#8221; for it to take effect.

#### Through Command Prompt:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/)

   ```console
   netsh interface ip set address name="Local Area Connection" static 192.168.0.100 255.255.255.0 192.168.0.1  
   netsh interface ip set dns name="Local Area Connection" static 192.168.0.250  
   netsh interface ip add dns name="Local Area Connection" 8.8.8.8 index=2
   ```

2. The first `netsh` command assumes your adapter is named &#8220;Local Area Connection&#8221; and you want set a &#8220;static&#8221; IP Address of &#8220;192.168.0.100&#8221; with the subnet of &#8220;255.255.255.0&#8221; and a gateway of &#8220;192.168.0.1&#8221;.

3. The second `netsh` command assumes your adapter is named &#8220;Local Area Connection&#8221; and you want set a &#8220;static&#8221; IP Address of &#8220;192.168.0.250&#8221;

4. The third `netsh` command assumes your adapter is named &#8220;Local Area Connection&#8221; and you want set a add a second DNS IP of &#8220;8.8.8.8&#8221; at index number 2.

5. Repeat step 4 for each DNS server that you want to set, incrementing the index= number each time.

#### From the server:

1. Login to your DHCP server => Open up DHCP Management. Go to leases and convert a lease to a &#8220;reservation&#8221;. That's it!

  <img class="alignnone size-full wp-image-698" src="https://automationadmin.com/assets/images/uploads/2016/09/setting-a-static-ip.png" alt="setting-a-static-ip" width="168" height="547" srcset="https://automationadmin.com/assets/images/uploads/2016/09/setting-a-static-ip.png 168w, https://automationadmin.com/assets/images/uploads/2016/09/setting-a-static-ip-92x300.png 92w" sizes="(max-width: 168px) 100vw, 168px" />


2. Another way to add a static IP is to specify an IP Address and use the MAC of the device and add it to the reservations. This is my preferred method for printers.

3. That is generally best practice to set static IP's for network devices / key servers only! Computers and printers don't really need to be up before the DHCP server.

