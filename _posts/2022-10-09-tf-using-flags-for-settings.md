---
title: 'Terraform: Using Flags For Settings'
date: 2022-10-09T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/tf-using-flags-for-settings
tags:
  - Terraform
---
<!--more-->

### Description:

As you start developing Terraform [compositions](https://automationadmin.com/2022/08/calling-remote-modules) and modules, you will want to optionally deploy resources. We [discussed this in a previous post](https://automationadmin.com/2022/08/tf-conditional-deploy) by using the `count` [meta argument](https://automationadmin.com/2022/07/tf-count) to deploy a resource by setting its value to `1` to deploy and `0` to not deploy. Here is a few more examples:

### To Resolve:

1. So `Option 1` is to use count and check for a condtion to deploy a single resource like shown below:

   ```terraform
   module "azure_learning_rg" {
   count = var.region == "southcentralus" ? 1 : 0
   source              = "git::https://github.com/gerryw1389/terraform-modules.git//resource-group?ref=v1.0.0"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-test-remote-2"
   location            = var.region
   tags                = local.sbx_tags
   }
   ```

   - We see in [`main.tf`](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-07-tf-conditional-deploy/main.tf) that if the variable `region` is set to `southcentralus` which is its default in [`variables.tf`](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-07-tf-conditional-deploy/variables.tf) then it will deploy the Resource Group.

   - Cool, so it will conditionally deploy that one Resource Group and its associated lock.

1. `Option 2` is the same as option 1, but will deploy multiple resources. Here I will create a file called `C:\scripts\tf\local-state\blah.tf` :

   ```terraform
   terraform {
   required_providers {

      azurerm = {
         source  = "hashicorp/azurerm"
         version = ">3.10.0"
      }

   }
   required_version = ">1.1.0"
   }

   provider "azurerm" {
   client_id                  = var.client_id
   client_secret              = var.client_secret
   subscription_id            = var.subscription_id
   tenant_id                  = var.tenant_id
   skip_provider_registration = true
   features {}
   }

   variable "tenant_id" {
   description = "(Required) Service Principal AD Tenant ID - Azure AD for terraform authentication."
   type        = string
   }

   variable "subscription_id" {
   description = "(Required) Azure Subscription Id used to connect to AzureRM provider."
   type        = string
   }

   variable "client_id" {
   description = "(Required) Service Principal App ID - Azure AD for terraform authentication."
   type        = string
   }

   variable "client_secret" {
   description = "(Required) Service Principal Client Secret - Azure AD for terraform authentication."
   type        = string
   }

   locals {
   resource_groups = ["one", "two", "three"]
   }

   resource "azurerm_resource_group" "rg" {
   count    = length(local.resource_groups)
   name     = "aa-my-rg-${local.resource_groups[count.index]}"
   location = "southcentralus"
   }
   ```

   - Next I run each command one at a time:

   ```powershell
   cd C:\scripts\tf\local-state
   terraform init
   terraform plan -var-file="env.tfvars" -out="tf.plan"
   ```

   - where `env.tfvars` just has stuff to connect to Azure as required variables.

   - I get this output:

   ```escape
   > terraform plan -var-file="env.tfvars" -out="tf.plan"

   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg[0] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-one"
      }

   # azurerm_resource_group.rg[1] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-two"
      }

   # azurerm_resource_group.rg[2] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-three"
      }

   Plan: 3 to add, 0 to change, 0 to destroy.
   ```

   - OK, so this will deploy the same number of resources as the number of elements my list object `resource_groups` and will assign whatever their value is to the `name` argument for [`azurerm_resource_group`](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group#name).

   - Cool, but we [discussed this before](https://automationadmin.com/2022/07/tf-for-each), you should [always use for_each instead](https://www.terraform.io/language/meta-arguments/count#when-to-use-for_each-instead-of-count) so that you can update it freely without destroying and recreating all resources:

   ```terraform
   terraform {
   required_providers {

      azurerm = {
         source  = "hashicorp/azurerm"
         version = ">3.10.0"
      }

   }
   required_version = ">1.1.0"
   }

   provider "azurerm" {
   client_id                  = var.client_id
   client_secret              = var.client_secret
   subscription_id            = var.subscription_id
   tenant_id                  = var.tenant_id
   skip_provider_registration = true
   features {}
   }

   variable "tenant_id" {
   description = "(Required) Service Principal AD Tenant ID - Azure AD for terraform authentication."
   type        = string
   }

   variable "subscription_id" {
   description = "(Required) Azure Subscription Id used to connect to AzureRM provider."
   type        = string
   }

   variable "client_id" {
   description = "(Required) Service Principal App ID - Azure AD for terraform authentication."
   type        = string
   }

   variable "client_secret" {
   description = "(Required) Service Principal Client Secret - Azure AD for terraform authentication."
   type        = string
   }

   locals {
   resource_groups = [
      { name = "one" },
      { name = "two" },
      { name = "three"}
   ]
   }

   resource "azurerm_resource_group" "rg" {
   for_each = { for rg in local.resource_groups : rg.name => rg }
   name     = "aa-my-rg-${each.value.name}"
   location = "southcentralus"
   }
   ```

   - New output:

   ```escape
   > terraform plan -var-file="env.tfvars" -out="tf.plan"

   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg["one"] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-one"
      }

   # azurerm_resource_group.rg["three"] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-three"
      }

   # azurerm_resource_group.rg["two"] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-two"
      }

   Plan: 3 to add, 0 to change, 0 to destroy.
   ```

   - Here is the "before":

   - ![rg-for-each-1](https://automationadmin.com/assets/images/uploads/2022/10/rg-for-each-1.jpg){:class="img-responsive"}

   - For example, let's update the code to add 'bob' and 'jim' resource groups:

   ```terraform
   # <...> omitted for brevity
   locals {
   resource_groups = [
      { name = "one" },
      { name = "two" },
      { name = "bob"},
      { name = "three"},
      { name = "jim"}
   ]
   }

   resource "azurerm_resource_group" "rg" {
   for_each = { for rg in local.resource_groups : rg.name => rg }
   name     = "aa-my-rg-${each.value.name}"
   location = "southcentralus"
   }
   ```

   - This produces this output:

   ```escape
   > terraform plan -var-file="env.tfvars" -out="tf.plan"
   azurerm_resource_group.rg["three"]: Refreshing state... [id=/subscriptions/819cbf70-19ca-4614-b32b-9b8cbceeb10e/resourceGroups/aa-my-rg-three]
   azurerm_resource_group.rg["two"]: Refreshing state... [id=/subscriptions/819cbf70-19ca-4614-b32b-9b8cbceeb10e/resourceGroups/aa-my-rg-two]
   azurerm_resource_group.rg["one"]: Refreshing state... [id=/subscriptions/819cbf70-19ca-4614-b32b-9b8cbceeb10e/resourceGroups/aa-my-rg-one]

   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg["bob"] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-bob"
      }

   # azurerm_resource_group.rg["jim"] will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-my-rg-jim"
      }

   Plan: 2 to add, 0 to change, 0 to destroy.
   ```

   - And apply:

   - ![rg-for-each-2](https://automationadmin.com/assets/images/uploads/2022/10/rg-for-each-2.jpg){:class="img-responsive"}

2. OK, so `Option 3` is where you can use a "flag" to optionally deploy a setting as seen in this [`main.tf`](https://github.com/gerryw1389/terraform-modules/blob/main/subnet/main.tf) around line 25 for `server_farm_delegation`.

   - Notice that this makes use of the [`dynamic`](https://www.terraform.io/language/expressions/dynamic-blocks) blocks which will deploy settings optionally.
   - Like the documentation states, these should be [used sparingly](https://www.terraform.io/language/expressions/dynamic-blocks#best-practices-for-dynamic-blocks) as they can be confusing when used too often.

