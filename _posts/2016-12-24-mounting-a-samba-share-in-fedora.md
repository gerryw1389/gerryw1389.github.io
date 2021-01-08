---
title: Mounting A Samba Share In Fedora
date: 2016-12-24T08:06:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/mounting-a-samba-share-in-fedora/
categories:
  - Networking
  - Linux
tags:
  - LinuxClient
  - FileSystem
---
<!--more-->

### Description:

So I after setting up my Plex server and setting up a Samba server, I had no problems connecting Windows to the server => but my Linux machines were giving me fits. I eventually got it mounted, but I still have the issue that the shares are mounted as root:root even though I specified samba credentials to access. I'm still looking a fix for this.

### To Resolve:

1. First, we create a mount point:

   ```shell
   mkdir /home/gerry/data
   ```

2. Then install utils:

   ```shell
   sudo yum install samba-client samba-common cifs-utils
   ```

3. Test the connection to our server:

   ```shell
   smbclient -L 192.168.0.90/share -U homeUser
   # Enter password for user "homeUser"
   # Once it connects, just exit
   smb>exit
   ```

4. Now mount the share the default linux way:

   ```shell
   sudo mount -t cifs -o username=homeUser //192.168.0.90/share /home/gerry/data
   # Enter password for user "homeUser"
   ```

5. From here we are good to go. But if you want the drive to be persistent, we need to create a credentials file and then edit fstab:

   - Create your password in a single file on your home drive

   ```shell
   sudo touch ~/.smbcreds
   sudo vi .smbcreds

   # Enter your Windows username and password in the file:
   username=msusername
   password=mspassword

   # Set perms
   chmod 600 ~/.smbcredentials

   # Now we add to /etc/fstab (auto-mount)
   sudo vi /etc/fstab
   # Add:
   //192.168.0.90/share /home/gerry/data cifs credentials=/home/gerry/.smbcreds,_netdev,defaults 0 0
   ```

   - This persists through reboot, but it still shows up as root:root. Not sure why this works so well on Windows, but not on Linux. I've tried creating the user locally on Linux like I do on Windows when mounting shares, but it still mounts as root. Will look into this later as I can sudo for now.

6. UPDATE 2017-07-23: I got this working on CentOS. The key is to get your user id by typing &#8220;id -u (username)&#8221; and then doing the following:

   ```shell
   sudo yum install samba-client samba-common cifs-utils

   # Test mounting your file system:
   sudo mount -t cifs -o username=windowsuser,password=WindowsUserPassword,uid=1000,gid=976 //192.168.0.30/winshare /mnt/shared

   # Now we add to /etc/fstab (auto-mount)
   sudo vi /etc/fstab
   # Add the following:
   //192.168.0.30/winshare /mnt/shared cifs username=windowsuser,password=WindowsUserPassword,rw,uid=1000,gid=976 0 0

   # Note I used the gid as plex in this case because I was wanting plex to be able to write to my windows share
   ```

