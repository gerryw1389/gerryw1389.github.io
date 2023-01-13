---
title: 'Terraform: Assign Azure Role'
date: 2022-11-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/11/tf-assign-rbac
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description

It is very common to have to assign IAM roles at the resource level in Terraform. To do this, it is only a few lines of code:

### To Resolve:

1. Ensure the azuread provider is present in any of your `*.tf` files since terraform doesn't care (usually `backend.tf`, `providers.tf`, or `versions.tf`) :

   ```terraform
   provider "azuread" {
   tenant_id     = var.tenant_id
   client_id     = var.client_id
   client_secret = var.client_secret
   }
   ```

1. In `main.tf` just do a data lookup for the group and assign its `object_id` to the `principle_id` to whatever `scope` you want. For example, at the Resource Group level you would do something like:

   ```terraform
   data "azuread_group" "my_group" {
   display_name = "aa_group_name"
   }

   module "azure_learning_rg" {
   source              = "git::https://github.com/gerryw1389/terraform-modules.git//resource-group?ref=v1.0.0"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-test-remote"
   location            = var.region
   tags                = local.sbx_tags
   }

   resource "azurerm_role_assignment" "owner" {
   scope                = module.azure_learning_rg.id
   role_definition_name = "Owner"
   principal_id         = data.azuread_group.my_group.object_id
   }
   ```
