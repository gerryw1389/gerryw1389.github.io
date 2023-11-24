---
title: Mirror OneDrive Business To Azure Files
date: 2020-12-16T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/mirror-onedrive-to-azure-files
tags:
  - Azure
tags:
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

So I like to use an Azure Files (from an Azure Storage Account) that mounts to hybrid workers with an Azure Automation account to do SFTP transfers. But I need a way for internal users to be able to add files without giving them access to my storage account. In this example, we create a one drive folder on a service account and share it with different groups in the organization. We then have a Logic App that will go and copy each of the files to Azure Files on the storage account and then delete them from OneDrive. We can then create an Azure Runbook (Azure Automation) to go [and transfer the files to a third party service](https://automationadmin.com/2020/10/using-azure-automation-logic-apps-for-sftp).

### To Resolve:

1. Source code is [here](https://github.com/gerryw1389/terraform-examples/tree/main/2020-12-16-mirror-onedrive-to-azure-files/mirror-onedrive-to-azure-files/mirror-onedrive-to-azure-files.json)

2. Be sure to find/replace for `double open brackets` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

3. Pics

   - ![mirror1](https://automationadmin.com/assets/images/uploads/2020/12/mirror1.jpg){:class="img-responsive"}

   - ![mirror2](https://automationadmin.com/assets/images/uploads/2020/12/mirror2.jpg){:class="img-responsive"}

4. What makes this Logic App especially useful is that you have an array of folder names, and for each of them you loop through and move the files to the storage account!
