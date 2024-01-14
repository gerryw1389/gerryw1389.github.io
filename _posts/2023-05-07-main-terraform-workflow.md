---
title: 'Github Actions: Main Terraform Workflow'
date: 2023-05-07T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/05/main-terraform-workflow
tags:
  - Github
  - Terraform
---
<!--more-->

### Description

Following my [git flow model](https://automationadmin.com/2023/04/git-flow-model), I needed to find a way to use Terraform with Github Actions in a logical manner. I wanted it to trigger based on the files that I modified in a directory structure and only during Pull Requests to the `develop` branch and after approvals of those Pull Requests. Here is how I did it:

Note: You can see the code for this post on [my Github repo](https://github.com/AutomationAdmin-Com/sic.template/tree/main).
{: .notice--success}

### To Resolve:

1. For a long time, the only way I knew how to set this up was to create many workflows under `./.github/workflows/example1.yml`, `./.github/workflows/example2.yml`, etc.

1. Each of these workflows like example1.yml looked like this:

   ```yaml
   name: "nonprd_hub_eus_1_none"

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

   jobs:
   main_yaml:
      uses: gerryw1389/terraform-examples/.github/workflows/_main.yml@sprint
      with:
         config_files_path: "config/nonprd/hub/east/stage1/none/*"
         secrets_list: "spn-tenant-id spn-client-id spn-client-secret sa-access-key"
         spoke_subscription_secret_name: "hub-nonprd-sub-id"
         hub_subscription_secret_name: "hub-nonprd-sub-id"
         secrets_akv: "my-akv"
         common_subfolder: "stage1"
         workflow_path: ${/{ github.repository }}/${/{ github.workflow }}
         actor: ${/{ github.actor }}
      secrets:
         azure_cred: ${/{ secrets.AZURE_CREDENTIALS }}
         ssh_key_github_actions: ${/{ secrets.SSH_KEY_GITHUB_ACTIONS }}
   ```

   - example `example2.yml` :

   ```yaml
      name: "nonprd_hub_scus_1_none"

      on:
      push:
         branches:
            - "develop"
         paths:
            - "config/nonprd/hub/scus/stage1/none/*"
      pull_request:
         types: [opened, edited, synchronize]
         branches:
            - "develop"
         paths:
            - "config/nonprd/hub/scus/stage1/none/*/*"

      jobs:
      main_yaml:
         uses: gerryw1389/terraform-examples/.github/workflows/_main.yml@sprint
         with:
            config_files_path: "config/nonprd/hub/scus/stage1/none/*"
            secrets_list: "spn-tenant-id spn-client-id spn-client-secret sa-access-key"
            spoke_subscription_secret_name: "hub-nonprd-sub-id"
            hub_subscription_secret_name: "hub-nonprd-sub-id"
            secrets_akv: "my-akv"
            common_subfolder: "stage1"
            workflow_path: ${/{ github.repository }}/${/{ github.workflow }}
            actor: ${/{ github.actor }}
         secrets:
            azure_cred: ${/{ secrets.AZURE_CREDENTIALS }}
            ssh_key_github_actions: ${/{ secrets.SSH_KEY_GITHUB_ACTIONS }}
      ```

   - Can you spot the difference? It's subtle, but `eus` is replaced by `scus` in my [file tree](https://github.com/AutomationAdmin-Com/sic.mgmt/tree/feature/config/nonprd/hub) for the paths being monitored for changes.

   - Notice that the only way these workflows ran was if I changed a specific set of files in a specific directory and then opened a Pull Request to the `develop` branch.

1. So the way these worked is they would only run for changes to files under my `config/` directory and not any changes to `source/`. This is fine because if I wanted to run changes for a particular state file, I would just modify the appropriate `variables.tf` file in the appropriate directory and it would run the workflow.

1. In this example, the `_main.yml` that is called was my main terraform workflow that would copy the appropriately changed files and run your normal terraform init, plan, and apply with apply being only on a condition `github.ref_name == 'develop' && github.event_name == 'push'`. Here is the top part, file is too large to publish:

   ```yaml

   name: main_yml

   on:
   workflow_call:
      inputs:
         config_files_path:
         required: true
         type: string
         secrets_list:
         required: true
         type: string
         spoke_subscription_secret_name:
         required: true
         type: string
         hub_subscription_secret_name:
         required: true
         type: string
         secrets_akv:
         required: true
         type: string
         common_subfolder:
         required: true
         type: string
         workflow_path:
         required: true
         type: string
         actor:
         required: true
         type: string

      secrets:
         azure_cred:
         required: true
         ssh_key_github_actions:
         required: true

   permissions:
   contents: read

   jobs:
   terraform:
      name: "Terraform"
      runs-on: ubuntu-latest
      defaults:
         run:
         shell: bash

      steps:
         - name: "Echo Context"
         run: echo '${/{ toJSON(github) }}'

         - name: "Checkout Sprint Branch"
         uses: actions/checkout@v3

         - name: "Copy Files"
         run: |
            cd $GITHUB_WORKSPACE
            echo "Copying files"
            mkdir -p ./live
            cp ./${/{ inputs.config_files_path }}/* ./live/
            cp ./source/common/${/{ inputs.common_subfolder }}/* ./live/
            cp -R ./source/modules ./live/
            echo "File structure in root directory: "
            ls -l
            echo "File structure in terraform working directory: "
            ls -l ./live
   ```

   - Anyways, the main action I want to point out is the `Copy Files` action. Basically it would get the directory of the files that changed and copy them to a `./live` directory that it creates at run time.
   
   - It then copies the appropriate `stage` folder ( for example, [stage1](https://github.com/AutomationAdmin-Com/sic.mgmt/tree/feature/source/common/stage1) ) at runtime for the specific runtime `terraform.tfvars`, `backend.tf`, and `variables.tf` to be passed to them.

   - For example, in my prod hub subscription, if I wanted to deploy a Resource Group, I would simply modify config => prd => hub => east or scus => stage1 or stage2 => [variables.tf](https://github.com/AutomationAdmin-Com/sic.mgmt/blob/feature/config/prd/hub/scus/stage1/none/variables.tf). Then I would go down to stage1 or stage2 under source => common and call the appropriate modules or create the appropriate resources.

   - The idea behind common => stage1 is that you will deploy the same thing to all subscriptions eventually. So everything there must be `var.` for things to work unless you want something hard coded across all subscriptions, regions, environments, and possibly stages.

   - Anyhow, for the rest of the worklow you can see the version I use now in [main.yml](https://github.com/AutomationAdmin-Com/sic.template/blob/main/.github/workflows/main.yml).

1. Anyhow this workflow so far is fine and what I used for a long time until I stumbled upon this [Stack Overflow post about matrixes](https://stackoverflow.com/questions/73404735/execute-github-actions-workflow-job-in-directory-where-code-was-changed).
   - Now I knew these existed for a long time and read about them in [official docs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs), and I knew that we would one day figure out a way to use them to where we can "dynamically find files that changed" but I was not smart enough to figure it out.

   - Thankfully, the developer [theappnest](https://github.com/theappnest/terraform-monorepo-action/releases/tag/v2.3.1) created an action I could use. Again, I knew it would be a dynamic based on `git diff` or something, just couldn't figure it out but this guy did. 

1. So now I can just have a single workflow for each repo and not have to worry about the sometimes hundreds of files I used to create! Thank god! Working example is in [main.yml](https://github.com/AutomationAdmin-Com/sic.template/blob/main/.github/workflows/main.yml). Here is some screenshots showing how it can run multiple jobs in parrallel as expected:

   - ![3-subs](https://automationadmin.com/assets/images/uploads/2023/05/3-subs.png){:class="img-responsive"}

   - ![3-subs-2](https://automationadmin.com/assets/images/uploads/2023/05/3-subs-2.png){:class="img-responsive"}

1. I go over the main workflow in more detail [here](https://automationadmin.com/2023/10/terraform-workflow-repo-structure)