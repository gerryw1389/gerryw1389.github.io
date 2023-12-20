---
title: Main Terraform Workflow Repo Structure
date: 2023-10-22T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/10/terraform-workflow-repo-structure
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description

Continuing from my [previous post](https://automationadmin.com/2023/05/main-terraform-workflow), I wanted to go into more details about my repo structure because it is highly versatile and worth explaining in my opinion. 

Note: You can see the code for this post on [my Github repo](https://github.com/AutomationAdmin-Com/sic.template/tree/main).
{: .notice--success}

### Steps

1. This is the folder as it exists in Github and on the Github Runner right at the [checkout stage](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L27) before any modifications.

   ```escape
   C:.
   │   README.md
   │
   ├───.github
   │   └───workflows                               => This is where all pipelines are created. Github calls these "workflows"
   │           main_protector.yaml                 => These are workflow files covered in other posts.
   │           main.yml
   │
   ├───config                                      => This folder exists to make changes for a specific environment that is based on folder path. We call these "configs" because each dir has its own state file based on paths.
   │   └───nonprd                                  => Environment based, nonprd or prd. Could also add 'uat', 'maint', or some other stage by copying/pasting and changing the variables.tf and/or terraform.tfvar values underneath.
   │       └───spoke                               => Create one folder for as many Azure subscriptions that you want to switch on.
   │           └───scus                            => Create one folder for as many regions as you want to deploy to.
   │               └───stage1                      => We need to create one folder for each stage. For example, it's common to create an AKV in stage1 and then read in a cert from that AKV in stage2.
   │                   ├───blue                    => Last, create a sub folder for blue, green, or none. This is really only for deploying services that will do "blue green cutovers".
   │                   │       backend.tf          => State file location as well as building providers from the secrets from a Key Vault being passed to terraform by workflow.
   │                   │       terraform.tfvars    => Any environment specific vars.
   │                   │       variables.tf        => Global variable definitions for this stage.
   │                   │
   │                   └───green
   │                           backend.tf
   │                           terraform.tfvars
   │                           variables.tf
   │   └───prd                                     => Same tree as above but for prod instead of non-prod.
   │       └───spoke
   │           └───eus
   │               └───stage1                      
   │                   ├───blue
   │                   │       backend.tf          
   │                   │       terraform.tfvars    
   │                   │       variables.tf        
   │                   │
   │                   └───none
   │                           backend.tf
   │                           terraform.tfvars
   │                           variables.tf
   │
   └───source                                      => These are static files that should be like modules where almost all values are vars being passed in from above. Avoid hard coding anything here as it will apply to all environments!
      ├───common
      │   └───stage0                              => These should define resources that goes in stage0 for all subscription, regions, and environments.
      │           rg.tf
      │
      └───modules                                 => These are local module calls you can make at run time. During execution, our worflow will copy these files recursively to the `./live/*` folder.
         └───rand
                  random_string.tf
                  variables.tf
   ```

1. Now that we have these files in the repo and have explained their purpose, let's examine what happens at run time. There is a [critical step](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L78) where we copy the files in a specific way:

   - First, we create a folder called `./live` that exists on the Github Runner only during execution, it does not exist anywhere in our stored repo.
   - Next, since we are using a [matrix workflow](https://automationadmin.com/2023/05/main-terraform-workflow), this specific Github run will be running in parrallel with **all** the changes you made for this Pull Requests.

   - This means we could be running one, two, or twenty parrallel exucutions but each one with a specific `${/{ matrix.directories }}` value that coorelates to something like `config/nonprd/hub/east/stage2/none` or `config/prd/hub/east/stage2/none` or `config/prd/hub/scus/stage2/none` for example.

   - NOTE: [Jekyll Liquid Filters](https://jekyllrb.com/docs/liquid/filters/) clash with [Github Variables](https://docs.github.com/en/actions/learn-github-actions/variables#using-contexts-to-access-variable-values) so replace all instances of `${/{` by removing the forward slash :)

   - Next, we have a [parse script](https://github.com/AutomationAdmin-Com/sic.template/blob/main/.github/scripts/parse.sh) that is simply a bash script that looks at those paths and creates outputs dynamically as [explained in my post here](https://automationadmin.com/2023/11/using-akv-to-get-secrets) to create outputs. We are just getting the stage number in this case.

   - Next, we recursively copy all files under `./source/modules` so that all local module calls will be `./modules/$moduleName` as seen in [`rg.tf`](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/source/common/stage1/rg.tf#L23C26-L23C40)

1. Here is the task in the pipeline that will modify file placement so that terraform can run in a single directory:

1. This is the folder as it exists during a workflow execution **AFTER** the Copy Files task:

   ```escape
   C:.
   │   README.md
   │
   ├───.github
   │   └───workflows
   │           main_protector.yaml
   │           main.yml
   ├───config
   │   └───nonprd
   │       └───spoke
   │           └───eus
   │               └───stage1
   │                   ├───none
   │                   │       backend.tf
   │                   │       terraform.tfvars
   │                   │       variables.tf
   ├───live                                              => This is a brand new directory created at run time that contains all files needed for Terraform to run.
   │   │   backend.tf                                    => This came from config/nonprd/spoke/eus/stage1/none
   │   │   rg.tf                                         => This came from the source/common/stage1
   │   │   terraform.tfvars                              => This came from config/nonprd/spoke/eus/stage1/none
   │   │   variables.tf                                  => This came from config/nonprd/spoke/eus/stage1/none
   │   │
   │   └───modules                                       => This got copied from source/modules/rand. Files like `./rg.tf` above reference these locally like `./modules/moduleName
   │       └───rand
   │               random_string.tf
   │               variables.tf
   │
   └───source
      └───common
         └───stage1
   ```

1. You then see in [subsequent steps](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L163) that we continue to `cd $GITHUB_WORKSPACE/live` before running any terraform commands.

1. That's it! So really this workflow solves so many problems and allows a large enterprise to use Terraform effectively:

   - You can deploy to multiple Azure subscriptions in a single run. Example: "I need to deploy a key vault to prd-hub in the southcentralus region and I need to do the same thing to nonprd-spoke in the eastus region". Done, just:
     - Modify the `variables.tf` by adding a line break in `config/prd/hub/scus/stage1/none` folder and then ensure that you are creating a Key Vault in `./source/common/stage1/akv.tf` for example.
     - Modify the `variables.tf` by adding a line break in `config/nonprd/spoke/eus/stage1/none` folder and then ensure that you are creating a Key Vault in `./source/common/stage1/akv.tf` for example.

   - Each deployment will have a separate state file as seen in [`backend.tf`](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/config/prd/hub/scus/stage1/none/backend.tf#L8) and [`backend.tf here`](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/config/nonprd/spoke/east/stage1/none/backend.tf#L8)

   - You could easily modify the workflow for a specific run, like adding a new variable for example, by changing `./.github/workflows/main.yml` to `workflow dispatch` and then creating a new file with similar contents that runs based on a specific path [like discussed in previous post](https://automationadmin.com/2023/05/main-terraform-workflow) of how I used to do it. For example:

   ```yaml
   on:
   push:
      branches:
         - "develop"
      paths:
         - "config/nonprd/hub/east/stage1/none/*"
   pull_request:
      types: [opened, edited, synchronize]
      branches:
         - "develop"
      paths:
         - "config/nonprd/hub/east/stage1/none/*/*"
   ```

   - You could easily expand this template to have new stages, new subscriptions, new environments, or anything really. The magic lies in the parsing script that sets outputs dynamically, so be sure to read [my post covering this](https://automationadmin.com/2023/11/using-akv-to-get-secrets) to get an idea for your organization.

   - I'm sure there are other perks but overall this template is very powerful as I have ran it hundreds of times for hundreds of scenarios!
