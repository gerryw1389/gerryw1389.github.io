---
title: Clean Git Authors
date: 2021-09-08T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/09/clean-git-authors
categories:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description

Short post, I did a few steps to clean up some incorrect git authors (from other accounts on my same computer or different email addresses) on some of my Github repos:

### To Resolve:

1. First, find the commit id in Github that you want to erase:

   ```shell
   git rebase -i ede610e
   # this opens a commit history in vi. Press 'i' for insert mode and change lines 'pick' to the word 'edit'
   # save and quit

   # now type:
   git commit --amend --author="Gerry Williams <gerryw1389@gmail.com>" --no-edit

   # now type:
   git rebase --continue
   # keep doing this over and over

   # when done:
   git push -f
   ```

2. Check Github and all commits should be made by the author specified now.