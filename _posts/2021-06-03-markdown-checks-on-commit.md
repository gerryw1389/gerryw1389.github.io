---
title: 'Github Actions: Markdown Checks On Commit'
date: 2021-06-03T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/06/markdown-checks-on-commit
categories:
  - Azure
tags:
  - Cloud
  - CICD
---
<!--more-->

### Description

Follow this post to have Github Actions check URLs on Commit. It uses Github hosted runners with a node package that will check Markdown format and validity of external urls on your site. 

### To Resolve:

1. Go to [Azure-in-bullet-points](https://github.com/undergroundwires/Azure-in-bullet-points/tree/1bf689a77918a5bcfc9556235291d35791367ba2) repo

2. Copy the `package.json`, `package-lock.json` and `.github/workflows/quality-checks.yml` files to your site.

3. Try tweaking it if needed, but you should be able to do a push to Github and it will check URLs on your website. 

4. I have since removed it on mine due to the high amount of posts and low amount of effort I want to put in to fix :)
   - Original code is still retained [here](https://github.com/gerryw1389/misc/tree/main/old-github-actions) though if interested