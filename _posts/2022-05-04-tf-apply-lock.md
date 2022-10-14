---
title: 'Terraform: Apply Lock'
date: 2022-05-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/tf-apply-lock/
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

Continuing from my [previous post](https://automationadmin.com/2022/05/setup-azdo-terraform/), I then wanted to apply a resource lock to my newly deployed Resource Group to ensure it can't be deleted.

### To Resolve:

1. So first thing as always is to go to the [resource](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/management_lock) on Terraform Docs for the AzureRM provider and found the example and applied it to [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-05-04-tf-apply-lock/Deploy/main.tf):

   ```terraform
   resource "azurerm_management_lock" "resource-group-level" {
   name       = "BlockDelete"
   scope      = azurerm_resource_group.azure_learning_rg.id
   lock_level = "CanNotDelete"
   notes      = "Protect against accidental deletion"
   }
   ```

   - This resulted in an error on build:

   ```
   ╷
   │ Error: Reference to undeclared resource
   │ 
   │   on main.tf line 21, in resource "azurerm_management_lock" "resource-group-level":
   │   21:   scope      = azurerm_resource_group.azure_learning_rg.id
   │ 
   │ A managed resource "azurerm_resource_group" "azure_learning_rg" has not
   │ been declared in the root module.
   ╵
   ##[error]Bash exited with code '1'.

   ```

   - This is actually a good learning lesson. What it is saying is that you don't use the output from the `azure_learning_rg` module because it does not have an output associated with it. Instead, you use `module.azure_learning_rg.res_out_rg_id` because that is defined in the [output.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-05-04-tf-apply-lock/ResourceGroup/outputs.tf)

1. So after correcting and pushing, and then running the [build](https://github.com/gerryw1389/terraform-examples/blob/main/2022-05-04-tf-apply-lock/build.yaml), we now get:

   ```
   Terraform will perform the following actions:

   # azurerm_management_lock.resource-group-level will be created
   + resource "azurerm_management_lock" "resource-group-level" {
         + id         = (known after apply)
         + lock_level = "CanNotDelete"
         + name       = "BlockDelete"
         + notes      = "Protect against accidental deletion"
         + scope      = "/subscriptions/****/resourceGroups/aa-dev-tx-test"
      }

   Plan: 1 to add, 0 to change, 0 to destroy.
   ```

1. So next we run the [release](https://github.com/gerryw1389/terraform-examples/blob/main/2022-05-04-tf-apply-lock/release.yaml):

   ```
   azurerm_management_lock.resource-group-level: Creating...
   ╷
   │ Error: creating Management Lock (Scope: "/subscriptions/****/resourceGroups/aa-dev-tx-test"
   │ Name: "BlockDelete"): locks.ManagementLocksClient#CreateOrUpdateByScope: Failure responding to request: StatusCode=403 -- Original Error: autorest/azure: Service returned an error. Status=403 Code="AuthorizationFailed" Message="The client '****' with object id '****' does not have authorization to perform action 'Microsoft.Authorization/locks/write' over scope '/subscriptions/****/resourceGroups/aa-dev-tx-test/providers/Microsoft.Authorization/locks/BlockDelete' or the scope is invalid. If access was recently granted, please refresh your credentials."
   │ 
   │   with azurerm_management_lock.resource-group-level,
   │   on main.tf line 19, in resource "azurerm_management_lock" "resource-group-level":
   │   19: resource "azurerm_management_lock" "resource-group-level" {
   │ 
   ╵
   ##[error]Bash exited with code '1'.
   ```

   - Again, this is a good thing. It caused me to [read the docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json) which state: `Only the Owner and the User Access Administrator built-in roles can create and delete management locks. You can create a custom role with the required permissions.`

   - So now I update the permissions for `az-terraform` and rerun the pipeline and run it again.

1. This created the lock in the portal:

   - ![applied-lock-rg](https://automationadmin.com/assets/images/uploads/2022/05/lock-created.jpg){:class="img-responsive"}
