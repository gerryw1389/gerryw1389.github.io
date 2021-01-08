---
title: Create File Shares Using Storage Account
date: 2020-08-17T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/create-file-share-using-storage-account
categories:
  - Azure
tags:
  - Azure-StorageAccounts
---
<!--more-->

### Description:

This post is a quick easy post to share how I use file shares to share state between [two Windows Server Hybrid Workers](https://automationadmin.com/2020/04/moving-to-azure-automation) in an Azure Automation account. 

### To Resolve:

1. If you haven't already, create a storage account and a share called 'data' with 1 TB quota.
2. Copy the code it gives you to mount the drives.
3. Create a service account in your Local AD and have it sync up to your Azure Tenant
4. Give that account rights to do things in whatever resource group your automation account is in. Or at the subscription level if you will have the account do actions to other resources in other resource groups within the subscription.
5. Make it a local admin the hybrid worker server.
6. Sign in as the service account and map the drive using the code generated in step 2.
7. Now, have it on the service account's powershell profile to map the drive for all scripts:

   ```powershell
   Try 
   { 
   Get-PSDrive -Name "T" -ErrorAction "Stop" | Out-Null 
   }
   Catch
   { 
      Try
      {
         New-PSDrive -Name "T" -PSProvider "FileSystem" -Root "\\yourStorageAccount.file.core.windows.net\data" -ErrorAction "Stop" | Out-Null
      }
      Catch
      {
         Write-Output "Unable to mount T Drive"
      }
   }
   ````
8. Now, all you have to do is include the same snippet of code in your Azure Automation Runbooks and you can refer to paths locally no matter which hybrid worker you run on! Example: `cd T:\myfolder` will work on each hybrid worker you follow these steps on. We have had this running this way for over a year and the drives are always there connected so they don't disconnect and automation runs smooth.
