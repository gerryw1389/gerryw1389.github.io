---
title: Pipeline Caller Tag
date: 2022-09-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/09/pipeline-caller
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
  - Azure-Devops
---
<!--more-->


### Description:

Quick post here but I wanted to find a way to add a tag in the Azure portal for all resources deployed by the pipeline caller since the Terraform pipeline use a Service Principle that is shared by all users of a team. This helps reduce confusion because the Activity Log in the portal will just show that your Service Principle created a resource on a specific date but not who actually ran the pipeline to create the resources.

### To Resolve:

1. The main fix is to add the `Build.RequestedFor` and `Build.RequestedForEmail` [automatic variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml) from Azure Devops into the pipeline like so:

   - In your `build.yaml`, just add `-var="requested_for=$(Build.RequestedFor)" \ -var="requested_for_email=$(Build.RequestedForEmail)" \` in your terraform plan
   - Then in your `variables.tf`, add:

   ```terraform
   variable "requested_for" {
      description = "(Required) Azure Devops Automatic Variable used for tagging resources."
      type        = string
   }

   variable "requested_for_email" {
      description = "(Required) Azure Devops Automatic Variable used for tagging resources."
      type        = string
   }
   ```

- And then  in your `main.tf`, add something like:

   ```terraform
   locals {
      tags = {
         Owner       = "Automation Admin"
         CostCenter  = "100"
         EntAppname  = "Automation Admin Terraform POC"
         Environment = "tst"
         Contact     = "gerry@automationadmin.com"
         Latest_RunBy  = "${var.requested_for} - ${var.requested_for_email}"
      }
   }
   ```