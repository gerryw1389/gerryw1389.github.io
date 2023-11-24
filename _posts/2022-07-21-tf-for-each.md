---
title: 'Terraform: For_Each Loop'
date: 2022-07-21T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-for-each
tags:
  - Terraform
---
<!--more-->

### Description:

The [`for_each` loop in terraform](https://www.terraform.io/language/meta-arguments/for_each) accepts a map or a set of strings, and creates an instance for each item in that map or set. It is more dynamic than the [`count`](https://automationadmin.com/2022/07/tf-count) meta argument in that you can add elements to the map or set in any index without effecting the other elements. More details can be seen [here](https://www.terraform.io/language/meta-arguments/count#when-to-use-for_each-instead-of-count) on TF docs.

### To Resolve:

1. In the first example, we will iterate through a list of maps:

   ```terraform
   terraform {
   required_providers {

      azurerm = {
         source  = "hashicorp/azurerm"
         version = "~>3.10.0"
      }

   }
   required_version = "~>1.1.0"
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

   containers_list = [
      { name = "blob-1", access_type = "private" },
      { name = "blob-2", access_type = "blob" },
      { name = "blob-3", access_type = "container" }
   ]

   file_shares = [
      { name = "data1", quota = 50 },
      { name = "data2", quota = 50 }
   ]

   sa_name = "mystorageaccount"
   }

   resource "azurerm_storage_container" "storage_container" {
   for_each              = { for container in local.containers_list : container.name => container }
   storage_account_name  = local.sa_name
   name                  = each.value.name
   container_access_type = each.value.access_type
   }

   resource "azurerm_storage_share" "storage_share" {
   for_each             = { for shares in local.file_shares : shares.name => shares }
   storage_account_name = local.sa_name
   name                 = each.value.name
   quota                = each.value.quota
   }

   output "storage_container_names" {
   value = [
      for k, v in azurerm_storage_container.storage_container : v.name
   ]
   }

   output "storage_share_names" {
   value = [
      for k, v in azurerm_storage_share.storage_share : v.name
   ]
   }

   ```


   - This gives us:

   ```escape
   Changes to Outputs:
   + storage_container_names = [
         + "blob-1",
         + "blob-2",
         + "blob-3",
      ]
   + storage_share_names     = [
         + "data1",
         + "data2",
      ]
   ```

   - How does it work? Well `for_each = { for container in local.containers_list : container.name => container }` will first loop through `local.containers_list` and see the first element in the list is `{ name = "blob-1", access_type = "private" }`.
   - This is a map object so `container.name` and `container.access_type` are the two properties we can work with. 
   - The `container.name => container` part is a little confusing. What you have to look at is the full expression and notice how it starts with `{` and ends with `}`.
   - This tells us the final result will be a `map` object. 
   - So reading `container.name => container` what it is saying is that will take the object `{ name = "blob-1", access_type = "private" }` and create a key value pair that looks like:

   ```escape
   blob-1 = { 
      name = "blob-1", 
      container_access_type = "private"
   }
   ```

   - So it is giving whater you put in the `name` property the `key` value in the object it creates and at the same time it is copying whatever in `access_type` over to the `container_access_type` parameter needed for the [container](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_container#container_access_type) resource.

   - We can see this if we change

   ```escape
   output "storage_container_names" {
      value = [
         for k, v in azurerm_storage_container.storage_container : v.name
      ]
   }

   # to instead

   output "storage_containers" {
      value = azurerm_storage_container.storage_container
   }
   ```

   - which gives us:

   ```escape
   Changes to Outputs:
   + storage_containers  = {
         + blob-1 = {
            + container_access_type   = "private"
            + has_immutability_policy = (known after apply)
            + has_legal_hold          = (known after apply)
            + id                      = (known after apply)
            + metadata                = (known after apply)
            + name                    = "blob-1"
            + resource_manager_id     = (known after apply)
            + storage_account_name    = "mystorageaccount"
            + timeouts                = null
         }
         + blob-2 = {
            + container_access_type   = "blob"
            + has_immutability_policy = (known after apply)
            + has_legal_hold          = (known after apply)
            + id                      = (known after apply)
            + metadata                = (known after apply)
            + name                    = "blob-2"
            + resource_manager_id     = (known after apply)
            + storage_account_name    = "mystorageaccount"
            + timeouts                = null
         }
         + blob-3 = {
            + container_access_type   = "container"
            + has_immutability_policy = (known after apply)
            + has_legal_hold          = (known after apply)
            + id                      = (known after apply)
            + metadata                = (known after apply)
            + name                    = "blob-3"
            + resource_manager_id     = (known after apply)
            + storage_account_name    = "mystorageaccount"
            + timeouts                = null
         }
      }
   + storage_share_names = [
         + "data1",
         + "data2",
      ]
   ```

   - From there, we can access `each.value.name` and we know it will be `blob-1`, `blob-2`, and `blob-3` so we can assign these to `name` parameter for the `azurerm_storage_container` resource. Likewise, we can assign `each.value.access_type` in the same order so that `blob-1` will get `private`, `blob-2` will get `blob` and `blob-3` will get `container`. We can verify these by checking [the docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_container#container_access_type) to confirm they are acceptable values.

   - Although this looks complex, it will be my preferred way to pass values when iterating through loops since you could access as many `each.value.property` keys as you please which makes this great for passing many arguments to each specific instance.

   - Unlike `count`, each of the values will always be mapped to a specific resource. We can see this on the plan that it doesn't access them by index but instead by name which makes this far superior to count:

   ```escape
   > terraform plan -var-file="env.tfvars" -out="tf.plan" | Select-String -pattern "created","destroyed","Plan:"

   # azurerm_storage_container.storage_container["blob-1"] will be created
   # azurerm_storage_container.storage_container["blob-2"] will be created
   # azurerm_storage_container.storage_container["blob-3"] will be created
   # azurerm_storage_share.storage_share["data1"] will be created
   # azurerm_storage_share.storage_share["data2"] will be created
   ```


1. In another example, we have a list of strigs and will iterate through those. We first cast the list of strings to a set so that it will [remove any duplicates and sort them alphabetically](https://www.terraform.io/language/functions/toset) and then use for_each to loop through them.


   ```terraform
   terraform {
   required_providers {

      azurerm = {
         source  = "hashicorp/azurerm"
         version = "~>3.10.0"
      }

      random = {
         source  = "hashicorp/random"
         version = "~>3.3.2"
      }

   }
   required_version = "~>1.1.0"
   }

   provider "azurerm" {
   client_id                  = var.client_id
   client_secret              = var.client_secret
   subscription_id            = var.subscription_id
   tenant_id                  = var.tenant_id
   skip_provider_registration = true
   features {}
   }

   provider "random" {
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

   variable "sa_name" {
   description = "(Optional) A name for a storage account."
   type        = string
   default     = "aastorageaccount"
   }

   locals {

   storage_name = substr(replace(lower(var.sa_name), "/[^[:alnum:]]/", ""), 0, 24)
   storage_types = toset([
      "blobServices", "fileServices", "queuesServices", "tableServices"
   ])

   tst_tags = {
      Owner       = "Automation Admin"
      CostCenter  = "100"
      EntAppname  = "Automation Admin Terraform POC"
      Environment = "tst"
      Contact     = "gerry@automationadmin.com"
   }
   }

   resource "azurerm_resource_group" "rg" {
   name     = "aa-dev-tx-test-storage"
   location = "westus"
   tags     = local.tst_tags
   }

   resource "azurerm_storage_account" "storage" {
   name                     = local.storage_name
   resource_group_name      = azurerm_resource_group.rg.name
   location                 = "westus"
   account_tier             = "Standard"
   account_replication_type = "LRS"
   }

   resource "azurerm_monitor_diagnostic_setting" "diag_settings" {
   for_each           = local.storage_types
   name               = "diag-${each.key}"
   target_resource_id = "${azurerm_storage_account.storage.id}/${each.key}/default/"
   storage_account_id = azurerm_storage_account.storage.id

   log {
      category = "StorageRead"
      enabled  = true
      retention_policy {

         days    = 5
         enabled = false
      }
   }

   log {
      category = "StorageWrite"
      enabled  = true
      retention_policy {

         days    = 5
         enabled = false
      }
   }

   log {
      category = "StorageDelete"
      enabled  = true
      retention_policy {

         days    = 5
         enabled = false
      }
   }


   metric {
      category = "Transaction"
      enabled  = true
      retention_policy {
         days    = 0
         enabled = false
      }
   }
   }

   output "diag_settings" {
   value = [
      for k, v in azurerm_monitor_diagnostic_setting.diag_settings : v.name
   ]
   }

   ```

   - This gives us one resource group with one storage account and diagnostic settings for each of the services on the storage account:

   ```escape
   Changes to Outputs:
   + diag_settings = [
         + "diag-blobServices",
         + "diag-fileServices",
         + "diag-queuesServices",
         + "diag-tableServices",
      ]

   ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

   Saved the plan to: tf.plan

   To perform exactly these actions, run the following command to apply:
      terraform apply "tf.plan"
   me@server:C:\scripts
   > terraform plan -var-file="env.tfvars" -out="tf.plan" | Select-String -pattern "created","destroyed","Plan:"

   # azurerm_monitor_diagnostic_setting.diag_settings["blobServices"] will be created
   # azurerm_monitor_diagnostic_setting.diag_settings["fileServices"] will be created
   # azurerm_monitor_diagnostic_setting.diag_settings["queuesServices"] will be created
   # azurerm_monitor_diagnostic_setting.diag_settings["tableServices"] will be created
   # azurerm_resource_group.rg will be created
   # azurerm_storage_account.storage will be created
   Plan: 6 to add, 0 to change, 0 to destroy.
   ```

   - What's happening here? Well iterating through a list of strings is much less detailed than maps because both [`each.key` and `each.value` will be the same when iterating through a list](https://www.terraform.io/language/meta-arguments/for_each#the-each-object).

1. More examples can be found on my [testing locally](https://automationadmin.com/2022/07/tf-testing-locally) post.