---
title: Setting Up A Samba Server On CentOS
date: 2016-10-07T04:43:01+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/setting-up-a-samba-server-on-centos/
categories:
  - Linux
tags:
  - LinuxServer
  - FileSystem
---
<!--more-->

### Description:

Follow these steps to setup a Samba server on CentOS 7. You can learn about samba [here](https://www.samba.org/samba/what_is_samba.html). In this example, we are sharing a directory called &#8220;/homeShare&#8221; from our CentOS VM.

### To Resolve:

1. Open a terminal => type:

   ```shell
   # Install software needed
   sudo yum install -y samba samba-commons cups-libs policycoreutils-shell samba-client

   # Create a group for smb users
   sudo groupadd family
   sudo chgrp -R family /homeShare
   sudo chmod -R 770 /homeShare

   # Change selinux settings
   sudo chcon -R -t samba_share_t /homeShare/
   sudo semanage fcontext -a -t samba_share_t /homeShare/
   sudo setsebool -P samba_enable_home_dirs on

   # Create a user for smb purposes. This is the user that will access the share from other comptuers.
   sudo useradd smb
   sudo usermod -G family smb
   sudo smbpasswd -a smb
   <typePassword>

   # Make sure to make any local users part of the group if you want them to have access to the share
   sudo usermod -G family gerry
   sudo usermod -G family root

   # One thing that took me over an hour to figure out is you have log out and back in for it to take effect!!

   # Now we modify the config
   cd /etc/samba/
   sudo cp -p smb.conf smb.conf.orig
   sudo vi /etc/samba/smb.conf

   # Change workgroup to your Windows workgroup name. Add the hosts interfaces that will use the server and then the networks on those NICs. 
   # Then allow anything on whatever subnets you want to limit them to:

   Workgroup = windows workgroup
   interfaces = lo enp0s3 192.168.0.0/24
   hosts allow = 127. 192.168.0.

   # Now scroll down to your share name
   [homeShare]
   comment = shared-directory
   path = /homeShare
   public = no
   valid users = smb, @family
   writable = yes
   browseable = yes
   create mask = 0765

   # Save and exit

   # Now we need to make sure the following services are running:
   sudo vi /etc/services

   # Look for and add if missing (shouldn't be, but I don't set these up all the time so some may be):
   netbios-ns    137/tcp    # netbios name service
   netbios-ns    137/udp    # netbios name service
   netbios-dgm    138/tcp    # netbios datagram service
   netbios-dgm    138/udp    # netbios datagram service
   netbios-ssn    139/udp    # netbios session service
   netbios-ssn    139/udp    # netbios session service

   # Now just start the services and enable them for startup
   sudo systemctl start smb.service
   sudo systemctl start nmb.service
   sudo systemctl enable smb.service
   sudo systemctl enable nmb.service

   # Add firewall rules
   sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.0.0/24" service name="samba" log prefix="samba" level="info" limit value="1/m" accept'
   sudo firewall-cmd --reload
   ```

2. To access from Windows:

   - Run:

   ```powershell
   \\LinuxServerHostname\ShareName
   ```

   - Enter prompts for the username and password, should be &#8220;smb/whatever you set&#8221;

   - To map the Samba server share as a network drive either create it through My Computer manually, or right click on the share and select &#8220;map network drive&#8221;.

3. To access from Linux (smbclient must be installed on your system, if it isn't then install it.)

   - Open terminal => type:

   ```shell
   smbclient -L \\192.168.56.102 -U test
   ```

   - The IP address is that of the Samba server and the &#8220;test&#8221; is the user account. It will prompt for a password after running that command.

   - To mount it, just type:

   ```shell
   mount -t cifs //192.168.56.102/sharedrepo -o username=test /mnt/
   # Enter password
   ```

   - This maps the same Samba share with the same user to the &#8220;/mnt/&#8221; directory.

   - In some distro's you can browse Samba shares just by opening their file explorers and typing &#8220;smb://<ipaddress>&#8221; in the address bar.