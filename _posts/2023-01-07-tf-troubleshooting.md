---
title: 'Terraform: General Troubleshooting Tips'
date: 2023-01-07T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/tf-troubleshooting
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description

Some general troubleshooting tips for Terraform:

### To Resolve:

1. You [can view](https://developer.hashicorp.com/terraform/cli/v1.2.x/commands/state/list) resources in state file directly.

   - I talk about this in my [Remove Invalid Attribute From Statefile](https://automationadmin.com/2022/12/remove-invalid-attribute-statefile) and [Remove Invalid Resources](https://automationadmin.com/2022/12/remove-invalid-resources) posts for example.

2. You [can set](https://developer.hashicorp.com/terraform/internals/v1.2.x/debugging) `TF_LOG` to one of the log levels (in order of decreasing verbosity) `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR` to change the verbosity of the logs.

3. Take a look at various sections under [Terraform internals](https://developer.hashicorp.com/terraform/internals/v1.2.x).