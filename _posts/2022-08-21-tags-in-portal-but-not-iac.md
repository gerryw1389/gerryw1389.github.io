---
title: Tags In Portal But Not IaC
date: 2022-08-21T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tags-in-portal-but-not-iac
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

So one of the first things that came up when I was using Terraform was I would run a plan for a specific change and I noticed that Terraform was removing a tag that someone had placed on a resource in the portal. This post is how I would fix it in Terraoform to where it wouldn't remove the tag.

### To Resolve:

1. So let's say you have a `./modules/nic` folder in your repo that is used to modularize the [`azurerm_network_interface`](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface) resource in its `./modules/nic/main.tf` and you calling like so:

   ```terraform
   module "vm_nic" {
      name                = "example-nic"
      location            = azurerm_resource_group.example.location
      resource_group_name = azurerm_resource_group.example.name

      ip_configuration {
         name                          = "internal"
         subnet_id                     = azurerm_subnet.example.id
         private_ip_address_allocation = "Dynamic"
      }
   }
   ```

1. The first thing you need to do is find out if the resource supports a `tags` parameter. It [does](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface#tags).

   - Next, add a `./modules/nic/variables.tf` which you probably have already since it is a module, but just make sure it exists and then add the following variable to it:

   ```
   variable "tags" {
      description = "(Required) Tags associated with the NIC created"
   }
   ```

   - Then inside of its `main.tf` add the tags attribute so it can be passed in (`tags = var.tags`).

1. Finally, go back to where you call the module and add in the new parameter by modifying the module call:

   ```terraform
   module "vm_nic" {
      name                = "example-nic"
      location            = azurerm_resource_group.example.location
      resource_group_name = azurerm_resource_group.example.name

      ip_configuration {
         name                          = "internal"
         subnet_id                     = azurerm_subnet.example.id
         private_ip_address_allocation = "Dynamic"
      }
      
      tags = { Source = "Terraform" }
   }
   ```

1. Now re-run your pipeline and it shouldn't say anything about removing a tag because you set it yourself in IaC.

   - NOTE: You can repeat this process in many ways, not just tags. For example, any time `terraform plan` says it will be removing something, you can modify your code to add it instead to keep Iac in sync with your currently deployed resources, it just takes investigation.
   {: .notice--success}