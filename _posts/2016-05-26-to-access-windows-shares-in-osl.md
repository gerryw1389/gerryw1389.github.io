---
title: To Access Windows Shares In OSL
date: 2016-05-26T04:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/to-access-windows-shares-in-osl/
categories:
  - Linux
tags:
  - LinuxClient
  - FileSystem
---
<!--more-->

### Description:

If your computer is on the same network as a computer running Windows and you want to access a share, follow these steps:

### To Resolve:

1. Launch Dolphin File Manager and type `smb://(ip-address)` of the Windows share.

   - If you don't know the IP-address of the share, you can browse the local network by simply entering `smb:/` in the Dolphin location bar.

   - However, this will only work if you configure the firewall first.  

     - Kickoff menu => Computer tab => YaST => Security and Users => Firewall => Allowed Services => Select `Samba Client` and `Netbios Server` in the Service to allow combobox and add them.

2. To Share Your Files:

   - To share your files with MS Windows users, Mac OSX users or other GNU/Linux users on the local network you must configure the Samba Server (make sure the packages `yast2-samba-server` and `samba` are installed). You only need to perform the first three steps the first time you want share a folder.

   - Open the YaST Samba Server module. Kickoff menu => Computer tab => YaST => Network Services => Samba Server

   - In the tab Start-Up and select whether to autostart the Samba service during boot and whether to open the firewall ports required.

   - Go to the Shares tab, check the options Allow Users to Share Their Directories and Allow Guest Access. In the Identity tab you can configure your workgroup and share name.

   - Now open the Dolphin file manager, right click the folder you want to share, click Properties => Share.
