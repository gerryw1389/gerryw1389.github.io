---
title: Switching Between Type 2 Hypervisors
date: 2016-05-24T12:29:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/switching-between-type-2-hypervisors/
tags:
  - LocalSoftware
tags:
  - VirtualizationSoftware
  - VirtualizationSoftware
---
<!--more-->

### Description:

There are 3 main Type 2 hypervisors at this time: VMWare Workstation/Player, Oracle VirtualBox, and Windows Hyper-V. Each have their streangths and weaknesses. Type 2 Hypervisors allow VM's to run within an OS and Type 1 run directly on the hardware itself (ESXI, HyperV Server, ect.)

### W10 Hyper-V Setup:

1. Ensure that your BIOS supports virtualization

2. Install Hyper-V ( Run => `appwiz.cpl` => Add features (on left) => Check the box next to Hyper-V), reboot.

3. I then got a `The virtual machine could not start because the hypervisor is not running` error when trying to start a machine. Obviously the Hyper-V service was running because I could see all my VM's and edit their settings, but o' well. Lets research&#8230;

4. Search => Elevated CMD => Type:

   ```powershell
   Dism /online /enable-feature /featurename:microsoft-Hyper-V -All
   BCDEDIT /Set {current} hypervisorlaunchtype auto
   shutdown -r -t 03
   ```

5. You should now be able to startup Hyper V virtual machines.

### Oracle Virtualbox Setup:

NOTE: You have to uninstall Hyper-V in order for VirtualBox to work properly.

1. Installing vbox extensions for Fedora:  

   ```shell
   su  
   dnf install dkms  
   dnf install gcc # this said it was installed in the previous step, but I was just following [Chapter 4. Guest Additions](https://www.virtualbox.org/manual/)ch04.html#idp46457703730512>  
   reboot  
   # insert cd and then navigate to the drive  
   su  
   sh ./VBoxLinuxAdditions.run  
   reboot
   ```

2. For Windows, just insert the Guest addition CD under Devices => Insert Guest&#8230; It will be a next, next, finish install.

3. Activating Windows from changing file formats .vdi to .vmdk to .vhdx to .vhd and back and forth caused Windows to become unactivated despite my Datacenter licenses from Dreamspark, so I ended up running `slui 4` on Windows to bring up activation and just go through the manual process.

### File Conversions:

1. VMDK to VDI:

   - Shutdown the VM and remove the vmdk file from the guest VM (you can't convert it while it is attached to a VM)
   - [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `VBoxManage clonehd --format VDI myserver.vmdk myserver.vdi`

3. VMDK to VHD:

   - I used Microsoft Virtual Machine Converter for this.  
   - `Import-Module 'C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1`  
   - `ConvertTo-MvmcVirtualHardDisk -SourceLiteralPath C:\myserver.vmdk -VhdType DynamicHardDisk -VhdFormat vhdx -destination c:\myserver`

4. VHD to VHDX:  

   - I used Powershell  
   - `Convert-VHD myserver.vhd myserver.vhdx`  
   - Run `get-help convert-vhd` for more info. Make sure you have the Hyper-V role installed.

5. For anything else, use [StarWind V2V Converter](https://www.starwindsoftware.com/converter)