---
title: 'Terragrunt: Repo Structure V2'
date: 2023-01-04T08:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/terragrunt-repo-structure-v2
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

This post builds on [Terragrunt Repo Structure V1](https://automationadmin.com/2023-01-04-terragrunt-repo-structure-v1) by adding a few improvements:

   - It removes the 8 `terragrunt.hcl` files in the different directories
   - It shows how to split code if you want to have special use cases in environments by changing the `source` attribute in terragrunt.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v2). [Github Actions are here](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2023-01-04-terragrunt-repo-structure-v2/).
{: .notice--success}

### To Resolve:

1. So the first thing I had to get rid of when continuing to pursue [Terragrunt](https://terragrunt.gruntwork.io/) was the 8 `terragrunt.hcl` files from my previous post. For those unaware, I have 4 [subscriptions](https://automationadmin.com/2022/10/tf-new-subscription) in Azure: One hub prod, one hub nonprod, one spoke prod, and one spoke nonprod. This is an example setup for a larger organization that might use a hub-and-spoke network topology.

   - Anyways, I used terragrunt and got it inherting locals but the only problem was it was repeating by me having to copy/paste the same file multiple times.
   - The fix for this was to move the contents of [`root.hcl`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/root.hcl) into a new file a level down called [`all-nonprod.hcl`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/all-nonprod.hcl) and then update the downstream `terragrunt.hcl` files to just point to it like before by replacing:

   ```hcl
   # Include all settings from the root terragrunt.hcl file
   include "root_config" {
   path = find_in_parent_folders("root.hcl")
   }
   ```

   - with

   ```hcl
   # Include all settings from the nonprod terragrunt.hcl file
   include "nonprod_config" {
   path = find_in_parent_folders("all-nonprod.hcl")
   }
   ```

1. NOTE: I had originally tried adding a new include statement but got this error:

   ```escape
   time=2023-01-17T11:57:33Z level=error msg=Error processing module at '/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/hub/east/deployment/terragrunt.hcl'. How this module was found: Terragrunt config file found in a subdirectory of infra-config/nonprod/hub/east/deployment. Underlying error: /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/hub/east/deployment/terragrunt.hcl includes /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/all-nonprod.hcl, which itself includes /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v2/infra-config/root.hcl. Only one level of includes is allowed.
   time=2023-01-17T11:57:33Z level=error msg=Unable to determine underlying exit code, so Terragrunt will exit with error code 1
   ```

   - Next I tried moving the `include "root_config"` into `all-nonprod.hcl` and then from **there** importing but it gave the same error. Notice the verbiage `Only one level of includes is allowed.` 

   - So after merging the original contents of `root.hcl` into my new `all-nonprod.hcl`, everything worked as expected!

1. The second thing I needed to look at was customizing my Terraform `source` directory to be more specific if I have changes in my environment that would be too complicated to [conditionalize](https://automationadmin.com/2022/10/tf-using-flags-for-settings).

   - Well the fix is to just break the `infra` folder to have sub folders just like I normally structure my repos. Then just update the source to point to `nonprod` (see line 54 [here](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/all-nonprod.hcl)) or `prod` (see line 54 [here](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra-config/prod/all-prod.hcl)).

1. Let's discuss the pros of this approach:

   - First, the main one is you don't have to set a bunch of conditional flags like `enable_acr` or `enable_$thing` and then in your code do `count = var.enable_acr == true ? 1 : 0` for a [container resource](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/container_registry) for example. By using the [initial version of this repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v1) (see the infra folder has no subfolders so all terraform code has to not care about the region or environment that resources are deployed to), all terraform code will have to be the same for all environments and regions. 

     - This is of course ideal and what you want, but in large enterprises there may be too many differences between regions or environments for example and it might be easier to break them into sub folders.

   - So the pro of this approach is simplicity, you create sub folders under `infra` and then you create your custom code based on your desire and then just update your source as mentioned above.

   - The other pro to this is that you keep your terraform config separate from your terragrunt config. This is helpful because if you ever decide to quit using terragrunt, you can simply delete the terragrunt folder structure and copy/paste your `generate` blocks into a new `backend.tf` and be done!


1. Let's discuss the cons of this approach:

   - The only main con is that you will be creating infrastructure that is different based on some variable that you declare. For example if you create `./infa/nonprod` and `/infra/prod` folders, then it is assumed that there are significant differences between the environments to warrant copying your code set downstream from those folders.

   - Another con to this approach is that you would need to break your "root" hcl files based on which folder to target. This means that you can't simply point to one "root" hcl if you have different files per environment.

   - For example, in nonprod [here](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra-config/nonprod/all-nonprod.hcl), I could point to a storage account in a nonprod subscription and pass the source to the `infra/nonprod` folder as shown but then in prod copy/paste and do the exact same things but instead point to a prod storage account for my state file and point to the `./infra/prod` folder instead. This creates redundancy with minor differences between environments and is unneccessary. This is the very problme that terragrunt resolves! Nonetheless, I feel it is still worth it to break everything nonprod and prod up because this gives a clear delineation between environments!

1. Running the new build I see the outputs show the enviornment, subscriptions, and regions correctly now. It says it will create the Resource Groups as defined - [NonProd](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra/nonprod/main.tf) / [Prod](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra/prod/main.tf) :

   ```escape
   "aa-nonprod-dev-hub-scus-mgmt-nonprd-specific-rg" # nonprod/ hub / South Central
   "aa-nonprod-dev-hub-eus-mgmt-nonprd-specific-rg"  # nonprod/ hub / East
   "aa-nonprod-dev-spk-scus-mgmt-nonprd-specific-rg" # nonprod/ spoke / South Central
   "aa-nonprod-dev-spk-eus-mgmt-nonprd-specific-rg"  # nonprod/ spoke / East

   "aa-prod-prod-spk-scus-mgmt-prd-specific-rg"      # prod/ spoke / South Central
   "aa-prod-prod-spk-eus-mgmt-prd-specific-rg"       # prod/ spoke / East
   "aa-prod-prod-hub-eus-mgmt-prd-specific-rg"       # prod/ hub / East
   "aa-prod-prod-hub-scus-mgmt-prd-specific-rg"      # prod/ hub / South Central
   ```

