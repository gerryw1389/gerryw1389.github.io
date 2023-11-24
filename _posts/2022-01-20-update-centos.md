---
title: Update Centos To Stream
date: 2022-01-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/01/update-centos
tags:
  - Linux
---
<!--more-->

### Description:

Short post here, but I wanted to update my Plex server running on Centos 8 to Centos 8 Stream. Thankfully this was two commands and worked without a hitch.

### To Resolve:

1. Type the following two commands:

   ```shell
   dnf --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos
   dnf distro-sync
   ```

1. I tried looking into [Rocky](https://rockylinux.org/) linux and [Alma](https://almalinux.org/) linux and spent a bunch of time reading into each, but decided to just stick with Centos 8 Stream for now.