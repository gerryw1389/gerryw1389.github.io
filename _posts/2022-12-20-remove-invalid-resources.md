---
title: 'Terraform: Remove Invalid Resources'
date: 2022-12-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/12/remove-invalid-resources
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

So during my [terraform upgrades](https://automationadmin.com/2022/12/tf-version-upgrades) I came across issues where I would try to update a resource, the terraform plan would fail, and then I ended up having to remove the resource. But sometimes it would **still** fail even though all references to the resource were commented out in the code. In cases like this sometimes it's best to just find the resource in your statefile and remove it completely. 

NOTE: This should almost never be used as I don't know the full implications but messing with the statefile is usually not the right answer. You have been warned!
{: .notice--danger}

### To Resolve:

1. First, download your [statefile locally](https://automationadmin.com/2022/12/remove-invalid-attribute-statefile) and do a `terraform state list` to get the reference to the object you want to remove completely.

2. Next, just add a step in your release pipeline that runs commands to remove them from the state file before `terraform plan` but after `terraform init`.

   ```
   terraform state rm 'module.mymodule1'
   terraform state rm 'module.mymodule2'
   ```

1. Note that I have only ever done this to get my `terraform plan` to be clean and then readded the resources back if they existed before.