---
title: 'Hyper V: Add Space To VM'
date: 2016-05-24T13:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hyper-v-add-space-to-vm/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - VirtualizationSoftware
---
<!--more-->

### Description:

Adding extra hard drive space to a virtual machine.

### To Resolve:

1. Find out how much space is available on the host. Determine the amount of space you need to allocate and then power off the VM.

2. Within Hyper-V, right click the VM => Settings => Hard Drive => Edit => Expand

3. Power on the VM.

4. `Diskmgmt.msc` => Expand the partition. Done.