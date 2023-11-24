---
title: 'Terraform: Passing Providers Trap'
date: 2022-12-05T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/12/passing-providers-trap
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

So one of the things I did the other day was upgrade many of my modules to not use [providers](https://developer.hashicorp.com/terraform/language/providers) by deleting any references to providers within the module and then removing it from my backend.tf:

- Before

```terraform
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      configuration_aliases = [azurerm.hub-nonprod, azurerm.hub-prod, ]
      version = ">= 3.20.0"
    }
  }
}
```

- After

```terraform
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.20.0"
    }
  }
}
```

So the most common reason to pass providers to a module is if you want to do data lookups within the module but you need the lookup to happen in some other subscription. For example, in a [hub and spoke network like mine](https://automationadmin.com/2022/10/tf-new-subscription), you might have Log Analytics Workspaces that all spokes send to their Hubs:

- Spoke1-NonProd => Send logs for all resources to a Log Analytics Workspace in Hub-NonProd subscription
- Spoke2-NonProd => Send logs for all resources to a Log Analytics Workspace in Hub-NonProd subscription
- Spoke1-Prod => Send logs for all resources to a Log Analytics Workspace in Hub-Prod subscription
- Spoke2-Prod => Send logs for all resources to a Log Analytics Workspace in Hub-Prod subscription

- For an example, look at my [data-sources](https://github.com/gerryw1389/terraform-modules/tree/main/data-sources) module on Github.

In this case, if you have a Storage Account module, you will need Composition pipelines to call your module but you don't know where to send your logs? What if they are calling from a Nonprod deployment? A prod deployment? You can fix this by having them pass in the provider and you can then look up the log analytics workspace for them and send the logs from your Storage Account to their workspace.

But there is another option, remove data lookups altogether and just accept any input as a var. But this is more error prone right? Well yes, but if you have [frameworks in place](https://automationadmin.com/2022/11/data-sources-module) that set these values for you, then it's no big deal.

Anyways, I ended up having to revert this because what happens is, if you try to upgrade a module that used to use providers and remove them, you are immediately hit with the `terraform re-add the provider configuration to destroy` error. If you google this, it seems to be a known problem with terraform and how it stores resources that were created with providers. It appears that if a resource was created with a provider, it is stuck with it for life.

So now you have two options, either revert your change and add providers back, or just call your new module only for new resources since new resources won't get the new providers to begin with. That is why I call this a `trap` is because you have no choice but to keep your providers for existing resources but you have the option of not using them anywhere in your module until the day you remove the providers. Maybe just have two repos of the same terraform module one with providers and one without and gradually transition to the one without? Not sure.

### To Resolve:

1. What I ended up doing was the best of both worlds for now, I added back the providers in the module's `backend.tf` but then didn't use them anywhere in the module and at the same time added resource lookups as variables to be passed in.
