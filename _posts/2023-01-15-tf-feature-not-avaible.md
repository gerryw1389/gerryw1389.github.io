---
title: 'What To Do When No Feature Avail For Terraform'
date: 2023-01-15T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/tf-feature-not-available
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

When using Terraform with AzureRM, in general, you have 3 options when a feature isn't available and you need to complete a task:

### To Resolve:

1. You can try to use [AzAPI](https://registry.terraform.io/providers/Azure/azapi/latest/docs) provider to make calls to the appropriate Azure API endpoint. See links below for examples.

1. You can deploy the resource in the portal, then [get its template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal) and try to replicate with [`azurerm_template_deployment`](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/template_deployment).

   - As I get better and better with Terraform, I find myself doing this alot. Basically you reverse engineer.

2. You can use the [`null resource`](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource) to run a powershell command during terraform apply:

   ```
   resource "null_resource" "assign_retention" {
   provisioner "local-exec" {
      command     = <<EOH
      az login --service-principal -u ${var.client_id} -p ${var.client_secret} -t ${var.tenant_id}
      #az account set --subscription ${var.subscription_id}
      az version
      az account set --subscription  guid
      az monitor log-analytics workspace table update --subscription  guid --resource-group my-rg --workspace-name my-law --name Alert --retention-time 30
      EOH
      interpreter = ["PowerShell", "-Command"]
   }
   triggers = {
      always_run = timestamp()
   }
   }
   ```

   - Not sure how this works if you run this on linux build agent since it's using `powershell`. Might have to run bash instead.

   - Another problem is the `always_run = timestamp()` trigger which means for every pipeline run you will have to wait for this to complete even if it has already been set.

   - You could also run these in the pipeline and then [switch based on OS of the build agent](https://learn.microsoft.com/en-us/azure/devops/pipelines/scripts/cross-platform-scripting?view=azure-devops&tabs=yaml#switch-based-on-platform)

   - This method is least preferred because even though you may get the desired result, it is not officially "IaC". Ideally you would want terraform to manage the state of a resource so these should not be used.

3. Check the bicep documentation for the resource, for example here is for [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code?tabs=bicep#function-app)

   - Even go one level deeper and check the api version => [Microsoft.Web/sites@2022-03-01](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/2022-03-01/sites?pivots=deployment-language-bicep)
   - Just use this as a guidence though because you will have to first jump down the rabbit hole to see what version your provider is using under the hood. Since we [pin to versions](https://automationadmin.com/2022/08/git-tagging), this means we are rarely targeting the latest endpoint available.
   - For example, for AzureRM version 3.22, if you go to the [function app resource](https://github.com/hashicorp/terraform-provider-azurerm/blob/v3.22.0/internal/services/web/function_app_resource.go) it appears to be using `github.com/Azure/azure-sdk-for-go/services/web/mgmt/2021-02-01/web`. But I want to see what version of the azure-sdk-for-go they are using when they call that endpoint.
   - Thankfully I have found to see which version of the go provider they use in [modules.txt](https://github.com/hashicorp/terraform-provider-azurerm/blob/v3.22.0/vendor/modules.txt) which says [v66.0.0](https://github.com/Azure/azure-sdk-for-go/tree/v66.0.0/services/web/mgmt/2021-02-01/web) but I don't know what I'm looking at by that point. So I searched `azure-sdk-for-go docs` or you can click on the `SDK Reference` in the root README of that repo and it brings you to `https://pkg.go.dev/github.com/Azure/azure-sdk-for-go@v66.0.0+incompatible`. Next you just scroll down to `Directories` and expand `Services` and search for `web/mgmt/2021-03-01/web`
   - [Here](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go@v66.0.0+incompatible/services/web/mgmt/2021-03-01/web) is the docs link for Go developers to reference. It says `Package web implements the Azure ARM Web service API version 2021-02-01.` right at the top. So now we go back to our first link and hit the drop down and select [that version](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/2021-02-01/sites?pivots=deployment-language-terraform). We did it!