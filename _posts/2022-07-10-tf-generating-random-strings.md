---
title: 'Terraform: Generating Random Strings'
date: 2022-07-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-generating-random-strings
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

Follow these steps to use random string whatever reason. I usually use these for creating resources which won't gaurantee uniqueness, but most likely will. It will fail on apply if the resource just happens to exist but I've never seen it yet.

### To Resolve:

1. First, make sure to include `random` in your providers:

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
   ```

1. Next, just create a random resource. Optionally, if using Azure, I like to add `resource_group` to the [keepers](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/string#keepers) ( which points to [here](https://registry.terraform.io/providers/hashicorp/random/latest/docs#resource-keepers) ) which ensures the random resource will never regenerate unless that is changed:

   ```terraform
   resource "random_string" "naming_convention" {
   keepers = {
      resource_group = var.resource_group_name
   }
   length  = 5
   upper   = false
   lower   = true
   number  = true
   special = false
   }

   resource "null_resource" "naming_standard_key_vault_example" {
      name  = "some-resource-${random_string.naming_convention.result}"
   }
   ```

1. To create multiple random strings using `count`, see my [other post here](https://automationadmin.com/2022/07/tf-count) for an example.