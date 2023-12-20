---
title: Using Deploy Keys For Multiple TF Module Private Repos
date: 2023-10-08T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/10/using-deploy-keys-for-multiple-tf-module-repos
tags:
  - Github
  - Terraform
---
<!--more-->

### Description:

In Gihub Actions, you have two main ways you can call multiple Terraform Module private repos at run time, I have only documented and tested two ways:

   - Using Deploy Keys (this post)
   - Using a Github App as documented [here](https://automationadmin.com/2023/07/create-repo-bot-for-tf-modules)

Here I will show you how I used Deploy Keys for multiple TF Module repos.

### To Resolve:

1. Create [your module repo](https://github.com/AutomationAdmin-Com/module.rg) and reference it like: `git::ssh://git@github.com/AutomationAdmin-Com/module.rg.git?ref=v0.0.1` from your calling repo.

   - Pay special attention to the `/` after `github.com` which is different from the ssh address you will get if you navigate to the repo and copy the `ssh clone` command.
   - See [tf source](https://developer.hashicorp.com/terraform/language/modules/sources#generic-git-repository) for reference.

1. Next, we need to generate a SSH key pair and use that for the Github Agent to pull from whichever repos it needs. See [here](https://breadnet.co.uk/terraform-init-on-github-actions-with-private-modules/?mtm_campaign=github&mtm_kwd=terraform-actions-33) for the guide I followed: `ssh-keygen -t ed25519`

1. Next, take the public portion and upload it under AutomationAdmin-Com/module.rg => Settings => Security/Deploy Keys => +Add => Insert here with name `githubactions-terraform`

1. Next, take the private portion and upload it as a secret under AutomationAdmin-Com/sic.mgmt => Settings => Security/Secrets and Variables/Actions => +New Repository Secret => `SSH_KEY_GITHUB_ACTIONS`
   - Copy the full multi line private key into the secret.

1. Lastly, you just need the public runner to be able to access those repos so you add this before the terraform init step:

   ```yaml
   -   name: 'Setup SSH Keys and known_hosts'
         env:
            SSH_AUTH_SOCK: /tmp/ssh_agent.sock
         run: |
            ssh-agent -a $SSH_AUTH_SOCK > /dev/null
            ssh-add - <<< "${/{ secrets.SSH_KEY_GITHUB_ACTIONS }}"

   - name: "Terraform Init"
      id: init
      run: |
         cd $GITHUB_WORKSPACE/live
         terraform init -backend-config="access_key=${/{ steps.azure-keyvault-secrets.outputs.tfstateaccesskey }}"
      env:
         SSH_AUTH_SOCK: /tmp/ssh_agent.sock

   ```

   - I found this method works by following [this blog post](https://www.webfactory.de/blog/use-ssh-key-for-private-repositories-in-github-actions) step-by-step. Thanks!

1. There is one glaring issue with this though, what if you have **multiple** tf modules? It doesn't work, both Github Actions and Terraform don't know how to handle multiple SSH Keys if you just blindly add multiple SSH keys as secrets and try to keep adding them using the `ssh-add` like above.

   - Github [docs clearly say one key per repo](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#cons-of-deploy-keys)
   - Terraform just uses `git clone`, but with all addresses like `git::ssh://git@github.com` it won't know how to distinguish different repos with the same host name, even if the repo name is different.

1. Thankfully, I found the fix for this! It makes sense in hindsight but anyways, it's to setup and configure a SSH Config file on the public runner at run time and then reference your repos by different names. Here is an example config (NOTE: This assumes you have two modules, one for RG and one for CosmosDB and have uploaded their private keys as secrets to the repo) :

      ```yaml
      - name: "Setup SSH Keys and known_hosts"
         run: |
            cd $GITHUB_WORKSPACE
            chmod +x ./.github/scripts/update_ssh_agent.sh
            ./.github/scripts/update_ssh_agent.sh
         env:
            SSH_AUTH_SOCK: /tmp/ssh_agent.sock
            SSH_KEY_MODULE_RG: ${/{ secrets.ssh_key_module_rg }}
            SSH_KEY_MODULE_COSMOSDB: ${/{ secrets.ssh_key_module_cosmosdb }}
      ```

   - NOTE: [Jekyll Liquid Filters](https://jekyllrb.com/docs/liquid/filters/) clash with [Github Variables](https://docs.github.com/en/actions/learn-github-actions/variables#using-contexts-to-access-variable-values) so replace all instances of `${/{` by removing the forward slash :)

   - Here is the script:

      ```shell
      #!/bin/bash

      set -eu


      ssh-agent -a $SSH_AUTH_SOCK > /dev/null
      mkdir -p ~/.ssh
      touch ~/.ssh/config
      touch ~/.ssh/known_hosts
      ssh-keyscan github.com >> known_hosts

      # Create key files from Repo Secrets:
      echo "$SSH_KEY_MODULE_RG" > ~/.ssh/module_rg
      echo "$SSH_KEY_MODULE_COSMOSDB" > ~/.ssh/module_cosmosdb

      # Set perms on each:
      chmod 600 ~/.ssh/module_rg ~/.ssh/module_cosmosdb ~/.ssh/known_hosts

      # For each module, update SSH Config:
      echo "Host module-rg" >> ~/.ssh/config
      echo "  Hostname github.com" >> ~/.ssh/config
      echo "  IdentityFile=~/.ssh/module_rg" >> ~/.ssh/config
      echo "Host module-cosmosdb" >> ~/.ssh/config
      echo "  Hostname github.com" >> ~/.ssh/config
      echo "  IdentityFile=~/.ssh/module_cosmosdb" >> ~/.ssh/config

      # Add private key files to ssh-agent
      ssh-add ~/.ssh/module_rg
      ssh-add ~/.ssh/module_cosmosdb

      # Output to console in case of issues:
      cat ~/.ssh/config
      ```

      - You can test this is working by adding a few clone commands after it in the same script or a different one:

      ```shell
      echo "cloning..."
      GIT_SSH_COMMAND="ssh -vv" git clone git@module-rg:AutomationAdmin-Com/module.rg.git
      sleep 3
      echo "cloning second..."
      git clone git@module-cosmosdb:AutomationAdmin-Com/module.cosmosdb.git
      ```

1. Lastly, you have go to each `source` in your terraform code and update them to match the module you are calling:

   ```terraform
   module "cosmosdb_rg" {
   source              = "git@module-rg:AutomationAdmin-Com/module.rg.git?ref=v0.0.1"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-${var.sub_abbr}-${var.stage}-${var.color}-ga-rg"
   location            = var.region
   tags                = local.tags
   }


   module "cosmosdb_rg_2" {
   source              = "git@module-cosmosdb:AutomationAdmin-Com/module.cosmosdb.git?ref=sprint"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-${var.sub_abbr}-${var.stage}-${var.color}-ga-rg-2"
   location            = var.region
   tags                = local.tags
   }

   module "cosmosdb_rg_3" {
   source              = "git@module-cosmosdb:AutomationAdmin-Com/module.cosmosdb.git?ref=v0.0.2"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-${var.sub_abbr}-${var.stage}-${var.color}-ga-rg-3"
   location            = var.region
   tags                = local.tags
   }

   module "cosmosdb_rg_4" {
   source              = "git@module-rg:AutomationAdmin-Com/module.rg.git?ref=main"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-${var.sub_abbr}-${var.stage}-${var.color}-ga-rg-4"
   location            = var.region
   tags                = local.tags
   }
   ```

   - See the `git@module-rg`? See how that maches the SSH Config file identity hostname section from earlier? That's how it works.

1. So using this method, you can upload one, two, or twenty private keys to each calling repo's secrets and then build a complex ssh config file at run time. You then need to update all your Terraform `source` calls to match whatever name you give the host in that file.

1. As you can see this is clunky and might work if your org doesn't allow Github Apps, but going the [Github App route](https://automationadmin.com/2023/07/create-repo-bot-for-tf-modules) is much simpler in my opinion. It allows you to reference all module calls the same.
