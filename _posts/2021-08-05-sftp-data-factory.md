---
title: Using Azure Data Factory For SFTP Transfers
date: 2021-08-05T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/08/sftp-data-factory
tags:
  - Azure
tags:
  - Azure-DataFactory
---
<!--more-->

### Description

So currently I use [Hybrid Workers](https://automationadmin.com/2020/10/using-azure-automation-logic-apps-for-sftp) to SFTP files from my organization to another since I can set a public static IP on the workers and have them whitelist. Another option I'm looking into is Azure Date Factory. Here is an example using Data Factory to transfer a file from storage account [to a SFTP server](https://docs.microsoft.com/en-us/azure/data-factory/connector-sftp).

### To Resolve:

1. In the azure portal, create a data factory.

2. Go to datasets

   - source:
   - type: binary
	- location: Azure file storage, select any file
	
   - destination:
	- binary2
	- sftp - enter connection details - select a folder for file to land in.

3. Create pipeline:

   - Add step called `copy data`
		- Source: binary
		- Destination (sink): binary2

4. Click publish all

5. On pipeline, select 'run'. Notice that the binary select in source is transferred to destination. The SFTP uses the credentials specified in the SFTP connection.

   - To my knowledge, ADF uses 4 different IP addresses
   - I would like to look into this, but I'm currently leaning more toward [NAT Gateway with Function Apps](https://automationadmin.com/2020/12/setup-nat-gateway-for-azure-functions) since I mostly use those for everything currently
   - On my to-do-list is to update to use [Python](https://docs.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-python) instead if we go with ADF.
