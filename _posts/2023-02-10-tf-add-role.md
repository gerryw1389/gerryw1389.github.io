---
title: 'Terraform: Add Azure IAM Role'
date: 2023-02-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/02/tf-add-role
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

In this post, I will show how I create a custom Azure AD Role and assign it to a System Identity using Terraform. I actually didn't use terraform to create the role like I should have but used powershell. I see now that I could have used [role_definition](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/role_definition) but here is what I did for a role that can start/stop VMs, AKS clusters, and App Gateways: 

### To Resolve:

1. First I manually connected to Azure using powershell and created a custom role using a flow I use often:

   ```powershell
   $SubIDList = [System.Collections.Generic.List[PSObject]]@()
   $Subs = Get-AzSubscription
   Foreach ( $Sub in $Subs)
   {
      $subId = $($Sub.Id)
      $subStr = "/subscriptions/" + $subId
      [void]$SubIDList.Add($subStr)
   }

   # Create custom role
   $role = Get-AzRoleDefinition "Reader"
   $role.Id = $null
   $role.Name = 'Custom_Start_Stop'
   $role.Description = 'Has access to start and stop various resources.'
   $role.Actions.Add('Microsoft.Compute/virtualMachines/start/action')
   $role.Actions.Add('Microsoft.Compute/virtualMachines/deallocate/action')
   $role.Actions.Add('Microsoft.Network/applicationGateways/start/action')
   $role.Actions.Add('Microsoft.Network/applicationGateways/stop/action')
   $role.Actions.Add('Microsoft.ContainerService/managedClusters/stop/action')
   $role.Actions.Add('Microsoft.ContainerService/managedClusters/start/action')
   $role.AssignableScopes.Clear()
   Foreach ( $Sub in $SubIDList)
   {
      $role.AssignableScopes.Add($Sub)
   }
   New-AzRoleDefinition -Role $role

   # Output:
   # >  New-AzRoleDefinition -Role $role
   # Name             : Custom_Start_Stop
   # Id               : some-id
   # IsCustom         : True
   # Description      : Has access to start and stop various resources.
   # Actions          : {*/read, Microsoft.Compute/virtualMachines/start/action, Microsoft.Compute/virtualMachines/deallocate/action, Microsoft.Network/applicationGateways/start/action...}
   # NotActions       : {}
   # DataActions      : {}
   # NotDataActions   : {}
   # AssignableScopes : {/subscriptions/some-id, /subscriptions/some-id-2, ...}

   ```

   - Note that the AssignableScopes needs the format (`/subscriptions/` + `subscription id`) so I first created a list object and looped through all subscriptions to populate it.
   - Next I created the role based on built-in Reader as this is what I usually start with when creating a custom role
   - Then I add the actions I think will be needed.
   - Then I clear all Assignable Scopes and only add the ones I know the role can be used for. In many cases this list will be much smaller but this is just an example.

1. Now that the role exists, I can just add the role using Terraform just like usual using the [`azurerm_role_assignment`](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/role_assignment) resource:

   - You can see an example [here](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-20-tf-create-aa-with-source-control/main.tf) where the role scope is at the subscription level by readg it in first:

   ```terraform
   data "azurerm_subscription" "primary" {
   }

   resource "azurerm_role_assignment" "example" {
   scope                = data.azurerm_subscription.primary.id
   role_definition_name = "Reader"
   principal_id         = azurerm_automation_account.aa.identity[0].principal_id
   }
   ```

   - And then the principle_id is the identity of the Automation Account. This is a common pattern that you will use when using terraform.
