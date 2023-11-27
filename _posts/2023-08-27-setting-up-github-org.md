---
title: My Setup Of Github Organization
date: 2023-08-27T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/08/setting-up-github-org
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

So I decided in order to best showcase Github, it would make sense to create an organization and set a few things up. Here is my docs on it:

### To Resolve:

1. First, I registered the org ["AutomatonAdmin-Com"](https://github.com/AutomationAdmin-Com) because why not?

1. Next, I created a [module repo](https://automationadmin.com/2022/08/calling-remote-modules) called [`module.rg`](https://github.com/AutomationAdmin-Com/module.rg) that I will test calling from another repo soon.

1. Next, I created a module composition, which I call a "sic" as in "Shared Infrastructure Composition", called [`sic.mgmt`](https://github.com/AutomationAdmin-Com/sic.mgmt). The "mgmt" stands for management as in it should configure management groups and subscriptions. I cover these in later posts but for example subscriptions post can be found [here](https://automationadmin.com/2023/11/create-tf-subscriptions-payg).

   - This repo will have many posts covering what it is and why I created it so I will leave that for them, but for now, let's focus on calling our module.

1. In order to call our module from the sic.mgmt repo using Github Actions, we have two main methods that I have tested and written posts on:

   - We can [use Deploy Keys](https://automationadmin.com/2023/10/using-deploy-keys-for-multiple-tf-module-repos)
   - We can [use a Repo Bot Github App](https://automationadmin.com/2023/07/create-repo-bot-for-tf-modules)

1. I went with the Repo bot and I suspect most people will so that as the number of module repos grow, you only have to install the app to new repos and not generate multiple keys.

1. In the interest of explaining all the actions taken, I wanted to also explain the process for creating a new repo, we will  use [sic.template]() as an example because it is my main template repo at this time:

   - First, you do the normal create repo in the Github using the UI or you can do everything through REST API or using Github CLI, but I just create the repo in the UI with a README.md

   - Next, pull it to your machine like usual:
   
   ```shell
   cd to dir
   git clone https://

   #make change
   git add .
   git commit -m 'update'
   git push origin main
   # fill out github popup

   #create feature branch

   #copy files over
   ```

1. Next, go to Azure => Entra ID => App Registrations => Your Terraform Service Principal => Federated Credentials => Add [oidc auth](https://automationadmin.com/2023/08/setting-oidc-auth) credentials

1. Inside repo, create Prod environment and add the 4 secrets needed: `sub_id`, `tenant_id`, `client_id` and `repo_bot pem`

1. Next, in Azure, I created a Key Vault called `aa-prd-scus-hub-akv-v1` in my `prd-hub` subscription that I will use to pull other secrets at run time:

   - I add my user as `Key Vault Administrator`
   - I added my TF Service Principal as `Key Vault Secrets User`

   - I then added all my possible secrets to the AKV:

   ```escape
   prd-storage-account-access-key
   nonprd-storage-account-access-key
   spn-tenant-id
   spn-client-id
   nonprd-hub-id
   prd-hub-id
   nonprd-spoke-id
   prd-spoke-id
   ```

   - My environment is not built out yet completely, but you should absolutely have separate AKVs, Storage Accounts, Subscriptions, and everything really between non-prod and prod environments. I just have prod for now since this is just an example tenant for my blog.

   - Anyways, the last step is to set to `whitelist` in [networking for the AKV](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security#key-vault-firewall-enabled-ipv4-addresses-and-ranges---static-ips) to ensure that people on the internet cannot try to access my secrets!

1. Lastly, I just add my files to my feature branch which will [parse files that changed](https://automationadmin.com/2023/05/main-terraform-workflow) and then call the secrets from my Key Vault [at run time](https://automationadmin.com/2023/11/using-akv-to-get-secrets) which is the main goal!


