---
title: 'Azure Automation: Disable Public Access To Private Endpoint'
date: 2022-09-03T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/09/disable-public-access-to-pep
categories:
  - Azure
tags:
  - Cloud
  - Scripting-Powershell
---
<!--more-->

### Description:

So one task I wanted to setup after [deploying an Automation Account](https://automationadmin.com/2022/08/tf-create-aa-with-source-control) via Terraform was a scheduled task that will run a script nightly. The task will login to Azure, get all Storage Accounts for all subscriptions, and if they have a Private endpoint, disable the "Public Network Access". This setting is currently [in development](https://github.com/hashicorp/terraform-provider-azurerm/issues/16335) through the AzureRM provider so I will just run a script until it is completed.

### To Resolve:

1. First, to be clear, just because you create/enable a Private Endpoint (PEP), does not mean that public access is not enabled. 
   - I thought so when I first heard about it because of phrasing like `eliminating exposure from the public internet` from [this](https://docs.microsoft.com/en-us/azure/storage/common/storage-private-endpoints) article. 
   - But then I read it was a [good idea to disable public access after enabling PEP](https://docs.microsoft.com/en-us/azure/storage/common/storage-network-security?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal). 
   - Regardless, the takeaway is that enabling PEP adds an option to access the endpoint but doesn't take away anything on its own. 
   - You must go out of your way to disable all other traffic if you wish to restrict access to ONLY go through the PEP.

1. So this is the runbook I wrote to do just that - It will loop through all subscriptions and if a Storage Account has at least one PEP, it will set it to where all traffic has to go through the PEP :


   ```powershell
   Try
   {
      "Logging in to Azure..."
      # https://docs.microsoft.com/en-us/azure/automation/enable-managed-identity-for-automation
      Disable-AzContextAutosave -Scope Process
      $AzureContext = (Connect-AzAccount -Identity).context
      $AzureContext = Set-AzContext -SubscriptionName $AzureContext.Subscription -DefaultProfile $AzureContext
      "Logging in to Azure...Completed"
   }
   Catch 
   {
      Write-Error -Message $_.Exception
      throw $_.Exception
   }

   $Subscriptions = Get-AzSubscription -DefaultProfile $AzureContext

   Foreach ( $Subscription in $Subscriptions)
   {
      $CurrentContext = Set-AzContext -Subscription $($Subscription.Name)
      Write-Output "Processing Subscription: $($Subscription.Name)"
      $StorageAccounts = Get-AzStorageAccount -DefaultProfile $CurrentContext
      If ( $StorageAccounts.count -gt 0 )
      {
         Foreach ( $StorageAccount in $StorageAccounts )
         {
            Write-Output "Processing: $($StorageAccount.StorageAccountName)"
            Write-Output "Checking if Storage Account has Private Endpoint Enabled..."
            $PEP = Get-AzPrivateEndpointConnection -PrivateLinkResourceId $($StorageAccount.Id)

            If ( $null -eq $PEP )
            {
               Write-Output "Storage account does not have a Private Endpoint, moving on ...."
            }
            Else
            {
               
               # There may be one or more peps, but we only need the first one to know to disable public network access so we access it via PEP[0]
               $Status = $($PEP[0].PrivateLinkServiceConnectionStateText) | ConvertFrom-Json

               If ( ($PEP[0].ProvisioningState -eq "Succeeded") -and ($($Status.Status) -eq "Approved") )
               {
                  Write-Output "Storage Account has Private Endpoint Enabled. Checking if Public Network Access is set to Disabled..."
                  If ( $($StorageAccount.PublicNetworkAccess) -eq "Disabled" )
                  {
                     Write-Output "Storage Account Public Network Access already set to Disabled"
                  }
                  Else
                  {
                     Write-Output "Setting network access to disabled..."
                     Set-AzStorageAccount -ResourceGroupName $($StorageAccount.ResourceGroupName) -Name $($StorageAccount.StorageAccountName) -PublicNetworkAccess "Disabled"
                     Write-Output "Setting network access to disabled...Completed"
                  }
               }
               Else
               {
                  Write-Output "Storage account does have a Private Endpoint, but it may not be approved. Moving on ...."
               }
            }
         }
      }
      Else
      {
         Write-Output "Subscription has no Storage Accounts"
      }
      Write-Output "=========================="
   }
   ```
