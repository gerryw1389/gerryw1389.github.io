---
title: Github Desktop To VsCode
date: 2019-07-03T23:40:01-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/07/github-desktop-to-vscode/
tags:
  - Windows
tags:
  - PersonalConfig
---
<!--more-->

### Description:

I followed these steps to delete Github Desktop and just use VSCode for pushing to different repos.

### To Resolve:

1. In VSCode, set global options. I set my work email since most of my repos are set to go to their local Gitlab instance

   ```shell
   git config --global user.email "myemail@domain.com"
   git config --global user.name "Firstname Lastname"
   git config --global core.autocrlf true 
   ```

2. Uninstall any references to external programs
   - Uninstall Git Desktop ([Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `appwiz.cpl` => Remove Github Desktop)
   - Uninstall Credentials Manager:
     - `cd "C:\Program Files\Git\mingw64\libexec\git-core"`
     - `git-credential-manager.exe uninstall`
   - Reset credentials helper to use wincred 
     - `git config --global credential.helper wincred`

3. Used VS Code to Push some changes and re-input credentials. Usually something along the lines of:

   ```shell
   git remote add origin https://github.com/gerryw1389/gerryw1389.github.io
   git push --set-upstream origin master
   git add --all 
   git commit -m 'example'
   git pull
   git branch --set-upstream-to=origin/master
   git push
   ```

4. Repos: Since I have 4 different repos all in different folders, what I did was go to each repo and:

   - Run `git config -l` and look for the correct origin. 
     - If it is wrong, type `git remote rm origin` and `git remote add origin https://path/to/repository` then confirm `git remote get-url --all origin`

   - Run `git config --local user.name "Gerry Williams"` and `git config --local user.email "myemail@gmail.com"`. This is so that my personal email can be attached to Github repos while other repos will still get my work email by default.

   - Lastly for each repo I would create a test file and do a push and look for/resolve any errors. For example:

   ```shell
   touch myfile.txt
   git add .
   git commit -m 'testing vscode'
   git push origin
   ```

   - Sometime I would get

   ```escape
   error: the current branch master has no upstream branch
   ```

   - fix: `git push --set-upstream origin master`

   - You might then get

   ```escape
   fatal: refusing to merge unrelated histories
   ```

   - fix: `git push origin master --force`
