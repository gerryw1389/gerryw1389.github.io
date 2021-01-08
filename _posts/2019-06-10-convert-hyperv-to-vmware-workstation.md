---
title: Convert HyperV To Vmware Workstation
date: 2019-06-10T01:42:57-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/convert-hyperv-to-vmware-workstation/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

This is the steps I used to convert my VM's on my laptop from Hyper-V to VMWare Workstation 15. If this post doesn't seem to give enough information, see my previous test labs with [Virtualbox](https://automationadmin.com/2016/12/setting-up-a-lab-using-only-virtual-box/) or [HyperV](https://automationadmin.com/2017/09/setting-up-a-hyper-v-lab/)

### To Resolve:

1. Go to programs and features and uncheck Hyper-V. Reboot.

2. Installed VMWare Workstation.

3. Convert the VM's - Use Starwind Virtual Converter and choose the first option - Expanding vmware disk. 

4. Import the vm's to VMWare workstation

5. Open Virtual Network Editor as administrator

   - Delete all networks
   - Create one called "gwill_priv" which is a host only network
   - Disable DHCP

6. When I went to start the VM's after pointing them to the new networks, it gave an error
 
   - fix: Disable Device Guard/Credential Gaurd since I'm on Enterprise

   ```powershell
   # from https://www.microsoft.com/en-us/download/details.aspx?id=53337
   DG_Readiness.ps1 -Disable -AutoReboot
   ```

7. For linux VM's, you will have to start from scratch, at least I did. just reinstalled the OS. If you start them, they will end up in `dracut` errors and that is a rabbit-hole I didn't want to mess with. Since mine were just plain Centos 7 VMs with nothing on them yet, it was much easier to use the VMWare Workstation "Express install wizard".

8. Set startup script on host:

   ```escape
   @ echo off
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\vmware\pfsense\pfsense.vmx"
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\vmware\2016dc\2016dc.vmx"
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\vmware\puppet\puppet.vmx"
   ```

