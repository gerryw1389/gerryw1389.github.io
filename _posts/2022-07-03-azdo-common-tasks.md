---
title: 'AZDO: Common Tasks'
date: 2022-07-03T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/azdo-common-tasks
tags:
  - WebSoftware
tags:
  - CICD
---
<!--more-->

### Description:

Different tasks I have done in Azure Devops consolidated because they are too short for their own posts.

### To Resolve:

1. To create a new pipeline: Pipelines => New => Azure Repos Git => Point to Yaml you just pushed => Rename pipeline/Move to folder => Run pipeline

1. Give pipeline permissions to other pipelines => Settings => Service Connections => $connection => Elipses => Security => Add pipleline to list of pipleine permimissions

   - This is needed if you use one pipeline inside another

   ```yaml
   resources:
      repositories:
      - repository: Module_Repo_1
         type: git
         name: My_Project/Module_Repo_1
         ref: main
   ```

1. Create a new Repo: Repos => Dropdown of Repo name at the top => `+ New Repository` 