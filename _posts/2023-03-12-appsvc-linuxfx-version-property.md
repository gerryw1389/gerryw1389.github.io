---
title: AppSvc LinuxFX Property
date: 2023-03-12T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/03/appsvc-linuxfx-version-property
tags:
  - Azure
  - Azure-AppSvc
---
<!--more-->

### Description

Sometimes we will need to upgrade the [Stack Settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#configure-general-settings) for an App Service.

The general idea is that you update the Stack Settings and then the App owners can use Azure Devops/Github to deploy their application into this new App Service. From what I can tell it is only a metadata thing in that having the wrong or right stack does not appear to make a difference to the App Service.

I've been trying to investigate what it really means. Here are some links I have been reading:

- [OS Runtime](https://learn.microsoft.com/en-us/azure/app-service/overview-patch-os-runtime#when-are-supported-language-runtimes-updated-added-or-deprecated)
- [Language Support Policy](https://learn.microsoft.com/en-us/azure/app-service/language-support-policy)
- [AzureRmWebAppDeployment@4](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-rm-web-app-deployment-v4?view=azure-pipelines) which is what we use
- [Zip Deploy](https://learn.microsoft.com/en-us/azure/app-service/deploy-zip?tabs=cli)
- [Stack Overflow post](https://stackoverflow.com/questions/58392312/azure-webapp-stack-settings)

If you choose to "Export Template" for an App Service, you will see that "Stack Settings" really only coorelate to a field called `linuxFxVersion` which can be found under `siteConfig.linuxFxVersion` or `properties.linuxFxVersion`. When you [lookup these settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code?tabs=json#linux-3) they are only referenced by a linux App Service Plan. There is also [this Github Wiki](https://github.com/Azure/azure-functions-host/wiki/Using-LinuxFxVersion-for-Linux-Function-Apps) that semi explains things but I still have questions about mismatches.

Here is what appears to be an [official explanation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#app-service-site-settings) which is referenced by [this](https://learn.microsoft.com/en-us/azure/azure-functions/set-runtime-version?tabs=portal#manual-version-updates-on-linux).

### To Resolve

1. As far as implementing these stack version changes, I have used two methods:

   - Upgrade the App Stack version Terraform and then run an apply to upgrade the App Svc itself. Then have developers push new code that matches that stack afterwards. This is the "in-place upgrade" option.

1. The preferred option is to deply a new App Service and then have the developers push their code to it. Then we cut over traffic from the old App Service to the new which is the preferred "blue green method".

