---
title: Notes on Git
date: 2019-06-08T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/notes-on-git/
categories:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

So I have been using `git` for awhile now, but I still don't really know how it works. Here is my [initial post](https://automationadmin.com/2018/02/connect-to-github-private-repo/) with it. Here is some light reading you (or I can do to be more familiar with it): 

### To Resolve

1. See [here](http://yehudakatz.com/2010/05/13/common-git-workflows/) for common git workflows

2. Here are different git commands:
    
   ```escape
   git clone (url) - copies a repo locally
   git add (flename) - Used to add files to commit.
   git diff - shows differences
   git commit -m "message" - actually makes a save
   git commit -am "message" - adds and commits
   git status - most used command; shows info about git in current directory
   git push (repo name if needed)
   git pull - updates your version
   merge conflict - correct and commit again
   git log - shows log of commits
   git reset --hard <commit> - Reverts back
   git reset --hard (Repo name like - origin/master) - Reverts back to last pull.
   git branch <branch name>
   git checkout <branch name> - switches to that new branch
   git checkout -b  - creates a new branch and moves over to it.
   git merge <branch_name> - branches that branch with current branch
   ```

3. Something I have been fighting with recently is that Vscode ignores linux git settings you set if you have [WSL](https://automationadmin.com/2017/09/windows-subsystem-for-linux-wsl/) enabled. So I would set the global and local configs like mentioned below and vscode would ignore them. I ended up doing the steps in [my Github post](https://automationadmin.com/2018/02/connect-to-github-private-repo/) and installing [GCM](https://github.com/microsoft/Git-Credential-Manager-Core/releases/) which then allowed me to push/pull often without entering credentials.

4. Git has three levels of settings:

   - `system` settings can be found by running `git config --system --list`
     - These settings can be found by running: `git config --system --show-origin --list`

   - `global` settings can be found by running `git config --global --list`
     - These settings can be found by running: `git config --global --show-origin --list`

   - `local` settings can be found by running `git config --local --list` but the trick here is you HAVE to be inside of any repo folder (any folder you previously ran `git init` in) where it stores its settings inside a hidden folder called `.git` in a file called `config`.
     - These settings can be found by running: `git config --local --show-origin --list`

   - If you just run `cd` to any folder that is is a git repo and then type `git config -l` or `git config --list`, it will show a mixture of all git settings for that repo.

5. Operations to add,remove, and modify:

   - To change something, just type its current name and a new value, for example `git config --local user.email gerry.williams@domain.com` will overwrite whatever used to be `user.email` inside the local repo.
   - To remove a value completely, type `git config --global --unset help.format` replace `global` with `system` or `local` as needed. Keep in mind on Windows you will need to run Powershell as administrator to change `system` git settings since they are located in a system directory.
   - To add it back, type `git config --global help.format html`. Syntax is essentially `git config --global|local|system setting.name value`
