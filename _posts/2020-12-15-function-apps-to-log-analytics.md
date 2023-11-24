---
title: Function Apps To Log Analytics
date: 2020-12-15T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/function-apps-to-log-analytics
tags:
  - Azure
tags:
  - Azure-LogAnalytics
---
<!--more-->

### Description:

Follow these steps to get your Function App custom logs to show up in Log Analytics

### To Resolve:

1. Inside your Function App, go to Diagnostic Settings and have it send all of its logs to Log Analytics just like any other resource

2. Inside App Insights go to Properties and make sure it is [pointing to log analytics](https://stackoverflow.com/questions/55112648/azure-application-insights-or-log-analytics)

3. If you want to see the output of a log, you have two places to go for now:

   - Inside Application Insights => Logs => you can type `traces` and run. It should  have your python `logging.info("something")` statements
   - Example for a function called `GetProcessID`:

   ```escape
   traces
   | where customDeminsions.Category == "Function.GetProcessID.User"
   ```

   - Inside Log Analytics => Logs => you can type `FunctionAppLogs` and run. It should  have your python `logging.info("something")` statements

   ```escape
   FunctionAppLogs
   | where FunctionName == "GetProcessID"

   # another example to get Exceptions
   FunctionAppLogs
   | where ExceptionDetails != ""  
   | order by TimeGenerated asc

   ```

4. Actually, for best results, I have been typing `AppTraces` in Log Analytics to get my logging statement outputs.

  ```escape
  AppTraces
  | where OperationName == "Get-Status"
  | where TimeGenerated > ago(20m)
  | sort by TimeGenerated desc 
  | project TimeGenerated, Message, OperationId

  # Variation you could try:
  AppTraces
  | where OperationName == "Get-Status"
  | where TimeGenerated > ago(20m)
  | sort by TimeGenerated desc 
  | summarize by OperationId, TimeGenerated, Message
  ```
