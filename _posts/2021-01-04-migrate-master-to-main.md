---
title: Migrate Master To Main
date: 2021-01-04T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/migrate-master-to-main
tags:
  - SysAdmin
tags:
  - VersionControl
---
<!--more-->

### Description:

This post is documents how I updated my git repositories to rename from master to main and to update terminology when explaining things to IT people. See [here](https://cdm.link/2020/06/lets-dump-master-slave-terms/) and [here](https://www.zdnet.com/article/github-to-replace-master-with-main-starting-next-month/) for a background.

### To Resolve:

1. First, for each repo on your computer, cd into the repo and run:

   ```shell
   # Step 1 
   # create main branch locally, taking the history from master
   git branch -m master main

   # Step 2 
   # push the new local main branch to the remote repo (GitHub) 
   git push -u origin main

   # Step 3
   # switch the current HEAD to the main branch
   git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main

   # Step 4
   # change the default branch on GitHub to main
   # https://docs.github.com/en/github/administering-a-repository/setting-the-default-branch

   # Step 5
   # delete the master branch on the remote
   git push origin --delete master
   ```

2. Keep a mental note to use the new terms:

   ```escape
   master => main
   slave => secondary
   whitelist => allowlist
   blacklist => blocklist
   ```
