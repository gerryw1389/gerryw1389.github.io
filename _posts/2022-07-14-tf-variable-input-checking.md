---
title: 'Terraform: Input Variable Checking'
date: 2022-07-14T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/tf-variable-input-checking
tags:
  - Terraform
---
<!--more-->

### Description:

Quick post here about how you can go about using [Input Validation checks](https://www.terraform.io/language/expressions/custom-conditions#input-variable-validation) with Terraform variables.

### To Resolve:

1. A simple example with two values:

   ```terraform
   variable "region" {
      description = "(Optional) The name of the region. Example: West US."
      type        = string
      default     = "westus"

      validation {
         condition     = var.region == "westus" || var.region == "eastus"
         error_message = "The region must be westus or eastus."
      }
   }
   ```

1. An example with many values:

   ```terraform
   variable "sub_abbr" {
      description = <<EOF
      (Required) The abbreviated name of the subscription. Used for naming resources.
      Must be one of the following:
      abc  => subscription abc
      def  => subscription def
      ghi  => subscription ghi
      EOF
   
      type        = string
   
      validation {
      condition = (var.sub_abbr == "abc" ||
         var.sub_abbr == "def" ||
         var.sub_abbr == "ghi")
      error_message = "The subscription abbreviation must be one of: `abc,def,ghi` ."
   }
   }
   ```

1. A cleaner way using `contains`:

   ```terraform
   variable "sub_abbr" {
      description = <<EOF
      (Required) The abbreviated name of the subscription. Used for naming resources.
      Must be one of the following:
      abc  => subscription abc
      def  => subscription def
      ghi  => subscription ghi
      EOF
   
      type        = string
   
      validation {
         condition     = contains(["abc","def","ghi"], var.sub_abbr)
         error_message = "The subscription abbreviation must be one of: `abc,def,ghi` ."
      }
   }
   ```
