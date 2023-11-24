---
title: 'Terraform: For Loop'
date: 2022-07-28T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-for-loop
tags:
  - Terraform
---
<!--more-->

### Description:

The [ `for` loop in terraform](https://www.terraform.io/language/expressions/for) is used to transform one "complex object" into another "complex object". Here are some examples. The main thing to pay attention to is the output of the loop:

   - If you see `[ for b in blah ]` you know that the output will be a `list` object by the `[` and `]` characters. Note that you can cast to a set by using the [`toset()`](https://www.terraform.io/language/functions/toset) function if passing to something else that requires a set.
   - If you see `{ for b in blah }` you know that the output will be a `map` object by the `{` and `}` characters.

### To Resolve:

1. Take one list, and loop through it to produce another list making transformations on each object. The example in the link shows for example transoforming a list of string to uppercase:

   ```terraform
   terraform {
      required_version = "~>1.1.0"
   }

   variable "users" {
      description = "(Optional) List of users."
      type = list
      default = ["jim", "bob", "alice"]
   }

   locals {
      for_loop_users = [for s in var.users : upper(s)]
   }

   output "for_loop_users" {
      value = local.for_loop_users
   }

   ```

   - Output

   ```escape
   Changes to Outputs:
   + for_loop_users = [
         + "JIM",
         + "BOB",
         + "ALICE",
      ]
   ```

1. Same thing, but lets filter to get rid of `alice`:

   ```terraform
   terraform {
      required_version = "~>1.1.0"
   }

   variable "users" {
      description = "(Optional) List of users."
      type = list
      default = ["jim", "bob", "alice"]
   }

   locals {
      for_loop_users = [for s in var.users : upper(s) if s != "alice"]
   }

   output "for_loop_users" {
      value = local.for_loop_users
   }

   ```

   - Output

   ```escape
   Changes to Outputs:
   + for_loop_users = [
         + "JIM",
         + "BOB"
      ]
   ```

1. Reading a little bit lower on that page, I thought I would test with their example where you have a map object coming in:

   ```terraform

   terraform {
      required_version = "~>1.1.0"
   }

   variable "users" {

      description = "(Optional) List of users."

      type = map(object({
         is_admin = bool
      }))

      default = {
         "Jim" = { is_admin = true }
         "Bob" = { is_admin = true }
      }
   }

   locals {
      admin_users = {
         for name, user in var.users : name => user
         if user.is_admin
      }
      regular_users = {
         for name, user in var.users : name => user
         if !user.is_admin
      }
   }

   output "display_admin_users" {
      value = local.admin_users
   }

   output "display_regular_users" {
      value = local.regular_users
   }
   ```

   - Output

   ```escape
   Changes to Outputs:
  + display_admin_users   = {
      + Bob = {
          + is_admin = true
        }
      + Jim = {
          + is_admin = true
        }
    }
  + display_regular_users = {}
   ```

   - Now try tweaking `true` and `false` `is_admin` values for either "Bob"/"Jim" or both and see how the outputs change.

1. Here is one that takes a list of map objects and creates child map objects using the name property from each object:

   ```terraform
   terraform {
      required_version = "~>1.1.0"
   }

   variable "file_shares" {
      description = "(Optional) List of file shares."
      type = list
      default = [
         { name = "smbfileshare1", quota = 50 },
         { name = "smbfileshare2", quota = 50 }
      ]
   }

   locals {
      for_loop_shares = { for shares in var.file_shares : shares.name => shares }
   }

   output "for_loop_shares" {
      value = local.for_loop_shares
   }

   ```

   - Output

   ```escape
   Changes to Outputs:
   + for_loop_shares = {
         + smbfileshare1 = {
            + name  = "smbfileshare1"
            + quota = 50
         }
         + smbfileshare2 = {
            + name  = "smbfileshare2"
            + quota = 50
         }
      }
   ```

   - And if you only wanted to get the quotas, try something like:

   ```terraform
   output "for_loop_quota" {
      value = {
         for k, v in local.for_loop_shares : k => v.quota
      }
   }
   ```

   - Which will give you:

   ```escape
   Changes to Outputs:
   + for_loop_quota  = {
         + smbfileshare1 = 50
         + smbfileshare2 = 50
      }
   ```

   - If you would just prefer a list in the output for some reason, do the same but target a list:

   ```terraform
   output "for_loop_quota" {
      value = [
         for k in local.for_loop_shares : k.quota
      ]
   }
   ```

   - Which will give you:

   ```escape
   Changes to Outputs:
   + for_loop_quota  = [
      + 50,
      + 50,
    ]
   ```

