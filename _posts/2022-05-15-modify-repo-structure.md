---
title: Terraform Modify Repo Structure
date: 2022-05-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/modify-repo-structure/
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

Continuing from my [previous post](https://automationadmin.com/2022/05/setup-azdo-terraform/), I then wanted to format my repo in a way that will be scalable going forward. Source code for this post can be found [here](https://github.com/gerryw1389/terraform-examples/tree/main/resource-group-with-lock-with-template)

### To Resolve:

1. So the first thing I wanted to do was to reference the [Terraform Repo Guide](https://www.terraform.io/language/modules/develop/structure) which basically says to put your code in root of repo and then make module calls to a `Modules` folder.

1. After doing that, I then decided that I will stick with 3 standard files for all terraform code: `variables.tf` for input variables, `main.tf` for building resources, and `outputs.tf` if it is some kind of module that will be returning values.

1. In addition, my `main.tf` will always include a `providers` section at the top, a `locals` section second for any repeated code, and finally a `resources` section for all module calls and resources. I'm currently debating if I want a `data` section before or after the `resources` section, we will see. [Reference](https://github.com/gerryw1389/terraform-examples/blob/main/resource-group-with-lock-with-template/main.tf) for what I'm saying here.

1. The cool thing about going this route is I can now remove the following from my `build.yaml`:

   ```yaml
   - task: CopyFiles@2
      displayName: 'Copy Deploy Folder'
      inputs:
         SourceFolder: $(Build.SourcesDirectory)/Deploy
         Contents: "*"
         TargetFolder: $(Build.SourcesDirectory)
   ```

   - Since the files are now at the root of the repo, you don't have to copy them up on the build agent anymore.

1. In addition, I have taken to explicitly declaring required versions of things (see providers seciont of `main.tf`) so that I can move in a model to where you upgrade your deployments by testing against new versions of releases.

1. Lastly, after pushing changes to my repo in Azure Devops, the next step was to run a build and release pipeline to ensure it says the following in the `terraform plan` stage of the pipeline:

   ```escape
   module.azure_learning_rg.azurerm_resource_group.rg: Refreshing state... [id=/subscriptions/***/resourceGroups/aa-dev-tx-test]
   azurerm_management_lock.resource-group-level: Refreshing state... [id=/subscriptions/***/resourceGroups/aa-dev-tx-test/providers/Microsoft.Authorization/locks/BlockDelete]

   No changes. Your infrastructure matches the configuration.

   Terraform has compared your real infrastructure against your configuration
   and found no differences, so no changes are needed.
   Finishing: terraform plan
   ```

   - And this in the `terraform apply` stage of the pipeline

   ```escape
   ╷
   │ Warning: "use_microsoft_graph": [DEPRECATED] This field now defaults to `true` and will be removed in v1.3 of Terraform Core due to the deprecation of ADAL by Microsoft.
   │ 
   │ 
   ╵

   Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
   Finishing: terraform apply
   ```

