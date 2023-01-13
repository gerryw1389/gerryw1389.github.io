---
title: 'Terraform: Upgrading TF CLI Version and AzureRM Version'
date: 2022-12-02T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/12/tf-version-upgrades
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

So a critical part of using terraform across many repositories on a team is to practice version pinning to ensure consistency between environments. This was discussed in my [Git Tagging](https://automationadmin.com/2022/08/git-tagging) post but it was in reference to modules. Here we want to pin the Terraform CLI version and the AzureRM, AzureAD, and any other providers we use.

### To Resolve:

1. To ensure your Terraform CLI version, you can usually pass that as a parameter in your pipeline. For example:

   ```yaml
   - task: ms-devlabs.custom-terraform-tasks.custom-terraform-installer-task.TerraformInstaller@0
      displayName: 'Install Terraform 1.3.6'
      inputs:
         terraformVersion: 1.3.6
   ```

1. To ensure your provider versions, just mention them in any of your `*.tf` files, typically `backend.tf`, `versions.tf`, or `providers.tf`:

   ```terraform
   terraform {
   required_providers {
      azurerm = {
         source  = "hashicorp/azurerm"
         version = "3.37.0"
      }
      azuread = {
         source  = "hashicorp/azuread"
         version = "2.26.0"
      }
      random = {
         source  = "hashicorp/random"
         version = "3.4.3"
      }
   }
   required_version = "1.3.6"
   }
   ```

1. After updating, run a terraform plan and pay attention to the `terraform init` output in your pipeline. It should specifically mention what versions of providers it is installing.

1. I had an issue once where I was going crazy because I had pinned to a specific version and it kept updating to the latest versions. 

   - I first found [this link](https://developer.hashicorp.com/terraform/tutorials/configuration-language/provider-versioning#initialize-and-apply-the-configuration) which made me think that since I didn't have a lock file, that terraform was upgrading automatically like in the example so I created a lock file and pushed it.
   - That worked, but I later found the culprit. The pipeline had for whatever reason used [`terraform init -upgrade`](https://developer.hashicorp.com/terraform/cli/commands/init#upgrade) so I removed that flag and it started working as expected.

1. To create the lock file I did this:

   - `cd` to my repo
   - Run `terraform init .` on my dev box
   - Terraform creates a `.terraform.lock.hcl`
   - I then had to remove `.terraform` from my `.gitignore` so I can push lock to repo
   - Push file to repo

1. OK, so after updating the terraform CLI and the AzureRM, AzureAD, ect. providers, the next thing is to run `terraform plan` pipelines and fix any errors that come up. They are usually descriptive like `attribute depreciated, please use $x`. 

1. If you haven't already, ensure that you bookmark the Terraform docs to the version you use everywhere in your environment. This makes it easy to see what attributes are available for all resources using your pinned version. For example, I usually bookmark the [`azurerm_storage_account`](https://registry.terraform.io/providers/hashicorp/azurerm/3.33.0/docs/resources/key_vault) resource. Notice the version in the URL? `azurerm/3.33.0/docs`?