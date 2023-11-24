---
title: 'Create NFS Server'
date: 2019-12-03T09:41:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/12/create-nfs-server/
tags:
  - Linux
tags:
  - FileSystem
  - LinuxServer
---
<!--more-->

### Description:

If I ever need to create a 'share' that I know that only linux clients will be accessing, I usually just create a NFS server on a linux host using these commands:

### To Resolve

1. Type:

   ```shell
   yum install nfs-utils nfs-utils-lib
   mkdir /var/nfsshare
   chmod -R 755 /var/nfsshare
   chown nfsnobody:nfsnobody /var/nfsshare
   systemctl enable rpcbind
   systemctl enable nfs-server
   systemctl enable nfs-lock
   systemctl enable nfs-idmap
   systemctl start rpcbind
   systemctl start nfs-server
   systemctl start nfs-lock
   systemctl start nfs-idmap
   vi /etc/exports
   # replace with client IP address or subnet - 192.168.0.0/255.255.255.0
   /var/nfsshare    192.168.0.101(rw,sync,no_root_squash,no_all_squash)
   /home            192.168.0.101(rw,sync,no_root_squash,no_all_squash)
   systemctl restart nfs-server
   firewall-cmd --permanent --zone=public --add-service=nfs
   firewall-cmd --permanent --zone=public --add-service=mountd
   firewall-cmd --permanent --zone=public --add-service=rpc-bind
   firewall-cmd --reload
   ```

2.  Clients will access it like:

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