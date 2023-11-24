---
title: Quick Log Analytics Queries
date: 2020-09-23T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/quick-log-analytics-queries
tags:
  - Azure
tags:
  - Azure-LogAnalytics
---
<!--more-->

### Description:

Here are some Log Analytics queries we have saved for Logic Apps and Azure Automation logging. Note that many of these can be tied to Azure Monitor to produce alerts. [Example](https://automationadmin.com/2020/04/use-log-analytics-with-azure-automation-for-alerts) post.

### To Resolve:

#### Logic Apps

1. An "Automation view" for Logic Apps:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s <> "Running"
   | where OperationName == "Microsoft.Logic/workflows/workflowRunCompleted"
   | distinct resource_workflowName_s, TimeGenerated, status_s, startTime_t, endTime_t
   | extend LogicApp = resource_workflowName_s
   | extend Status = status_s
   | extend StartTime = startTime_t
   | extend EndTime = endTime_t
   | extend TimeCompleted = TimeGenerated
   | project TimeCompleted, LogicApp, Status, StartTime, EndTime
   | sort by TimeCompleted desc
   ```

2. Count of Logic Apps:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | distinct resource_workflowName_s
   | summarize count(resource_workflowName_s)
   | extend LogicApp_Count = count_resource_workflowName_s
   | project LogicApp_Count
   ```

3. Get Recurrence triggers:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where resource_triggerName_s == "Recurrence"
   | where OperationName == "Microsoft.Logic/workflows/workflowTriggerCompleted"
   | distinct resource_workflowName_s, TimeGenerated, status_s, startTime_t, endTime_t
   | extend LogicApp = resource_workflowName_s
   | extend Status = status_s
   | extend StartTime = startTime_t
   | extend EndTime = endTime_t
   | extend TimeCompleted = TimeGenerated
   | project TimeCompleted, LogicApp, Status, StartTime, EndTime
   | sort by TimeCompleted desc
   ```

4. Logic Apps with Errors:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   //we want "1" (Captured Error), "Terminated", "ActionFailed", "BadRequest", "Unauthorized" or others...
   | where status_s == "Failed" and code_s <> "BadGateway" and code_s <> "429" and code_s <> "GatewayTimeout" 
   | extend LocalTimestamp = TimeGenerated
   | project LocalTimestamp, LogicAppName = resource_workflowName_s, Error = error_code_s
   ```

5. Succeeded:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s == "Succeeded" and OperationName == "Microsoft.Logic/workflows/workflowRunCompleted"
   | extend LocalTimestamp = TimeGenerated
   | extend LogicAppName = resource_workflowName_s
   | project LocalTimestamp, LogicAppName
   ```

6. Total Runtime (this requires that you use Tags to group. For example, this uses `JobStream` tag with a value of "My Group Tag" that would be added to multiple Logic Apps):

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.LOGIC"
   | where status_s <> "Running"
   | where OperationName == "Microsoft.Logic/workflows/workflowRunCompleted"
   | where tags_JobStream_s == "My Group Tag"
   | extend ID = correlation_clientTrackingId_s
   | project startTime_t,ID, Duration = endTime_t - startTime_t
   | summarize totalrun=sum(Duration) by ID
   ```

#### Azure Automation

1. Job Error:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (ResultType == "Failed" or ResultType == "Stopped" or ResultType == "Suspended")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   ```

2. Job Success:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (ResultType == "Completed")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   ```

3. Job stream error: Can also by output and verbose

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobStreams" and StreamType_s == "Error"
   | project TimeGenerated , RunbookName_s , StreamType_s , Resource , ResultDescription
   ```

4. Specific job success:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (RunbookName_s == "My-Runbook-1" or RunbookName_s == "My-Runbook-2") and (ResultType == "Completed")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   ```

5. Count of Automation runbook runs:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs"
   | distinct RunbookName_s
   | summarize count(RunbookName_s)
   | extend Runbook_Count = count_RunbookName_s
   | project Runbook_Count
   ```
