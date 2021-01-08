---
title: VMware ESXI Overview
date: 2016-05-24T13:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/vmware-esxi-overview/
categories:
  - SysAdmin
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

VMWare ESXI is a hypervisor just like VMWare Workstation, MS HyperV and Oracle Virtual Box but instead of running inside the OS, you run it AS the OS. You then use vSphere on another computer to connect to your hypervisor by name or IP.

### To Install:

1. Install the ISO to a VM using the hypervisor of your choice. You install the ESXi bare-metal hypervisor as the first step to creating a vSphere environment. In a typical interactive installation, you boot the ESXi installer and respond to the installer prompts to install ESXi to the local host disk.

2. Install directly on a box. I haven't done this yet but the steps should be the same.

3. After you finish the interactive installation of ESXi, use the direct console to configure your host. Assign the host a specific IP address and review the configuration options that the direct console provides.

4. Login to your ESXI host and deploy a virtual machine by using the vSphere client (from a different machine or the ESXI host). To deploy virtual machines and perform administrative tasks, you must install the vSphere Client and use it to manage the host. You can download the vSphere Client installer binary from your host. Use the standalone vSphere Client application to manage your host directly before you move on to more complex environments. You can use vCenter Server and the browser-based vSphere Web Client to manage multihost environments.

5. (Optional: Used for Multi-VM Environment)You can install vCenter Server in a Microsoft Windows virtual machine that runs on an ESXi host. To use the virtual machine as a host system for your vCenter Server instance with the network conventions of this scenario, assign to the virtual machine the IP address 192.168.0.10. In the next scenario, the administrative account of the Windows virtual machine is set as your vCenter Server account.
