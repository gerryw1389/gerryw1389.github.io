---
title: 'Logic App File System Error: Check Your Parameters'
date: 2020-05-12T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/logic-app-file-system-error-check-your-parameters
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

After [creating an on-prem data gateway](https://automationadmin.com/2020/05/automation-with-azure-data-gateway), when creating a `File System - Create File` Logic App action, I kept getting the following error:

   ```escape
   Check your request parameters

   {
   "status": 400,
   "message": "The requested action could not be completed. Check your request parameters to make sure the path 'G:\\Test\\input/7.csv' exists on your file system.\r\nclientRequestId: 53a6bf6a-c7ec-4cf2-9a41-d02816a4e6e5",
   "error": {
      "message": "The requested action could not be completed. Check your request parameters to make sure the path 'G:\\Test\\input/7.csv' exists on your file system."
   },
   "source": "filesystem-scus.azconn-scus.p.azurewebsites.net"
   }
   ```

### To Resolve:

1. Go inside your Logic App and go to 'API Connections'. Often you will see where you created a connection to a specific folder like `G:\Test2` and you are trying to write a file to `G:\Test`, this will not work. To fix, just create a new connection to the correct folder and use that one instead when building your Logic App.

2. Also, make sure you do not use `account@domain.com` for credentials and instead use `domain.com\account`
