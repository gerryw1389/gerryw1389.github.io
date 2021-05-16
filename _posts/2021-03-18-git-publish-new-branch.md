---
title: Git Publish New Branch
date: 2021-03-18T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/03/git-publish-new-branch/
categories:
  - SysAdmin
tags:
  - VersionControl
---
<!--more-->

### Description:

It is considered a good practice to publish a new branch called `dev_your_id` or something and then set that up for submitting pull requests before merging into a `testing` and a `main` branch. Here is how I set up my repos lately.

### To Resolve:

1. First, get [connected to Github Enterprise private repo](https://automationadmin.com/2018/02/connect-to-github-private-repo/)

2. Next, create a new branch locally and push it to the repo:

   ```shell
   git status
   # on branch main
   
   git checkout -b testing
   touch myfile
   git add --all
   git commit -m 'add myfile'
   git push origin testing
   
   git checkout -b dev_gerry
   touch myfile
   git add --all
   git commit -m 'add myfile'
   git push origin dev_gerry
   git status
   # on branch dev_gerry
   ```

3. Next, setup brach protection rules to where you cannot push directly into `testing` or `main`, but first have to get an approval from a pull request:

   - Inside Github, select the repo and go to Settings => Branches => Branch protection rule
   - Check the box: Require pull request reviews before merging => Reviews: 1
   - Branch name pattern: `testing`
   - Copy this a second time to the `main` branch:
   - Branch name pattern: `main`
   - On the main rule, make sure to check the box `Include Administrators`

4. So what this effectively does is make it to where you can do a pull request from `dev_gerry` to `testing` and, if you wish, use your admin privileges on the repo to force a merge between the branches. But you have to get another approver to merge `testing` into `main` or anything into `main`. What I would like to know is how do you stop `dev_gerry` from even being able to do a pull request to `main`? Hopefully I will figure this out and update later.
