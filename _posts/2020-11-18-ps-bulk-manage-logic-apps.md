---
title: 'PS: Bulk Manage Logic Apps'
date: 2020-11-18T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/ps-bulk-manage-logic-apps
tags:
  - Azure
tags:
  - Azure-LogicApps
  - Powershell
---
<!--more-->

### Description:

I have a folder I keep called 'portal-scripts' but really they are just a way to use powershell to manage Logic Apps in Bulk in the Azure portal. Here are some examples:

### To Resolve:

1. As usual, you start by signing into  your account in vscode:

   ```powershell
   Import-Module Az
   $sub = '697e3adsfadf'
   Connect-AzAccount -SubscriptionId $sub -UseDeviceAuthentication
   ```

2. Then you usually create an array of resources to loop through by their name in the Azure portal:

   ```powershell
   $apps = @(
   'DoSomething-002',
   'DoSomething-003',
   'DoSomething-004',
   'DoSomething-005')
   ```

3. Then do one of these:

   - Clone logic apps

   ```powershell
   $Workflow = Get-AzLogicApp -ResourceGroupName "My-Logic-Apps" -Name "DoSomething-002"

   foreach ( $a in $apps )
   {
   New-AzLogicApp -ResourceGroupName "My-Logic-Apps" -Name $a -State "Enabled" -Definition $Workflow.Definition -Parameters $Workflow.Parameters -Location "southcentralus"
   #Start-Sleep -Seconds 15

   }
   ```

   - Enable log analytics

   ```powershell
   $omsWorkspace = Get-AzOperationalInsightsWorkspace
   foreach ( $a in $apps )
   {
   $currentLA = Get-AzLogicApp -ResourceGroupName "My-Logic-Apps" -Name $a 
   Set-AzDiagnosticSetting -ResourceId $($currentLA.Id) -WorkspaceId $($omsWorkspace.ResourceId) -Enabled $true -Name "my-analytics-account-name"
   #Start-Sleep -Seconds 15
   }
   ```

   - Get all disabled

   ```powershell
   Get-AZlogicapp | where { $_.state -eq "Disabled" } | select name
   ```

   - Get all without logging

   ```powershell
   $WarningPreference = 'SilentlyContinue'
   $logicapps = Get-AZlogicapp -ResourceGroupName "My-Logic-Apps"
   foreach ( $logicapp in $logicapps)
   {
   $enabled = Get-AzDiagnosticSetting -ResourceId $($logicapp.id)
   If ( $null -eq $enabled )
   {
   Write-Output "Log Analytics is not enabled: $($logicapp.name)"
   }
   Else
   {
   #Write-Output "Log Analytics is enabled: $($logicapp.name)"
   }
   }
   ```
