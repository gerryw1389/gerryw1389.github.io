---
title: 'Hyper V: Decommission A VM'
date: 2016-05-24T13:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hyper-v-decommission-a-vm/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - VirtualizationSoftware
---
<!--more-->

### Description:

Follow these steps to de-commision a VM. As a general rule of thumb, it's always better to rename or move than to delete. But when it comes to virtual machines, there is a lot of space involved so act accordingly.

### To Resolve:

1. Before decommissioning a VM, it is good practice to leave it running along side its replacement for a couple days. Chances are, if anything is needed from the old VM, you will find out with a couple days because users will be calling and letting you know.

2. Assuming its safe to go. Go ahead and turn the VM off. What we usually do from here is export it to our NAS. To do this, you just right click the VM => Export => and specify the location.

3. Once the VM has been exported, feel free to delete the VM inside of Hyper V. Note this only deletes the config files, you will have to manually browse to the .vhd file and delete it as well.