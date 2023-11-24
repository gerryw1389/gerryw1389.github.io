---
title: Sharing Files In Linux And Windows
date: 2017-05-24T14:48:13+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/05/sharing-files-in-linux-and-windows/
tags:
  - Linux
  - Networking
tags:
  - FileSystem
---
<!--more-->

### Description:

Although I have these steps in a couple places, I wanted to make a single post with the different combinations of sharing folders between Windows/Linux. Updating to include `scp` commands for one off transfers as you wouldn't mount a drive just to copy a file one time :)

### To Resolve:

### CIFS/SMB

- Stateful protocol that executes each command in the context of the user that you connect as; most common in Windows environments

1. Using CIFS from from Windows Server => Windows client (most common):

   - Create the share using the steps above
   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `\\WindowsComputerName\ShareName`
   - Enter the username and password from above

2. Using CIFS from Windows Server => Linux Client (most common)
   - Networking and Sharing => File/Print sharing
   - Share the folder, set permissions for everyone
   - Under the security settings either add a specific user or add `everyone` and set permissions to what you need access for.
   - From Linux, install the cif-utils package: `sudo apt-get install cifs-utils`
   - Now create a new folder on your desktop and mount the Windows share to that folder: `mount –t cifs –o username=gerry,password=pa55word //WindowsComputerNameName/ShareName /home/username/path`

3. Using CIFS from from Linux Server => Windows Client - also see [here](https://automationadmin.com/2016/10/setting-up-a-samba-server-on-centos/) :

   - Install Samba

   ```shell
   sudo apt-get install samba
   # Configure username/password that will be used in Windows to access the share:
   smbpasswd -a smb
   # Create a folder to share:
   mkdir ~/Desktop/Share
   ```

   - Edit Samba config file - `sudo vi /etc/samba/smb.conf` and edit:

   ```escape
   []
   path = /home/username/Desktop/Share;
   available = yes
   valid users = smb;
   read only = no
   browsable = yes
   public = yes
   writable = yes

   # Save and close the file
   ```

   - Restart the SMB service for changes to take effect:

   ```shell
   sudo service smbd restart

   # Note: I like to do a "chmod 770 -R" on the shared directory

   # Note: I like to do a "chown user:group -R" on the shared directory
   ```

4. Using CIFS from Linux Server => Linux client using (uncommon unless Linux server is serving Windows clients/Servers):

   - From terminal on the linux client:

   ```shell
   # Install Samba Client:
   sudo apt-get install smbclient

   # To list all shares:
   smbclient -L //LinuxServerComputerName/sharedFolderName -U user

   # To connect:
   smbclient //LinuxServerComputerName/sharedFolderName -U user

   #  To mount:
   mount –t cifs –o username=gerry,password=pa55word //LinuxServerComputerName/sharedFolderName /home/username/path

   #  To access via File Browser GUI:
   smb:///LinuxServerComputerName/sharedFolderName

   # to make permanent
   vi /etc/fstab

   # add the following
   //LinuxServerComputerName/sharedFolderName /home/username/path  cifs vers=3.0,username=user,password=Pa55word,rw,uid=1000,gid=1000 0  0
   
   # save and exit, then mount
   mount -a
   ```

### NFS

- Stateless protocol that allows clients access based on their IP address and linux permissions; most common in Linux environments with higher speeds than CIFS/SMB is most cases

1. Using NFS from Linux Server => Linux client (most common):

   ```shell
   yum install nfs-utils
   
   # See mount points of Linux Server by IP address (most common)
   showmount -e 192.168.0.100

   # Create local directory and mount the share
   mkdir -p /mnt/nfs-home

   # try mounting with any of these, I think the last is most common
   mount -t nfs 192.168.0.100:/home /mnt/nfs-home
  
   # or try the following
   # mount -t nfs4 192.168.0.100:/home /mnt/nfs-home
   # mount 192.168.0.100:/home /mnt/nfs-home
   # mount.nfs4 -v 192.168.0.100:/home /mnt/nfs-home

   # check the mount if successful, if it is not, check the /etc/exports on the server side and make sure your client is in the correct IP range
   df -h

   # to make permanent
   vi /etc/fstab

   # add the following
   192.168.0.100:/home /mnt/nfs-home/  nfs      defaults    0       0
   # or try the following (look up which ever options are best for your environment)
   # 192.168.0.100:/home /mnt/nfs-home/  nfs      nosuid,rw,sync,hard,intr    0       0
   # 192.168.0.100:/home /mnt/nfs-home/  nfs      rw,async,all_squash,anonuid=1000,anongid=1000    0       0
   
   # save and exit, then mount
   mount -a
   ```

2. Using NFS from Linux Server => Windows client - See [my post](https://automationadmin.com/2019/04/connect-to-nfs-share-from-windows/) on this

### SCP

- SCP is a protocol for transferring files through a SSH session using RCP commands on a Unix system. Unlike FTP, SCP retains file permissions and timestamps through inclusion with the transferred files themselves, thereby ensuring data confidentiality during transit.

1. From Linux to Linux:

   ```shell
   cd /home/username/path
   scp foo.txt  root@remoteServer.domain.com:/home/username/path/foo.txt
   # Enter password for user root at remoteServer.domain.com

   # now /home/username/path/foo.txt is copied to remoteServer.domain.com at /home/username/path/foo.txt
   ```

2. From Windows [with WSL](https://automationadmin.com/2017/09/windows-subsystem-for-linux-wsl/) to Linux:

   ```shell
   cd /mnt/c/scripts # c:\scripts in Windows File Explorer
   scp foo.txt  root@remoteServer.domain.com:/home/username/path/foo.txt
   # Enter password for user root at server.domain.com

   # now /mnt/c/scripts/foo.txt is copied to remoteServer.domain.com at /home/username/path/foo.txt
   # which is the same as: c:\scripts\foo.txt is copied to remoteServer.domain.com at /home/username/path/foo.txt
   ```

3. (Really Neat!) From your machine, you can grab a file off a remote system and bring it to you:

   ```shell
   cd /mnt/c/scripts/
   # The dot represents your current directory
   scp root@remoteServer.domain.com:/var/log/foo.log .
   # Enter password for user root at remoteServer.domain.com

   # now /var/log/foo.log from remoteServer exists on your machine at /mnt/c/scripts
   # You can also specify a full path:
   scp root@remoteServer.domain.com:/var/log/foo.log /mnt/c/scripts/foo.log
   # Enter password for user root at remoteServer.domain.com

   # now foo.log is at c:\scripts on your Windows machine
   ```
