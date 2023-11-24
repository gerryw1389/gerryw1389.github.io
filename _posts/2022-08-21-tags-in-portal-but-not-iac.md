---
title: Tags In Portal But Not IaC
date: 2022-08-21T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tags-in-portal-but-not-iac
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

So one of the first things that came up when I was using Terraform was I would run a plan for a specific change and I noticed that Terraform was removing a tag that someone had placed on a resource in the portal. This post is how I would fix it in Terraoform to where it wouldn't remove the tag.

### To Resolve:

1. So let's say you have a `./modules/nic` folder in your repo and in another part of your repo, you are calling it like so:

   ```terraform
   module "vm_nic" {
      source                                = "./modules/nic"
      name                                  = "example-nic"
      location                              = azurerm_resource_group.example.location
      resource_group_name                   = azurerm_resource_group.example.name
      ip_conf_name                          = "internal"
      ip_conf_subnet_id                     = azurerm_subnet.example.id
      ip_conf_private_ip_address_allocation = "Dynamic"
   }
   ```

1. The first thing you need to do is go to the file `./modules/nic/main.tf` (or wherever the `azurerm_network_interface` resource is being set in the module, usually main.tf) and add a `tags` parameter. 

   - NOTE: Remember that a parameter is a function definition and an argument is the value passed to it. [MSDN references](https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/language-features/procedures/differences-between-parameters-and-arguments) like a parameter is a 'P'arking space and an argument is an 'A'utomobile. Many different automobiles can fit into a single parking space, i.e. different arguments can be passed to a single defined parameter.
   {: .notice--success}


   - So it may look like this before:

   ```terraform
   resource "azurerm_network_interface" "example" {
      name                = var.name
      location            = var.location
      resource_group_name = var.resource_group_name

      ip_configuration {
         name                          = var.ip_conf_name
         subnet_id                     = var.ip_conf_subnet_id
         private_ip_address_allocation = var.ip_conf_private_ip_address_allocation
      }
   }
   ```

   - And this after

   ```terraform
   resource "azurerm_network_interface" "example" {
      name                = var.name
      location            = var.location
      resource_group_name = var.resource_group_name

      ip_configuration {
         name                          = var.ip_conf_name
         subnet_id                     = var.ip_conf_subnet_id
         private_ip_address_allocation = var.ip_conf_private_ip_address_allocation
      }
      tags = var.tags
   }
   ```

   - Next, add a `./modules/nic/variables.tf` which you probably have already since it is a module, but just make sure it exists and then add the following variable to it:

   ```
   variable "tags" {
      description = "(Required) Tags associated with the NIC created"
   }
   ```

2. Finally, go back to where you call the module and add in the new argument by modifying the module call:

   ```terraform
   module "vm_nic" {
      source                                = "./modules/nic"
      name                                  = "example-nic"
      location                              = azurerm_resource_group.example.location
      resource_group_name                   = azurerm_resource_group.example.name
      ip_conf_name                          = "internal"
      ip_conf_subnet_id                     = azurerm_subnet.example.id
      ip_conf_private_ip_address_allocation = "Dynamic"
      tags                                  = { Source = "Terraform" }
   }
   ```

3. Now re-run your pipeline and it shouldn't say anything about removing a tag because you set it yourself in IaC.

   - NOTE: You can repeat this process in many ways, not just tags. For example, any time `terraform plan` says it will be removing something, you can modify your code to add it instead to keep Iac in sync with your currently deployed resources, it just takes investigation.
   {: .notice--success}