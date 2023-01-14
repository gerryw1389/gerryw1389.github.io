---
title: 'Terraform: Setup New Subscription'
date: 2022-10-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/tf-new-subscription
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-Powershell
---
<!--more-->

### Description:

In order for my blog to mirror my organization more, I decided to buy a few more `pay-as-you-go` subscriptions from Azure. After buying the subs, they show up under the `Tenant Root Group` Management group with default names. All I have done in the UI is move them under my `Automation Admin` management group and renamed them. Since my [az-terraform](https://automationadmin.com/2022/05/setup-azdo-terraform/) Service Principle has contributor at the management group level, I should be able to use Terraform to manage all resources in these subscriptions. I wanted to write a post on what you could do with terraform to setup a new subscription. Let's go.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2022-10-20-tf-new-subscription).
{: .notice--success}

### To Resolve:

1. First, a view of what to work with:

   - ![management-groups](https://automationadmin.com/assets/images/uploads/2022/10/mgmt.jpg){:class="img-responsive"}

1. OK, to manage these subscriptions in IaC, the first thing we will need is their subscription IDs. This is because you normally setup providers in Terraform to pass to modules. In Github, I just added these Repository Secrets:

   - HUB_NONPROD
   - HUB_PROD
   - SPOKE_NONPROD
   - SPOKE_PROD

   - I then added these to my [composite action workflow file](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/composite-build.yaml) in the env section to pass to my action. See link for details.
   - Then in [my action](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-10-20-tf-new-subscription/build/action.yaml), I bring them in and pass them to terraform as environmental variables. See link for details.

1. Now all we have to do is focus on Terraform. The first thing to do is add these as new variables in my [variables.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-10-20-tf-new-subscription/variables.tf)

1. Next, we need to create providers with these variables. I have lately been using a [`backend.tf`](https://github.com/gerryw1389/terraform-examples/blob/main/2022-10-20-tf-new-subscription/backend.tf) for all `terraform` and `provider` blocks.

1. I then setup [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-10-20-tf-new-subscription/main.tf) to create a Resource Group in each subscription.

2. The plan looks good, it is going to create 4 Resource Groups, one in each subscription.

   ```escape
   Run cd ./2022-10-20-tf-new-subscription
   /home/runner/work/_temp/8fb7ce4e-ce88-486d-9ddc-29dcf0350e84/terraform-bin plan -var=subscription_id=*** -var=tenant_id=*** -var=client_id=*** -var=client_secret=*** -var=hub_prod_id=*** -var=hub_nonprod_id=*** -var=spoke_prod_id=*** -var=spoke_nonprod_id=***

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.hub_nonprod_rg will be created
   + resource "azurerm_resource_group" "hub_nonprod_rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-dev-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "dev"
            + "Owner"       = "Automation Admin"
         }
      }

   # azurerm_resource_group.hub_prod_rg will be created
   + resource "azurerm_resource_group" "hub_prod_rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-dev-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "dev"
            + "Owner"       = "Automation Admin"
         }
      }

   # azurerm_resource_group.spoke_nonprod_rg will be created
   + resource "azurerm_resource_group" "spoke_nonprod_rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-dev-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "dev"
            + "Owner"       = "Automation Admin"
         }
      }

   # azurerm_resource_group.spoke_prod_rg will be created
   + resource "azurerm_resource_group" "spoke_prod_rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-dev-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "dev"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 4 to add, 0 to change, 0 to destroy.
   ```

1. Now change the composite to the [release folder](https://github.com/gerryw1389/terraform-examples/tree/main/.github/workflows/2022-10-20-tf-new-subscription/release) and run it and we get 4 Resource Groups created!

   ```escape
   Run cd ./2022-10-20-tf-new-subscription
   /home/runner/work/_temp/91afde23-0771-4071-abf6-6a01744f99ca/terraform-bin apply -auto-approve -input=false ./tf.plan
   ╷
   │ Warning: "use_microsoft_graph": [DEPRECATED] This field now defaults to `true` and will be removed in v1.3 of Terraform Core due to the deprecation of ADAL by Microsoft.
   │ 
   │ 
   ╵
   azurerm_resource_group.hub_prod_rg: Creating...
   azurerm_resource_group.spoke_nonprod_rg: Creating...
   azurerm_resource_group.spoke_prod_rg: Creating...
   azurerm_resource_group.hub_nonprod_rg: Creating...
   azurerm_resource_group.hub_prod_rg: Creation complete after 1s [id=/subscriptions/***/resourceGroups/aa-dev-scus-mgmt-rg]
   azurerm_resource_group.spoke_nonprod_rg: Creation complete after 1s [id=/subscriptions/***/resourceGroups/aa-dev-scus-mgmt-rg]
   azurerm_resource_group.spoke_prod_rg: Creation complete after 1s [id=/subscriptions/***/resourceGroups/aa-dev-scus-mgmt-rg]
   azurerm_resource_group.hub_nonprod_rg: Creation complete after 1s [id=/subscriptions/***/resourceGroups/aa-dev-scus-mgmt-rg]

   Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
   ::debug::Terraform exited with code 0.
   ```

   - Initially I had gotten the error:

   ```
   azurerm_management_group.mgmt_hub_nonprod: Creation complete after 30s [id=/providers/Microsoft.Management/managementGroups/58839054-cbf1-49cc-83e4-df3caf6fc58e]
   ╷
   │ Error: [DEBUG] Error assigning Subscription ID "***" to Management Group "6ed437f4-c81d-497d-9f54-51c14a7c0969": managementgroups.SubscriptionsClient#Create: Failure responding to request: StatusCode=400 -- Original Error: autorest/azure: Service returned an error. Status=400 Code="BadRequest" Message="Permission to write and delete on resources of type 'Microsoft.Authorization/roleAssignments' is required on the subscription or its ancestors." Details=[{"raw":"Subscription ID: '/subscriptions/***'"}]
   │ 
   │   with azurerm_management_group.mgmt_hub_prod,
   │   on main.tf line 53, in resource "azurerm_management_group" "mgmt_hub_prod":
   │   53: resource "azurerm_management_group" "mgmt_hub_prod" {
   │
   ```

   - But this was because my `az-terraform` Service Principle only had `Contributor` access and needed `Owner`. Once I gave it owner and re-ran, everything worked as expected.

   - Sure enough when viewing in the UI we see them:

   - ![resource-groups](https://automationadmin.com/assets/images/uploads/2022/10/resource-groups.jpg){:class="img-responsive"}

2. Now that we have proof of concept, we have a few options:

   - One, we can have one giant repo where we pass in all these vars, build providers, and create resources in each subscription like in the example.
   - Two, we can create one repo per subscription and only pass in its var as `subscription_id` and not use all four at once. How often will we be deploying apps to all four subscriptions? Probably never.
   - Three, we can use something like [Terragrunt](https://automationadmin.com/2023/01/terragrunt-repo-structure-v1) to deploy to subscriptions dynamically.

3. Anyways, it is common when you first setup a new sub to build framework like the examples below:

4. To build Management groups you would do something like:

   ```terraform
   # Read in parent
   data "azurerm_management_group" "management" {
   name = "Automation Admin"
   }

   # Create child "Hub"
   resource "azurerm_management_group" "mgmt_hub" {
   display_name               = "Hub"
   parent_management_group_id = data.azurerm_management_group.management.id
   subscription_ids           = [var.hub_prod_id, var.hub_nonprod_id]
   }

   # Create child "Spoke"
   resource "azurerm_management_group" "Spoke" {
   display_name               = "Spoke"
   parent_management_group_id = data.azurerm_management_group.management.id
   subscription_ids           = [var.spoke_prod_id, var.spoke_nonprod_id]
   }
   ```

   - Or maybe you want to split the children between nonprod and prod, so you can take it a step further like seen in [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-10-20-tf-new-subscription/main.tf).

   - These just magically show up correctly in the portal after you run the apply!

   - ![mgmt-groups-2](https://automationadmin.com/assets/images/uploads/2022/10/mgmt-2.jpg){:class="img-responsive"}

5. Next, you just keep creating resources and running applies. Eventually you might get an error about a provider not being registered:

   ```escape
   Error: creating/updating Virtual Network: (Name "xx-xx-xxx-x" / Resource Group "xx-xx-x-x-x-x"): network.VirtualNetworksClient#CreateOrUpdate: Failure sending request: StatusCode=409 -- Original Error: Code="MissingSubscriptionRegistration" Message="The subscription is not registered to use namespace 'Microsoft.Network'. See https://aka.ms/rps-not-found for how to register subscriptions." Details=[{"code":"MissingSubscriptionRegistration","message":"The subscription is not registered to use namespace 'Microsoft.Network'. See https://aka.ms/rps-not-found for how to register subscriptions.","target":"Microsoft.Network"}]
   ```

   - The fix is easy, just go to [this link](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-services-resource-providers) and get a list of resources you want to be able to deploy and register them with a quick powershell script:

   ```powershell

   # Add namespaces from this list => https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-services-resource-providers
   $Providers = @(
         "Microsoft.KeyVault",
         "Microsoft.Storage",
   )

   # Import-Module Az
   # $sub = 'some-guid'
   # $AzureContext = Connect-AzAccount -SubscriptionId $sub -UseDeviceAuthentication

   $Subscriptions = Get-AzSubscription -DefaultProfile $AzureContext

   Foreach ( $Subscription in $Subscriptions)
   {
      Try 
      {
         Set-AzContext -Subscription $($Subscription.Name)
      }
      Catch 
      {
         Write-Error "Failed to select subscription to register resource providers."
         Exit 1
      }

      foreach ($provider in $Providers)
      {
         
         Write-Output "Registering provider: $provider"
         Try
         {
            Register-AzResourceProvider -ProviderNamespace $provider -ErrorAction "Stop"
            Write-Output "Successfully registered provider: $provider"
         }
         Catch
         {
            Write-Output "Failed registering provider: $provider"
            Write-Output "Moving on..."
         }
      }
   }

   ```