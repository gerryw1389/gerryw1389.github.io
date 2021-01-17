---
title: Get Tracked Properties In Log Analytics
date: 2020-09-12T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/get-tracked-properties
categories:
  - Azure
tags:
  - Azure-LogicApps
  - Azure-LogAnalytics
---
<!--more-->

### Description:

This is how I was finally able to get [tracked properties](https://docs.microsoft.com/en-us/azure/logic-apps/monitor-logic-apps-log-analytics#send-diagnostic-data-to-azure-storage-and-azure-event-hubs) to show up in Log Analytics. These can be valuable as they allow you to store the value of variables in Log Analytics with a specific run. For example, we use it to get a process ID from a third party system that is unique to each Logic App run.

### To Resolve:

1. Inside a Logic App:

   - Create an 'Initialize Variable' action after you have a variable you want captured in logs.
   - Data Type string
   - Value `$myvar` where myvar is the variable you want to capture
   - Click on the ellipsis on the right for the 'Initialize Variable' action and go to Settings
     - Tracked Properties section:
     - Name: Whatever you want it to show up as in Log Analytics
     - Value: `"@action().inputs.variables[0].value"`

2. Let it run a couple times and you should be able to query for it now:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s <> "Running"
   | where tags_JobStream_s == "My_Logic_App"
   | where OperationName == "Microsoft.Logic/workflows/workflowActionCompleted"
   | extend ProcessID = trackedProperties_ProcessID_s
   | extend LogicApp = resource_workflowName_s
   | extend Status = status_s
   | extend StartTime = startTime_t
   | extend EndTime = endTime_t
   | extend TimeCompleted = TimeGenerated
   | extend CoorelationID = correlation_clientTrackingId_s
   | project TimeCompleted, LogicApp, Status, ProcessID, StartTime, EndTime, CoorelationID
   ```

3. Pay particular attention to `workflowActionCompleted`. Another example where I filter on the action called `Initialize-logAnalyticsProcessID` from the instructions in step 1:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s <> "Running"
   | where tags_JobStream_s == "My_Logic_App"
   | where OperationName == "Microsoft.Logic/workflows/workflowActionCompleted"
   | where resource_actionName_s == "Initialize-logAnalyticsProcessID"
   | extend ProcessID = trackedProperties_Process_ID_s
   | extend LogicApp = resource_workflowName_s
   | extend Status = status_s
   | extend StartTime = startTime_t
   | extend EndTime = endTime_t
   | extend TimeCompleted = TimeGenerated
   | extend CoorelationID = correlation_clientTrackingId_s
   | project TimeCompleted, LogicApp, Status, ProcessID, StartTime, EndTime, CoorelationID
   ```
