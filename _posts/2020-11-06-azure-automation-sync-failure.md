---
title: Azure Automation Sync Failure
date: 2020-11-06T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/azure-automation-sync-failure
categories:
  - Azure
tags:
  - Azure-Automation
---
<!--more-->

### Description:

Clicking on an error inside Azure Automation for 'Sync-SourceControl' gives you a huge output with no good information.

### To Resolve:

1. What I did was run the following in the Azure Portal:

   ```powershell
   $body = [ordered]@{
      'SourcecontrolName'     = 'azure-github'
      'ResourceGroupName'     = 'My-Automation-RG'
      'AutomationAccountName' = 'My-Automation-Account'
      'Verbose' = $true 
   }
   Start-AzAutomationSourceControlSyncJob @body

   $body = [ordered]@{
      'SourcecontrolName'     = 'azure-github'
      'ResourceGroupName'     = 'My-Automation-RG'
      'AutomationAccountName' = 'My-Automation-Account' 
   }
   Get-AzAutomationSourceControlSyncJob @body


   $body = [ordered]@{
      'SourceControlSyncJobId' = '2f39a5d8-798f-41be-a537-29171b08e2af'
      'SourcecontrolName'     = 'azure-github'
      'ResourceGroupName'     = 'My-Automation-RG'
      'AutomationAccountName' = 'My-Automation-Account' 
   }
   (Get-AzAutomationSourceControlSyncJob @body).Exception
   ```

2. In this case, there was nothing we could do as that runbook is handled by Microsoft and was resolved in less than 24 hours. But what you could do is remove your source control configuration and add it back if it is giving issues.