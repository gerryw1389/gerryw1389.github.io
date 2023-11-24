---
title: OSL Samba Server Config
date: 2016-05-26T04:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/osl-samba-server-config/
tags:
  - Linux
tags:
  - LinuxClient
  - FileSystem
---
<!--more-->

### Description:

Sharing NTFS shares on OpenSuse Linux (OSL) requires the following:

### To Resolve:

**On Windows:**

1. Cmd => `net config workstation` # take note of the workgroup name.

2. Cmd => `notepad c:\windows\system32\drivers\etc\hosts` # add the opensuse hostname and IP.

**On Opensuse:**

1. Yast => Network Services => Samba Server => Startup tab: During boot radio button, Open port in Firewall. Shares tab: Select share path and then check the boxes for &#8220;Allow users to share their directories&#8221; and &#8220;Allow guest access&#8221;. Identity tab: Enter your workgroup name. Done here.

2. Yast => System => System Services (Runlevel) => Highlight &#8220;nmb&#8221; and &#8220;smb&#8221; and select enable (one at a time).

3. Open up the directory in your file explorer (Dolphin by default), right click the shared folder and go to Properties. Here check the boxes to &#8220;Share with Windows&#8221; and &#8220;Allow guests&#8221;

4. Open up terminal and type:

   ```shell
   sudo smbpasswd -a username
   # fill out the password
   ```

5. Now just go to Dolphin => Network => Samba Shares => (Your Workgroup)

   - Samba config file is located at `/etc/samba/smb.conf`
   - Back On Windows, Run => `\\opensuseIP` # You should be able to browse network shares.