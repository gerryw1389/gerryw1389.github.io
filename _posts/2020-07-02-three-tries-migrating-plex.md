---
title: Three Tries Migrating Plex
date: 2020-07-02T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/07/three-tries-migrating-plex
categories:
  - LocalSoftware
tags:
  - MediaEditing
  - LinuxServer
---
<!--more-->

### Description:

So I borked my Plex install on Centos 7 with Virtualbox because I kept shutting down my computer without stopping the VM for various things. No big deal, I back it up often - but I wanted to see if I could have it run with Docker instead! So I wiped my PC and setup [Docker with WSL2](https://automationadmin.com/2020/06/docker-windows-host-with-wsl2). I noticed weird performance issues so instead created it once again in a Centos 8 VM this time with Hyper-V. Lastly, I decided to move it locally on the machine instead of with Docker because I still need to be able to import playlists and I couldn't figure out how to do it with Docker mounts. All things considered, I will continue to test Docker but wanted to just get Plex back up and running like it was before!

### To Resolve:

1. So first using Windows Host machine with WSL2:

   - I went to Plex's [official Docker repo](https://github.com/plexinc/pms-docker) and read what I needed:
   - Get the [correct timezone string](https://docs.diladele.com/docker/timezones.html) - America/Chicago
   - Get a [claim token](https://www.plex.tv/claim)
   - Ensure my user has rights to read/write to certain directories on a different drive letter in Windows (see below)
   -  So after getting the information I needed, I opened up VSCode and ensured that the `Remote Development` extension was working with WSL2 by typing `wsl` followed by `code .` which will launch vscode from the remote environment. While in the remote-wsl, I also ran `docker --help` and ensured that it could run docker commands. Lastly, I simply ran two commands to pull down the docker container and set it up as I wanted:

   ```shell
   # make sure my user is in correct group
   sudo usermod -aG docker gerry
   docker run \
   -d \
   --name plex \
   -p 32400:32400/tcp \
   -p 3005:3005/tcp \
   -p 8324:8324/tcp \
   -p 32469:32469/tcp \
   -p 1900:1900/udp \
   -p 32410:32410/udp \
   -p 32412:32412/udp \
   -p 32413:32413/udp \
   -p 32414:32414/udp \
   -e TZ="America/Chicago" \
   -e PLEX_CLAIM="claim-mYxClaim" \
   -e ADVERTISE_IP="http://192.168.33.30:32400/" \
   -h "plex" \
   -v /mnt/s/plex/db:/config \
   -v /mnt/s/plex/transcode:/transcode \
   -v /mnt/s/:/data \
   plexinc/pms-docker
   ```

2. So before this, I had folders under my `s:\` in Windows that I shared to my Centos 7 VM that would mount them on boot and use those to read into the Plex library. Now I get to point it locally!. But I had a problem... all my directory permissions were read/execute only even though I had `computername\Adminstrators` as full control to the root of the `S:\` with inheritance enabled.

   - So I was able to create folders if I launched powershell as administrator, then typed `wsl` and then `cd /mnt/s/somefolder` and `mkdir whatever`. 
   - But I didn't want to launch PS as admin every time....
   - Found the fix was just to add my user explicitly to root of `S:\` NTFS Security and then run `wsl` again and it would pick up that my user had permissions!

3. So after I got permissions sorted and the container running, I went to `localhost:32400` in my browser and Plex was running! I signed in and removed my old server and pointed to this server. Now, I just need to run `wsl -e docker start plex` in my startup script to start my container instead of [launching vbox](https://automationadmin.com/2019/09/virtualbox-startup-changes/).

   - Some docker commands:
   - Start the container: `docker start plex`
   - Stop the container: `docker stop plex`
   - Shell access to the container while it is running: `docker exec -it plex /bin/bash`
   - See the logs given by the startup script in real time: `docker logs -f plex`
   - Restart the application and upgrade to the latest version: `docker restart plex`

4. But after using it for a day or two and testing at a friends house, I noticed subpar performance. So I decided to replicate everything again in a Centos 8 VM in Hyper-v:

   - First, install the role and create a network switch called `Shared-LAN` that pointed to an external network which is my NIC in my host machine.
   - Setup Centos 8 minimal install
   - Setup docker and docker-compose:

   ```shell
   dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
   dnf list docker-ce
   dnf install docker-ce --nobest -y
   systemctl start docker
   systemctl enable docker
   docker --version
   # Docker version 18.06.3-ce, build d7080c1
   docker run hello-world

   dnf install curl -y
   curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   chmod +x /usr/local/bin/docker-compose
   /usr/local/bin/docker-compose --version
   #docker-compose version 1.25.0, build 0a186604
   ```

   - On my host Windows machine, created `Data` and `Vids` shares to be used by Plex VM.

   - I then mounted CIFS like my old Plex server:


   ```shell
   # Test smb stuffs
   smbclient -m SMB3 -U user //192.168.30.30/Data
   (enter password)
   # Prompt changes to: smb:> 
   exit

   smbclient -m SMB3 -U user //192.168.30.30/Vids
   (enter password)
   # Prompt changes to: smb:> 
   exit

   #create creds
   cd ~
   vi .smbcred
   username=msusername
   password=mspassword
   Save the file, exit the editor.
   chmod 600 ~/.smbcred

   # setup auto mount
   sudo vi /etc/fstab
   //192.168.30.30/Data /mnt/data cifs vers=3.0,credentials=/home/gerry/.smbcred,rw,uid=1000,gid=976 0 0
   //192.168.30.30/Vids /mnt/vids cifs vers=3.0,credentials=/home/gerry/.smbcred,rw,uid=1000,gid=976 0 0

   # mount and test
   mkdir -p /mnt/data
   mkdir -p /mnt/vids


   cd /mnt/data
   ls
   #empty
   cd /mnt/vids/
   ls
   #empty
   mount -a


   cd /mnt/data
   ls
   #stuff
   cd /mnt/vids/
   ls
   #stuff
   ```

   - Now just start my docker container using new mount points:

   ```shell
   docker run -d --name plexmediaserver --network=host -e TZ="America/Chicago" -e PLEX_CLAIM="my-claim" -h "plex" -v /mnt/s/vids/linux/plexmediaserver/db:/config -v /mnt/s/vids/linux/plexmediaserver/transcode:/transcode -v /mnt/s/vids/linux/plexmediaserver/data:/data plexinc/pms-docker
   ```

   - Ran into an issue:

   ```escape
   Attempting to obtain server token from claim token
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                           Dload  Upload   Total   Spent    Left  Speed
   0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0curl: (6) Could not resolve host: plex.tv
   ```

   - It won't get to the screen where you claim your server...
   - Fix found [here](https://serverfault.com/questions/987686/no-network-connectivity-to-from-docker-ce-container-on-centos-8)

   ```shell
   # Masquerading allows for docker ingress and egress (this is the juicy bit)
   firewall-cmd --zone=public --add-masquerade --permanent

   # Specifically allow incoming traffic on port 80/443 (nothing new here)
   firewall-cmd --zone=public --add-port=32400/tcp --permanent


   # Reload firewall to apply permanent rules
   firewall-cmd --reload

   #Reboot or restart dockerd, and both ingress and egress should work.

   systemctl restart docker

   #then run the docker run command again - good now!

   # add my user to plex
   sudo usermod -aG docker gerry
   ```

5. Set it to run on System Startup:

   - Inside Hyper-V, just set the VM to always run on startup.

   - Inside the Centos 8 VM, create:

   ```shell
   vi ~/start.sh

   #paste in
   #!/usr/bin/env bash

   docker run \
   -d \
   --name plex \
   -p 32400:32400/tcp \
   -p 3005:3005/tcp \
   -p 8324:8324/tcp \
   -p 32469:32469/tcp \
   -p 1900:1900/udp \
   -p 32410:32410/udp \
   -p 32412:32412/udp \
   -p 32413:32413/udp \
   -p 32414:32414/udp \
   -e TZ="America/Chicago" \
   -e PLEX_CLAIM="my-claim" \
   -e ADVERTISE_IP="http://192.168.30.50:32400/" \
   -h "plex" \
   -v /plex/db:/config \
   -v /plex/transcode:/transcode \
   -v /mnt/data:/data \
   -v /mnt/vids:/data-vids \
   plexinc/pms-docker:1.19.4.2935-79e214ead

   # save and exit
   # Add it to crontab so it will run at system startup
   crontab -e
   # paste in
   @reboot	/home/gerry/start.sh
   ```

6. As mentioned, this was working fine and I could have left it at that, but I wanted to be able to import my MediaMonkey playlists and it still doesn't have an import playlist that's easy. I went through tons of articles [playing around with Postman](https://www.reddit.com/r/PleX/comments/ecirqa/how_to_manually_import_an_m3u_playlist_into_plex/), but eventually just decided to use a local plex install again:

   - Run:

   ```shell
   vi /etc/yum.repos.d/plex.repo
   # paste in:
   [PlexRepo]
   name=PlexRepo
   baseurl=https://downloads.plex.tv/repo/rpm/$basearch/
   enabled=1
   gpgkey=https://downloads.plex.tv/plex-keys/PlexSign.key
   gpgcheck=1
   # save and exit
   # now install
   sudo yum install plexmediaserver -y
   ```

   - Now to use my [playlist importer](https://automationadmin.com/2016/12/import-playlist-to-plex/) which still works surprisingly! I may look at [this](https://www.reddit.com/r/PleX/comments/aacg7o/i_made_an_automated_way_to_sync_m3u_playlists_to/) in the future if Plex doesn't offer anything.
