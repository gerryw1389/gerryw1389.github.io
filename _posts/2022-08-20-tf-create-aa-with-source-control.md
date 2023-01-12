---
title: 'Terraform: Create Automation Account With Source Controlled Runbooks'
date: 2022-08-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tf-create-aa-with-source-control
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
  - Azure-Automation
---
<!--more-->

### Description:

You can provision an Azure Automation Account and source control the runbooks in the same code. 

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2022-08-20-tf-create-aa-with-source-control).
{: .notice--success}

### To Resolve:

1. First, I ran a plan and it said it would create 9 resources.

1. Then I ran the apply and it failed because I haven't registered the provider yet:

   ```
   Error: creating Automation Account: (Name "aa-sbx-scus-aa" / Resource Group "aa-sbx-scus-aa-rg"): automation.AccountClient#CreateOrUpdate: Failure responding to request: StatusCode=409 -- Original Error: autorest/azure: Service returned an error. Status=409 Code="MissingSubscriptionRegistration" Message="The subscription is not registered to use namespace 'Microsoft.Automation'. See https://aka.ms/rps-not-found for how to register subscriptions." Details=[{"code":"MissingSubscriptionRegistration","message":"The subscription is not registered to use namespace 'Microsoft.Automation'. See https://aka.ms/rps-not-found for how to register subscriptions.","target":"Microsoft.Automation"}]
   ```

   - You can use a powershell script, az cli, or the GUI to register providers. I just went to the Subscription in the UI and registered by going to the `Resource Providers` blade and searching 'automation'. I also did 'network' because I will probably create a VNET in the future, more to come later.

1. Anyways, re-ran the apply and this time it was gave a different error about the automation schedule:

```escape
╷
│ Error: start_time is "2022-08-01 16:05:16 -0700 -0700" and should be at least "5m0s" in the future
│ 
│   with azurerm_automation_schedule.monday_tuesday,
│   on aa-schedules.tf line 2, in resource "azurerm_automation_schedule" "monday_tuesday":
│    2: resource "azurerm_automation_schedule" "monday_tuesday" {
│ 
╵
╷
│ Error: start_time is "2022-08-01 16:05:16 -0700 -0700" and should be at least "5m0s" in the future
│ 
│   with azurerm_automation_schedule.wednes_thurs,
│   on aa-schedules.tf line 14, in resource "azurerm_automation_schedule" "wednes_thurs":
│   14: resource "azurerm_automation_schedule" "wednes_thurs" {
│ 
╵
```

1. So I corrected the timezones and schedule and it was successful. Here is what it did:

   - Created rg: `aa-sbx-scus-aa-rg`
   - Created automation account: `aa-sbx-scus-aa`
   - Created two runbooks: `Show-VMs (aa-sbx-scus-aa/Show-VMs)` and `Show-VMs-2 (aa-sbx-scus-aa/Show-VMs-2)`
   - The Automation Account got a System Identity Assigned
   - The Automation Account System Identity is linked to the `Reader` role at the subscription level allowing the runbook permissions.

1. Output from Show-VMs:

   ```escape
   Mode             : Process
   ContextDirectory : 
   ContextFile      : 
   CacheDirectory   : 
   CacheFile        : 
   Settings         : {}

   Successfully authenticated and logged in using Automation Accounts System Identity

   Subscription has no VM objects

   Current Virtual Machines: 

   Example reading vars....

   Variable value: Hello, Terraform Basic Test.

   ```

1. As expected, output from Show-VMs-2:

   ```escape
   Mode             : Process
   ContextDirectory : 
   ContextFile      : 
   CacheDirectory   : 
   CacheFile        : 
   Settings         : {}

   Successfully authenticated and logged in using Automation Accounts System Identity

   Subscription has no VM objects

   Current Virtual Machines: 

   Example reading vars....

   Variable value: Hello, Terraform Basic Test.

   This is example 2

   ```

1. I then ran my [destroy workflow](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-08-20-tf-create-aa-with-source-control/destroy.yaml) to save on costs.