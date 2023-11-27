---
title: Azure Automation PS Version Mismatch Woes
date: 2023-06-04T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/06/azure-automation-ps-version-mismatch-woes
tags:
  - Azure
  - Terraform
  - Azure-Automation
---
<!--more-->

### Description

When using Azure Automation, it is common for powershell to work on your computer but behave different when ran from the Azure Automation account in the portal. Windows 10 uses runtime `5.1` but the Az module version for Automation Accounts is only [8.0.0](https://www.powershellgallery.com/packages/Az/8.0.0) (you can see the on the Modules blade of an Automation Account in the portal). This causes many pain points so be aware. Also reference [this doc](https://learn.microsoft.com/en-us/azure/automation/automation-runbook-types?tabs=lps51%2Cpy27#limitations-and-known-issues) from Microsoft when you find yourself having issues coding runbooks. 

Anyhow, I would like to discuss an issue I had around 2023-08 where I was trying to get runbooks to shut down/start up AKS clusters...

For the scripts like `12x5-start-aks-appg.ps1` (link coming soon), I thought I could update them because they were using code like:

   ```powershell
   Set-Item Env:\SuppressAzurePowerShellBreakingChangeWarnings "true"

   try
   {
      "Logging in to Azure..."
      Connect-AzAccount -Identity
   }

   catch {
      Write-Error -Message $_.Exception
      throw $_.Exception
   }

   get-AzAksCluster | ForEach-Object {                       
   Get-AzResource -ResourceId $_.id } | Get-AzResource  | where { $_.Properties.Powerstate.code -eq "Running" -and $_.Properties.ProvisioningState -eq "Succeeded" -and $_.Tags.Schedule -eq "adhoc"} | 
   ForEach-Object { 
      Stop-AzAksCluster -Name $_.Name -ResourceGroupName $_.ResourceGroupName -AsJob 
      Get-AzApplicationGateway -ResourceGroupName $_.ResourceGroupName | Stop-AzApplicationGateway -AsJob}
   ```

But it turned out to me a lot more difficult than I had planned! Here is what happened:

### Steps

1. So first, I tried a more modern approach like:

   ```powershell
   # Step 1: Loop through all Clusters, filter based on tags, and stop them

   $Clusters = Get-AzAksCluster

   Write-Output "Processing $($Clusters.count) clusters..."

   $filteredClusters = $Clusters | Where-Object { $_.Powerstate.code -eq "Running" -and $_.ProvisioningState -eq "Succeeded" -and $_.Tags.Schedule -eq "adhoc" }

   if ( $null -eq $filteredClusters )
   {
      Write-Output "No Clusters meet criteria to continue..."
      Write-Output "Completed"
   }
   Else
   {
      Foreach ($Cluster in $filteredClusters )
      {
         Write-Output "Stopping cluster $($Cluster.Name) ..."
         Stop-AzAksCluster -Name $($Cluster.Name) -ResourceGroupName $($Cluster.ResourceGroupName) -AsJob
         Write-Output "Stopping cluster $($Cluster.Name) ...Completed"
         Write-Output "Stopping all App Gateways in $($Cluster.ResourceGroupName) ..."
         Get-AzApplicationGateway -ResourceGroupName $($Cluster.ResourceGroupName) | Stop-AzApplicationGateway -AsJob
         Write-Output "Stopping all App Gateways in $($Cluster.ResourceGroupName) ...Completed"
      }
   }
   ```

   - Clean and simple. Works on my machine when testing. But when it runs in the portal you get:

   ```escape
   Logging in to Azure...


   Mode             : Process
   ContextDirectory : 
   ContextFile      : 
   CacheDirectory   : 
   CacheFile        : 
   Settings         : {}

   Logging in to Azure...Completed

   Processing 1 clusters...

   No Clusters meet criteria to continue...

   Completed
   ```

1. I eventually found it was because it was not able to get the power state:

   ```powershell
   # Step 1: Loop through all Clusters, filter based on tags, and stop them

   $Clusters = Get-AzAksCluster

   Write-Output "Processing $($Clusters.count) clusters..."

   Write-output "Clusters:"
   Write-Output $Clusters

   $filteredClusters = $Clusters | Where-Object { $_.Powerstate.code -eq "Running" -and $_.ProvisioningState -eq "Succeeded" -and $_.Tags.Schedule -eq "adhoc" }

   Write-Output $filteredClusters

   Write-OUtput "Powerstate:"
   Write-Output $clusters[0].Powerstate.code

   ```

   - Produces

   ```escape
   Logging in to Azure...


   Mode             : Process
   ContextDirectory : 
   ContextFile      : 
   CacheDirectory   : 
   CacheFile        : 
   Settings         : {}

   Logging in to Azure...Completed

   Processing 1 clusters...

   Clusters:


   ProvisioningState       : Succeeded
   MaxAgentPools           : 100
   KubernetesVersion       : 1.25.6
   DnsPrefix               : aa-nonprd-scus-spk-aks
   Fqdn                    : aa-nonprd-scus-spk-aks-nwzpzdge.hcp.westus.azmk8s.io
   PrivateFQDN             : aa-nonprd-scus-spk-aks-nwzpzdge.hcp.westus.azmk8s.io
   AgentPoolProfiles       : {aksctrlplane, user1}
   WindowsProfile          : Microsoft.Azure.Commands.Aks.Models.PSManagedClusterWindowsProfile
   AddonProfiles           : {[azureKeyvaultSecretsProvider, 
                           Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAddonProfile], [azurepolicy, 
                           Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAddonProfile], 
                           [ingressApplicationGateway, 
                           Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAddonProfile], [omsagent, 
                           Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAddonProfile]}
   NodeResourceGroup       : MC_aa-nonprd-scus-spk-aks-rg-7gmwo_aa-my-akso_westus
   EnableRBAC              : True
   EnablePodSecurityPolicy : 
   NetworkProfile          : Microsoft.Azure.Commands.Aks.Models.PSContainerServiceNetworkProfile
   AadProfile              : Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAadProfile
   ApiServerAccessProfile  : Microsoft.Azure.Commands.Aks.Models.PSManagedClusterAPIServerAccessProfile
   IdentityProfile         : {[kubeletidentity, 
                           Microsoft.Azure.Commands.Aks.Models.PSManagedClusterPropertiesIdentityProfile]}
   Identity                : Microsoft.Azure.Commands.Aks.Models.PSManagedClusterIdentity
   LinuxProfile            : 
   ServicePrincipalProfile : Microsoft.Azure.Commands.Aks.Models.PSContainerServiceServicePrincipalProfile
   ResourceGroupName       : aa-nonprd-scus-spk-aks-rg-7gmwo
   Id                      : /subscriptions/2cf2f1ee-99712e83048/resourcegroups/aa-nonprd-scus-spk-aks-rg-7gm
                           wo/providers/Microsoft.ContainerService/managedClusters/aa-my-akso
   Name                    : aa-my-akso
   Type                    : Microsoft.ContainerService/ManagedClusters
   Location                : westus
   Tags                    : {[AppEnv, nonprd], [Apppoc, me@domain.com], [CC, 113], [Creation_Time, 
                           2023-03-16_07:52:27 PST]...}


   Powerstate:

   ```


1. So next, I thought, maybe you **have** to pipe to `Get-AzResource` by passing the ResourceId and then use that to get the power state:

   ```powershell
   $filteredClusters = @{}

   Foreach ($Cluster in $Clusters )
   {
      
      $currentCluster = Get-AzResource -ResourceId $($Cluster.Id)
      $powerstate = $($currentCluster.Properties.Powerstate.Code)
      $provisioning = $($Cluster.ProvisioningState)
      $sched = $($Cluster.Tags.Schedule)

      Write-Output "Processing $($Cluster.Name) ..."
      Write-Output "Resource ID: $($Cluster.Id) "
      Write-Output "Power State: $($Cluster.Powerstate.Code) "
      Write-Output "Provisioning State: $($Cluster.ProvisioningState) "
      Write-Output "Schedule Tag: $($Cluster.Tags.Schedule)"

      If ( $powerstate -eq "Running" -and $provisioning -eq "Succeeded" -and $sched -eq "adhoc")
      {
         Write-Output "Adding cluster to filtered clusters list:  $($Cluster.Name), $($Cluster.ResourceGroupName) "
         $filteredClusters.Add( $($Cluster.Name), $($Cluster.ResourceGroupName) )
      }
   }

   ```

   - The above was trimmed a little to show the line `$currentCluster = Get-AzResource -ResourceId $($Cluster.Id)`. This produced an error:

   ```escape
   Get-AzResource : No registered resource provider found for location 'westus' and API version '2023-08-02-preview' for type 'managedClusters'. The supported api-versions are '2017-08-31, 2018-03-31, 2018-08-01-preview, 2019-02-01, 2019-04-01, 2019-06-01, 2019-08-01, 2019-10-01, 2019-11-01, 2020-01-01, 2020-02-01, 2020-03-01, 2020-04-01, 2020-06-01, 2020-07-01, 2020-09-01, 2020-11-01, 2020-12-01, 2021-02-01, 2021-03-01, 2021-05-01, 2021-07-01, 2021-08-01, 2021-09-01, 2021-10-01, 2021-11-01-preview, 2022-01-01, 2022-01-02-preview, 2022-02-01, 2022-02-02-preview, 2022-03-01, 2022-03-02-preview, 2022-04-01, 2022-04-02-preview, 2022-05-02-preview, 2022-06-01, 2022-06-02-preview, 2022-07-01, 2022-07-02-preview, 2022-08-01, 2022-08-02-preview, 2022-08-03-preview, 2022-09-01, 2022-09-02-preview, 2022-10-02-preview, 2022-11-01, 2022-11-02-preview, 2023-01-01, 2023-01-02-preview, 2023-02-01, 2023-02-02-preview, 2023-03-01, 2023-03-02-preview, 2023-04-01, 2023-04-02-preview, 2023-05-01, 2023-05-02-preview, 2023-06-01, 2023-06-02-preview, 2023-07-01, 2023-07-02-preview'. The supported locations are 'australiacentral, australiacentral2, australiaeast, australiasoutheast, brazilsouth, brazilsoutheast, canadacentral, canadaeast, centralindia, centralus, eastasia, eastus, eastus2, francecentral, francesouth, germanynorth, germanywestcentral, japaneast, japanwest, jioindiacentral, jioindiawest, koreacentral, koreasouth, northcentralus, northeurope, norwayeast, norwaywest, polandcentral, qatarcentral, southafricanorth, southafricawest, southcentralus, southindia, southeastasia, swedencentral, switzerlandnorth, switzerlandwest, uaecentral, uaenorth, uksouth, ukwest, westcentralus, westeurope, westus, westus2, westus3'. StatusCode: 400 ReasonPhrase: Bad Request OperationID : a19e3844-c665-4246-9a2d-ba9890f9087b At line:38 char:22 + $currentCluster = Get-AzResource -ResourceId $($Cluster.Id) + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + CategoryInfo : CloseError: (:) [Get-AzResource], ResourceManagerCloudException + FullyQualifiedErrorId : Microsoft.Azure.Commands.ResourceManager.Cmdlets.Implementation.GetAzureResourceCmdlet
   ```

1. This is frustrating! Why can't the [Get-Azresource](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azresource?view=azps-10.2.0) cmdlet work with ResourceID, it is the main purpose of the cmdlet! So then I did some digging to see why the [Get-AzAKSCluster](https://learn.microsoft.com/en-us/powershell/module/az.aks/get-azakscluster?view=azps-10.2.0) cmdlet can't get the powerstate on its own. Well the module loaded in the Automation account is 4.1.0 per the Modules blade of the Automation Account.

   - So I then went to its [source](https://www.powershellgallery.com/packages/Az.Aks/4.1.0) and downloaded the nupkg and extracted. Unfortuntely everything is in dll's so I can't view.
   - I then wanted to look online to see what version the Automation Account returns when you run the Get-AzAks resource. 
   - So what you do is scroll down on the [cmdlet page](https://learn.microsoft.com/en-us/powershell/module/az.aks/get-azakscluster?view=azps-10.2.0) and go to the outputs section and you will see [PSKubernetesCluster](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.commands.aks.models.pskubernetescluster?view=az-ps-latest)
   - Next, you change the drop down on the left to `Azure - Powershell Commands => 5.9.0`. This seems to coorelate to Powershell 5 which matches the runtime of 5.1.
   - [Now](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.commands.aks.models.pskubernetescluster?view=az-ps-5) you can see where we get `ProvisioningState` and `Tags` but no power state.
   - Mystery solved. So how do we get the Power state?

1. So I went back to the [Get-AzResource](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azresource?view=azps-10.2.0) and found that I got the same thing on my machine when I passed in a `ResourceId`.

   ```escape
   Foreach ($Cluster in $Clusters )
   {
      $currentCluster = Get-AzResource -ResourceId $($Cluster.Id)
      $powerstate = $($currentCluster.Powerstate.Code)
      $provisioning = $($currentCluster.ProvisioningState)
      $sched = $($currentCluster.Tags.Schedule)

      Write-Output "Processing $($Cluster.Name) ..."
      Write-Output "Resource ID: $currentCluster "
      Write-Output "Power State: $powerstate "
      Write-Output "Provisioning State: $provisioning "
      Write-Output "Schedule Tag: $sched"

      If ( $powerstate -eq "Running" -and $provisioning -eq "Succeeded" -and $sched -eq "adhoc")
      {
         Write-Output "Adding cluster to filtered clusters list:  $($Cluster.Name), $($Cluster.ResourceGroupName) "
         $filteredClusters.Add( $($Cluster.Name), $($Cluster.ResourceGroupName) )
      }
   }
   Processing aa-my-akso ...
   Resource ID: Microsoft.Azure.Commands.ResourceManager.Cmdlets.SdkModels.PSResource
   Power State:
   Provisioning State:
   Schedule Tag: adhoc
   ```

   - Hmm, why am I getting the class `Microsoft.Azure.Commands.ResourceManager.Cmdlets.SdkModels.PSResource` instead of the actual resource id?
   - So then I decided to try `Get-AzResource -Name $($Cluster.Name) -ResourceGroupName $($Cluster.ResourceGroupName)` and that seemed to work. I got back an object. But when I checked its properties, it was null.

1. So then I googled "No properties returned for get-azresource" and found [this post](https://stackoverflow.com/questions/75375911/get-properties-for-an-object-returned-by-get-azresource-on-azure). 
   - The answer was to pass an `-ExpandProperties` switch to the cmdlet. Yeah right I thought, this Automation Account cmdlet is probably running an ancient version that doesn't support that switch but ran it anyways.
   - To my amazement, it worked! So there you have it, a single little switch allows us to the get the Powerstate which we can then plug in to our script and now we can shut down/start up AKS clusters.

