---
title: Logic Apps Write To Custom Log
date: 2021-03-10T21:49:19-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/03/write-custom-log/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-LogAnalytics
---
<!--more-->

### Description:

So you can already connect Log Analytics queries to power Power BI applications or Dashboards and share those to users inside Microsoft Teams, but what we were wanting to do is write to a specific table a set of specific values. Thankfully, this is easy to do with the [Send Data](https://docs.microsoft.com/en-us/connectors/azureloganalyticsdatacollector/#send-data) action for Log Analytics inside Logic Apps. Here is an example of how you could write a bunch of data for each of your Logic Apps. Keep in mind that it would probably be much easier (and better) to stick with [Tracked Properties](https://automationadmin.com/2020/09/get-tracked-properties) which natively can record values in Log Analytics.

### To Resolve:

1. At the beginning of each Logic app:

   - Initialize RunID (string) => Expression => `guid('N')`
   - Initialize strStepStart (string) => Expression => `convertTimeZone(utcnow(),'UTC','Central Standard Time')`
   - Initialize strStepEnd (string) => blank
   - Initialize payload (string) => blank

2. At the end of each Logic app:

   - Set-strStepEnd => Expression => `convertTimeZone(utcnow(),'UTC','Central Standard Time')`
   - Set-Payload => `Set Variable` Action => Value:

   ```json
   {
      "description": "Enter a full description",
      "worflow_name": "Enter a job name",
      "run_id": "@{variables('RunID')}",
      "os": "null",
      "sftp": "null",
      "status": "Success",
      "step_end": "@{variables('strStepEnd')}",
      "step_number": "01",
      "step_start": "@{variables('strStepStart')}"
   }
   ```

   - Send-Data-Success => Action - Send Data
      - JSON Request body => `payload`
      - Custom Log Name => `My_Log_Analytics_Table_Name`

3. So what you can do is declare a bunch of variables throughout your Logic App and then place the `Condition` action at multiple points and write out to this Log Analytics table at any point.

   - For example, you could set `"status" : "failed",` if something fails a condition and then add the `Terminate` action right after it. This means the Logic App will write to Log Analytics that it failed and then throw an exception.
   - You could set `"step_number" : "02",` if you have a Logic app with multiple steps. This can show up in a Dashboard as a single run with multiple steps since you can bind them with the same `RunID` declared at the top.
   - You could  set `"run_id": "@{variables('RunID')}",` to be any key-value pair that you want to record. Most of our JSON payloads we send to Log Analytics have 20+ key-value pairs.
     - These each show up as a separate column in Log Analytics and thus another data point you can manipulate with Power BI.
   - With `strStepStart` and `strStepEnd` you have two Datetime objects that you can perform calculations on that determine how long it took the Logic App to run. Very useful for long Logic Apps with 60+ actions and a metric that management will want to see on a dashboard.