---
title: Hyper-V High Availability
date: 2016-05-29T04:11:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hyper-v-high-availability/
categories:
  - WindowsServer
tags:
  - VirtualizationSoftware
  - WindowsServer-Roles
---
<!--more-->

### Description:

Follow these steps to setup High Availability between two or more servers. Note that High Availability can be used for many things, in my test lab I set it up to be used with Hyper-V applications since that is a common scenario. The following steps will setup &#8220;Hyper-V with Fail Over Clustering&#8221;. Please make sure that you have two VM's with the same OS, same roles, same everything for this to work. I had to do this three times due to subtle differences.

### To Resolve:

1. First, setup an iSCSI Share or some kind of shared storage solution between the two servers. I recommend following the steps in [FreeNAS](https://automationadmin.com/2016/05/freenas-install/).

2. Install the &#8220;Hyper-V&#8221; role and the &#8220;Fail Over Clustering&#8221; feature from Server Manager and grab an iso for a VM (I used a Linux Mint VM due to small file size). Do this for each server. If you are doing this in VMWare Workstation, follow these sub steps:

   - First, shut down the VM.
   - Make certain that you've enabled VT-x/EPT in your virtual machine under Settings => Processors.
   - Modify the vmx file associated with your VM by opening the file in Notepad and adding these lines at the end and saving:

   ```escape
   hypervisor.cpuid.v0 = "FALSE"  
   mce.enable = "TRUE"
   ```

   - Boot your VM back up. If it gives and error and corrects it, just ignore it (mine did).

3. Launch the Failover Cluster Manager, select the option to &#8220;Validate Configuration&#8221; which will launch a wizard. Add the host names of the two servers and run all tests.

   - So this was a little bit of a hastle for me because I had my iSCSI share on the same subnet as my internal network. To fix, I added another network adapter with it's own subnet and configured FreeNAS, the DHCP server on my DC, and my two VM's all point to the new segregated iSCSI subnet.

  <img class="alignnone size-full wp-image-664" src="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-1.png" alt="hyper-v-ha-1" width="788" height="311" srcset="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-1.png 788w, https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-1-300x118.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-1-768x303.png 768w" sizes="(max-width: 788px) 100vw, 788px" />


4. Back to the good stuff, now we create a cluster by launching &#8220;create a cluster&#8221;. So give it a name and make sure only to select your subnet and give it an IP address. The screenshot below was the first time I ran this and I ended up failing miserably. The second time I was on DHCP and it automatically selected both network cards and took DHCP as a valid source, so I went with it.


  <img class="alignnone size-full wp-image-665" src="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-2.png" alt="hyper-v-ha-2" width="683" height="358" srcset="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-2.png 683w, https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-2-300x157.png 300w" sizes="(max-width: 683px) 100vw, 683px" />


5. At this point you have a cluster! Now, to to your cluster => Roles => Configure Role => Virtual Machines => Next => Finish.

6. Next, we need to get &#8220;Shared Access Rights&#8221; for the disks. Highlight your cluster name and then go to Actions => More Actions => Configure Cluster Quorum Wizard => Next => Select the Quorum Witness => Do not configure a Quorum Witness => Next => Done. Note: I only had one disk in this share and when the cluster was created, it automatically assigned it as a quorum. To learn more about Quorums, see [here](https://technet.microsoft.com/en-us/library/jj612870.aspx). What I chose said it was not &#8220;Best Practice&#8221;, but again, I just want to get the damn thing to work at this point AND its in a lab. I would research more before doing something like this in production.

7. Now navigate down to Storage => Disks => Right click your disk => Add to Clustered Shared Volumes (CSV)

8. On both servers, open up Hyper-V Manager, go to Hyper-V Settings and change the default storage to your newly created Volume 1 path. I created a sub-folder for each host name in my cluster so their VM's can be separated.

  <img class="alignnone size-full wp-image-666" src="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-3.png" alt="hyper-v-ha-3" width="732" height="130" srcset="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-3.png 732w, https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-3-300x53.png 300w" sizes="(max-width: 732px) 100vw, 732px" />

9. Now comes the fun part. Spin up the VM's on each server and then on one of them, right click on the VM and choose Move => Live Migration => Select Node => Choose the other server in the list. It will move the VM over in about 30 seconds!

  <img class="alignnone size-full wp-image-667" src="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-4.png" alt="hyper-v-ha-4" width="751" height="352" srcset="https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-4.png 751w, https://automationadmin.com/assets/images/uploads/2016/09/hyper-v-ha-4-300x141.png 300w" sizes="(max-width: 751px) 100vw, 751px" />

   - If you really want to play with this. Move both VM's to the same server and then go to Nodes => Select the server with both running VMs => Right Click => More => Stop Cluster Service. Then hurry and go to your Roles tab in the navigation tree and watch them migrate over to the other server without an issue. Check the Youtube video in the links for a visual representation.

### References:

["Virtualization: Hyper-V and High Availability"](https://technet.microsoft.com/en-us/magazine/hh127064.aspx)    
["Using FreeNAS 8 to Create an iSCSI Target for Windows 7"](https://www.pluralsight.com/blog/software-development/freenas-8-iscsi-target-windows-7)