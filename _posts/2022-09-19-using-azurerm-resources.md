---
title: 'Terraform: Using azurerm_resources'
date: 2022-09-19T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/09/using-azurerm-resources
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

So one of the things you can setup in your modules is data sources that read your current infrastructure. You can have generic [data](https://www.terraform.io/language/data-sources) blocks but you can also have this [`azurerm_resources`](https://registry.terraform.io/providers/hashicorp/azurerm/3.0.0/docs/data-sources/resources) block that gets a list object of specific types of resources, resources with specific tags, or all resources in a specific Resource Group.

This works well when you have logic like "I need all Storge Accounts with this tag to be the ones we send our Network Watcher Flow Logs to" or other scenarios like that.

### To Resolve:

1. The example they use (in the `azurerm_resources` link above) is that of network spokes peering to a Hub network:

   ```terraform
   # Get resources by type, create spoke vNet peerings
   data "azurerm_resources" "spokes" {
   type = "Microsoft.Network/virtualNetworks"

   required_tags = {
      environment = "production"
      role        = "spokeNetwork"
   }
   }

   resource "azurerm_virtual_network_peering" "spoke_peers" {
   count = length(data.azurerm_resources.spokes.resources)

   name                      = "hub2${data.azurerm_resources.spokes.resources[count.index].name}"
   resource_group_name       = azurerm_resource_group.hub.name
   virtual_network_name      = azurerm_virtual_network.hub.name
   remote_virtual_network_id = data.azurerm_resources.spokes.resources[count.index].id
   }
   ```

   - It doesn't show it, but there needs to be a `azurerm_virtual_network` resource that is the hub network that these spoke networks will peer to.

1. In order to use this resource effectively, you should:
   - Always use a `count = length(data.azurerm_resources.spokes.resources)` type block where you will apply your logic on all the resources that you find no matter if it finds 0, 1, or 20 objects.
   - Next, find the attribute you are looking for, usually an `id` and put the current count as the index like in the example => `remote_virtual_network_id = data.azurerm_resources.spokes.resources[count.index].id`

1. For example, if I'm reading in all Storage Accounts with the tag 'Purpose = NetworkWatcherLogs', then it will look like this:

   ```terraform
   provider "azurerm" {
      alias = "spoke"
   }

   data "azurerm_resources" "storageaccount" {
      resource_group_name = "some-storage-rg"
      type                = "Microsoft.Storage/storageAccounts"
      required_tags = {
         Purpose = "NetworkWatcherLogs"
      }
      provider = azurerm.spoke
   }
   ```

   - See [this post](https://automationadmin.com/2022/08/tf-read-multiple-subs) about using providers for multiple subscriptions.


   - Then under the network watcher flow logs, I will do as mentioned:

   ```terraform
   resource "azurerm_network_watcher_flow_log" "networkWatcherFlowLog" {
      storage_account_id        = data.azurerm_resources.storageaccount.resources[count.index].id
      # <...> Removed other arguments for brevity
   }
   ```
