---
title: Migrating Logic Apps Between RGs
date: 2021-02-18T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/02/migrating-logic-apps/
tags:
  - Azure
tags:
  - Azure-LogicApps
---
<!--more-->

### Description:

Because of the use API Connections, we have been weary of migrating Logic Apps between one resource group and another so this is what we have done to make this easier.

### To Resolve:

1. In a new Resource Group, create a Logic App called `api-connections-test` or something like that and then add a bunch of actions that connect to a bunch of things:

   - Office 365 Email
   - Azure Automation
   - Sharepoint
   - Azure Storage Accounts (file shares/table storage/ect)
   - Any other connections...

2. Now go to "code view" and copy the json keys and values for each of the connections to a markdown document and put that in Github.

3. Now, to migrate a Logic App from an older RG to a new one, just:

   - Copy the older Logic Apps "code view" json in Notepad.
   - Clone your `api-connections-test` Logic App.
   - Overwrite its json with the json from the older Logic App's code view.
   - Lastly, replace the API connection values with the matching ones from step 2.
   - Click "Designer" and verify that all connections and actions don't have grey boxes with X's next to them (indicating invalid connections)
