---
title: Google Backup And Sync Re-syncing ALL Files
date: 2018-05-06T07:23:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/google-backup-and-sync-re-syncing-all-files/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

On the last feature upgrades of W10, I seem to have issues with Google Drive (Backup and Sync) not wanting to work properly. The issues are usually:

  1. Uninstalls itself or treats the computer like it's never been installed.
  2. Two Factor authentication screen grays out when trying to put in Authenticator app passcode.
  3. It wants to sync to %userprofile% instead of my custom location.
  4. It wants to resync all my files instead of the ones that were synced up just fine before the upgrade.

In my case, I got passed the two factor and selecting the folder issue, but Backup and Sync was trying to re-sync ALL my files (400+ GB). This is what I did to resolve:

### To Resolve:

1. First option is &#8220;Delete cloud_graph&#8221;:  
   - Run => `%LocalAppData%\Google`  
   - Find Drive folder, enter it and delete `cloud_graph`  
   - Relaunch Backup and Sync. This will cause it to re-evaluate all files.

2. Second option, the one I chose, is &#8220;Full (Advanced) Reinstall&#8221;:  
   - Quit Backup and Sync  
   - Uninstall it.  
   - Run => `%LocalAppData%\Google`  
   - Delete the entire `Drive` folder.  
   - Reinstall it.

3. Now just reinstall it following these steps SPECIFICALLY:

   - Enter email / Enter password  
   - Sign in on web if you have two factor, the screen will just gray out if you use the Authenticator app => Will probably be fixed in a later release.  
   - Skip the screen about backing up continuously (although that is what you want to do) => DO NOT CHOOSE a folder here.  
   - On the screen where it checks the box to sync google drive, HERE is where you select the folder. If you have a sym link, select that folder.  

4. For example, I have a solid state with limited space so I ran in Admin Powershell prompt (a long time ago):

   ```powershell
   cd c:\
   mklink /d google q:\google
   ```

   - This links a folder at `c:\google` to my `Q drive` which is a 2 TB to a folder called `google` on the root.
   - So when I get to this step, I choose `c:\google` even though it's really at `Q:\google`. It may sound silly, but LOTS of software doesn't know how to act when you point to other drives besides `C:\` !
   - Finish the install. It will scan and only upload changed files. NOTE: This took a very long time, but when it was done, it only synced changed files!

5. I tested these steps twice and I had to follow them both times as if you try skipping the part where you delete the &#8220;Drive&#8221; folder, it will always come back with &#8220;Google wants to merge 1000+ files&#8221; and if you follow these steps, it will come back with &#8220;Needs to merge 30 files&#8221; or however many have changed in the short time you took to upgrade Windows.