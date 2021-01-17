---
title: Move Git From Backup And Sync
date: 2020-09-02T14:27:17-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/move-git-from-backup-and-sync
categories:
  - Windows
tags:
  - VersionControl
  - NoteTaking
---
<!--more-->

### Description:

So up until now, I have always been using a folder under my Google Drive for repo's in Github both personal and work but I have read about these getting out of sync and wanted to get ahead of the curve although everything is currently working (google 'google drive git corrupt', [example](https://stackoverflow.com/questions/31984751/google-drive-can-corrupt-repositories-in-github-desktop)). Here is what I did:

### To Resolve:

1. On my home computer, which is starting to be my work computer now due to Covid and permanent work from home (yay!), I copied `path://google/my-git-repo` to `c:/git/my-git-repo`. I then did:

   - Deleted  `path://google/my-git-repo`
   - Created a batch file with: `robocopy C:\git\my-repo Q:\google\my-git-repo /mir /xd .git`
   - I then changed my VS Code workspaces to go from old location to new location:

   - Old:

   ```json
   {
      "folders": [
         {
               "path": "Q:\\google\\my-git-repo",
         }
      ],
      "settings": {}
   }
   ```

   - New:

   ```json
   {
      "folders": [
         {
               "path": "C:\\git\\my-repo",
         }
      ],
      "settings": {}
   }
   ```

   - Or, lately I have moved all my Powershell repo's to one workspace so it actually looks like:

   ```json
      {
         "folders": [
            {
                  "path": "C:\\git\\my-repo",
            },
            {
                  "path": "C:\\git\\my-repo-2",
            },
            {
                  "path": "C:\\git\\my-repo-3",
            }
         ],
         "settings": {}
      }
      ```

2. After this, I just set that batch file to run daily at midnight so that my git repo's are still backed up (although really not needed).
