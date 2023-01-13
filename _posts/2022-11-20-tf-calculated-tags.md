---
title: 'Terraform: Calculated Tags Module'
date: 2022-11-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/11/tf-calculated-tags
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

So a previous issue I discussed was 'how do I have terraform calculate a tag but only one time but also NOT try to change the tag on every apply?' This was discussed in [Pipeline Caller Tag](https://automationadmin.com/2022/09/pipeline-caller) and [LastUpdated](https://automationadmin.com/2022/09/tf-lastupdated-tag) posts. Here is a solution to that problem - store the information in your statefile.


Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-modules/tree/main/calc-tags).
{: .notice--success}


### To Resolve:

1. Create a module that pulls in these providers:

   ```
   required_providers {
      time = {
         source  = "hashicorp/time"
         version = "0.9.1"
      }

      static = {
         source  = "tiwood/static"
         version = "0.1.0"
      }
   }
   ```

1. Then, in your module's [`main.tf`](https://github.com/gerryw1389/terraform-modules/blob/main/calc-tags/main.tf) use them like in the link.

1. Now, in your [composition](https://automationadmin.com/2022/08/calling-remote-modules), you just merge a common set of tags with these auto generated tags each time you want to time stamp resources. This will store the pipeline caller and the resource creations in your state file and will not update on subsequent applies!

   ```
   locals {
      tst_tags = {
         Owner       = "Automation Admin"
         CostCenter  = "100"
         EntAppname  = "Automation Admin Terraform POC"
         Environment = "tst"
         Contact     = "gerry@automationadmin.com"
      }
   }
   module "calculated_tags" {
      source              = "git::https://github.com/gerryw1389/terraform-modules.git//calc_tags?ref=v1.0.0"
      requested_for       = var.requested_for
      requested_for_email = var.requested_for_email
   }
   resource "azurerm_resource_group" "data_sources_1" {
      name     = "unittest-calculated-tags"
      location = "southcentralus"
      tags     = merge(local.tst_tags, module.calculated_tags.run_specific_tags)
   }
   ```

1. Let's break this down

   - We have a common set of tags, `local.tst_tags` defined
   - We then call our module passing in information such as the pipeline callers name and email address. 

   - We currently use Azure Devops so this is `Build.RequestedFor` and `Build.RequestedForEmail` [automatic variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml)
   - But Github Actions has a [similar idea](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables) (GITHUB_ACTOR) that you can pass to terraform in your pipeline.

   - The module responds back with a single output, `run_specific_tags` which is a map object.
   - This map contains two keys: `Creation_Time` and `Pipeline_Creation_User`. Both of these are calculated one time and stored in the state file.
   - On subsequent runs, these will not update.

1. The only catch here is that you will need to create a new block for each time you create a new resource or set of resources:

   ```
   module "calculated_tags_2" {
         source              = "git::https://github.com/gerryw1389/terraform-modules.git//calc_tags?ref=v1.0.0"
         requested_for       = var.requested_for
         requested_for_email = var.requested_for_email
   }
   resource "azurerm_resource_group" "data_sources_2" {
      name     = "unittest-calculated-tags-2"
      location = "southcentralus"
      tags     = merge(local.tst_tags, module.calculated_tags_2.run_specific_tags)
   }
   ```

   - I don't see a way around this just yet, but progress so far!