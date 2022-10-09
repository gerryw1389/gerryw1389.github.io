---
title: 'GPO: User Backup To File Share'
date: 2016-05-29T04:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-user-backup-to-file-share/
categories:
  - WindowsServer
tags:
  - GroupPolicy
  - Backup
---
<!--more-->

### Description:

This is a quick user backup solution for users on a domain. We needed to setup a backup for users over the network that would backup their documents, favorites, and desktop.

NOTE: We only have like 80 users on our domain so YMMV. If you have a large user base this is not suggested.
{: .notice--success}

### 

1. Create this user logon script batch file

   ```escape
   cd c:\windows\system32\  
   mkdir c:\users\%username%\Documents\IT  
   robocopy C:\Users\%username%\Documents \\fileservername\userbackups\%username%\Documents /E /log:c:\users\%username%\Documents\IT\robo.log  
   robocopy C:\Users\%username%\Desktop \\fileservername\userbackups\%username%\Desktop /E /log:c:\users\%username%\Documents\IT\robo.log  
   robocopy C:\Users\%username%\Favorites \\fileservername\userbackups\%username%\Favorites /E /log:c:\users\%username%\Documents\IT\robo.log
   ```

   - What it does: This script backs up all the files in those locations. If the user deletes them, they still stay on the fileserver.

2. Created a new GPO at the OU container for all users (Domain.com\CorporateUsers)

3. Edited the GPO, went to User Configuration\Policies\Windows Settings\Scripts(Logon/Logoff) and pointed to the script.

   - Located at: \\domain.com\SysVol\domain.com\Policies\{437B28BF-AEBB-45A6-B092-D65E463D5A95}\User\Scripts\Logon

4. Run => cmd => gpupdate on the server and on my computer.

### Maintenance:

1. When the user logs in for the first time, the folder will be created in the share automatically.

2. We then go into the share and edit the permissions for that folder:

   - Disable inheritance and convert to explicit permissions.

   <img class="alignnone size-full wp-image-718" src="https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-2.png" alt="user-backup-to-fileshare-2" width="540" height="275" srcset="https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-2.png 540w, https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-2-300x153.png 300w" sizes="(max-width: 540px) 100vw, 540px" />

   - Remove all users except that user and administrator.

   <img class="alignnone size-full wp-image-719" src="https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-3.png" alt="user-backup-to-fileshare-3" width="369" height="392" srcset="https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-3.png 369w, https://automationadmin.com/assets/images/uploads/2016/09/user-backup-to-fileshare-3-282x300.png 282w" sizes="(max-width: 369px) 100vw, 369px" />


3. After an employee leaves, we move their folder over to another after x amount of days.