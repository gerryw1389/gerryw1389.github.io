---
title: 'Terraform: Display Outputs'
date: 2022-05-22T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/tf-display-outputs/
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
  - Scripting-HCL
  - CICD
---
<!--more-->

### Description:

By default, Terraform will display outputs during a terraform plan or apply, but follow this step if you need it to display a secret variable's output.

### To Resolve:

1. Let's say you have a private key you need to connect to a linux server after creation. 

   - inside `outputs.tf` you have:

   ```terraform
   output "tls_private_key" {
      value     = tls_private_key.vm_ssh_key.private_key_pem
      sensitive = true
   }
   ```

1. Then in your pipeline, just add this step after the terraform apply command:

   ```yaml
   - script: terraform output -raw tls_private_key
      displayName: 'terraform display key'
   ```