---
title: 'Terraform: Template'
date: 2023-02-27T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/02/terraform-template
tags:
  - Azure
  - AzureDevops
  - Terraform
---
<!--more-->

### Description:

So after using [terragrunt](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2) for a few weeks, it dawned on me that you could technically do everything that terragrunt does with native terraform and a bit of work so that got me thinking of creating a "terraform template repo". This would allow our team to use a file system just like terragrunt does and then pass values based on the environment by creating static files like discussed in my [generate post](https://automationadmin.com/2023/02/terragrunt-generate). Here is how you could go about doing this:

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-02-27-terraform-template).
{: .notice--success}

### To Resolve:

1. So the file system will have 3 folders at the root:

   - `./yaml` => This is our pipeline files that will call the terraform executable. I have not ported these to Github actions yet so they are Azure Devops formatted.
   - `./docs` => This is our [changelog](https://automationadmin.com/2023/01/update-changelog) and other docs.
   - `./infra` => This is the root or our directory structure that will split between `./infra/nonprod` and `./infra/prod`

1. So all you have to do is build each of them out. I have 4 subscriptions for my domain so it looks like this:

   ```escape
   Folder PATH listing
   Volume serial number is CE88
   C:.
   │   .gitignore
   │   README.md
   │
   ├───docs
   │       changelog.md
   │       pull_request_template.md
   │
   ├───infra
   │   ├───nonprod
   │   │   ├───hub
   │   │   │   ├───eus
   │   │   │   │       backend.tf
   │   │   │   │       common_data_lookup.tf
   │   │   │   │       main.tf
   │   │   │   │       nonprod_eus.tf
   │   │   │   │       terraform.tfvars
   │   │   │   │       variables.tf
   │   │   │   │
   │   │   │   └───scus
   │   │   │           backend.tf
   │   │   │           common_data_lookup.tf
   │   │   │           main.tf
   │   │   │           nonprod_scus.tf
   │   │   │           terraform.tfvars
   │   │   │           variables.tf
   │   │   │
   │   │   └───spoke
   │   │       ├───eus
   │   │       │       backend.tf
   │   │       │       common_data_lookup.tf
   │   │       │       main.tf
   │   │       │       nonprod_eus.tf
   │   │       │       terraform.tfvars
   │   │       │       variables.tf
   │   │       │
   │   │       └───scus
   │   │               backend.tf
   │   │               common_data_lookup.tf
   │   │               main.tf
   │   │               nonprod_scus.tf
   │   │               terraform.tfvars
   │   │               variables.tf
   │   │
   │   └───prod
   │       ├───hub
   │       │   ├───eus
   │       │   │       backend.tf
   │       │   │       common_data_lookup.tf
   │       │   │       main.tf
   │       │   │       prod_eus.tf
   │       │   │       terraform.tfvars
   │       │   │       variables.tf
   │       │   │
   │       │   └───scus
   │       │           backend.tf
   │       │           common_data_lookup.tf
   │       │           main.tf
   │       │           prod_scus.tf
   │       │           terraform.tfvars
   │       │           variables.tf
   │       │
   │       └───spoke
   │           ├───eus
   │           │       backend.tf
   │           │       common_data_lookup.tf
   │           │       main.tf
   │           │       prod_eus.tf
   │           │       terraform.tfvars
   │           │       variables.tf
   │           │
   │           └───scus
   │                   backend.tf
   │                   common_data_lookup.tf
   │                   main.tf
   │                   prod_scus.tf
   │                   terraform.tfvars
   │                   variables.tf
   │
   └───yaml
      │   bump_module_steps.yaml
      │   bump_module_version.yaml
      │   nonprod-build.yaml
      │   nonprod-release.yaml
      │   prod-build.yaml
      │   prod-release.yaml
      │
      ├───hub
      │   ├───build
      │   │       nonprod-eus-linux.yaml
      │   │       nonprod-eus-windows.yaml
      │   │       nonprod-scus-linux.yaml
      │   │       nonprod-scus-windows.yaml
      │   │       prod-eus-linux.yaml
      │   │       prod-eus-windows.yaml
      │   │       prod-scus-linux.yaml
      │   │       prod-scus-windows.yaml
      │   │
      │   └───release
      │           nonprod-eus-linux.yaml
      │           nonprod-eus-windows.yaml
      │           nonprod-scus-linux.yaml
      │           nonprod-scus-windows.yaml
      │           prod-eus-linux.yaml
      │           prod-eus-windows.yaml
      │           prod-scus-linux.yaml
      │           prod-scus-windows.yaml
      │
      └───spoke
         ├───build
         │       nonprod-eus-linux.yaml
         │       nonprod-eus-windows.yaml
         │       nonprod-scus-linux.yaml
         │       nonprod-scus-windows.yaml
         │       prod-eus-linux.yaml
         │       prod-eus-windows.yaml
         │       prod-scus-linux.yaml
         │       prod-scus-windows.yaml
         │
         └───release
                  nonprod-eus-linux.yaml
                  nonprod-eus-windows.yaml
                  nonprod-scus-linux.yaml
                  nonprod-scus-windows.yaml
                  prod-eus-linux.yaml
                  prod-eus-windows.yaml
                  prod-scus-linux.yaml
                  prod-scus-windows.yaml
   ```

1. So basically, you split based on environment, subscription, and then region. Using this setup has these pros:

   - You can use native terraform.
   - All the work has been done ahead of time, the values for `./infra/prod/hub/eus/terraform.tfvars` for example will be scoped to values only in prod environment, hub subscription, and east region.
   - If you want to deploy a new subscription in that region, just copy that folder and change just a few variable values. Everything else will be easily expandable.
   - Likewise, if you want to expand on any part of the template you can do that - just copy and paste at the appropriate level and then tweak your copy by replacing just what you need.
   - If you apply this template in many repos, all developers will be familiar with a consistent structure. You just need documentation explaining why you made certain design choices.
   - Each environment/subscription/region will have its own statefile in the `backend.tf`. This gets you the same result as [`path_relative_to_include()`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v2/infra-config/prod/all-prod.hcl#L47) that we used to do with terragrunt.
   - Each environment/subscription/region will have its own locals in the `nonprod_eus.tf`, `prod_eus.tf`, `nonprod_scus.tf`, or `prod_scus.tf` but the name of the local will be the same across each. So you can do `local.eh_id` for each of these files and use it anywhere in your deployment but not have to think about its value. This replaces the [`generate`](https://automationadmin.com/2023/02/terragrunt-generate) we used to do with terragrunt. See that post for more details of what I mean here.

1. Using this setup has these cons:

   - Lots of duplication going on, supposed to be what Terragrunt solves by keeping code DRY. This personally doesn't bother me due to all the pros listed above.
   - What if you need to change something everywhere? Like checking out a new repo? Well you can actually use multi/line find/replace in VSCode so this is still not an issue. I've done plenty of commits that effected 200+ files and my pipelines run fine! For example, I need to replace:

   ```
   terraform plan \
            -var="subscription_id=$ARM_SUBSCRIPTION_ID" \
            -var="tenant_id=$ARM_TENANT_ID" \
            -var="client_id=$ARM_CLIENT_ID" \
            -var="client_secret=$ARM_CLIENT_SECRET" \
            -out "tf.plan"
   ```

   - with 

   ```
   terraform plan \
               -var="subscription_id=$ARM_SUBSCRIPTION_ID" \
               -var="tenant_id=$ARM_TENANT_ID" \
               -var="client_id=$ARM_CLIENT_ID" \
               -var="client_secret=$ARM_CLIENT_SECRET" \
               -var="my_secret=$My_Secret" \
               -out "tf.plan"
   ```

   - So I do a find/replace. But what if I only want it for my linux build agents because Windows uses a `^` as a line continuation? No problem, just in the "files to include" type `*linux.yaml`
   - Or what if only east but not south central? Same thing, in the "files to include", search for `*-east-*.yaml`. For example:
   - ![regex-example](https://automationadmin.com/assets/images/uploads/2023/03/regex.jpg){:class="img-responsive"}

   - So all in all, not really seeing any major cons to using a template for terraform deployments. Consistency trumps effeciency in my book because I've worked places where people did what they wanted and everything was done differently and it's hard to onboard new developers.

1. So how does the template work?

   - The first landing zone of the template is [`./yaml/nonprod-build.yaml`](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/nonprod-build.yaml), `./yaml/nonprod-release.yaml`, `./yaml/prod-build.yaml`, or `./yaml/nonprod-release.yaml` where you will create pipelines in Azure Devops off of these. They allow developers to choose the subscription, region, and build agent on each run with some defaults set so they don't have to always make a selection.
   - These will then call children based on what the user selects. The children can be `./yaml/hub/build/nonprod-westus-linux.yaml` or whatever for example and they are the actual pipeline files that will get executed. They are based off a simple powershell like `switch` statement as seen in that link.
   - Next, the child pipelines will copy your terraform files to your `$(Build.SourcesDirectory)` and then either run `terraform plan`, `terraform apply`, or some combination of both (depending if you chose build or release).
   - The main thing is that, you as the developer, do not have to think about the values for `local.eh_rg` or whatever because it's already there available to you, you just have to focus on your scoped deployment.
   - So if I want to deploy a keyvault in hub prod east region where would I go? I don't know, maybe `./infra/prod/hub/east` and create a file called `./keyvault.tf` in that directory? Haha pretty easy.
   - The real power of this template is, let's say you have a module for Keyvault and you need to pass a Log Analytics Workspace to it so it can setup diagnostic settings, well using this template you won't have to think you can just pass `local.law_name` like we [used to do in a module](https://github.com/gerryw1389/terraform-modules/blob/main/data-sources/examples/common.tf#L158) but now its baked into the template with no lookups.
   - So basically instead of a module and then switching based on environment/subscription/region its the opposite, we hard code based on environment/subscription/region one time and then set all deployments do use those values.

1. For this to work, it is also best to give nonprod and prod the same display names for Secrets in your Keyvault like you see in my variable groups [nonprod-secrets](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/spoke/release/nonprod-scus-linux.yaml#L15) and [prod-secrets](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/spoke/release/prod-scus-linux.yaml#L15) whre they both use same display name for `TF_VAR_subscription_id: $(aa-spoke-id)` and `TF_VAR_hub_subscription_id: $(aa-hub-id)` but in the KeyVaults they could be mapped like so:
   - Nonprod Keyvault: aa-spoke-id => Subscription ID for automationadmin-spoke-nonprod
   - Nonprod Keyvault: aa-hub-id => Subscription ID for automationadmin-hub-nonprod
   - Prod Keyvault: aa-spoke-id => Subscription ID for automationadmin-spoke-nonprod
   - Prod Keyvault: aa-hub-id => Subscription ID for automationadmin-hub-prod
