---
title: 'Terraform: Data Sources Module'
date: 2022-11-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/11/data-sources-module
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

So if your organization uses a [hub and spoke](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/software-defined-network/hub-spoke) like structure [like mine](https://automationadmin.com/2022/10/tf-new-subscription), you most likely will have certain resources that you point all your subscriptions to. For example, you could say something like 'all resources must send their logs to one of our Log Analytics workspaces based on environment and region'. Here is a way you could develop a module that will automatically resolve the correct Log Analytics Workspace to send logs to that you can copy and paste freely between your different [module compositions](https://automationadmin.com/2022/08/calling-remote-modules).

Note that is one of the [official ways](https://developer.hashicorp.com/terraform/language/modules/develop/composition#data-only-modules) to use Terraform.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-modules/tree/main/data-sources).
{: .notice--success}

### To Resolve:

1. First create a module called 'data_sources' or something like that. Mine is here => [data-sources](https://github.com/gerryw1389/terraform-modules/tree/main/data-sources)

1. Inside the module, accept providers for each of your hub network environments:

   ```terraform
   terraform {
   required_providers {
      azurerm = {
         source  = "hashicorp/azurerm"
         configuration_aliases = [azurerm.nonprod-hub, azurerm.prod-hub, ]
         version = ">= 3.20.0"
      }
   }
   }
   ```

   - NOTE: I used to build providers inside the module but I kept getting errors in my terraform plan saying this was [depreciated](https://developer.hashicorp.com/terraform/language/modules/develop/providers#legacy-shared-modules-with-provider-configurations) and that you should pass them in instead. Makes sense, modules should have very little except vars and code.

1. Next, just start doing data lookups like [here](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/data_event_hub.tf), [here](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/data_law.tf), and [here](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/data_priv_dns.tf) where you query resources from your hub network based on environment.

   - Couple things to note here:
   - We are querying both Nonprod and Prod environments as well as South Central and East regions and getting their resources at the same time.
   - We are accessing whatever properties are available of those resources like `name`, `id`, etc. and exporting them as outputs.

3. Ok, so now we have `module.dataLookup.law_pe_rg` and `module.dataLookup.law_pe_name`, how does that help? Well the real power of this you can use a [lookup](https://developer.hashicorp.com/terraform/language/functions/lookup) function in your module composition like [so](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/examples/common.tf) :

   - Let's break this [`common.tf`](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/examples/common.tf) down:

   - First, we call our module so we get all of its outputs in `module.dataLookup.$some_output`
   - Next, we pass in **our** `${var.env_stage_abbr}` and `${var.region_abbr}` and store them as a string with an underscore separator in `local.lookup` (line 65)
   - Next, we create a map object for each combination of environments and regions. NOTE I only did by environment in this example but you can extend this logic to make some pretty sweet lookups.
   - For example, you could do `environment_region_filter` or something if you want to have lookups based on different environments, Azure regions, or some other filter like `logical stage` or something.
   - Either way, you then create a lookup table that maps all possible values to all possible combinations.
   - Man this is a lot of work, why do it?

4. You may wonder why do all this work to begin with just to get a stupid `id` for a Log Analytics workspace. Well the power of this is that you only have to do this once and you can store it as a `common.tf` or something and copy it between all your module compositions. The real power of this comes from deploying between different regions and environments, since the data lookup will match based on that, you will never have to change your code!!

   - For example, every time I need to pass a `log_analytics_workspace_id`, I can just pass `local.law_id` blindly and know it will perform the lookup for me!

1. NOTE: I have recently started playing with [Terragrunt](https://automationadmin.com/2023/01/terragrunt-repo-structure-v1) and it seems like it does the same thing but without a module call/lookup. I will update on it shortly.