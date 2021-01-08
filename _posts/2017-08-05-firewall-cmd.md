---
title: Firewall-CMD
date: 2017-08-05T05:27:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/firewall-cmd/
categories:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

In CentOS I created the following firewall zones:

### To Resolve:

1. First, I create a new zone, and then allow only hosts/ports that I specify:

   ```shell
   firewall-cmd --new-zone=gerry --permanent
   firewall-cmd --reload
   firewall-cmd --set-default-zone=gerry #NOTE: You have to reload first before you can select a custom zone as your default zone
   firewall-cmd --zone=gerry --add-source 192.168.0.20/32 --permanent
   firewall-cmd --zone=gerry --add-port=22/tcp --permanent
   firewall-cmd --zone=gerry --add-service=ssh --permanent
   firewall-cmd --reload
   ```

2. Next, to stop other hosts even on the same network from being able to access ports:

   ```shell
   firewall-cmd --remove-active-zone=public
   # Learned quickly that interfaces override source addresses, put that interface in DROP!
   firewall-cmd --zone=public --remove-interface=enp0s3 --permanent
   firewall-cmd --zone=drop --add-interface=enp0s3 --permanent
   firewall-cmd --get-active-zone
   # Should see: gerry - source and drop - interface
   ```

   - Steps 1 and 2 are my setup for initial CentOS VM's. With this setup all incoming ports are blocked except 192.168.0.20:22. You can then add hosts/ports as needed.

3. To check firewall settings:

   ```shell
   sudo firewall-cmd --zone=gerry --list-all
   # Or
   sudo firewall-cmd --zone=gerry --list-sources
   sudo firewall-cmd --zone=gerry --list-services
   sudo firewall-cmd --zone=gerry --list-ports
   ```

4. To add sources, services, and ports:

   ```shell
   # See services:
   firewall-cmd --get-services

   # Then to add (examples from above):
   firewall-cmd --zone=gerry --add-source 192.168.0.20/32 --permanent
   firewall-cmd --zone=gerry --add-port=22/tcp --permanent
   firewall-cmd --zone=gerry --add-service=ssh --permanent
   ```

4. To enable/disable panic mode (block all):

   ```shell
   sudo firewall-cmd --panic-on
   sudo firewall-cmd --panic-off
   ```

5. Common task that I do is add a 'Rich Rule':

   ```shell
   sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.254.24.12/32" port port="3306" protocol="tcp" accept'
   
   # if I need to remove it:
   firewall-cmd --permanent --remove-rich-rule 'rule family="ipv4" source address="10.254.24.12/32" port port="3306" protocol="tcp" accept'

   firewall-cmd --reload
   
   # To view the list of ports being used in total:
   # firewall-cmd --zone=public --list-all

   # Lastly, to test the connection
   curl -v telnet://127.0.0.1:3306

   # look for 'connected'
   # if it doesn't work, see if the port is listening state
   netstat -natl
   # netstat --all --listening --numeric --tcp
   ```

