---
title: 'Terragrunt Generate'
date: 2023-02-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/02/terragrunt-generate
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

When using terragrunt, I wanted a way to move my [shared data sources module](https://automationadmin.com/2022/11/data-sources-module) to instead be locals because that is one of the main points of terragrunt is that you can set locals which [will get inherited above](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2) in the file system.

   - For example, the value for `local.eh_id` will be whatever the region is [no matter where I deploy](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/examples/common.tf)
   - As you can see, using a data lookup module you can set values to outputs based on variables passed in.

So I had two choices with terragrunt to accomplish this, either use [dependencies](https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/#dependency) or [generate](https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/#generate) the files at run time. I decided the latter due to simplicity.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-02-04-terragrunt-generate).
{: .notice--success}


### To Resolve:

1. So the way it works is you create a directory under `./infra-config` called `./generate` and then create some files like:

   - prod_scus.tf
   - nonprod_scus.tf
   - ... other combinations as needed

1. Each of these files will have the exact same locals block, but will hard code the values from the environment:
   - [prod_scus.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/generate/prod_scus.tf)
   - [nonprod_eus.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/generate/nonprod_eus.tf)
   - Click on the two links and compare them. They look almost identical right? This is the point, you want to be able to declare something like `local.eh_id` and know that it will automatically get the correct ID in your deployment.

1. But won't those conflict? You can't declare the same local twice? Well no, because you will only point to your combination:

   - Look under [`/infra-config/nonprod/all_nonprod_eastus.hcl`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/nonprod/all_nonprod_eastus.hcl#L54-L60) and you will see that you are only calling the main `common.tf` which is shared across all environments, and then your specific file for nonprod/eus locals.
   - Look again under [`/infra-config/prod/all_prod_southcentralus.hcl`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/prod/all_prod_southcentralus.hcl#L54-L60) and you will see that you are only calling the main `common.tf` which is shared across all environments, and then your specific file for prod/scus locals.

1. OK, that makes sense. But where is `${local.data_sources_aaprod_id}` being defined? Well that's why you also have a [`common.tf`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/generate/common_data_lookup.tf) where you build your providers. Here are the steps in that file:
   
   - So here we are first querying all subscriptions.
   - Then we create locals that will store the subscription ID's in a local for consumption later.
   - Next, we can build providers and pass those subscription ID's or use them directly like in the other files. Either way, we have the subscription ID's available at runtime. Neat!

1. Anways, after the directory and files are created, you just call the `generate()` function in your main terragrunt config file [like we do here](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/prod/all_prod_southcentralus.hcl#L18) and you point to your region specific file and a generic file for all environments:

   ```terraform
   # https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/#generate
   generate "locals_prod_scus" {
   path      = "locals_prod_scus.tf"
   if_exists = "overwrite_terragrunt"
   contents  = file("${get_repo_root()}/infra-config/generate/prod_scus.tf")
   }
   generate = local.terragrunt_generated.generate
   ```

   - Note that you can mix between a block and an attribute as seen above, just [read the docs on it](https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/#generate).

   - In this case, the value for `local.terragrunt_generated.generate` was in the locals block above with the value of `read_terragrunt_config(find_in_parent_folders("terragrunt_generated.hcl"))` which just points to [a file with more `generate` blocks](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-04-terragrunt-generate/infra-config/terragrunt_generated.hcl). So at the end of the day, all generate's are a block.
   - At run time, terragrunt will generate a file called 'providers.tf' and 'common_data_lookup.tf' from the `local.terragrunt_generated.generate` block and then it will generate 'locals_prod_scus.tf' from the `generate "locals_prod_scus"` block.

