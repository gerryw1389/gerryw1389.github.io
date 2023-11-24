---
title: Create Terraform Service Principle
date: 2021-10-04T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/10/create-terra-az-ad-app
tags:
  - Azure
---
<!--more-->

### Description

Before using Terraform to create resources in Azure, you need to first create an Azure AD Application and give it rights to your subscription to deploy resources. Here are the steps to follow. It is recommended to follow the [official](https://docs.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-powershell?tabs=bash) source as well, but this is just my notes on what I did.

### To Resolve:

1. Create the application as a service principle:

   ```powershell
   $password = 'somePassword'
   $securePassword = ConvertTo-SecureString -Force -AsPlainText -String $password
   $azTerraformapp = New-AzADApplication -DisplayName 'az-terraform' -HomePage 'http://az-terraform' -IdentifierUris 'http://az-terraform' -Password $securePassword
   New-AzADServicePrincipal -ApplicationId $azTerraformapp.ApplicationId.Guid -SkipAssignment
   ```

1. Grab the client ID from output

   ```escape
   app id
   bb581ce9-xxx
   ```

2. Get object id:

   ```powershell
   (Get-AzADApplication -ApplicationId "bb581ce9-xxx").ObjectId
   ae9f0a7a-xxx
   ```

3. Get the client secret

   ```powershell
   $SecureStringPassword = ConvertTo-SecureString -String "someSecret" -AsPlainText -Force
   New-AzADAppCredential -ObjectId "ae9f0a7a-xxx" -Password $SecureStringPassword
   ```

4. Get your tenant info

   ```powershell
   (Get-AzSubscription).TenantId
   b525d9fd-xxx

   subscription-id
   (Get-AzSubscription).Id
   700b8c1a-xxx
   ```

5. Assign them to the bashrc profile for later deployments from cloudshell:

   ```shell
   vi ~/.bashrc
   # add the following
   export TF_VAR_ARM_SUBSCRIPTION_ID="700b8c1a-xxx"
   export TF_VAR_ARM_TENANT_ID="b525d9fd-xxx"
   export TF_VAR_ARM_CLIENT_ID="bb581ce9-xxx"
   export TF_VAR_ARM_CLIENT_SECRET="someSecret"
   ```

6. Assign the service principle contributor at subscription level.

   - IAM blade, add `contributor` role for the Service Principle.

7. In preparation for modifying `.tf` files, inside VSCode, install the two following extensions:

   ```powershell
   code --install-extension 4ops.terraform
   code --install-extension hashicorp.terraform
   ```

8. Feel free to try this using Bash instead of Powershell by following the above article. I switch between the two for now.