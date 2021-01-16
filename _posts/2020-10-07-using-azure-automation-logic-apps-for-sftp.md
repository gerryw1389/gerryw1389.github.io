---
title: Using Azue Automation With Logic Apps For SFTP Transfers
date: 2020-10-07T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/10/using-azure-automation-logic-apps-for-sftp
categories:
  - WebSoftware
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-StorageAccounts
  - Azure-Automation
---
<!--more-->

### Description:

One of the cool ways to use [Azure Automation Hybrid Workers](https://automationadmin.com/2020/04/moving-to-azure-automation) is to schedule them to do SFTP transfers. Here is how:

### To Resolve:

1. Follow the steps in [Moving To Azure Automation](https://automationadmin.com/2020/04/moving-to-azure-automation) to create an Azure Automation account linked to Github.

   - Ensure an Azure Files share is mounted as the service account user
   - Ensure that each of your hybrid workers have a static public IP. 
     - Also make sure all third party vendors that you want to SFTP files to have this IP whitelisted as many will require this.

2. Next, create a Logic App with a recurrence trigger that starts the action [Create Job](https://docs.microsoft.com/en-us/connectors/azureautomation/#create-job) 

3. Lastly, just create a `.ps1` file in the `/runbooks` directory of your Azure Automation repo that:

   - Grabs a file from the mounted drive
   - Copies it to the Hybrid Worker's local C drive to a temp folder
   - Uses the [ WinSCP dll](https://winscp.net/eng/docs/library_from_script) to transfer the file to a third party 
   - [Example](https://winscp.net/eng/docs/library_powershell#example)
