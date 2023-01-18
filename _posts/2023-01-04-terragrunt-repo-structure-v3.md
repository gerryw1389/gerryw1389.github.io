---
title: 'Terragrunt: Repo Structure V3'
date: 2023-01-04T09:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/terragrunt-repo-structure-v3
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

This post builds on [Terragrunt Repo Structure V1](https://automationadmin.com/2023-01-04-terragrunt-repo-structure-v1) by simply showing the pros/cons of embedding terraform files in the same structure as terragrunt files.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v3). [Github Actions are here](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2023-01-04-terragrunt-repo-structure-v3/).
{: .notice--success}

### To Resolve:

1. In this post I just want to show that it is **possible** but not recommended to put your terraform files in the same file structure as you terragrunt files.

1. Let's discuss the pros of this approach:

   - It is very noobie friendly. People don't have to get confused with terragrunt stuff as they can clearly see that the [deployment folder here](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v3/infra-config/nonprod/hub/southcentral/deployment) contains terraform files specific to nonprod => hub => south central region. So it is easy to add a variable or a new resource that is scoped specifically to that area, no guess work involved.

2. Let's discuss the cons of this approach:

   - Main con is lots of duplication. It is highly unlikely that your infrastructure is unique at each and every level of your folder structure.
   - For example, resources deployed in the `east` will be highly similar to those deployed in the `south central us`
   - Nonprod and prod I can see separation needed, but that is covered in [Terragrunt Repo Structure V2](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2).
   - What about between subscriptions? It shouldn't matter what code is deployed between `hub` and `spoke` subscriptions right? Remember that you can have a different repo with different state files that manage things in one subscription but not another, no need to have everything in one single repo with one giant statefile per environment/region/subscription though you could if you wanted.

3. For any excuse you can give to embed your terraform files in with your terragrunt files, you can still move them up to a different folder structure as discussed in [Terragrunt Repo Structure V2](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2).

   - For example, you could have:

   - `./infra/nonprod/east` and then in your `./infra-config/nonprod/hub/east/deployment/terragrunt.hcl` just point your `source` to `"${find_in_parent_folders("infra")}//nonprod//hub//east"`. Yes this would be a lot of duplication of folder structures, but at least your terragrunt and terraform files are separated.