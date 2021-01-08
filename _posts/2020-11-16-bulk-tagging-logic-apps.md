---
title: Bulk Tagging Logic Apps
date: 2020-11-16T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/bulk-tagging-logic-apps
categories:
  - Azure
tags:
  - Azure-LogicApps
---
<!--more-->

### Description:

Here are the steps to tag resources in Bulk using powershell

### To Resolve:

1. Create a powershell file on your machine and paste in:

   ```
   Import-Module Az
   $sub = '697adfadfasdfasdfas'
   Connect-AzAccount -SubscriptionId $sub -UseDeviceAuthentication
   ```

   - Where `$sub` if your subscription ID if you have multiple subscriptions

2. Now add a couple line breaks and paste in the rest:

   ```powershell
   $names = @(
   'MyLogicApp1-002',
   'MyLogicApp1-024',
   'MyLogicApp2-001',
   'MyLogicApp2-002',
   'MyLogicApp2-003',
   'MyLogicApp2-004',
   'MyLogicApp2-005',
   'MyLogicApp2-006',
   'MyLogicApp2-007')

   $count = 0

   foreach ($name in $names)
   {
      $count += 1
      
      $stepCount = $count.tostring()
      If ($($stepCount.Length) -gt 1)
      {
         $currentCount = "0" + $stepCount
      }
      Else
      {
         $currentCount = "00" + $stepCount
      }
      
      Write-Output "Step: $currentCount"
      $currentLA = Get-AZlogicapp -ResourceGroupName "My-Logic-App-RG" -Name $name
      
      Write-Output "Processing $($currentLA.name)"

      [hashtable]$currentTags = $($currentLA.Tags)
      
      Write-Verbose "Looping through key value pairs to add to $($currentLA.name)"
      $newTags = @{
         "Step"              = $currentCount
         "JobStream"         = "MyGroupName"
      }

      foreach ($key in $($newTags.keys) )
      {
      
         $value = $newTags[$key]
         Write-Verbose "Key to add: $key"
         Write-Verbose "Value to add: $value"
      
         If ($currenttags.ContainsKey($key) )
         {
               $currenttags.Remove($key)
               $currentTags.Add($key, $value)
         }
         Else
         {
               $currentTags.Add($key, $value)
         }
      }

      Set-AzResource -ResourceId $($currentLA.Id) -Tag $currentTags -Force

      Write-output "Added tag to $($currentLA.name) "
      #Start-Sleep -Seconds 10

   }
   ```

3. So this will loop through a list of Logic Apps defined in `$names` and set various tags on them. It will only update tags or add new ones but keep all the existing ones. Feel free to use!