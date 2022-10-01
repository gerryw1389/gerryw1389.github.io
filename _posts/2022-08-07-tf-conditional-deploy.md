---
title: 'TF: Conditional Deploy'
date: 2022-08-07T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-conditional-deploy
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

So far, HCL has been an easy language to learn as you mostly just look at pointers and see what certain values are. I would say the hardest time I have had since starting is learning the [count](https://automationadmin.com/2022/07/tf-count) and [for_each](https://automationadmin.com/2022/07/tf-for-each) to deploying multiple reosurces and how to use them. In this post I will show how count is commonly not only used to deploy a group of resources, but conditionally deploy a resource based on any expression. Code for this post can be found [here](https://github.com/gerryw1389/terraform-examples/tree/main/2022-08-07-tf-conditional-deploy).

### To Resolve

1. First, take a look at [main](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-07-tf-conditional-deploy/main.tf) and notice the `count`. See how if `var.region` is `southcentralus` the count will equal `1` and if false, it will equal `0`? That means that if I pass that value to that var it will deploy the resource and if I pass any other value it won't.

   - This can be seen [here](https://github.com/gerryw1389/terraform-examples/actions/runs/3165731412/jobs/5154975241) where I pass the value by letting its default deploy it. Notice it deletes my older RG and deploys the new one.
   - This can be seen [here](https://github.com/gerryw1389/terraform-examples/actions/runs/3165740011/jobs/5154990092) where it doesn't deploy it because I set the region to `eastus` at [line 50 here](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-08-07-tf-conditional-deploy-release.yaml) and instead deletes the Resource Group that was deployed from my previous run. This is because count was set to `0` which means there should be no instance of that deployed.

   - Also take note that both `module azure_learning_rg` and `resource azurerm_management_lock` both have to make that same reference? This is because you can't tie a lock to a resource that doesn't exist silly :)

2. See [here](https://github.com/kumarvna/terraform-azurerm-virtual-machine/blob/v2.3.0/main.tf) for many examples of conditional deploys.

3. This is a common and core concept of Terraform so practice this alot because it is something you will be wanting to do often. I will try to come up with more posts with examples of this and link back to this one in the future.

4. Also, this can also be done with `for_each` with dynamic blocks as mentioned [in this post on a different blog](https://codeinthehole.com/tips/conditional-nested-blocks-in-terraform/).