---
title: Dual Boot W10/Linux Mint
date: 2016-05-21T21:38:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/dual-boot-w10linux-mint/
categories:
  - Linux
tags:
  - Setup
---
<!--more-->

### Description:

After upgrading my laptop to Windows 10 with the free upgrade, it didn't take long before I wanted to switch back to Linux Mint. The main reason for this switch was a mix between the ever so persistent spying settings and the fact the OS seemed sluggish as hell. Also, my mouse would not work sometimes on W10 but had no issues with Linux. This was after updating the drivers from Dell's website to the newest version. I did the following steps to dual boot Windows with Linux (had to leave Windows for the wifey).

### To Resolve:

1. In Windows, I used a program called Mini-Partition Tool although you can do these steps in `diskmgmt.msc` if you wish. What you want to do is keep the Windows &#8220;System 100 MB Partition&#8221; and your Windows files, but &#8220;shrink it&#8221; to whatever size you wish. However much you shrink will determine your Linux partition size. The keys is to keep the free space UNALLOCATED.

   NOTE: This guide was for installing on a single hard drive. Steps will be different if you have Linux on a separate disk.
   {: .notice--success}

2. Burn the Linux ISO to a USB drive using your favorite tool, I use Rufus or Unetbootin. Reboot your computer and tap `F12` on startup to launch the &#8220;one time boot menu&#8221; (for Dell's anyways). Choose the option for USB Mass Storage.

3. Once in the Linux Mint Live CD, just select the option to install Linux. Go through the defaults until you get to the &#8220;Installation Type&#8221; screen. Choose the option &#8220;something else&#8221;. NOTE: There is an option to install Linux Mint along side&#8230; but I didn't choose it, most guides don't say to either.

4. On the next screen, look at your different partitions. /dev/sda1 and 2 should be your Windows installation. You need to create at least two more out of the free space: One will be your /root and /home partitions and the other will be your swap partition. This part is up to you, but I just chose to have /root and /home on the same 160 GB space and I chose to create a swap partition of around 7 GB. Make sure you choose &#8220;ext4&#8221; for the Linux partition and &#8220;/&#8221; as the mount point.

   - ![dual-boot-win10-linux-mint](https://automationadmin.com/assets/images/uploads/2016/09/dual-boot-win10-linux-mint.png){:class="img-responsive"}

5. Now this part I most likely messed up because I had to do this twice. The first time, I just click Install Now after the previous step and the computer never let me go into Linux. It just booted Windows every time, Grub was no where to be found (even after holding shift after the BIOS). So I redid the steps up to this point and changed the &#8220;Device for boot loader selection&#8221; to equal the one that said &#8220;Windows 7 (loader)&#8221; so that it would overwrite. After this, just select Install Now and do defaults until reboot.

6. After reboot, I was able to get into Linux just fine => but if I selected Windows 7 (which was really Windows 10), it just brought me right back to the grub menu.

7. After some research, I downloaded Grub Customizer for Linux Mint:

   ```shell
   sudo add-apt-repository ppa:danielrichter2007/grub-customizer
   sudo apt-get update
   sudo apt-get install grub-customizer
   ```

8. I did some more research for why Windows wouldn't boot and found the fix was to modify the boot source for the Windows 7 (loader) option in Grub. It had the following script:

   ```shell
   insmod part_msdos
   insmod ntfs
   set root='hd0,msdos3'
   if [ x$feature_platform_search_hint = xy ]; then
   search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos3 --hint-efi=hd0,msdos3 --hint-baremetal=ahci0,msdos3 --hint='hd0,msdos3' 264CA3CF4CA39857
   else
   search --no-floppy --fs-uuid --set=root 264CA3CF4CA39857
   fi
   parttool ${root} hidden-
   chainloader +1

   #I changed it to:
   insmod part_msdos
   insmod ntfs
   insmod ntldr
   set root='hd0,msdos1'
   if [ x$feature_platform_search_hint = xy ]; then
   search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 EE8E607C8E603F69
   else
   search --no-floppy --fs-uuid --set=root EE8E607C8E603F69
   fi
   parttool ${root} hidden-
   ntldr ($root)/bootmgr
   ```

9. Saved the changes and rebooted => It worked!!

### References:

["How To Dual Boot Linux Mint And Windows 10"](https://itsfoss.com/guide-install-linux-mint-16-dual-boot-windows)

["How To Install Grub Customizer 4.0.6 On Ubuntu"](http://linuxg.net/how-to-install-grub-customizer-4-0-6-on-ubuntu-linux-mint-elementary-os-and-their-derivative-systems/)