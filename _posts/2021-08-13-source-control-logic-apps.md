---
title: Source Control Logic Apps
date: 2021-08-13T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/08/source-control-logic-apps
categories:
  - WebSoftware
tags:
  - Cloud
  - Azure-LogicApps
  - VersionControl
---
<!--more-->

### Description

Follow these steps to source control Logic Apps. In this example, I will create a Logic App called `email_filter` that will look for emails in my inbox with the subject of `SOMETHING UNIQUE` and have an attachment. When an email arrives that matches both conditions, it will copy the attachment to a storage account under a location called `logic-apps` to a file called `unique.csv`. In addition, it will write information to a Log Analytics workspace such as the name of the Logic app, when it started, when it finished, and any other custom data I would like to record. Why record custom data? Well you can already send diagnostic data to a Log Analytics Workspace, but with conditional data, you can write JSON payloads that will conditionally write to your workspace under a specific table. This is powerful for Power BI dashboards for example.

### To Resolve:

1. Create a subscription using the plan "Azure For Students" or "Pay as you go" or whatever works best for you.

2. Create a Resource Group called "logic-apps"

3. Create a Resource group called "storage"

4. In the storage resource group, create a storage account and add two shares:
	- cloud-shell (not needed for this post, but best practice for when you use cloud shell)
	- logic-apps

5. Create a log analytics workspace, then go Settings => Agents Management and copy `Workspace ID` and `Primary Key` to notepad

6. Now, this one time we need to get some API connections created. I have found the easiest way is to create a logic app that doesn't make sense and just add a bunch of actions to different connections and then copy its connection properties for the next steps. 

   - Create a logic app called `api-connections`:

	- Trigger: 
		- Schedule => Recurrence => Once every 3 months
	- Action: 
		- Office 365 => Send an Email v2 => Click 'Sign in' to create the api object in the background.
	- Action: 
		- Azure File Storage => Create File => Point to storage account `/logic-apps` file share location.
	- Action: 
		- Initialize variable => Name: object => Type: Object => Value: `{"key":"bob"}`
	- Action: 
		- Azure Log Analytics Data Connector => Send Data => Enter a name and the two options copied from notepad from previous step.
		- JSON: object => Custom Log Name: LogicApps
		
   - Save and run. Go to Log analytics and look for bob

   - Now go to `Code View` and copy everything around `$connections` to notepad:

   ```
   "$connections": {
      "value": {
         "azurefile": {
            "connectionId": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/resourceGroups/logic-apps/providers/Microsoft.Web/connections/azurefile",
            "connectionName": "azurefile",
            "id": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/providers/Microsoft.Web/locations/southcentralus/managedApis/azurefile"
         },
         "azureloganalyticsdatacollector": {
            "connectionId": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/resourceGroups/logic-apps/providers/Microsoft.Web/connections/azureloganalyticsdatacollector",
            "connectionName": "azureloganalyticsdatacollector",
            "id": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/providers/Microsoft.Web/locations/southcentralus/managedApis/azureloganalyticsdatacollector"
         },
         "office365": {
            "connectionId": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/resourceGroups/logic-apps/providers/Microsoft.Web/connections/office365",
            "connectionName": "office365",
            "id": "/subscriptions/700b8c1a-701c-4d49-b283-5718830ef8a2/providers/Microsoft.Web/locations/southcentralus/managedApis/office365"
         }
      }
   }
   ```

7. Copy and paste the ARM template for this logic app from [here](https://github.com/gerryw1389/terraform-examples/blob/main/logic-apps/email-filter-1/email_filter.json) into VSCode on your machine.
   - Overwrite lines 335-354 (or wherever $connections begin and end)
   - In the Azure portal, go to Templates. Then select => New => Paste this in and deploy it!

8. Assuming a successful deployment, open [myapps.microsoft.com](https://myapps.microsoft.com) in a new window and send an email to yourself with any attachment and the subject line of `SOMETHING UNIQUE`. This should trigger the logic app.

   - For best results, make your attachment a CSV file with whatever header/information you want. This will make viewing it easier on the next step.

9.  Lastly, just verify that everything worked by going to your storage account => File Shares => logic-apps => `unique-values.csv`. 
   
   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2021/10/unique-values-file.jpg){:class="img-responsive"}
   
   - Does it look like what you emailed yourself? Congrats! 

   - Lastly, just go to Log Analytics => Logs => just paste `LogicApps_CL` and view the results. 

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2021/10/log-analytics.jpg){:class="img-responsive"}

10. Send an email again and try with the subject of `SOMETHING UNIQUE 2`. Did it run the same way?
