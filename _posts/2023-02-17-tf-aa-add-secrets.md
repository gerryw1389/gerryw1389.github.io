---
title: 'Terraform: Adding Secrets To Azure Automation Accounts'
date: 2023-02-17T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/02/tf-aa-add-secrets
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

Let's say you have an Azure Automation Account you [managed with Terraform](https://automationadmin.com/2022/08/tf-create-aa-with-source-control) and you need to add a secret from a Key Vault to the Automation Account as a variable for your runbooks. 

I will display how you could do it by passing a secret called `my-api-username` and `my-api-secret` from your Azure Devops Libary that is linked to a Keyvault. It is assumed that you created these secrets and populated them with `dummy` data at first because we will display them in a runbook further down. Once you verify everything we will update them to the real values. Anyways, here are the steps:

### To Resolve:

1. Inside your pipeline, give it permissions to the keyvault in the `variables - group` area and then in the `terraform plan` and `terraform apply` sections add the new secret as an environmental variable like so:

   ```yaml
      TF_VAR_api_username: $(my-api-username)
      TF_VAR_api_password: $(my-api-secret)
   ```

1. Then in the landing spot for your TF files, add the new variable definitions so that Terraform knows about them:

   ```terraform
   # Requried Vars
   variable "api_username" {
   description = "(Required) The Active Directory account that has My API Access."
   type        = string
   }

   variable "api_password" {
   description = "(Required) The Active Directory account password that has My API Access."
   type        = string
   }
   ```

1. Then, in your [aa-variables.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-20-tf-create-aa-with-source-control/aa-variables.tf) add them like so:

   ```terraform
   resource "azurerm_automation_variable_string" "api_user_password" {
   name                    = "api-user-password"
   resource_group_name     = azurerm_resource_group.aa_rg.name
   automation_account_name = azurerm_automation_account.aa.name
   value                   = var.api_password
   encrypted               = true
   }
   ```

1. Now create a runbook that will display them just to ensure the secret is being passed correctly.

   ```powershell

   # WARNING!!! This runbook shows values of encrypted variables and should only be used for troubleshooting only!!!

   $ErrorActionPreference = "Stop"
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

   # get from Variables blade of Automation Account
   Function Get-MyVar
   {
      $val = (Get-AzAutomationVariable -Name "tfex-example-var-1" -AutomationAccountName "aa-sbx-scus-aa" -ResourceGroupName "aa-sbx-scus-aa-rg" -ErrorAction "Stop").value
      return $val
   }

   Function Get-MyVar2
   {
      # https://learn.microsoft.com/en-us/azure/automation/shared-resources/variables?tabs=azure-powershell#powershell-cmdlets-to-access-variables
      $val = Get-AutomationVariable -Name "api-user-name"
      return $val
   }

   Function Get-MyVar3
   {
      # https://learn.microsoft.com/en-us/azure/automation/shared-resources/variables?tabs=azure-powershell#powershell-cmdlets-to-access-variables
      $val = Get-AutomationVariable -Name "api-user-password"
      return $val
   }


   Write-Output "Example reading vars...."

   Try
   {
      Write-Output "Getting var..."
      $varValue = Get-MyVar
      Write-Output "Getting var...Completed"
   }
   Catch
   {
      Write-Output "Error while reading variable..."
      Write-Error "Exit"
   }

   Write-Output "Variable value: $varValue"

   Try
   {
      Write-Output "Getting var2..."
      $varValue = Get-MyVar2
      Write-Output "Getting var2...Completed"
   }
   Catch
   {
      Write-Output "Error while reading variable2..."
      Write-Error "Exit"
   }

   Write-Output "Variable2 value username: $varValue"

   Try
   {
      Write-Output "Getting var3..."
      $varValue = Get-MyVar3
      Write-Output "Getting var3...Completed"
   }
   Catch
   {
      Write-Output "Error while reading variable3..."
      Write-Error "Exit"
   }

   Write-Output "Variable3 user pass value: $varValue"
   ```

   - Note that regular secrets can be accessed vai `Get-AzAutomationVariable` but encrypted ones are accessed via `Get-AutomationVariable`. Follow the footnote in the [link](https://learn.microsoft.com/en-us/azure/automation/shared-resources/variables?tabs=azure-powershell#powershell-cmdlets-to-access-variables) where it says *"You can't use this cmdlet to retrieve the value of an encrypted variable. The only way to do this is by using the internal Get-AutomationVariable cmdlet in a runbook or DSC configuration."*.