---
title: Logic Apps Mirror Storage
date: 2020-12-13T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/la-mirror-storage
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

So I have, the past, setup an Azure Container Group that accepts files to be placed into it. I then create the following Logic App that will copy the files from one storage account to another so that I don't have user's uploading directly into my storage account (best practice!).

### To Resolve:

1. Source code is [here](https://github.com/gerryw1389/terraform-examples/tree/main/logic-apps/mirror-storage/mirror-storage.json)

2. Be sure to find/replace for `double open brackets` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

3. Pics

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/mirror-storage.jpg){:class="img-responsive"}

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/mirror-storage2.jpg){:class="img-responsive"}
