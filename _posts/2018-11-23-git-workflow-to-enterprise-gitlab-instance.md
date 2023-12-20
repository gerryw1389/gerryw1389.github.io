---
title: Git Workflow To Enterprise Gitlab Instance
date: 2018-11-23T18:50:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/git-workflow-to-enterprise-gitlab-instance/
tags:
  - Linux
tags:
  - VersionControl
  - Bash
---
<!--more-->

### Description:

Similar to my post on how to connect [to Github](https://automationadmin.com/2018/02/connect-to-github-private-repo/), this post is how to use Git to connect to an enterprise internal Gitlab instance. First, find out what branches exist in your company and what their workflow is. It is typically like: development => testing => production. So you will `checkout` development, make changes locally by `commiting`, then `pull/push` often to development branch. When you reach a checkpoint, you will `merge` development into testing/production assuming the code passes all checks.

### To Resolve:

1. First follow the steps in [Connect to Github](https://automationadmin.com/2018/02/connect-to-github-private-repo) to setup your repo to where you can make changes.

2. Now just check out the development branch:

   ```shell
   cd /to/your/git/directory
   git checkout development
   ```

3. Make changes and push often with `git push` and use `git status` to see if you have any issues.

4. Lastly, to merge the development branch with upstream branches, you have to check them out and merge them.

   ```shell
   git checkout testing
   git pull testing
   git merge development

   git checkout production
   git pull production
   git merge testing
   ```

5. Switch back to your local working branch and keep making changes for the next push.

   ```shell
   git checkout development
   ```

