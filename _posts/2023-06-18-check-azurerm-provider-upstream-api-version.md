---
title: Check AzureRM Provider Upstream API Version
date: 2023-06-18T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/06/check-azurerm-provider-upstream-api-version
tags:
  - Azure
  - Terraform
  - Azure-APIM
  - RestAPI
---
<!--more-->

### Description

I once got an email like : `Breaking Change Notice: Update your API Management API version to 2021-08-01 or later by 30 Sept` . This was odd because our APIM instance was deployed with Terraform pretty recently so it was odd to get this email, here is what I did to track it down:

### Steps

1. First, like my [feature not available post](https://automationadmin.com/2023/01/tf-feature-not-available), I tracked down the version of API that my version of Terraform was using by following :

   - Our version of AzureRM for APIM is currently `3.20.0` which can be found [here](https://github.com/hashicorp/terraform-provider-azurerm/tree/v3.20.0)

   - By going to ./internal/services/apimanagement, we then go to the resource we use which is `azurerm_api_management` and can be found [here](https://github.com/hashicorp/terraform-provider-azurerm/blob/v3.20.0/internal/services/apimanagement/api_management_resource.go)

   - Next, we find the version of the Azure SDK they are using by looking at the `import` line which is `github.com/Azure/azure-sdk-for-go/services/apimanagement/mgmt/2021-08-01/apimanagement`

   - Next, we find the cooresponding Azure SDK version by referencing ./vendor/modules.txt found [here](https://github.com/hashicorp/terraform-provider-azurerm/blob/v3.20.0/vendor/modules.txt) by searching `2021-08-01/apimanagement` and see it points to `github.com/Azure/azure-sdk-for-go v65.0.0+incompatible`

   - Next, we go to [this](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go@v65.0.0+incompatible) site.

   - Next you just scroll down to Directories and expand Services and search for "apimanagement" and click on `latest/apimanagement/mgmt/apimanagement`. On this page, click on the `imports` at the top and it will take you to a page with a link that says: Imports in module "github.com/Azure/azure-sdk-for-go" => github.com/Azure/azure-sdk-for-go/services/apimanagement/mgmt/2021-08-01/apimanagement

   - This finally lands you at a page that says "Package apimanagement implements the Azure ARM Apimanagement service API version 2021-08-01."

1. So we are already on the version it wants us to update to, what gives? Next, I repeated the process for the latest version of the AzureRM provider and found it's still using the same version of the API.

1. So next we go to Azure's Rest API repo and look at where they publish APIs and see what the latest version is: [2022-08-01](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2022-08-01)

1. This means that we would need to use the [AzAPI provider](https://registry.terraform.io/providers/Azure/azapi/latest/docs) to access any functions needed until the AzureRM developers catch up.

1. Anways, back to the email. If we are already on that version or were at that version when we deployed, why send this email? It turns out you just need to go into Azure and read the "Recommendation":

   - If you click on the `Remediation Steps` for the alert, it tells you exactly what needs to happen:

   ```escape
   To set the minimum API version of your API Management instance:
   1. In the Azure portal, find your API Management Resource
   2. Navigate to the Management API blade
   3. Select Management API settings
   4. Under Prevent users with read-only permissions from accessing service secrets, select 'Yes'
   5. Select 'Save.'
   ```

1. The problem when I do this in APIM in my test tenant, it fills in `2022-08-01` as the latest version [which is correct](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable) , but that would mean we couldn't use Terraform to manage the instance because our provider only allows up to `2021-08-01` so this is a no go!

1. What I need to do is set the [min_api_version](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/api_management#min_api_version) to `2021-08-01` inside Terraform but this will most likely break other deployments into the service from developers - oh well!