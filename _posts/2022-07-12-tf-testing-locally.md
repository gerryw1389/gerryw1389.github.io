---
title: 'Terraform: Testing Locally'
date: 2022-07-12T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-testing-locally
tags:
  - Terraform
---
<!--more-->

### Description:

Follow these steps to test locally on your machine assuming you have Terraform installed.
  

### To Resolve:

1. Ensure Terraform is installed:

   ```powershell
   Set-ExecutionPolicy RemoteSigned
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   choco install terraform -y --limitoutput
   ```

1. To test locally if only using native resources that don't connect to anything like testing language features specifically:

   - Create a folder: `c:\scripts\test1` then `cd c:\scripts\test1`
   - Paste the following to `c:\scripts\test1\test.tf`

   ```terraform
   terraform {
      required_providers {
         random = {
            source  = "hashicorp/random"
            version = "~>3.3.2"
         }
      }
      required_version = "~>1.1.0"
   }

   provider "random" {
   }

   resource "random_string" "naming_convention_unique" {
      count   = 5
      length  = 5
      upper   = false
      lower   = true
      numeric = true
      special = false
   }

   output "random" {
      value = ["${random_string.naming_convention_unique.*.result}"]
   }
   ```

   - Run: `terraform init`
   - Run: `terraform plan -out tf.plan`
   - Run: `terraform apply -auto-approve -input=false ./tf.plan`
   - This will create `c:\scripts\test1\terraform.tfstate`, `c:\scripts\test1\tf.plan`, `c:\scripts\test1\terraform.lock.hcl`, and a folder called `c:\scripts\test1\.terraform`
   - What's happening here?
      - Terraform initializes locally and downloads whatever providers during the `init`.
      - During the `plan` it will see that no `terraform.state` exists so it should only create new resources.
      - During the `apply` it will create the local `terraform.state` file in the current directory.

