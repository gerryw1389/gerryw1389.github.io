---
title: Use Log Analytics With Azure Automation For Alerts
date: 2020-04-25T08:06:24-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/use-log-analytics-with-azure-automation-for-alerts
categories:
  - Azure
tags:
  - Cloud
  - Orchestration
  - Azure-LogAnalytics
  - Azure-Automation
---
<!--more-->

### Description:

After setting up an automation account in Azure, the first thing you want to setup is Azure Monitor alerts so that you can be emailed when runbooks fail. This should be setup before you start moving runbooks to production. Follow this post if your organization is willing to pay for Log Analytics. If not, you can still get alerts on failed runbooks natively (free) following [this](https://docs.microsoft.com/en-us/azure/automation/automation-alert-metric) document, but I don't know how to set it up to get alerts on errors within the runbook. I believe that if you use `throw` keyword in your powershell scripts, they can fail the runbook so that should be all you need.

In this guide, we will be able to get better ideas of alerts because my organization purchased Log Analytics for the Automation Account to forward its logs to so we can alert on failed jobs and failed lines within a job.

### To Resolve:

1. From my [previous post](https://automationadmin.com//2020/04/moving-to-azure-automation), make sure you have your automation account sending logs to your Log Analytics workspace:

   ```powershell
   Get-AzResource -ResourceType "Microsoft.OperationalInsights/workspaces"
   # copy output from previous command
   $l = '/subscriptions/longpath/log-analytics'
   Get-AzResource -ResourceType "Microsoft.Automation/automationAccounts"
   # copy output from previous command
   $a = '/subscriptions/longpath/automation'
   Set-AzDiagnosticSetting -ResourceId $a -WorkspaceId $l -Enabled 1

   # Verify
   Get-AzDiagnosticSetting -ResourceId $automationAccountId
   ```

2. Setup an alert that will run every 5 minutes and email you once with all errors found within those 5 minutes for Azure Runbooks that have failed:

   - Go to Azure Monitor => Alerts => Manage Alert Rules => New Alert Rule
   - Resources: Your Log Analytics Workspace
   - Condition: Signal => Custom Log Search
   - Query:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (ResultType == "Failed" or ResultType == "Stopped" or ResultType == "Suspended")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   | extend LocalTimestamp = TimeGenerated - 5h
   | project LocalTimestamp , RunbookName_s , ResultType 
   ```

   - NOTE: Change the `5h` to whatever time zone you are in, for me it is Central Time
   - Alert Logic: `Number of results`, `greater than`, `0`
   - Evaluation based on: Period in minutes `5`, Frequency in minutes `5`
   - Action Groups: 'email_automation_team'
   - Alert Rule Name: `automation_joblog_failed`

3. Setup an alert that will run every 5 minutes and email you once with all errors found within those 5 minutes for errors within Azure Runbooks that have failed:

   - Go to Azure Monitor => Alerts => Manage Alert Rules => New Alert Rule
   - Resources: Your Log Analytics Workspace
   - Condition: Signal => Custom Log Search
   - Query:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobStreams" and StreamType_s == "Error"
   | project TimeGenerated , RunbookName_s , StreamType_s , Resource , ResultDescription
   | extend LocalTimestamp = TimeGenerated - 5h
   | project LocalTimestamp , RunbookName_s ,  StreamType_s , ResultDescription
   ```

   - NOTE: Change the `5h` to whatever time zone you are in, for me it is Central Time
   - Alert Logic: `Number of results`, `greater than`, `0`
   - Evaluation based on: Period in minutes `5`, Frequency in minutes `5`
   - Action Groups: 'email_automation_team'
   - Alert Rule Name: `automation_jobstream_failed`

4. So those alerts are really all you need if you want an overview of ALL runbooks in your account - they will run every 5 minutes and send you a list of errors.
   - To be clear, the reason we created `jobstream` separate from `joblog` is that `jobstream` will alert for runbooks that complete successfully but still throw errors. In powershell, you can use a `Try{}Catch{}` with `Catch{}` containing a `Write-Error "blah"` and the runbook will still complete successfully unless you explicitly set `$ErrorPreference = "Stop"`.

5. What if you want to alert on error in a specific runbook? Well setup the same structure but put this in the query instead:

   - Error specific runbooks, for example `My-Runbook-1` or `My-Runbook-2`:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (RunbookName_s == "My-Runbook-1" or RunbookName_s == "My-Runbook-2") and (ResultType == "Failed" or ResultType == "Stopped" or ResultType == "Suspended")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   | extend LocalTimestamp = TimeGenerated - 5h
   | project LocalTimestamp , RunbookName_s , ResultType
   ```

6. What if you want to alert on success in a specific runbook? Well setup the same structure but put this in the query instead:

   - Success specific runbooks, for example only `My-Runbook-2`:

   ```escape
   AzureDiagnostics
   | where ResourceProvider == "MICROSOFT.AUTOMATION" and Category == "JobLogs" and (RunbookName_s == "My-Runbook-2") and (ResultType == "Completed")
   | project TimeGenerated , RunbookName_s , ResultType , Resource
   | extend LocalTimestamp = TimeGenerated - 5h
   | project LocalTimestamp , RunbookName_s , ResultType
   ```

7. If you don't want to use this setup (i.e. not pay for Log Analytics), and what I had done initially, is you can just set your scripts to send emails using `Try{}Catch{}` blocks:

   ```powershell
   Function Get-EmailAccountUser
   {
      $cred = Get-AutomationPSCredential -Name 'Office365 Email User'
      $val = $cred.UserName
      return $val
   }
   Function Get-EmailAccountPass
   {
      $cred = Get-AutomationPSCredential -Name 'Office365 Email User'
      $val = $cred.GetNetworkCredential().Password
      return $val
   }
   Function Send-Email
   {
      [CmdletBinding()]
      param 
      (
         [string]$Subject,
         [string]$Body,
         [string]$Username,
         [string]$Password
      )
      $pw = ConvertTo-SecureString -String $Password -AsPlainText -Force
      $EmailCred = New-Object System.Management.Automation.PSCredential($userName, $pw)

      $Params = @{
         'UseSSL'     = $True
         'From'       = 'user@domain.com'
         'To'         = 'user2@domain.com'
         'Cc'         = @('user3@domain.com')
         'Subject'    = $Subject
         'BodyAsHTML' = $True
         'Body'       = $Body
         'SmtpServer' = "smtp.office365.com"
         'Port'       = "587"
      }
      [System.Net.ServicePointManager]::ServerCertificateValidationCallback = { return $true }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      Send-MailMessage @Params -Credential $EmailCred
   }

   # Some stuff in the runbook runs here

   Try
   {
      # generate some error
   }
   catch
   {
      
      $emailUser = Get-EmailAccountUser
      $emailPass = Get-EmailAccountPass
      $params = @{
         Subject  = "Runbook Failed: This Runbook Name"
         Body     = "CSV file not created"
         Username = $emailUser
         Password = $emailPass
      }
      Send-Email @params
      
      Write-Error "CSV file not created"
      Exit 1
   }
   ```
