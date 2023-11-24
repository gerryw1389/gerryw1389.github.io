---
title: SFTP Server Migration
date: 2016-05-30T04:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ftp-server-migration/
tags:
  - WindowsServer
tags:
  - Migration
---
<!--more-->

### Description:

We needed to setup a new FTP server that is SFTP compliant and can run on Server 2012. This ended up being a similar to process to migrating a file server.

### To Resolve:

1. Follow the steps on [Create A New VM](https://automationadmin.com/2016/05/hyper-v-to-create-a-new-vm/).

2. Once the VM is created, install the SFTP server software.

3. After installation, open up the old box and the new one and mirror the directories and users exactly. We didn't have many users so we recreated them and changed their passwords. For mirroring the directories of the FTP server to the SFTP server, we just used robocopy:

   ```escape
   robocopy z: g: /mir
   ```

^Assuming the original FTP data was shared out and mapped on the SFTP server as the Z: with the SFTP server hosting the SFTP data on the G: