---
title: Install Guest Additions To Fedora
date: 2016-05-24T13:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/install-guest-additions-to-fedora/
categories:
  - Linux
tags:
  - LinuxClient
  - VirtualizationSoftware
---
<!--more-->

### Description:

After installing Fedora on VirtualBox with 3 monitors I was happy with Fedora being main work computer. The issue then became a &#8220;virtual box kernel stopped working&#8221; on login. This was after I installed the guest additions the first time. I then followed these steps to do it again:

### To Resolve:

1. Change root user:

```shell
su
```

2. Make sure that you are running latest kernel:

```shell
dnf update kernel*
```

\# reboot if it installs a newer kernel

3. Mount VirtualBox Guest Additions: Click Devices > Install Guest Additions in VB. Open up a terminal and type:

```shell
mkdir /media/VirtualBoxGuestAdditions
mount -r /dev/cdrom /media/VirtualBoxGuestAdditions
```

4. Install following packages:

```shell
dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl
```

5. Add KERN_DIR environment variable:

```shell
KERN_DIR=/usr/src/kernels/`uname -r`
export KERN_DIR

# for Centos: yum install kernel -devel.x86_64 0:3.10.0-327.el7
yum install kernel -devel -4.2.3-300.fc23.x86_64.rpm
```

6. Install Guest Additions:

```shell
cd /media/VirtualBoxGuestAdditions
./VBoxLinuxAdditions.run
```

7. Reboot guest system:

```shell
sudo reboot
```

### References:

["VirtualBox Guest Additions on Fedora 30/29, CentOS/RHEL 8/7/6/5"](http://www.if-not-true-then-false.com/2010/install-virtualbox-guest-additions-on-fedora-centos-red-hat-rhel)