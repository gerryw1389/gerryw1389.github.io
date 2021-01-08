---
title: How To Group Logic Apps Executions
date: 2020-09-03T14:27:17-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/how-to-group-logic-apps-executions
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-LogAnalytics
---
<!--more-->

### Description:

So we are currently chaining a bunch of Logic Apps together by creating them with `HTTP Request` triggers and at the end they call the next one or more than one in a sequence. This is working great and logs are going to Log Analytics as intended. Follow these steps to get executions in order:

### To Resolve:

1. Open Log Analytics => Type in:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s <> "Running"
   | where tags_JobStream_s == "Test-Gerry"
   | where OperationName == "Microsoft.Logic/workflows/workflowRunCompleted"
   | extend LogicApp = resource_workflowName_s
   | extend Status = status_s
   | extend StartTime = startTime_t
   | extend EndTime = endTime_t
   | extend TimeCompleted = TimeGenerated
   | extend CoorelationID = correlation_clientTrackingId_s
   | project TimeCompleted, LogicApp, Status, StartTime, EndTime, CoorelationID
   ```

   - Make sure you have a `JobStream` tag in each Logic App and replace my value with yours. 

2. Once the results are returned, select the radio button to 'Group Results' and then drag the column 'CoorelationID' up and you can now see a group of Logic Apps that were called by each other. You can learn about [clientTrackingId here](https://docs.microsoft.com/en-us/azure/logic-apps/monitor-logic-apps-log-analytics#extend-data).