---
title: Azure Functions Mounting Azure Storage File Shares
date: 2021-01-21T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/azure-functions-mounting-storage/
tags:
  - Azure
tags:
  - Azure-FunctionApps
  - Azure-StorageAccounts
  - Scripting-Python
---
<!--more-->

### Description:

Follow this post to mount storage to your Function Apps. Following [this post](https://docs.microsoft.com/en-us/azure/azure-functions/storage-considerations) what I did was:

### To Resolve:

1. Inside Azure Portal, open up Bash and type in:

   ```shell
   az webapp config storage-account add -g my_RG -n my-cool-function-app \
   --custom-id my-cool-function-app \
   --storage-type AzureFiles \
   --account-name my-cool-storage-account \
   --share-name my-share-name-in-storage-account \
   --access-key 1soD6tfrxdLD/8MMEzANYEgA== \
   --mount-path /data

   # It responds with:
   # This command is in preview. It may be changed/removed in a future release.
   {
   "my-cool-function-app": {
      "accessKey": "1soD6tfrxdLD/8MMEzANYEgA==",
      "accountName": "my-cool-storage-account",
      "mountPath": "/data",
      "shareName": "my-share-name-in-storage-account",
      "state": "Ok",
      "type": "AzureFiles"
      }
   }
   ```

2. Now, in my [Function Apps](https://automationadmin.com/2021/01/function-apps-with-logic-apps/), I listed the files in some directories:

   ```python
   import os

   files_in_share = os.listdir("/my-share/data")
   logging.info("files: {}".format(files_in_share))

   files_in_share2 = os.listdir("/my-share/data/myuser/shared/install")
   logging.info("files in shared/install dir: {}".format(files_in_share2))
   ```

3. Sure enough, in Application Insights I was able to see the output I was expecting!

  ```escape
  2020-12-09T21:13:06Z   [Verbose]   Initiating background SyncTriggers operation
  2020-12-09T21:13:06Z   [Information]   files: ['archived', 'sched-tasks', 'scripts', 'shared']
  2020-12-09T21:13:06Z   [Information]   files in shared/install dir: ['npp.exe', 'python-3.8.2.exe', 'skypeonlineconnector.exe', 'StorageExplorer.exe']
  2020-12-09T21:13:06Z   [Information]   Called function ReadXML3
  ```
