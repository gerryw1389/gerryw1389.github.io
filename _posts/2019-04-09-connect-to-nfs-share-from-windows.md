---
title: Connect To NFS Share From Windows
date: 2019-04-09T15:55:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/connect-to-nfs-share-from-windows/
categories:
  - Windows
---
<!--more-->

### Description:

Follow this guide to connect to a NFS mount from a Windows machine.

### To Resolve:

1. First install the `Services for NFS` feature in add/remove programs or powershell.

   ```powershell
   Install-WindowsFeature FS-NFS-Service -IncludeAllSubFeature -IncludeManagementTools
   ```

   Default mounts as read only: `mount -o anon \\192.168.10.20\mnt\vms z:`

1. Login to NFS server and get the UID and GUID of a user with write permissions.

2. Then on the Windows box:

   ```powershell
   regedit
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default.
   # Create a new New DWORD (32-bit) Value inside the Default folder named AnonymousUid and assign the UID found on the UNIX directory as shared by the NFS system.
   # Create a new New DWORD (32-bit) Value inside the Default folder named AnonymousGid and assign the GID found on the UNIX directory as shared by the NFS system.
   ```

4. Restart the `NFS client` service or reboot the computer, now the mount should have the appropriate permissions

   - First time connecting takes a long time, after that it is much faster.

   - If this still isn't working, check your `nfs exports` file on the Linux box to ensure it allows connections from Windows machines.

5. 2019-06 Update: One thing to check is the `NFS Settings` tab in File Explorer to get the appropriate UID and GID to set
   - For example:
   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2019/06/nfs-settings.png){:class="img-responsive"}
