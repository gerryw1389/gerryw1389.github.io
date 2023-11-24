---
title: 'Terraform: Split To Get Values'
date: 2022-10-12T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/tf-split-to-get-values
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

As with many languages, you can perform a [split](https://developer.hashicorp.com/terraform/language/functions/split) function on a string in Terraform. Here is an example of how I can target to get specific values.

### To Resolve:

1. For example, let's say I want to get some value from a Storage Account ID, I could do something like the following:

```
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

resource "azurerm_resource_group" "rg" {
  name     = "tx-storage-rg"
  location = "southcentralus"
}

resource "azurerm_storage_account" "example" {
  name                = "aatxstorage145"
  resource_group_name = azurerm_resource_group.rg.name

  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

}

output "data1" {
   value = azurerm_storage_account.example.id
}

output "data2" {
   value = split("/", azurerm_storage_account.example.id)[2]
}

output "data3" {
   value = split("/", azurerm_storage_account.example.id)
}
```

1. When I run an apply, I get the following:

```
> terraform apply -auto-approve -input=false ./tf.plan
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
Outputs:
data1 = "/subscriptions/xxx-xxxx-xxx/resourceGroups/tx-storage-rg/providers/Microsoft.Storage/storageAccounts/aatxstorage145"
data2 = "xxx-xxxx-xxx"
Changes to Outputs:
+ data3 = [
      + "",
      + "subscriptions",
      + "xxx-xxxx-xxx",
      + "resourceGroups",
      + "tx-storage-rg",
      + "providers",
      + "Microsoft.Storage",
      + "storageAccounts",
      + "aatxstorage145",
    ]
```

1. Now that we know the values for each index, we can simply pass them around as needed:

   - Using `split("/", azurerm_storage_account.example.id)[2]` will get us the subscription ID the Storage Account is in.
   - Using `split("/", azurerm_storage_account.example.id)[4]` will get us the Resource Group the Storage Account is in.
   - Using `split("/", azurerm_storage_account.example.id)[8]` will get us the Storage Account Name.

1. Commonly, you will use these in locals for a simple value that can be passed to other places as needed:

```
locals {
   sa_sub_id = split("/", azurerm_storage_account.example.id)[2]
   sa_rg = split("/", azurerm_storage_account.example.id)[4]
   sa_name = split("/", azurerm_storage_account.example.id)[8]
}
```

1. Note that it is better and preferred to get the output of a resource instead of relying on parsing the `id`. This was just an example of how you can take a string, split it, and store its values in other variables to be referenced in other places.

   - For example, [sa_rg should be `azurerm_storage_account.resource_group_name`](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/storage_account#argument-reference)
   - And [sa_name should be `azurerm_storage_account.name`](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/storage_account#argument-reference)
   - But where would you get the subscription ID the storage account is deployed to? One option, as listed above, is to parse the `id` property and extract it.
