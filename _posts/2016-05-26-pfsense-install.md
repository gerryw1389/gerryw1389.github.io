---
title: PFSense Install
date: 2016-05-26T04:08:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/pfsense-install/
tags:
  - Unix
tags:
  - Router
  - Setup
---
<!--more-->

### Description:

Follow these steps to install and configure Pfsense, the free router OS.

### To Resolve:

1. Get the download file from [pfsense.org](https://www.pfsense.org/). I chose the 64-bit (v2.2.24 LiveCD) version.

2. Launch your VM creation software (VMware Workstation for me).

3. Select FreeBSD 64bit and finish installing how you normally do. Make sure you have two network adapters, one bridged (WAN) and one internal (LAN to be assigned by PF). Make sure that you don't enable the DHCP server on the Network editor if you want Pfsense or a domain controller to be assigning IP's on that subnet.

   - So to recap:
   - NIC1: VMnet0 => Bridged (automatic)
   - NIC2: VMnet10 => Host-Only 10.13.13.0 (just make up any subnet, you will change it anyways) MAKE SURE DHCP is not enabled in your virtual network editor.

4. Once it launches, it will bring you to a menu and start to boot automatically. Let it get to the screen where it counts down from 10, and type &#8220;I&#8221; to launch the installer.

5. On the installer, just hit &#8220;accept these settings&#8221; and continue. On the next screen select &#8220;OK&#8221;, and then &#8220;Standard Kernel&#8221;, then &#8220;reboot&#8221;.

6. Pfsense is now installed! Now press F1 to boot into it. If you have been following along, your screen should look like mine below. Note that I had the bridge adapter set as my first NIC and it has the name of &#8220;em0&#8221; (WAN) and my second internal network adapter NIC is called &#8220;em1&#8221; which will be my LAN link.

  <img class="alignnone size-full wp-image-687" src="https://automationadmin.com/assets/images/uploads/2016/09/pfsense.png" alt="pfsense" width="688" height="277" srcset="https://automationadmin.com/assets/images/uploads/2016/09/pfsense.png 688w, https://automationadmin.com/assets/images/uploads/2016/09/pfsense-300x121.png 300w" sizes="(max-width: 688px) 100vw, 688px" />

7. Now select the option &#8220;2&#8221; to set a static IP for your LAN link. I set mine to 172.21.14.1 with a start dhcp of 172.21.14.100 and ending of 172.21.14.200.

8. Now just leave that running and open up a client VM and assign it the same network as the LAN link on Pfsense (VMnet10 for me) and run a quick:

   ```console
   ipconfig /release  
   ipconfig /renew
   ```

9. After this, the client should be able to access the UI for Pfsense. Open up a web browser and go to the LAN IP you assigned in step 7.

10. Login using &#8220;admin/pfsense&#8221; and either skip the wizard or go through it to configure your new router. Enter the information for your router and get to the part where you change your PFsense password. After that, it reloads and you are done! Now all you have to do is configure the router the way you want for your network.