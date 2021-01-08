---
title: Mapped Network Drives Issues
date: 2016-05-21T22:13:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/mapped-network-drives-issues/
categories:
  - Networking
tags:
  - FileSystem
---
<!--more-->

### Description:

A mapped network drive is a drive or a folder connected to a computer that is being shared from another. The one sharing is called the &#8220;server&#8221; even though it's not always an actual server and the computer mapping the drive is called the &#8220;client&#8221;. Most networks have a server sharing out a &#8220;Data&#8221; drive that all the workstations map. Different issues arise with these connecting from time to time, usually indicating the source of the drive (the server) has gone offline. If you can open the drive in Windows Explorer, the drive is currently connected and working. If there is a red &#8220;X&#8221; on the drive or it never opens, try the following steps.

### To Resolve:

1. On the client computer, Run => `\\ServerComputerName` to see if it can read the shared files. If this returns a `Network Path Unavailable` error, see [One Workstation Won't Connect To the Network](https://automationadmin.com/2016/05/one-workstation-cannot-connect-to-the-network/). Make sure to complete those steps first.

2. If the drive is mapped and asks for credentials when you open it, you need to add the credentials from the client to the server. Example: I am logged in on a workstation as `user\12345`. The server needs to have a local user with the same exact credentials in order for the mapped drive to work. You will need to get on the server computer and add your user info to its list of users. To do this, Run => `compmgmt.msc` => local users and groups => users => add user => enter your info. You cannot have the same user name with different passwords, it will not work. If you are on a workgroup with all users the same name, they need to have the same password if they are all mapped to a single shared folder/ drive.

3. Make sure the server computer is sharing out with full permissions if you want all computers to connect to it or make sure all client users are in the correct group that has &#8220;Read&#8221; access to the folder/drive. Really, they should have &#8220;Full Control&#8221; so that each user can read/ write/ modify files on this drive/ folder.

4. If it's still not working, look at the Windows Time. Go to time and date settings => internet time => and change time.windows.com to any of the others. This gets bogged down sometimes and can get tampered during networking issues.

5. Check the link speed of the client computer to the server computer. Run a series of pings to determine if they are able to communicate at normal speeds, should be >1ms or so.

6. Once the issue is resolved, on the client computer, right click on the drive and &#8220;Disconnect&#8221; it (if it was previously connected), then Run => `\\ServerComputerName` => Right click on the drive => Map Network Drive. Enter the login credentials for the server computer and remember to check the &#8220;reconnect at logon&#8221; and &#8220;remember my credentials&#8221; boxes.This will re-add the drive with your new credentials.

### To Use A Batch File For Startup:

1. Should look like: `net use m: \\ServerComputerName\d_drive /persistent:yes`  
   - where &#8220;server&#8221; is the server computer's NETBIOS name and &#8220;d_drive&#8221; is the name of the folder/drive being shared. Note that the letter &#8220;m:&#8221; plays no significant role.

### If A Mapped Drive Doesn't Want To Delete:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `Net use n: /delete` # where n is drive letter. Use `\*` to delete all mapped drives at once, ex Type: `net use \* /delete`

2. If that doesn't work, Run => `Regedit` => Navigate to: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints\2`

3. You will see `\\ServerComputerName\share` subfolders. Delete the folders you don't want and reboot.

### References:

["Unable to delete a network drive in windows 7"](http://superuser.com/questions/416295/unable-to-delete-a-network-drive-in-windows-7)