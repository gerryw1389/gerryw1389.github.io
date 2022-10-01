---
title: 'TF: Using AzDo With No Service Connection'
date: 2022-08-02T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/tf-no-service-connection
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

In this post, I will briefly outline how to use Azure Devops deployment into Azure without setting up a Service connection as mentioned [in my original post](https://automationadmin.com/2022/05/setup-azdo-terraform/). Code for this post can be found [here](https://github.com/gerryw1389/terraform-examples/tree/main/2022-08-02-tf-no-service-connection).


### To Resolve:

1. Basically, just add a bash task to login using the Service Principle that you deploy resources as:

   ```yaml
   - task: Bash@3
      displayName: "Az Login"
      inputs:
         targetType: inline
         failOnStderr: true
         script: |
            az login --service-principal -u $(az-tf-client-id) \
               -p $(az-tf-client-secret) \
               -t $(tenant-id) \
               --output none
            az account set --subscription $(subscription-id)
   ```

1. Note that if you populate your secrets from an Azure Keyvault, you will most likely need to authenticate as a KeyVault user, update your pipeline secrets, and then move on if you want to do this using only a Service Principle. Since I plan to migrate to Github Actions though, I will be doing something like [this](https://learn.microsoft.com/en-us/azure/developer/github/github-key-vault) instead.