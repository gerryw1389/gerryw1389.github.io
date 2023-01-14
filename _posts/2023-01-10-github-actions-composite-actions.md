---
title: 'Github Actions: Composite Actions'
date: 2023-01-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/github-actions-composite-actions
categories:
  - WebSoftware
tags:
  - CICD
---
<!--more-->

### Description:

So in my [workflows directory](https://github.com/gerryw1389/terraform-examples/tree/main/.github/workflows) was getting packed with Github Action Workflows from all my previous posts so I decided to move them only to find out that Github Actions require them to be in that folder directly, [not a subfolder](https://stackoverflow.com/questions/64009546/how-to-run-multiple-github-actions-workflows-from-sub-directories). Boo! Following the guidence in that link I was able to create [composite actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#runs-for-composite-actions) that call [action files](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action#creating-an-action-metadata-file). This is the final result:

### To Resolve:

1. Similar to templates in Azure Devops, I just have the [build](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/composite-build.yaml) point to any of my subfolders and pass in parameters there.

1. Same for [release](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/composite-release.yaml), I just update the directory I'm passing to.

