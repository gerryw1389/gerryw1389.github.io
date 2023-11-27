---
title: Create PayAsYouGo Azure Subs Using Terrform
date: 2023-11-23T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/11/create-tf-subscriptions-payg
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description

One of the first things I wanted to show after [creating an organization](https://automationadmin.com/2023/08/setting-up-github-org) in Github is how to configure Azure completely via IaC, with little to no clicking in the GUI. Well the first step to do that is to create subscriptions. I was certain that you could not do that with "Pay as You Go" types, but sure enough, it's [one of the options](https://registry.terraform.io/providers/hashicorp/azurerm/3.80.0/docs/resources/subscription#example-usage---creating-a-new-alias-and-subscription-for-a-microsoft-customer-account)!

### Steps

1. The first thing I did was give my Service Principal rights to create subscriptions at the correct "Invoice Section" level:

   - ![subscription-creator](https://automationadmin.com/assets/images/uploads/2023/11/subscription-creator.png){:class="img-responsive"}

   - It can be confusing the hierarchy, but thankfully the [docs](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#microsoft-customer-agreement) cover this well. It's just Billing Account => Profile => Invoice Section.

1. So before using Terraform to create new subscriptions, you have to get the `id` property of your Billing Account, Billing Profile, and Invoice Section. This tripped me up so bad because the Terraform docs say `billing_name` as in the `name` property so I don't have to expose the `id` for the world to see, but **NOPE**, that won't work! It has to be the `id`. So confusing! In hindsight looking at the example does show ID values instead of name values.

   - Anyhow, once you get them, just [plug them in to your data source](https://github.com/AutomationAdmin-Com/sic.mgmt/blob/facf9eeb7dc99966174b83cc230868eaf1c86b0b/source/common/stage1/sub.tf#L2) and then run your apply.

1. What happens is, the first two subscriptions created almost instantly, but the third one timed out. I can't find the logs or I would show you :/

1. I already knew the fix for this from dealing with it in the past, basically you just have to **wait**. This is because Microsoft doesn't want customers spinning up hundreds of subscriptions per hour because a subscription is a high level billing resource that holds many things, pretty much the highest level you go on a daily basis so they throttle it. Anyways, I was going to wait 24 hours, but I just re-ran the same pipeline about 12 hours later and it worked.

   - ![subscription-created](https://automationadmin.com/assets/images/uploads/2023/11/subscription-created.png){:class="img-responsive"}

1. So there you go, you can create PAYG subscriptions using Terraform pretty easily these days. In the past, [I always did these by hand](https://automationadmin.com/2022/10/tf-new-subscription) and then used [terraform to place them in correct management groups](https://github.com/gerryw1389/terraform-examples/blob/main/2022-10-20-tf-new-subscription/main.tf) but now I can control the subscription objects themselves.
