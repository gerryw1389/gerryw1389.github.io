---
title: 'Terraform: Get Next Subnet'
date: 2022-08-03T07:15:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tf-get-next-subnet
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

So let's say you are building a [subnet module](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet) and you want it to dynamically calculate the next available CIDR Range to fill in the required `address_range` attribute, how would you do this? Here is a post on a possible solution.

```terraform
resource "azurerm_subnet" "example" {
  name                 = "example-subnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"] # <== Where do we get this?
}
```


### To Resolve

1. So one possible solution is to have a `data` block that queries some kind of web app that can dynamically get the next CIDR range for a given subnet. Thankfully, this has [already been set up](https://github.com/gamullen/FindNextCIDRRange) (also see associated [blog post](https://techcommunity.microsoft.com/t5/azure-networking-blog/programmatically-find-next-available-cidr-for-subnet/ba-p/3266016) ).

1. After deploying the Function App above, the next step is to give the app `Reader` role to all subscriptions that you want it to be able to query Vnets for, probably the whole tenant.

1. So in your subnet module, you can make a data block call like:

   ```terraform
   data "external" "json" {
   program = ["sh", "-c", "curl -X GET -v -L -H 'Connection: close' 'https://{{pathToFunctionApp}}?subscriptionId={{subscriptionId}}&resourceGroupName={{resourceGroupName}}&virtualNetworkName={{virtualNetworkName}}&cidr={{cidr}}' "]
   }
   ```

   - Then in your subnet resource:

   ```terraform
   resource "azurerm_subnet" "example" {
   name                 = "example-subnet"
   resource_group_name  = azurerm_resource_group.example.name
   virtual_network_name = azurerm_virtual_network.example.name
   address_prefixes     = [data.external.json.result["proposedCIDR"]]
   }
   ```

3. But how to you handle when multiple calls to the subnet are made at the same time since Terraform evaluates all at once? For this one of my coworkers modified the function to have a `previous_address` parameter that you could pass the Function App and it would use that as a basis before generating a new subnet. Then when you called our custom subnet module you had to pass that attribute as another CIDR block.

4. Another limitation is this Function App will not work if you create a blank VNET with no default subnets like through Terraform. Not sure why the Azure Rest API even allows you to create a VNET with no subnets in the first place. But the fix is to manually in the UI go and create a default subnet like a /24 and then call the Function App.

5. Honestly, I'm a powershell/python guy myself so I would just rewrite this Function App using [python with http trigger](https://automationadmin.com/2020/11/azure-function-python-http-template) (also see my [other examples](https://automationadmin.com/tags/#azure-functionapps) ) to handle all this logic but I'm pretty busy these days :)

   - The requirments for this web app would be:
   - Required inputs: `subscription_id`, `vnet_resource_group`, `vnet_name`, `desired_cidr`
   - Optional inputs: `previous_cidr`
   - Logic: 

   ```
   If `previous_cidr` specified:
      Check if a default subnet exists (dont trust the user who called the module that they know what they are talking about )
         if true, continue
         if false, create it

      Next, Query the vnet for the next `desired_cidr` block after it

   Else:
      Check if a default subnet exists (dont trust the user who called the module that they know what they are talking about )
         if true, continue
         if false, create it

      Next, give me the next `desired_cidr` block available
   ```

6. Update: [Here](https://github.com/gerryw1389/PS-FindNextCIDRRange) is a link to this in powershell. Feel free to send a pull request for improvements as it's currently really messy but has been working so far in my testing.