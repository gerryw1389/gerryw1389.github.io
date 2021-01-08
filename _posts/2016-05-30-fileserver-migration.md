---
title: FileServer Migration
date: 2016-05-30T03:25:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/fileserver-migration/
categories:
  - WindowsServer
tags:
  - Migration
  - Backup
---
<!--more-->

### Description:

Migrating a file servers is a relatively easy task. That being said, if you don't setup the permissions and shares successfully, people are quick to notice when their working directory is not available.

### To Resolve:

1. So our current server is WS08 and I wanted to move to WS2012R2. So I created a dynamically expanding WS2012R2 vm. I then got it prepped by doing the following:

   - CMD => `netsh firewall set icmpsetting 8 enable` # allows ping  
   - Turned on RDP and made a rule for it in the firewall using the GUI.  
   - Disabled UAC.  
   - Ran Windows Updates over and over rebooting as often as it asks.  
   - Renamed the server to FILE2 since our current server is called FILE.

2. I paused replications in Veeam where FILE was being replicated to another server in case it crashed. I then had to decide on how to copy the primary shares data. I went with on my favorite tools => Robocopy. I really want to use Powershell more but Robocopy is beast with anything syncing directories.

3. I mapped the current share as the &#8220;Z:&#8221; on FILE2 and then joined it to the domain.

4. I then ran: `robocopy z:\ g:\ /mir /sec /secfix /v /mt:20 /log:c:robocopy.log /tee`

5. Once the directories were mirrored, I then just had to check FILE for any leftover data, scheduled tasks, local users, ect. and make sure they got migrated to FILE2. Thankfully, we have plenty of specific VM's so there wasn't anything else to move over.

   - It took us a while having both servers and waiting to do the migration so I setup a scheduled task to point to the following batch file to run everyday at 2 AM:

   ```escape
   cd C:\Windows\System32  
   net use z:\ \\FILE\data  
   robocopy z:\ g:\ /mir /sec /secfix /copyall /R:5 /W:1 /log:C:robo.log /tee
   ```

#### On Migration Day:

6. I went in the DC and took note of the Reservation setup for FILE1. I then deleted FILE1 from DNS and DHCP. I also took it off the domain and renamed it to FILE-OLD.

7. Renamed FILE2 to FILE1. Took note of the MAC address and setup a reservation for it in DNS and DHCP.

8. Done! All clients that pointed to FILE will never know that the sever changed. Our setup was a simple one since it was a flat file system migration. Microsoft advises you follow [this](https://technet.microsoft.com/en-us/library/jj863566.aspx) link for more advanced file server migrations.