---
title: On-Prem Data Gateways To Table Storage
date: 2020-06-29T13:49:58-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/data-gateway-to-runbooks-and-table-storage
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

So when looking at our current Logic Apps, I was looking for a way to not have to use On-Prem Data Gateways and try to use everything either within the Logic App itself [like our goal](https://automationadmin.com/2020/05/general-automation-goals-with-azure) or to at least call an Azure Hybrid Worker and pass values that way. Here is two approaches I have used.

### To Resolve:

1. First, is to try and pass the values to Azure Table storage and then have my powershell runbook pull those values in the next step:

   - Inside Logic App Designer, first get the variables you need and put them in Variables. In this case `strDate` and `strConcat` which is a long json string with other variables.
   - Pass those to a 'Insert Entity' action like so:

   ```json
   #Table: Some table
   #Entity:
   {
   "PartitionKey": @{variables('strDate')},
   "RowKey": "PROD-my-rowkey-the-script-will-search-for",
   "Status": "waiting",
   "Value": "@{variables('strConcat')}"
   }
   ```

   - Then do the regular 'Create Job' from Azure Automation to run a runbook that will [read table storage and get the values](https://automationadmin.com/2020/05/ps-write-to-table-storage) and change the record to 'completed' so that the next flow won't try to process it.

2. This, of course, is kinda silly seeing as Runbooks have native ways to pass parameters! So instead, create parameters for your runbook and then when you choose the 'Create Job' action for Azure Runbooks - you just fill in the parameters since Azure will automatically populate the input parameters by name! I would show a screenshot here but I don't have anything with generic parameters so I will link [this](https://docs.microsoft.com/en-us/azure/automation/runbook-input-parameters) instead.


