---
title: 'Hyper V: To Create A New VM'
date: 2016-05-24T13:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hyper-v-to-create-a-new-vm/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - VirtualizationSoftware
---
<!--more-->

### Description:

Follow these steps to create a new virtual machine in Hyper V.

### To Resolve:

1. Obviously, make sure we have the HDD space and Memory available before attempting to create a new VM. Check the physical host for these requirements.

2. Next, you want to figure out what network segment the VM is going to be hosted on. Inside Hyper-V, there is a virtual network manager that you have to setup prior to installing any VM's. This is built in and is usually configured in parallel with the physical network ports.

   - In the screenshot below, both virtual NIC's are set to share the network adapter with the physical NICs.

  <img class="alignnone size-full wp-image-731" src="https://automationadmin.com/assets/images/uploads/2016/09/vritual-nic-config.png" alt="vritual-nic-config" width="739" height="416" srcset="https://automationadmin.com/assets/images/uploads/2016/09/vritual-nic-config.png 739w, https://automationadmin.com/assets/images/uploads/2016/09/vritual-nic-config-300x169.png 300w" sizes="(max-width: 739px) 100vw, 739px" />

2. Start the wizard: New => Virtual Machine => Use an iso for the CD drive or place a physical CD in the host server's DVD drive for the install. Start up the VM.

3. Install the VM step by step: 4 processors, usually 4096 MB of memory, and figure out the appropriate HDD space needed.

4. Install the OS and run the VM one time to get the MAC address assigned by Hyper V.

5. Shut down the VM and set the MAC address statically. We do this so that we can then go into our domain controller and add a DHCP reservation for the new server.
