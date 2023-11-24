---
title: Using Docker To Install OpenVAS On CentOS
date: 2018-04-01T00:00:46+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/using-docker-to-install-openvas-on-centos/
tags:
  - Linux
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

Saw a post on [r/sysadmin](https://reddit.com/r/syadmin) the other day with a walkthrough on using Docker for the first time. Thought I would take some notes:

### To Resolve:

1. On the host computer, open up Hyper V and create a new Virtual Machine. Download the Centos7 iso if you don't already have it.

2. Before starting the virtual machine, we need to edit its properties:

   - Change UEFI option to UEFI Authority
   - Change Network Adapter to Enable MAC Address spoofing
   - Enable Nested Virtualization. On the host machine, open Powershell as admin and type:

   ```powershell
   Set-Vmprocessor -Vmname Docker -Enablevirtualizationextensions $True
   ```

3. Install Centos7 [minimal](https://automationadmin.com/2017/08/centos-mate-to-centos-core/) on a Virtual Machine.

4. Update it and give it a static IP, and install Docker stuff:

   ```powershell
   # Update:
   sudo yum update

   # Set a static ip = https://automationadmin.com/2016/10/setting-a-static-ip-in-centos/

   # Install docker
   yum install -y yum-utils device-mapper-persistent-data lvm2
   yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   yum-config-manager --enable docker--ce-edge
   yum-config-manager --enable docker--ce-test
   yum install docker-ce

   # Start and enable docker
   systemctl start docker
   systemctl enable docker
   ```

5. Now that docker is installed, we can search for images to run. For example, let's install OpenVAS:

   ```powershell
   # Search docker images:
   docker search openvas

   # Download an image
   docker pull mikesplain/openvas

   # See images
   docker images
   ```

6. Now lets start and run it:

   ```powershell
   # To run: The command breakdown is: -d is background (detach), -p is ports, --name is just a name, and last is the image file.
   docker run -d -p 443:443 -p 9390:9390 --name openvas mikesplain/openvas

   # To see running docker images:
   docker ps

   # To see installation logs
   docker logs -ft mikesplain/openvas

   # Add firewall exceptions:
   firewall-cmd --zone=public --add-port=443/tcp --permanent
   firewall-cmd --zone=public --add-port=9390/tcp --permanent
   firewall-cmd --reload

   # To see all containers created, but some may be offline
   docker ps -a
   ```

7. That is it, if you want to see the OpenVAS web GUI, just go to https://10.10.10.23 (if the Centos VM static IP is 10.10.10.23) in a browser on CentOS. It should bring up OpenVAS login! Creds are `admin/admin`

### References:

["Docker Part 1: Getting Started"](https://www.youtube.com/watch?v=vIa7UYAe_U4&feature=youtu.be)