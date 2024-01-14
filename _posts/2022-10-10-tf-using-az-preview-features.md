---
title: 'Terraform: Using AzPreview Features'
date: 2022-10-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/tf-using-az-preview-features
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

Follow this post to use features not yet available in Terraform but are available at the AzureRM level.

### To Resolve:

1. In my organization, the flowchart for Terraform development happens in this order:

   - Microsoft releases a new [AzureRM API](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) endpoint for new/existing resources.
   - Hashicorp Terraform developers write [Go lang wrappers](https://github.com/hashicorp/terraform) around the new API.
   - They release a new version of the [AzureRM provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest) to Terraform Registry.
   - We then consume that version in our modules/infrastructure compositions and provide options for our developers to deploy resource in Azure following **our custom business rules**.

1. So what happens is sometimes we need to use a feature that is available at the AzureRM level but is not yet provided via Terraform.

   - An example is the [`public_network_access_enabled`](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account#public_network_access_enabled) attribute that is now available in the latest version of the AzureRM provider but [was not enabled recently](https://automationadmin.com/2022/09/disable-public-access-to-pep). See [here for v3.20.0 for example](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/storage_account). Of course this makes sense, newer versions of the AzureRM provider will expose new settings.

1. How would you use this setting "ahead of time" so to speak you may wonder? The answer is to use the provider [AzApi](https://registry.terraform.io/providers/Azure/azapi/latest/docs).

   - For example, you can see in [this issue](https://github.com/hashicorp/terraform-provider-azurerm/issues/16335) that users were able to use the provider like so:

   ```
   resource "azapi_update_resource" "example" {
   type        = "Microsoft.Storage/storageAccounts@2021-09-01"
   resource_id = azurerm_storage_account.example.id

   body = jsonencode({
      properties = {
         publicNetworkAccess = "Disabled"
      }
   })
   }
   ```

1. I haven't personally tested this but that is the general idea if you want to accomplish something available at the API level but not yet available by the AzureRM provider.

1. In researching how the Azure RM Rest provider works, I found some interesting documents about it, feel free to read through:

   - [Main document of how Resource Manager works](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
   - [Rest API](https://learn.microsoft.com/en-us/azure/governance/resource-graph/first-query-rest-api)
   - [AzCLI uses Rest API under the hood](https://stackoverflow.com/questions/49291889/does-the-azure-cli-use-the-azure-rest-api)
   - [Getting started](https://learn.microsoft.com/en-us/rest/api/azure/)
   - [There are differences between Rest API and commands though](https://github.com/Azure/azure-cli/issues/7944)
   - [Another example of differences](https://learn.microsoft.com/en-us/answers/questions/730116/is-it-right-that-az-cli-command39s-result-is-diffe.html)
   - [AzCLI Rest](https://learn.microsoft.com/en-us/cli/azure/use-cli-effectively?tabs=bash%2Cbash2#rest-api-commands-az-rest)
   - [powershell](https://devblogs.microsoft.com/scripting/using-the-windows-azure-rest-apis-with-powershell/)

1. Main takeaway from all the links:

   - When Microsoft develops features on Azure, they expose these features as AzureRM Rest API Endpoints.
   - You can use Powershell, Az Cli, or the Portal (or SDKs and other tools I'm sure) to call these endpoints in a specific order to get a desired result.
   - The key takeaway is that there isn't a one-to-one mapping between all these tools and the rest endpoints. A single cmdlet like `Get-AzStorageAccount` may call multiple [Rest API endpoints](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts) under the hood.
   - But at the end of the day, all these tools will rely only on data types that can be sent and retrieved to a Rest Endpoint. You cannot perform an operation anywhere in Azure that doesn't use an endpoint. The key is to look at the `API Version` and to read the docs to see what payloads and responses are available for that version to know what is possible in Azure.

1. For example, [storage account create version 2022-05-01 will have these features](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts/create?tabs=HTTP)
   - The URI params will require multiple strings
   - The Request Body will require multiple properties being passed.
   - The response object received back will be of type [Storage Account](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts/create?tabs=HTTP#storageaccount) which has its own properties like `id`, `kind`, etc.
   - Try switching between the different code sets in the [example](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts/create?tabs=HTTP#storageaccountcreate). Does it make sense now that you can interact with Azure in multiple different ways but they all translate to a Rest API operation in the background? This was incredibly insightful when I first found this out.
