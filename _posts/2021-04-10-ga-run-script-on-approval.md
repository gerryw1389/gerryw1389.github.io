---
title: 'Github Actions: Run Python Script On Approval Pull Request'
date: 2021-04-10T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/04/ga-run-script-on-approval/
categories:
  - Azure
tags:
  - Cloud
  - CICD
  - Scripting-Python
---
<!--more-->

### Description:

This post will build on a [previous post with Github Actions](https://automationadmin.com/2020/08/github-actions-search-for-string) in which we will run a python script instead of a bash script on Pull Requests. It is also built on [the publish new branch](https://automationadmin.com/2021/03/git-publish-new-branch/) post so give that a read as well if you haven't already.

### To Resolve:

1. So the first thing you will need to do is go to your repo inside Github Web UI and add the secret `API_MGMT_KEY` which matches your `Ocp-Apim-Subscription-Key` value for the header you will pass to your API Mgmt endpoint.

2. Next, go to my [Github](https://github.com/gerryw1389/python/tree/main/scripts/example-run-python-script-on-approval/.github) and copy all the files under `example-run-python-script-on-approval`

   - Make sure you have the `workflow` and `script` folders with their associated files.

3. The way this works is that when you do a pull request where you are merging from your `dev_gerry` branch to branch `testing`, it will perform one of two actions:
   - If the approver approves and the branches are merged, a script `api-testing-branch.py` is fired.
   - Likewise on branch `main` a script `api-main-branch.py` is fired.
