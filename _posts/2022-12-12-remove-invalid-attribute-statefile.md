---
title: 'Terraform: Remove Invalid Attribute From Statefile'
date: 2022-12-12T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/12/remove-invalid-attribute-statefile
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

In this post, I will cover something I recently found out where I had removed an invalid attribute for a resource in a statefile as part of my [terraform upgrades](https://automationadmin.com/2022/12/tf-version-upgrades). So let's say I have a storage account I'm trying to upgrade and it is giving me issues. I can download the statefile and then run `terraform state show 'module.myStorage.azurerm_storage_account.storage'` and I get: 

```escape
unsupported attribute "allow_blob_public_access"
# module.myStorage.azurerm_storage_account.storage:
resource "azurerm_storage_account" "storage" {
```

If I go in the line in the statefile and delete the line `"allow_blob_public_access": false,` under the resource and re-run that command I then get a full valid json output. Initially this came up because I was trying to upgrade a storage account from an old version of a module to a newer version but instead of updating in-place like I expected, it kept saying that `storage account blah has been deleted` and then `storage account blah will be created` in the terraform plan. I don't get it, in that same plan it reads in the storage account with the exact ID of the resource in Azure...

NOTE: This should almost never be used as I don't know the full implications but messing with the statefile is usually not the right answer. You have been warned!
{: .notice--danger}

### To Resolve:

1. Anyways, here are the steps to remove an attribute in your statefile if that even fixes anything:

   - TLDR

   ```
   # download statefile, cd to dir
   terraform state pull | sc 1.json
   # open 1.json, delete your attribute from your resource, increment the serial at the top by 1, save and exit
   terraform state push 1.json
   # rename to terraform.tfstate
   # upload back to storage account
   ```

2. First, download your statefile from your storage account

3. Next, open powershell and cd to the directory and do a `terraform state pull | sc 1.json`

   - NOTE that you cannot do `terraform state pull > state.json` on Windows like you see in many examples because Windows will [set the BOM incorrectly](https://github.com/hashicorp/terraform/issues/24986) and you will have issues reimporting the state.

   - Example:

   ```powershell
   PS > terraform state pull > state.json
   PS > terraform state push state.json
   Error reading source state "state.json": 2 problems:

   - Unsupported state file format: The state file could not be parsed as JSON: syntax error at byte offset 1.
   - Unsupported state file format: The state file does not have a "version" attribute, which is required to identify the format version.
   ```

   - But using `Set-Content` works fine on Windows

   ```powershell
   PS > terraform state pull | sc 1.json
   PS > terraform state push 1.json
   ```

4. Anyways, now that we have `1.json`, we can do a Ctrl+F for our `module.myStorage` and find the one of type `Microsoft.StorageAccounts` or whatever the type name is, and then delete the offending attribute. In our case it was `"allow_blob_public_access": false,` .

5. Next, at the top of the statefile you need to increment the `serial` attribute by one: (ex "serial": 21, -> "serial": 22,)

6. Now save and exit your json file. Next you will push it back: `terraform state push 1.json`

1. Now just rename the file to `whatever.tfstate` or in my case, many blobs in azure have no extensions, so just rename to `tfstate` or whatever and then upload back. What I like to do is upload back as a new blob and then in my terraform code just change the statefile to point to the new blob instead of the old one. This leaves a clear fallback if needed.

### References:

1. [link](https://github.com/hashicorp/terraform-provider-aws/issues/14431)

1. [link](https://github.com/hashicorp/terraform/issues/25752#issuecomment-672217777)

1. [link](https://stackoverflow.com/questions/63427604/how-do-you-fix-terraform-unsupported-attribute-ses-smtp-password-after-upgradi)