---
title: 'Azure Automation: VMList To Storage Account'
date: 2022-09-26T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/09/vm-list-with-storage-account
tags:
  - Azure
  - Terraform
tags:
  - Scripting-Powershell
  - Azure-Automation
---
<!--more-->

### Description:

So one task I wanted to setup after [deploying an Automation Account](https://automationadmin.com/2022/08/tf-create-aa-with-source-control) via Terraform was to show an example of how I can use the Automation Account to write blobs to a Storage Account.

### To Resolve:

1. First, just add a few resources to [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-20-tf-create-aa-with-source-control/main.tf) from before and then redeploy to Azure.

   ```terraform
   resource "azurerm_storage_account" "storage" {
      name                     = "storageaccountname"
      resource_group_name      = azurerm_resource_group.example.name
      location                 = azurerm_resource_group.example.location
      account_tier             = "Standard"
      account_replication_type = "GRS"
   }


   resource "azurerm_role_assignment" "storage_blob_contributor" {
      scope                = azurerm_storage_account.storage.id
      role_definition_name = "Storage Blob Data Contributor"
      principal_id         = azurerm_automation_account.aa.identity[0].principal_id
   }

   ```

1. Next I wrote a script that will upload a blob of all VMs for all subscriptions that my System Identity has read access to :

   ```powershell
   Import-Module Az.Automation
   Import-Module Az.Storage

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

   Set-AzContext -Subscription "my-subscription"

   Function Get-StorageAccountName
   {
      $val = (Get-AzAutomationVariable -Name "linked-storage-account" -AutomationAccountName "my-automation-account" -ResourceGroupName "my-automation-account-rg" -ErrorAction "Stop").value
      return $val
   }

   Try
   {
      $StorageAccountName = Get-StorageAccountName
   }
   Catch {
      Write-Output "Error while attempting to get StorageAccountName variable..."
      Write-Error "Exit"
   }

   # Generate a SAS so we can write to file later
   $StartTime = Get-Date
   $EndTime = $startTime.AddHours(1.0)
   $stgAccount = Get-AzStorageAccount -Name $StorageAccountName -ResourceGroupName "my-automation-account-rg" 
   Write-Output "Storage Account: $($stgAccount.StorageAccountName)"
   $SASToken = New-AzStorageAccountSASToken -Service "Blob" -ResourceType "Container","Object" -Permission "racwdlup" -startTime $StartTime -ExpiryTime $EndTime -Context $($StgAccount.Context)
   $stgcontext = New-AzStorageContext -storageAccountName $($stgAccount.StorageAccountName) -SasToken $SASToken

   $Subscriptions = Get-AzSubscription -DefaultProfile $AzureContext

   $VMList = [System.Collections.Generic.List[PSObject]]@()
   $Intro = 'Subscription,Subscription_ID,VM_Name,ResourceID' # Enter column names
   [void]$VMList.Add($Intro)

   Foreach ( $Subscription in $Subscriptions)
   {
      $CurrentContext = Set-AzContext -Subscription $($Subscription.Name)

      $SubscriptionName = $($CurrentContext.Subscription.Name)
      $SubscriptionID = $($CurrentContext.Subscription.Id)
      Write-Output "Current subscription: $SubscriptionName"

      $VMObjects = Get-AZVM -DefaultProfile $CurrentContext
      If ( $($VMObjects.count) -gt 0)
      {
         Foreach ( $VM in $VMObjects)
         {
            #Write-Output "Virtual machine name: $($VM.Name)" 

            $CSVRow = $SubscriptionName, $SubscriptionID, $($VM.Name), $($VM.Id) -join ","
            #Write-Output "Adding row to CSV: $CSVRow"
            [void]$VMList.Add($CSVRow)
         
         }
      }
      Else
      {
         Write-Output "Subscription has no VM objects" 

         $CSVRow = $SubscriptionName, $SubscriptionID, "null", "null" -join ","
         #Write-Output "Adding row to CSV: $CSVRow"
         [void]$VMList.Add($CSVRow)
      }
   }

   # 
   $OutputFileName = ((Get-Date -Format "yyyy-MM-dd") + "-vmlist.csv")
   Write-Output "Output file: $OutputFileName"
   $VMList | Out-File $OutputFileName -Encoding "ascii"

   Write-Output "Writing CSV and exiting..."
   Set-AzStorageBlobContent -File $OutputFileName -Container "vminventory" -Context $stgcontext -Force
   Write-Output "Writing CSV and exiting...Completed"
   ```
