---
title: 'Terraform: Deploy Powershell Function App'
date: 2022-10-07T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/tf-deploy-ps-function-app
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
  - Azure-FunctionApps
---
<!--more-->

### Description:

In this post, I will build on my [previous post](https://automationadmin.com/2022/08/tf-get-next-subnet) where I created a Powershell Function App that will get the next CIDR Range for a VNET. In this post I will show how I deployed the function app in my tenant.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2022-10-07-tf-deploy-ps-function-app).
{: .notice--success}

### To Resolve:

1. First, I ran a plan and it said it would create [5 resources](https://github.com/gerryw1389/terraform-examples/actions/runs/3205584699).

   NOTE: This is a basic example so I did not include Log Analytics or anything I would normally do in an Enterprise Environment.
   {: .notice--success}

1. I then ran an apply and it build the Function App as intended. What I really want to talk about though is the trouble I went through while developing the solution...

1. So the first thing I did was create a Function App manually and used the [Code + Test](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal#test-the-function) blade of the Function App to build my Powershell app. This was not integrated with Github at the time. I did this until I got it working before uploading to my [public repo](https://github.com/gerryw1389/PS-FindNextCIDRRange).

   - This is where I ran into the issue I [posted about before](https://automationadmin.com/2022/10/ps-function-app-az-module-issue) with the Az module not loading. Fix is in that post.

2. Next, I searched the Terraform registry for [`function_app`](https://registry.terraform.io/providers/hashicorp/azurerm/3.0.0/docs/resources/function_app) (I like to explicitly use version 3.0.0 of the provider as seen in my [template](https://github.com/gerryw1389/terraform-examples/blob/main/_template/main.tf) - line 32) and found it. Cool, next I saw that the resource includes things like:

   - `scm_type` - So I can set this to `ExternalGit`
   - `source_control` block so that I can point to my Github public repo.

3. BUT, I didn't want to ignore the red box at the top saying it will be depreciated and I should use `azurerm_linux_function_app` or `azurerm_windows_function_app` instead. So eventually I found them and their associated `azurerm_app_service_source_control` resource and tried that.

   - This appeared to be on the correct path except I got this when deploying:

   ```escape
   Error: creating Source Control configuration for Web App: (Site Name "****" / Resource Group "****"): web.AppsClient#UpdateSourceControl: Failure responding to request: StatusCode=404 -- Original Error: autorest/azure: Service returned an error. Status=404 Code="NotFound" Message="Cannot find User with name ***." Details=[{"Message":"Cannot find User with name ***."},{"Code":"NotFound"},{"ErrorEntity":{"Code":"NotFound","ExtendedCode":"51004","Message":"Cannot find User with name ***.","MessageTemplate":"Cannot find {0} with name {1}.","Parameters":["User","***"]}}]
   ```

   - So I created yet another Function App in the GUI, but this time pointing to my Github repo and the wizard wanted me to LOGIN to my Github so that it could monitor git commits for Continuous Deployments. Well, I don't want that, I just want a copy of my Function App at a point in time, same today pointing to `main` branch's latest commit. 

   - I found that the fix is you don't enable continuous deployment and instead just deploy a blank Function App.

   - Then, you go to `Deployment Center` blade and there you can point to Github public repos with no need for any authentications.

1. So while troubleshooting I had done a few things regarding `integration` that I only caught in hindsight:

   - First, I had added this block to my `azurerm_windows_function_app` resource:

   ```terraform
   provisioner "local-exec" {
      command = join("", list("az functionapp deployment source config --ids ", azurerm_function_app.fa.id), " --repo-url https://github.com/gerryw1389/PS-FindNextCIDRRange", " --branch main --manual-integration")
   } 
   ```

   - But before running it, I had place the following block instead (based off some [search results](https://github.com/hashicorp/terraform-provider-azurerm/issues/1104)):

   ```terraform
   provisioner "local-exec" {
   command = <<EOH
      az login --service-principal -u ${var.client_id} -p ${var.client_secret} -t ${var.tenant_id}
      az account set --subscription ${var.subscription_id}
      az functionapp deployment source config --ids ${azurerm_function_app.fa.id} --repo-url https://github.com/gerryw1389/PS-FindNextCIDRRange --branch main --manual-integration
      EOH

   interpreter = ["PowerShell", "-Command"]
   }
   ```

   - But then before running, this got me thinking, what's up with this `--manual-integration` flag? I then went to the [docs](https://learn.microsoft.com/en-us/cli/azure/functionapp/deployment/source?view=azure-cli-latest#az-functionapp-deployment-source-config) and noticed that this turns off continuous deployment which is exactly what I'm looking for!

1. So at the end of the day what happened was I had written the `app_service_source_control` [resource](https://registry.terraform.io/providers/hashicorp/azurerm/3.0.0/docs/resources/app_service_source_control) like this:

   ```terraform
   resource "azurerm_app_service_source_control" "fa_sc" {
   app_id                 = azurerm_windows_function_app.fa.id
   repo_url               = "https://github.com/gerryw1389/PS-FindNextCIDRRange"
   branch                 = "main"
   }
   ```

   - and I should have like this because `use_manual_integration` defaults to `false`:

   ```terraform
   resource "azurerm_app_service_source_control" "fa_sc" {
   app_id                 = azurerm_windows_function_app.fa.id
   repo_url               = "https://github.com/gerryw1389/PS-FindNextCIDRRange"
   branch                 = "main"
   use_manual_integration = true
   }
   ```

1. This default setting of `false` makes sense because you typically want to follow Function App commits that you use for any updates and fixes. But sometimes you may just want to use something as it was at a specific point in time like I talked about in my previous post where you follow [based on specific git tags](https://automationadmin.com/2022/08/git-tagging) and only update by manually testing first *and then* bumping the version.