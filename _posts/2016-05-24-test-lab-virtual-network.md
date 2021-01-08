---
title: 'Test Lab: Virtual Network'
date: 2016-05-24T13:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/test-lab-virtual-network/
categories:
  - Networking
tags:
  - TestLab
---
<!--more-->

### Description:

These are the steps I took to put my VMs on a private virtual network.


### To Resolve:

1. First thing I wanted to do was to decide on which type of network these machines will reside on, if you want internet on each machine, you could simply install a "Bridged Networking" NIC on each of the VMs and assign them an IP on your LAN. But like most who are building a test lab, I wanted a segregated network where the machines can talk to each other, but not to the WAN or any of my machines on the LAN (except for my host).

2. So you launch VMWare workstation and go to Edit => Virtual Network Editor. It will bring up 3 defaults VMNet0, 1, and 8. Don't use any of these, select your own.

3. It will default to "Host-Only" => this is what you want. Make sure to uncheck the DHCP Server option if you have a Server OS that will have have the DHCP server role. Feel free to to change the subnet to whatever. I used VMNet 13 with the IP: `10.10.13.0` and subnet mask `255.255.255.0`. Done.

4. Now go to each VM => Settings => Change the NIC to "Custom" and select the network you just created.

5. Follow the steps in [Test Lab Domain Setup](https://automationadmin.com/2016/05/test-lab-domain-setup/) for further DHCP Settings, but the virtual private network is officially setup after step 4.

### References:

["Creating subnets in VMware Workstation (1020480)"](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1020480)