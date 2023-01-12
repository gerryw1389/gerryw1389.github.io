---
title: 'Terraform: LastUpdated Tag'
date: 2022-09-10T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/09/tf-lastupdated-tag
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
---
<!--more-->

### Description:

Quick post about how you can use the [`timestamp`](https://www.terraform.io/language/functions/timestamp), [`timeadd`](https://www.terraform.io/language/functions/timeadd), and [`formatdate`](https://www.terraform.io/language/functions/formatdate) functions in Terraform to set localized times for tagging your resources. More details from [this post](https://clebergasparoto.com/how-to-manipulate-date-and-time-with-terraform), example below.

Update: This has been fixed in a new post, please view it [here](https://automationadmin.com/2022/11/tf-calculated-tags)!

### To Resolve:

1. The following `locals` block will build a string that will look like: `2022-10-15-09:10 AM PST` for example:

   ```terraform
   locals {
      now     = timestamp()
      pst_tz  = timeadd(local.now, "-7h")
      time    = formatdate("YYYY-MM-DD-HH:mm AA", local.pst_tz)
      created = join(" ", [local.time, "PST"])
      tags = {
            Owner       = "Automation Admin"
            CostCenter  = "100"
            EntAppname  = "Automation Admin Terraform POC"
            Environment = "tst"
            Contact     = "gerry@automationadmin.com"
            Latest_RunBy  = "${var.requested_for} - ${var.requested_for_email}"
            LastUpdated     = local.created
      }
   }
   ```

1. The main problem with this is everytime you run your pipeline it will update that tag. While it's pretty obvious you want the `LastUpdated` tag to be the last time an object was touched, there may be better solutions out there like querying [Microsoft Graph Explorer](https://learn.microsoft.com/en-us/azure/governance/resource-graph/how-to/get-resource-changes?tabs=azure-powershell) for last time a resource was updated. But maybe you can use these time functions for other things so will still keep this in mind.