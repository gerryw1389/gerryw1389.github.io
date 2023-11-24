---
title: FreeNAS Install
date: 2016-05-26T04:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/freenas-install/
tags:
  - Unix
tags:
  - Setup
---
<!--more-->

### Description:

FreeNAS is an open source software that allows you to create sharable volumes based off the Free BSD operating system (derived from Unix). This software is similar to that of Vphere where you install this on a machine and then use a browser to control it remotely. Follow these steps to install FreeNAS:

NOTE: I don't have any actual hardware devices to install this to so I am using VMWare Workstation 10 to create a VM.

### To Resolve:

1. Get the .iso from their main website and create a VM for it with bridged networking (it will receive an IP on my LAN). Give it 8 GB memory and two drives at least.

2. Boot up the VM and install just like any other OS installation, it installs on FreeBSD so it will use *nix commands.

   - If you see a screen with a lot of dots and plus signs, that is okay. I guess that means its setting things up.

3. Once its created, it will ask to remove the disk and reboot. Do that and you get to a 14 option menu with an IP address where you can see the GUI. Go to it.

4. In the installation wizard follow the prompts until you get to the storage type and make sure to select iSCSI.

   - You sign in with username: root and the password you created during setup.

5. First thing you want to do is go to the Network tab and verify all is correct as far as DHCP, Default Gateway, and Subnet settings.

6. Once logged in, navigate to the Directory tab and make sure you are connected to Active Directory under the NT4 subsection.

7. Go to Storage => Volumes and make sure you change the permissions for the volume to Windows.

   - ![freenas-1](https://automationadmin.com/assets/images/uploads/2016/09/freenas-1.png){:class="img-responsive"}

8. Go to: Sharing => Block (isSCSI) => Portals (subtab). Select &#8220;add portal&#8221; and then select the IP address it gives you or select one from the drop down.

   - ![freenas-2](https://automationadmin.com/assets/images/uploads/2016/09/freenas-2.png){:class="img-responsive"}

9. Now go to the Initiators tab and &#8220;add initiators&#8221;. These are the clients that will connect, select the default &#8220;ALL&#8221; in here or specific hostnames/IP's.

10. On the Authorized Access tab, fill out the username as the domain admin user name and set a passcode that is between 12-16 characters long.

11. On the Add Target tab, create a target name and associate it with the appropriate portal.

   - ![freenas-3](https://automationadmin.com/assets/images/uploads/2016/09/freenas-3.png){:class="img-responsive"}

12. On the extents tab, make up a name for an extent, select to browse to your volume from the previous step and append the name on the end of it, then create a size in bytes (Mine is roughly 40 GB in the example). It is recommended to choose &#8220;File&#8221; extents over device extents from what I have read on the intertubes.

   - ![freenas-4](https://automationadmin.com/assets/images/uploads/2016/09/freenas-4.png){:class="img-responsive"}

13. On the Associated Targets tab, select the target name you created and the extent name in the drop downs, click OK.

14. Now scroll down to services and enable the iSCSI service.

**On the Domain Controller:**

1. Open up Server Manager and go to iSCSI Initiator.

2. Hit refresh and select the disk. Then go to the auto-configure tab for Windows to autoconfigure your share.

3. Run => `diskmgmt.msc` => initiate the disk and create a volume.

   - If the disk is Offline with the message `the disk is offline because of policy set by an administrator`, read [this article](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2000767)

4. Once you create a volume, your done. As an extra precaution, I went to the security tab and gave my domain admin full control on the drive in Explorer. Now you can start setting up high availability if you wish.

### References:

["10. Sharing"](http://doc.freenas.org/9.3/freenas_sharing.html)  
["How To Configure and Install FreeNAS for iSCSI Target"](https://www.youtube.com/watch?v=nhME_CbZrQs)  
["Configure iSCSI target on FreeNAS 8.3 & access same target from Windows 2012 Server"](https://www.youtube.com/watch?v=7jn2q2ysr5g)  