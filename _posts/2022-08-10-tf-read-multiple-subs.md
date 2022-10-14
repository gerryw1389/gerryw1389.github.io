---
title: 'Terraform: Read Multiple Subscriptions'
date: 2022-08-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tf-read-multiple-subs
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

Use the following code blocks to test reading multiple subscriptions at the same time.

### To Resolve:

1. First, the code, then we can talk about it:

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

   # Subscription 1 will be the default block
   provider "azurerm" {
   client_id                  = var.client_id
   client_secret              = var.client_secret
   subscription_id            = var.subscription_id
   tenant_id                  = var.tenant_id
   skip_provider_registration = true
   features {}
   }

   provider "azurerm" {
   client_id     = trimspace(var.client_id)
   client_secret = trimspace(var.client_secret)
   tenant_id     = trimspace(var.tenant_id)
   features {}
   alias                      = "subscription-2"
   skip_provider_registration = true
   subscription_id            = "xxxx-xxxxx-xxxxx"
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

   data "azurerm_resources" "storageaccount" {
   resource_group_name = "sub1-storage-rg"
   type                = "Microsoft.Storage/storageAccounts"
   required_tags = {
      Purpose = "Mgmt"
   }
   }

   output "data" {
   value = data.azurerm_resources.storageaccount.resources[0].id
   }

   data "azurerm_resources" "storageaccount_sub2" {
   resource_group_name = "sub2-storage-rg"
   type                = "Microsoft.Storage/storageAccounts"
   required_tags = {
      Purpose = "Mgmt"
   }
   provider =  azurerm.subscription-2
   }

   output "data_2" {
   value = data.azurerm_resources.storageaccount_sub2.resources[0].id
   }
   ```

1. Run:

   ```terraform
   cd C:\scripts\tf\local-state
   terraform init
   terraform plan -var-file="env.tfvars" -out="tf.plan"
   ```

1. Output:

   ```terraform
   > terraform plan -var-file="env.tfvars" -out="tf.plan"

   Changes to Outputs:
   + data     = "/subscriptions/***/storage1"
   + data_2   = "/subscriptions/***/storage2"

   You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.
   ```

1. So what is happening?

   - First, there are two `provider` blocks but only 1 has an `alias` attribute. Terraform will use the first provider when it queries `data "azurerm_resources" "storageaccount" ` because that is the default provider.
   - Then, it will use the second provider when it queries `data "azurerm_resources" "storageaccount_sub2"` because we provided `provider =  azurerm.subscription-2` to it.
   - That's it really, the only gotcha with providers is that sometimes you have to pass them as a map object like when you call a `module` but when you call a `data` or `resource` you pass it as an attribute. For example:

   ```terraform
   ## Calling module has two provider blocks like the example above: one with alias `spoke-subscription` and the other other with alias `hub-subscription`
   module "learning-subnet" {
   source                                      = "git::https://some/path/terraform-modules//Subnet?ref=v4.1.0"
   <..> # other attributes removed for brevity
   providers = {
      azurerm.spoke = azurerm.spoke-subscription
      azurerm.hub    = azurerm.hub-subscription
   }
   }
   ```

   - Then in the subnet module, it will have preset `provider` block defined that expect to be passed in:

   ```terraform
   provider "azurerm" {
   alias = "spoke"
   }

   provider "azurerm" {
   alias = "hub"
   }
   ```

   - We may be able to rewrite the subnet module to read data blocks instead, might need to follow up on this. Passing providers seems to be working well enough though.

