---
title: Run Every Minute To Event Based
date: 2020-05-08T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/run-every-minute-to-event-based
categories:
  - SysAdmin
  - Azure
tags:
  - Cloud
---
<!--more-->

### Description

So let's say you have the current setup:

- User fills out a Catalog item in Service Now
- Azure Automation has a runbook that runs every minute that scans Service Now for a new item based on the 'short description'
- If it finds one, it parses the information and sends to [Netiq Identity Governance](https://www.microfocus.com/en-us/products/netiq-identity-governance/overview#) (shortened to IDG) for approvals
- Writes relevant information to Table Storage in Azure
- A separate runbook that runs every minute reads table storage and if the approval has been completed, it will close the request in Service Now
- More details [here](https://automationadmin.com/2020/02/idg-create-app-for-approvals)

The problem:

- Not really a problem yet [since documentation says it's fine](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#process-automation) but it seems like wasted CPU resources to scan systems every minute and only run sometimes.

Now let's move to an Event based flow:

- User fills out a Catalog item in Service Now
- Service Now sends a simple POST to Event Grid with a unique GUID that matches the catalog item
- Event Grid kicks off a Logic App that calls the same runbook as before
- In IDG, create a script that will upload CSV's once they are created to Blob Storage
- Create logic app that has a trigger of 'when a new blob is written' that will parse the CSV and call a runbook that completes the workflow.

Almost every post in the last year helps build on this topic so feel free to reference them.

### To Resolve

1. So first we need Service Now to send a POST to a unique GUID, I have this outlined [here](https://automationadmin.com/2020/04/azure-event-grid-trigger-logic-app). This is just a matter of building out different logic apps for each Service Now Catalog Item.

2. Next, we have IDG send a CSV to blob storage as posted [here](https://automationadmin.com/2020/04/logic-app-parse-csv-sent-from-azcopy-to-azure-blob). This is just a matter of filtering on the variables in the CSV and having those start runbooks.

3. The overall workflow can be described [here](https://automationadmin.com/2020/02/idg-create-app-for-approvals)
