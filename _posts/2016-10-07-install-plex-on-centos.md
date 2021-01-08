---
title: Install Plex On CentOS
date: 2016-10-07T04:05:58+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/install-plex-on-centos/
categories:
  - Linux
tags:
  - LinuxServer
  - MediaEditing
---
<!--more-->

### Description:

Follow these steps to install Plex on CentOS 7.

### To Resolve:

1. Go to [Plex Downloads](https://www.plex.tv/downloads/) and get the latest installer for your OS, in this case CentOS 7:

   ```shell
   sudo yum install plexmediaserver_0.9.8.18.290-11b7fdd_x86_64.rpm

   # Start the service
   sudo systemctl start plexmediaserver.service

   # Set the service to run on startup
   sudo systemctl enable plexmediaserver.service

   # Open a firewall port for it
   firewall-cmd --zone=public --add-port=32400/tcp --permanent

   # If you set it to a different port (which is recommended), add it to the SEMANAGE exceptions
   sudo semanage port -a -t http_port_t -p tcp (portNumber)
   ```

2. To Change the Plex User:

   - All of my media files are on a Samba share with permissions of 770, so I had to change Plex to access the share as my user:

   ```shell
   # Stop the service
   sudo systemctl stop plexmediaserver

   # Add my user to the plex group
   sudo usermod -a -G plex gerry

   # Edit the config file that tells Plex which user to run as
   sudo vi /etc/sysconfig/PlexMediaServer

   # Change user to gerry
   sudo chown -R gerry /var/lib/PlexMediaServer

   # Change the user in the service config file
   sudo vi /lib/systemd/system/plexmediaserver.service

   # Reload the daemon
   sudo systemctl daemon-reload

   # Start the service again
   sudo systemctl start plexmediaserver
   ```

3. To Update Plex:

   ```shell
   # Download the update to your downloads and open a up a terminal
   systemctl stop plexmediaserver
   wget https://downloads.plex.tv/plex-media-server-new/1.16.5.1554-1e5ff713d/redhat/plexmediaserver-1.16.5.1554-1e5ff713d.x86_64.rpm
   rpm -Uvh plexmediaserver-vXXXX
   systemctl start plexmediaserver
   ```