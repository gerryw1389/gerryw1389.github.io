---
title: Sync Azure Devops Repo
date: 2020-05-20T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/sync-azure-devops-repo
categories:
  - Azure
tags:
  - Cloud
  - Azure-Devops
---
<!--more-->

### Description:

So I will eventually be moving from Github to Azure Devops but first I wanted to see about using just Azure Repo so I had a test project created and tried to sync it to my machine with VScode. Here are the steps:

### To Resolve:

1. First create a project called `TEST` and a repo called `TEST`. Then go create a token by clicking `generate credentials`.

2. As [usual](https://automationadmin.com/2018/02/connect-to-github-private-repo/) just do:

   ```powershell
   cd c:\scripts\devops-test
   git init .
   git config --local user.name 'Gerry'
   git config --local user.email 'gerry@domain.com'
   New-Item -itemtype File -Name "myfile.txt"
   git add --all
   git commit -m 'first'
   git remote add origin https://test@dev.azure.com/test/_git/test
   git push -u origin --all
   ```

3. Enter your credentials when prompted. Be advised I got an error `Error: 'security token doesn't have enough privledges..'` and the fix was to go back to the project and make my user an Administrator of the project.
