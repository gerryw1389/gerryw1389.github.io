---
title: Setup Pi-Hole
date: 2019-04-09T15:38:17+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/setup-pi-hole/
categories:
  - Hardware
  - Networking
tags:
  - Setup
---
<!--more-->

### Description:

So after [setting up](https://automationadmin.com/2017/08/setting-up-raspberry-pi-3/) my PI, I installed Pi-hole for my network on it.

### To Resolve:

1. First you ssh to it:

   ```shell
   sudo vi /etc/dhcpcd.conf
   # set static IP; save and exit
   # change to root
   sudo su
   curl -sSL https://install.pi-hole.net | bash
   ```

   - When I did this, the installer wasn't able to continue because I had changed the IP address of the pi. I then had to modify /etc/dhcpcd.conf and /etc/resolv.conf to also point to 8.8.8.8 for DNS since it cleared it and set everything to only point to 127.0.0.1. I then re-ran the installer for it to setup completely.

2. At the end of the install it gives you the admin password, copy it somewhere. Then type:

   ```shell
   pihole -a -p
   ```

3. Configure router to point to pi => This will vary from vendor to vendor but you typically login to your routers LAN interface in your web browser, then go to lan settings => and set the DNS server handed by DHCP to that of your pi-hole.

4. Commands:

   ```escape
   pihole -b example.com => Adding a site to blacklist  
   pihole -wild example.com => Adding a site and all its subsites to blacklist  
   pihole -w example.com => Adding a site to whitelist  
   pihole -wild -d pubnub.com => Remove a blacklist  
   pihole -up => update it  
   pihole -c => shows stats  
   pihole status => shows stats  
   pihole -q hulu => to query a specific domain  
   pihole disable / enable => Self explanatory  
   pihole restartdns => restart dns server
   ```

5. If you want to block Youtube, add the following to your blacklist section:

   ```escape
   (^|\.)googlevideo\.com$
   (^|\.)youtube\.com$
   (^|\.)ytimg\.l\.google\.com$
   ```

6. Recommended blocklists to add:
   - [MasterBlocklist](https://dbl.oisd.nl/) 
   - [Ransomware](https://tspprs.com/dl/ransomware)  
   - [Scam](https://tspprs.com/dl/scam)  
 

7. Couple other commands I used to clean it up:

   ```shell
   sudo apt update
   sudo apt full-upgrade
   sudo apt clean
   apt -y purge "pulseaudio*"
   ```

   - Update: `pihole -up`

