---
title: 'Terraform: Export Object'
date: 2023-01-19T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/tf-export-object
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

Short post, but I wanted to help someone with a [module](https://automationadmin.com/2022/08/calling-remote-modules) and I noticed that the object wasn't being exported from the module because it was using a `count`. Here is how I fixed it:

### To Resolve:

1. First, if you want specific properties that is easy when you have a resource [with count, you just use a wildcard like so](https://developer.hashicorp.com/terraform/language/expressions/references#references-to-resource-attributes):

   ```terraform
   output "databasesql_database_ids" {
   value = azurerm_mssql_database.sql_database.*.id
   }

   output "databasesql_database_names" {
   value = azurerm_mssql_database.sql_database.*.name
   }
   ```

   - Note that the same link says that if I were to instead use `for_each`, the outputs would be like:


   ```terraform
   output "databasesql_database_ids" {
   value = [for value in azurerm_mssql_database.sql_database: value.id]
   }

   output "databasesql_database_names" {
   value = [for value in azurerm_mssql_database.sql_database: value.name]
   }
   ```

1. But what if you want `all of the properties?` There doesn't seem to be many examples of this online but the fix (for a resource with count) is to just not include the properties:

   ```terraform
   output "databasesql_database_objects" {
   value = azurerm_mssql_database.sql_database[*]
   }
   ```

   - I haven't tested, but I assume with for_each you would do

   ```terraform
   output "databasesql_database_objects" {
   value = [for value in azurerm_mssql_database.sql_database: value]
   }
   ```

