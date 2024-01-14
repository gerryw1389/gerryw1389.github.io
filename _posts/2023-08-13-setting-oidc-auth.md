---
title: Setting Up OIDC Auth For Azure Login and Terraform
date: 2023-08-13T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/08/setting-oidc-auth
tags:
  - Github
  - Azure
  - Terraform
---
<!--more-->

### Description

So almost every example you will see online for connecting to Azure or Terraform is to use a Service Principal. I have shown this a couple times, but [here](https://automationadmin.com/2022/05/setup-azdo-terraform/) is one I point people to often. Anways, there appears to be multiple ways you can authenticate with Azure/Terraform and I want to go through what I did to setup OIDC Auth.

### To Resolve:

1. First, let's tackle [azure login](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L91) because that is straight forward:

   - Basically, they list the ways to [connect via OIDC auth](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure?tabs=azure-portal%2Cwindows) but to summarize:
   - Create a Service Principal
   - Navigate to it in Azure AD
   - Go to "Federated Credentials" blade
   - Click `Add`
   - For organization, choose your org: `AutomationAdmin-Com` in my case
   - For repo, choose your repo: `sic.template` in my case
   - For Entity type, you have a few options like `Environment, branch, PR, Tag`, I always choose `Environment`
   - For Github Name you have to specify from the previous selection the selector. For example, environement has to match the Github Environment you will deploy from in your workflow, branch has to match a branch, etc. I chose `production` which I will show you shortly.
   - For name, you just give a unique name for the credential: I chose `sic-template-env-prod`.

1. Next, inside my [sic.template](https://github.com/AutomationAdmin-Com/sic.template) repo, I added these 3 required secrets for the action:  `${/{ secrets.CLIENT_ID }}`, `${/{ secrets.TENANT_ID }}`, and `${/{ secrets.SUB_ID }}` where SUB_ID is just one of my Azure Subscriptions `id` property, it doesn't matter which one.

   - NOTE: [Jekyll Liquid Filters](https://jekyllrb.com/docs/liquid/filters/) clash with [Github Variables](https://docs.github.com/en/actions/learn-github-actions/variables#using-contexts-to-access-variable-values) so replace all instances of `${/{` by removing the forward slash :)

1. Next, in my Github Actions workflow, I had to enable 2 things:
   - First, I had to set `id-token: write` [permission](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L15)
   - Next, I had to set environment to [`production`](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L47) even though my deployments won't always target production as seen in my [main template post](https://automationadmin.com/2023/05/main-terraform-workflow) ( or [part 2](https://automationadmin.com/2023/10/terraform-workflow-repo-structure) ).

1. OK, so we can now get past Azure Login as seen in the logs from a most recent run:

   ```escape
   Run azure/login@v1
   Using OIDC authentication...
   Federated token details: 
   issuer - https://token.actions.githubusercontent.com 
   subject claim - repo:AutomationAdmin-Com/sic.template:environment:production
   /usr/bin/az cloud set -n azurecloud
   Done setting cloud: "azurecloud"
   Login successful.
   ```

1. Next, we need to set Terraform to know about OIDC Auth. Thankfully, [this is documented well](https://registry.terraform.io/providers/hashicorp/azurerm/3.80.0/docs/guides/service_principal_oidc) in the provider docs. To summarize:

   - Remove any passing of `client_secret` as a secret to terraform and remove the variable altogether from `variables.tf` or any other place.
   - Next, in your providers, just replace that reference with `use_oidc = true` everywhere you would have used client_secret. That's it!
   - You can verify by going to any of my [`backend.tf` files](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/config/nonprd/hub/scus/stage1/none/backend.tf#L39C3-L39C36)

1. What I haven't tested yet is verifying the providers that get built get passed correctly but I know terraform doesn't error so I assume the providers build correctly. Will need to remember to update this later once I test!