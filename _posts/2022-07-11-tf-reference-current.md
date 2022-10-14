---
title: 'Terraform: Reference Current Infra'
date: 2022-07-11T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-reference-current
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

Many times we will need to reference current resources and then pass other information to build on them. For example, adding a Virtual Machine to an already existing Resource Group. I'm not sure how to `modify` these resources just yet, that will have to be a different post.

### To Resolve:

1. To get the resource ID of the [current subscription](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subscription):

   ```terraform
   data "azurerm_subscription" "current" {}

   output "sub_name" {
      value = data.azurerm_subscription.current.id
   }

   output "tenant_name" {
      value = data.azurerm_subscription.current.tenant_id
   }
   ```

   - Output:

   ```escape
   sub_name    = "/subscriptions/subscription-id-guid"
   tenant_name = "tenant-id-guid"
   ```

1. You can do this for any existing resource. For example:

   ```terraform
   data "azurerm_virtual_network" "vnet" {
      name                = var.vnet_name
      resource_group_name = var.rg
   }

   data "azurerm_subnet" "my_subnet" {
      resource_group_name  = var.rg
      virtual_network_name = data.azurerm_virtual_network.vnet.name
      name                 = var.subnet_name
   }
   ```

   - You can reference them by syntax: `data.$ARM_Resource_Name.$Alias.output` where `ARM_Resource_Name` matches the resource in [Azure Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) and `$alias` is whatever [label](https://www.terraform.io/language/resources/syntax) you give the resource.

1. You can check outputs by going to their AzureRM (ARM) documents at [AzureRM Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

   - For example, I see [Virtual Network](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network) has many attributes exported such as `id`, `name`, `resource_group_name`, and more.

   - This means that later in my code I can reference like: `data.azurerm_virtual_network.vnet.resource_group_name` for example or `data.azurerm_virtual_network.vnet.name`
