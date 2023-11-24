---
title: 'Veeam: Creating A Backup Job'
date: 2017-08-26T05:18:06+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/veeam-creating-a-backup-job/
tags:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

I realized I didn't have a post about this yet, so I wanted to throw this out there.

### To Resolve:

1. First you need to organize your backups according to retention schedules. We do 21 days for file servers and 14 days for everything else.

2. Next, open the Veeam GUI and create a new backups job:

   - Name = Whatever

   - Virtual Machines = Select the VM host and then add each one

   - Storage = Choose backup repository , Restore points to keep on disk (14 or 21 => Advanced: Backup => Use Encryption (Storage Tab) and incremental (default on the Backup tab)  
Guest Processing = Enable Application aware processing and then click the &#8220;Applications&#8221; button. For anything other than SQL or DC, click &#8220;Disable Application Processing&#8221; on the General tab. For SQL/DC just leave defaults which is &#8220;Require success; truncate logs&#8221;  
Guest OS Credentials = In the main box select the host servers login credentials then click the credentials button to select credentials for each VM. Make sure to do &#8220;Test Now&#8221; after entering them, even if you know they are right. Sometimes it will fail and you need to make sure you can access `\\ServerComputerName\c$` from Windows Explorer.

   - Schedule = Run automatically # Suggest you stagger your backups to where fileserver, normal, fileserver, normal.

   - Save/Finish