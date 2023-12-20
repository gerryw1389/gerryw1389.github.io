---
title: Connecting To Azure
date: 2022-05-20T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/azure-connect/
tags:
  - Azure
tags:
  - Powershell
---
<!--more-->

### Description

When it comes to connecting to Azure, there are two main ways people connect:

   - Using `az cli`
   - Using powershell with the `Az` module.

I would bookmark the [device login](https://microsoft.com/devicelogin) page since I use it often for interactive logins.

### To Resolve:

1. Here is how to use Powershell Az module for `interactive` powershell connection:

   ```powershell
   # Install the module if you haven't already
   Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

   Import-Module Az
   $sub = 'some-guid-subscription-id'
   Connect-AzAccount -SubscriptionId $sub -UseDeviceAuthentication

   # now connected, run something like
   Get-AZvm 

   ```

1. For Automation (no human interaction) using a Service Princple (Application Registration inside Azure AD), you will want to usually store `clientID`, `clientSecret`, and `tenantID` inside environmental variables and pass them securely to login to Azure. Here is an example logging this way:

   ```powershell
   param (
      $tenantId,
      $clientId,
      $Secret, 
      $subscription
   )

   $password = ConvertTo-SecureString $Secret -AsPlainText -Force
   $pscredential = New-Object System.Management.Automation.PSCredential ($clientId, $password)
   Connect-AzAccount -ServicePrincipal -Credential $pscredential -Tenant $tenantId

   $sub = Get-AzSubscription -TenantId $tenantId -SubscriptionId $subscription
   Set-AzContext -Subscription $sub

   Write-Output $sub.Name

   $vms = Get-AzVm
   Write-Output $vms
   ```

1. For Automation Accounts logging in using the Automation Account's RunAs Service Principle, I have seen this most commonly used:

   ```powershell
   [string] $FailureMessage = "Failed to execute the command"
   [int] $RetryCount = 3 
   [int] $TimeoutInSecs = 20
   $RetryFlag = $true
   $Attempt = 1

   do
   {
      $connectionName = "AzureRunAsConnection"
      try
      {
         Write-Output "Logging into Azure subscription using Az cmdlets..."
         
         # Get the connection "AzureRunAsConnection "
         $servicePrincipalConnection = Get-AutomationConnection -Name $connectionName         

         $AzureContext = Add-AzAccount `
            -ServicePrincipal `
            -TenantId $servicePrincipalConnection.TenantId `
            -ApplicationId $servicePrincipalConnection.ApplicationId `
            -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint 
         
         Write-Output "Successfully logged into Azure subscription using Az cmdlets..."

         $RetryFlag = $false
      }
      catch 
      {
         if (!$servicePrincipalConnection)
         {
            $ErrorMessage = "Connection $connectionName not found."

            $RetryFlag = $false

            throw $ErrorMessage
         }

         if ($Attempt -gt $RetryCount) 
         {
            Write-Output "$FailureMessage! Total retry attempts: $RetryCount"

            Write-Output "[Error Message] $($_.exception.message) `n"

            $RetryFlag = $false
         }
         else 
         {
            Write-Output "[$Attempt/$RetryCount] $FailureMessage. Retrying in $TimeoutInSecs seconds..."

            Start-Sleep -Seconds $TimeoutInSecs

            $Attempt = $Attempt + 1
         }   
      }
   }
   while ($RetryFlag)
   ```

1. Here is how to use az-cli for `interactive` powershell connection:

   ```shell
   az login --use-device-code
   az account set --subscription "some-guid-subscription-id"

   # To see context: az account show
   
   az vm list
   ```

1. I haven't written any automation that uses az cli for service account connections yet since I mostly use powershell with Azure Automation runbooks so I will come back to this for an example.

1. Connecting to AKS Cluster using powershell

   ```powershell
   # Install the module if you haven't already
   Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

   Import-Module Az
   $sub = 'some-guid-subscription-id'
   Connect-AzAccount -SubscriptionId $sub -UseDeviceAuthentication

   $cluster = Get-AzAksCluster -ResourceGroupName "cluster" -Name "name"
   Import-AzAksCredential -InputObject $cluster -Admin
   
   # This will write a context file to c:\users\yourUser\.kube\
   ```

1. Now you can use `kubectl` or `k9s` [to connect](https://automationadmin.com//2022/07/kubectl-k9s) and interact with your cluster using the context file.

1. Connecting to AKS Cluster using az-cli:

   ```shell
   az login --use-device-code
   az account set --subscription "some-guid-subscription-id"
   az aks get-credentials --resource-group my-cluster-rg --name my-cluster --admin
   ```
