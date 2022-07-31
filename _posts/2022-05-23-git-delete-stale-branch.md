---
title: Git Delete Stale Branch
date: 2022-05-23T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/git-delete-stale-branch/
categories:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

So I had an issue the other day where I ran `git branch -va` and saw a bunch of branches that existed locally and not on the remote server. Here is what you do to fix this to get them back in sync.

### To Resolve:

1. First list my current branches

   ```shell
   me@server.domain.com:/home/myuser/my-repo (main) 
   $ git branch 
   MySprint_1.3
   MySprint_1.6
   * main
   ```

1. Then list just the remotes

   ```shell
   me@server.domain.com:/home/myuser/my-repo (main) 
   $ git branch -r
   origin/HEAD -> origin/main
   origin/main
   ```

1. Now remove stale branches from remote and then delete all the branches local that don't match up:


   ```shell
   me@server.domain.com:/home/myuser/my-repo (main) 
   $ git remote prune origin
   URL: git@ssh.dev.azure.com:v3/organization/project/repo
   * [pruned] origin/Sprint_1.3
   $ git branch -D MySprint_1.3
   # Deleted branch MySprint_1.3 (was 510ce91).
   ```

