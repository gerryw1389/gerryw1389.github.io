---
title: 'Terraform: Official Sleep Example'
date: 2022-11-23T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/11/official-sleep-example
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

So the other day I was working on App Service in terraform and I kept having an issue with the [App Service Slot Custom Hostname Binding](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/app_service_slot_custom_hostname_binding) resource where it would fail if you pass in multiple domains and hostnames and use count to iterate over them:


```escape
CreateOrUpdateHostNameBindingSlot: Failure responding to request: StatusCode=409 -- Original Error: autorest/azure: Service returned an error. Status=409 Code="Conflict" Message="Cannot modify this site because another operation is in progress

╷
│ Error: creating App Service Slot Custom Hostname Binding: (Host Name Binding Name "slot-1.a.example.com" / Slot Name "slot-1" / Site Name "my-app-service" / Resource Group "unittest-app-service"): web.AppsClient#CreateOrUpdateHostNameBindingSlot: Failure responding to request: StatusCode=409 -- Original Error: autorest/azure: Service returned an error. Status=409 Code="Conflict" Message="Cannot modify this site because another operation is in progress. Details: Id: 52866c8e-dabe-488d-95fe-503b3b75cb09, OperationName: Update, CreatedTime: 12/28/2022 8:57:50 PM, RequestId: b1b7ebc3-8882-4bd7-94bd-004da4056451, EntityType: 3" Details=[{"Message":"Cannot modify this site because another operation is in progress. Details: Id: 52866c8e-dabe-488d-95fe-503b3b75cb09, OperationName: Update, CreatedTime: 12/28/2022 8:57:50 PM, RequestId: b1b7ebc3-8882-4bd7-94bd-004da4056451, EntityType: 3"},{"Code":"Conflict"},{"ErrorEntity":{"Code":"Conflict","ExtendedCode":"59203","Message":"Cannot modify this site because another operation is in progress. Details: Id: 52866c8e-dabe-488d-95fe-503b3b75cb09, OperationName: Update, CreatedTime: 12/28/2022 8:57:50 PM, RequestId: b1b7ebc3-8882-4bd7-94bd-004da4056451, EntityType: 3","MessageTemplate":"Cannot modify this site because another operation is in progress. Details: {0}","Parameters":["Id: 52866c8e-dabe-488d-95fe-503b3b75cb09, OperationName: Update, CreatedTime: 12/28/2022 8:57:50 PM, RequestId: b1b7ebc3-8882-4bd7-94bd-004da4056451, EntityType: 3"]}}]
│ 
│   with module..azurerm_app_service_slot_custom_hostname_binding.main_private_slot[0],
│   on .terraform/modules/appsvcTst/custombinding_private_slot.tf line 94, in resource "azurerm_app_service_slot_custom_hostname_binding" "main_private_slot":
│   94: resource "azurerm_app_service_slot_custom_hostname_binding" "main_private_slot" {
│ 
```

### To Resolve:

1. In my quest to resolve the issue I came across many links:

   - [link](https://stackoverflow.com/questions/71422681/dependencies-within-count)
   - [link](https://github.com/hashicorp/terraform-plugin-sdk/issues/67)
   - [link](https://stackoverflow.com/questions/63744524/sequential-resource-creation-in-terraform-with-count-or-for-each-possible)
   - [link](https://discuss.hashicorp.com/t/0-13-parallel-module-for-each-executions/12342/4)

1. What finally fixed it was just passing the `parallelism=1` flag to the [terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply#parallelism-n) in the pipeline. By default, terraform does 10 iterations on each resource if you use count or for each, and, as far as I know, this is the only way to force it to do them sequentially. I have no background in ARM templates, but I found that the `copy` function or whatever has a `mode` property you can [set to `serial`](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/copy-resources#syntax), I just need the same thing in Terraform for App Service.

1. Anyways, if you want to deploy **resources** sequentially (and not wait between iterations in a loop), this can be done using the time_sleep resource and there are many examples online. For example (all credit to `pet2cattle.com`) :

   ```terraform
   # https://pet2cattle.com/2021/06/time-sleep-between-resources

   resource "helm_release" "ampa" {
   name       = "ampa"
   chart      = "/home/git/ampa/helm-ampa"
   timeout    = 600

   namespace = var.namespace
   }

   resource "time_sleep" "wait_for_ingress_alb" {
   create_duration = "300s"

   depends_on = [helm_release.ampa]
   }

   data "kubernetes_ingress" "web" {
   metadata {
      name      = "votacions-ampa"
      namespace = var.namespace
   }

   time_sleep = [time_sleep.wait_for_ingress_alb]
   }
   ```

   - First, you need to use the `time` provider and the [`time_sleep`](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/sleep) resource.
   - In your code you deploy resource1 first, then set time_sleep to have a dependency on resource1 using `depends_on`, then you declare resource2 or data1 with a `depends_on` to the `time_sleep` resource.
   - So it goes: resource1 => time_sleep => data1/resource2 in that order.