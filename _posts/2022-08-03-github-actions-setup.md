---
title: Setup Github Actions For Terraform
date: 2022-08-03T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/github-actions-setup
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - CICD
---
<!--more-->

### Description:

Similar to my [Setup Azure Devops](https://automationadmin.com/2022/05/setup-azdo-terraform/) post, this post is how I connected to Azure via Github Actions instead of Azure Devops Pipelines. 

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2022-08-03-github-actions-setup).
{: .notice--success}

### To Resolve:

1. The first thing to do if you want to connect to Azure from Github is to store your Service Principle credentials in Githubs Repo encrypted:

   ```
   AZURE_CLIENT_ID
   AZURE_CLIENT_SECRET 
   AZURE_SUBSCRIPTION_ID
   AZURE_TENANT_ID
   ```

2. Next, in your repo, you will create a `.github` folder and a `workflows` subfolder. Then you can create as many `*.yml` files as you want and these will be the same as your `azure-pipelines.yaml` you may be used to if you are coming from AzDo. For now, while I'm still new at Terraform, I will continue to separate my [builds](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-08-03-github-actions-setup/build.yaml) and my [releases](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-08-03-github-actions-setup/release.yaml) in seperate files so I created the seperate.

3. OK, so first thing to do is to turn of Continous Integration for now so that we can only run these pipelines from the UI. We will turn it back on later once we have everything working as intended. For that, you will use the [on](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on) keyword with the [workflow-dispatcher](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow) flow.

1. Next, you will use the [Terraform Github Action](https://github.com/hashicorp/setup-terraform) by Hashicorp to use the Terraform CLI in your pipeline to deploy to Azure as normal.

1. Since we are using the ubuntu build agents and forcing the use of Bash, I like to add a `|` for all `run` commands and then write multiline scripts. For example:

   ```yaml
   - name: Terraform Plan
      id: plan
      run: |
         cd ./2022-08-03-github-actions-setup
         terraform plan \
         -var="subscription_id=$ARM_SUBSCRIPTION_ID" \
         -var="tenant_id=$ARM_TENANT_ID" \
         -var="client_id=$ARM_CLIENT_ID" \
         -var="client_secret=$ARM_CLIENT_SECRET" \
         -out "tf.plan"
      continue-on-error: false
   ```

   - So the first line `cd ./2022-08-03-github-actions-setup` has a line break and the yaml will accept that because of `run: |` which is a [literal block scalar](https://yaml-multiline.info/) (see 'keep newlines' in Block Scalar Style) in yaml.

   - But the next line that starts our long `terraform plan \` uses a [line continuation](https://www.gnu.org/software/bash/manual/bash.html#Escape-Character) character that bash uses which will put all the following lines as spaces.

   - A few lines above is where we are forcing the build agent to use bash even if it is a windows machine:

   ```yaml
   defaults:
      run:
         shell: bash
   ```

1. Anyways, running our build we can see that it successfully connect to Azure and runs a plan.

   - One thing I noticed different between how I have Azure Devops working and Github Actions is that I'm no longer passing the storage account's Access Key as a var [like I was before](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-02-tf-no-service-connection/build.yaml) (see line 38).

   - I'm not sure why I was passing that before but I think it had to do with Terraforms [backend](https://www.terraform.io/language/settings/backends/azurerm) provider and maybe the version of Terraform CLI I was using with Azure Devops? See `When authenticating using the Access Key associated with the Storage Account:` at the previous link. I think now we are just connecting as a Service Principle.

   - Looking into this more, I found [this post](https://www.schaeflein.net/understanding-azure-storage-data-access-permissions/) which says that since I'm authenticating as `Owner` as my Service Principle, I can `list keys` which will then get me access to blobs on the storage account. See [here](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access?tabs=portal) where it says:

   ```
   However, if a user has been assigned a role with Microsoft.Storage/storageAccounts/listKeys/action permissions, then the user can use the portal with the storage account keys, via Shared Key authorization. To use the storage account keys, Shared Key access must be permitted for the storage account. For more information on permitting or disallowing Shared Key access, see Prevent Shared Key authorization for an Azure Storage account.
   ```

   - So I think this means that setting `Allow storage account key access` under `Configuration` of the Storage Account, then I would need to give my Service Principle [Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role in order to read/write blobs using the Azure RBAC route instead of Shared Key. 

   - Putting this together means that currently Github Actions is using my Service Principle to store the state file in blob storage using Shared Key authorization.

1. Another thing about Github Actions is that since the `.github/workflows` folders are at the root of the repo, I have it setup to where I will `cd` to the correct folder in my steps ( [see lines 33 and 44](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2022-08-03-github-actions-setup/build.yaml) ) and then create a pipeline [for each blog post](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/) to share about.