1. To just test expressions locally, try [Terraform Console command](https://www.terraform.io/cli/commands/console)

1. To test locally connecting to Azure but using a local state file:

   - Create a folder: `c:\scripts\test2` then `cd c:\scripts\test2`
   - Paste the following to `c:\scripts\test2\test.tf`

   ```terraform

   terraform {
      required_providers {

         random = {
         source  = "hashicorp/random"
         version = "~>3.3.2"
         }

         azurerm = {
         source  = "hashicorp/azurerm"
         version = "~>3.10.0"
         }

      }
      required_version = "~>1.1.0"
   }

   provider "random" {
   }

   provider "azurerm" {
      client_id                  = var.client_id
      client_secret              = var.client_secret
      subscription_id            = var.subscription_id
      tenant_id                  = var.tenant_id
      skip_provider_registration = true
      features {}
   }

   variable "tenant_id" {
      description = "(Required) Service Principal AD Tenant ID - Azure AD for terraform authentication."
      type        = string
   }

   variable "subscription_id" {
      description = "(Required) Azure Subscription Id used to connect to AzureRM provider."
      type        = string
   }

   variable "client_id" {
      description = "(Required) Service Principal App ID - Azure AD for terraform authentication."
      type        = string
   }

   variable "client_secret" {
      description = "(Required) Service Principal Client Secret - Azure AD for terraform authentication."
      type        = string
   }

   resource "random_string" "naming_convention_unique" {
      length  = 5
      upper   = false
      lower   = true
      numeric = true
      special = false
   }

   resource "azurerm_resource_group" "rg" {
      name     = "my-rg-${random_string.naming_convention_unique.result}"
      location = "westus"
      tags = {
         Owner       = "Automation Admin"
         CostCenter  = "100"
         EntAppname  = "Automation Admin Terraform POC"
         Environment = "tst"
         Contact     = "gerry@automationadmin.com"
      }
   }

   output "res_out_rg_name" {
      value = azurerm_resource_group.rg.name
   }

   output "res_out_rg_id" {
      value = azurerm_resource_group.rg.id
   }
   ```
   
   - Create a new file `c:\scripts\test2\env.tfvars`

   ```
   subscription_id="some-guid"
   tenant_id="some-guid"
   client_id="some-guid"
   client_secret="some-guid"
   ```

   - Run: `terraform init`
   - Run: `terraform plan -var-file="env.tfvars" -out="tf.plan"`
   - Run: `terraform apply -auto-approve -input=false ./tf.plan`
   - This will create `c:\scripts\test2\terraform.tfstate`, `c:\scripts\test2\tf.plan`, `c:\scripts\test2\terraform.lock.hcl`, and a folder called `c:\scripts\test2\.terraform`
   - What's happening here?
      - Terraform initializes locally and downloads whatever providers during the `init`.
      - During the `plan` it will see that no `terraform.state` exists so it should only create new resources.
      - During the `plan` it will read in `env.tfvars` and inject their values into the `variable $x{}` blocks inside `test.tf`.
      - You could also pass them manually by writing `'terraform plan -var="tenant_id=myvar1_value" -var="subscription_id=myvar2_value" -var="client_id=myvar3_value" -var="client_secret=myvar4_value" -out="tf.plan"'`
      - Not sure if that will work exactly as you might have to escape some `"` or add some in some places, it's usually just easier to point to a local file.
      - During the `apply` it will create the local `terraform.state` file in the current directory.

1. To test locally connecting to Azure but using a remote state file:

   - Create a folder: `c:\scripts\test3` then `cd c:\scripts\test3`
   - Paste the following to `c:\scripts\test3\test.tf`:

   ```terraform

   terraform {
      
      backend "azurerm" {
         resource_group_name  = "tx-storage-rg"
         storage_account_name = "automationadminstorage"
         container_name       = "tfstatesbx"
         key                  = "learning_rg"
      }
      
      required_providers {

         random = {
         source  = "hashicorp/random"
         version = "~>3.3.2"
         }

         azurerm = {
         source  = "hashicorp/azurerm"
         version = "~>3.10.0"
         }

      }
      required_version = "~>1.1.0"
   }

   provider "random" {
   }

   provider "azurerm" {
      client_id                  = var.client_id
      client_secret              = var.client_secret
      subscription_id            = var.subscription_id
      tenant_id                  = var.tenant_id
      skip_provider_registration = true
      features {}
   }

   variable "tenant_id" {
      description = "(Required) Service Principal AD Tenant ID - Azure AD for terraform authentication."
      type        = string
   }

   variable "subscription_id" {
      description = "(Required) Azure Subscription Id used to connect to AzureRM provider."
      type        = string
   }

   variable "client_id" {
      description = "(Required) Service Principal App ID - Azure AD for terraform authentication."
      type        = string
   }

   variable "client_secret" {
      description = "(Required) Service Principal Client Secret - Azure AD for terraform authentication."
      type        = string
   }

   resource "random_string" "naming_convention_unique" {
      length  = 5
      upper   = false
      lower   = true
      numeric = true
      special = false
   }

   resource "azurerm_resource_group" "rg" {
      name     = "my-rg-${random_string.naming_convention_unique.result}"
      location = "westus"
      tags = {
         Owner       = "Automation Admin"
         CostCenter  = "100"
         EntAppname  = "Automation Admin Terraform POC"
         Environment = "tst"
         Contact     = "gerry@automationadmin.com"
      }
   }

   output "res_out_rg_name" {
      value = azurerm_resource_group.rg.name
   }

   output "res_out_rg_id" {
      value = azurerm_resource_group.rg.id
   }
   ```
   
   - Create a new file `c:\scripts\test3\env.tfvars`

   ```
   subscription_id="some-guid"
   tenant_id="some-guid"
   client_id="some-guid"
   client_secret="some-guid"
   ```

   - Create a new file `c:\scripts\test3\backend.hcl`

   ```
   access_key="my-access-key"
   ```

   - Run: `terraform init -backend-config="backend.hcl"`
   - Run: `terraform plan -var-file="env.tfvars" -out="tf.plan"`
   - Run: `terraform apply -auto-approve -input=false ./tf.plan`
   - This will create `c:\scripts\test3\tf.plan`, `c:\scripts\test3\terraform.lock.hcl`, and a folder called `c:\scripts\test3\.terraform` but NOT `c:\scripts\test3\terraform.tfstate` because that will be stored on the `backend`.
   - What's happening here?
      - Terraform initializes locally and downloads whatever providers during the `init` but this time it will reach out to Azure using the `access_key` variable which should be the access key of the storage account where your state file exists.
      - During the `plan` it will see that a `terraform.state` exists so it will read your changes against the current file like a normal plan does.
      - During the `plan` it will read in `env.tfvars` and inject their values into the `variable $x{}` blocks inside `test.tf`.
      - During the `apply` it will update the state file you pointed to in the `terraform { backend {} }` block in `test.tf`.


1. One of the things you can do since you are testing locally is pipe the output to just get the changes:

   ```powershell
   terraform plan -var-file="env.tfvars" -out="tf.plan" | Select-String -pattern "created","destroyed","Plan:"
   ```

1. Lastly, to inspect map objects (or other possible uses I haven't thought of yet), you might be able to do [the following locally](https://github.com/ContainerSolutions/terraform-examples/blob/main/local/null_resource/for_each/main.tf) to test:

   ```terraform
   terraform {
   required_version = "~>1.1.0"
   }

   locals {
   map1 = {
      item1 = {
         name1 = "item1value1"
         name2 = "item1value2"
      }
      item2 = {
         name1 = "item2value1"
         name2 = "item2value2"
      }
   }
   }

   resource "null_resource" "for_each" {
   for_each = local.map1
   provisioner "local-exec" {
      command = "echo ${each.key} ${each.value.name1} ${each.value.name2}"
   }
   }
   ```


   - Which gives me:

   ```escape
   null_resource.changeme_null_resource_foreach["item1"]: Destroying... [id=2211496336822316780]
   null_resource.changeme_null_resource_foreach["item2"]: Destroying... [id=799620883465416640]
   null_resource.changeme_null_resource_foreach["item1"]: Destruction complete after 0s
   null_resource.for_each["item2"]: Creating...
   null_resource.for_each["item1"]: Creating...
   null_resource.changeme_null_resource_foreach["item2"]: Destruction complete after 0s
   null_resource.for_each["item2"]: Provisioning with 'local-exec'...
   null_resource.for_each["item1"]: Provisioning with 'local-exec'...
   null_resource.for_each["item2"] (local-exec): Executing: ["cmd" "/C" "echo item2 item2value1 item2value2"]
   null_resource.for_each["item1"] (local-exec): Executing: ["cmd" "/C" "echo item1 item1value1 item1value2"]
   null_resource.for_each["item2"] (local-exec): item2 item2value1 item2value2
   null_resource.for_each["item1"] (local-exec): item1 item1value1 item1value2
   null_resource.for_each["item2"]: Creation complete after 1s [id=3764591095398055352]
   null_resource.for_each["item1"]: Creation complete after 1s [id=7664239314724568197]
   ```
