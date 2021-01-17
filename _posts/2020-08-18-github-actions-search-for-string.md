---
title: 'Github Actions: Search For String'
date: 2020-08-18T11:10:16-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/github-actions-search-for-string
categories:
  - WebSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

So I wanted a way that when I did a push to my Github repo, it would scan all my files for a particular phrase and fail the job if it found it. This is because I have two repos - one prod and one test, but each uses different servers on-prem for REST API calls and such. Well sometimes when I copy/paste between TEST/PROD, I will accidentally copy those server names and forget to switch them.

Using Github Actions, I could get a 'failed' notification on push if it finds these server names - perfect! So first, I tried to setup this action with [18 stars](https://github.com/marketplace/actions/find-and-replace), but when I tried it - it didn't do anything. No error, but the string I wanted it to replace was still there. Here is what ended up working:

### To Resolve:

1. Locally, in vscode, I created `.github/workflows/ps-check.yml` in my repo with the following:

   ```yml
   name: ps-check-workflow
   on: [push, pull_request]
   jobs:
   build:
      runs-on: ubuntu-latest
      steps:
         - uses: actions/checkout@v2
         
         - name: PS-Check
         uses: SleepySysadmin/github-action-pscheck@v0.4.2
   ```

   - This is not related to the original issue, but what it does is run PSScriptAnalyzer on every push so my push should fail if I have invalid code.

2. Created `.github/workflows/run-script.yml` in my repo with the following:

   ```yml
   name: run-script-workflow
   on: [push, pull_request]
   jobs:
   build:
      runs-on: ubuntu-latest
      steps:
         - uses: actions/checkout@v2

         - name: Check for prod server names
         run: |
            chmod +x ./.github/scripts/run-check.sh;
            ./.github/scripts/run-check.sh
         env: 
            MYVAR: something-unique
         shell: bash
   ```

   - This is the action that will call my bash script in the next steps

3. Created `.github/scripts/run-check.sh` in my repo with the following:

   ```shell
   #echo "MYVAR: $MYVAR"

   search=$(grep -r 'prodServer' ./runbooks/*.ps1)

   if [[ -z "$search" ]]
   then
      :
   else
      MYVAR='not-unique'
   fi

   searchSN=$(grep -r 'prodServer2.domain.com' ./runbooks/*.ps1)
   if [[ -z "$searchSN" ]]
   then
      :
   else
      MYVAR='not-unique'
   fi


   if [ $MYVAR == "something-unique" ]
   then
      exit 0
   else
      echo $search
      echo $searchSN
      exit 1
   fi
   ```

   - Ran locally before pushing: `git update-index --chmod=+x ./.github/scripts/run-check.sh`

4. With those files created and chmod command ran, do a push to your repo. Now in Github, go the Actions tab in your repo and you should see two actions running - `ps-check-workflow` and `run-script-workflow`. Congrats!

5. Optionally, in my `README.md` at the repo root, I entered `![ps-check-workflow](https://github.com/myuser/myrepo/workflows/ps-check-workflow/badge.svg)` at the top of my file and pushed again and got the cool badge notifications that will say `passing` or `failed`. See [here](https://docs.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#adding-a-workflow-status-badge-to-your-repository) for more info.
