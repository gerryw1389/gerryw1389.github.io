---
title: VirtualBox Centos 7 Mouse Stops Working
date: 2019-05-06T12:34:08+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/05/virtualbox-centos-7-mouse-stops-working/
categories:
  - Linux
tags:
  - LinuxServer
  - VirtualizationSoftware
---
<!--more-->

### Description:

In a CentOS guest VM, you will notice the mouse stops working in a CentOS VM.

### To Resolve:

1. The old fix so far has been to [logout and then back in](https://stackoverflow.com/questions/53918767/mouse-stopped-clicking-in-centos-running-in-virtual-box)

2. The current fix: [Upgrade kernel](https://access.redhat.com/errata/RHSA-2019:0512), so `sudo yum update -y`