---
title: 'Powershell Function App AZ Module Issue'
date: 2022-10-06T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/10/ps-function-app-az-module-issue
tags:
  - Azure
tags:
  - Scripting-Powershell
  - Azure-FunctionApps
---
<!--more-->

### Description:

In this post, I will build on my [previous post](https://automationadmin.com/2022/08/tf-get-next-subnet) where I created a Powershell Function App that will get the next CIDR Range for a VNET. These are the steps I did to build the Function App in the GUI before using [terraform](https://automationadmin.com/2022/10/tf-deploy-ps-function-app) to deploy the Function App later through IaC.

### To Resolve:

1. So using the UI, I deployed a Powershell Function App using runtime `~4`. I then went to the [Code + Test](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal#test-the-function) blade and pasted in a basic HTTP template:

   ```powershell
   using namespace System.Net

   param($Request, $TriggerMetadata)
   Write-Output "Starting Function App Invocation..."

   $SubscriptionID = "some-guid"
   Set-AzContext -Subscription $SubscriptionID

   $name = $Request.Query.Name
   $json = @{
         "Details"      = "Successfully logged into development subscription"
         "proposedCIDR" = ""
         "name" = $name

   } | ConvertTo-Json
   Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
         StatusCode     = [HttpStatusCode]::OK
         Body = $json
         
   })
   ```

   - Notice that I'm calling the `Set-AzContext` cmdlet because my Function App will be using a Managed Identity to read VNETs.
   - At this point in the development, I did not pass anything into the `Query` property of the `$Request` object because I wanted to isolate tesing `Az` cmdlets first.


1. Well before you can use any `Az` cmdlets, you have to enable a few things:

   - First, the [`host.json`](https://github.com/gerryw1389/PS-FindNextCIDRRange/blob/main/host.json) `managedDependency` needs `Enabled: true` to that the Function App run time will automatically download/install any modules you specify.
   - Next, you specify modules in the [`requirements.psd1`](https://github.com/gerryw1389/PS-FindNextCIDRRange/blob/main/requirements.psd1). Usually the `Az` module is enough, more on that next.
   - That's it in general, but I had a few more steps since the goal is to read a VNET I had to:
     - Enable System Managed Identity for the Function App
     - Set `Reader` role of the Function App Managed Identity to the VNET I was targeting.

1. So the issue I had is that even with that simple HTTP script in step 1, I kept getting errors like:

   ```escape
   Result: Failure Exception: Failed to install function app dependencies. Error: 'Failed to install function app dependencies. Error: 'The running command stopped because the preference variable "ErrorActionPreference" or common parameter is set to Stop: Unable to save the module 'Az'.'' Stack: at Microsoft.Azure.Functions.PowerShellWorker.DependencyManagement.DependencyManager.WaitOnDependencyInstallationTask() in D:\a\_work\1\s\src\DependencyManagement\DependencyManager.cs:line 246 at Microsoft.Azure.Functions.PowerShellWorker.DependencyManagement.DependencyManager.WaitForDependenciesAvailability(Func`1 getLogger) in D:\a\_work\1\s\src\DependencyManagement\DependencyManager.cs:line 164 at Microsoft.Azure.Functions.PowerShellWorker.RequestProcessor.ProcessInvocationRequest(StreamingMessage request) in D:\a\_work\1\s\src\RequestProcessor.cs:line 247
   ```

   - And I had set `'Az' = '8.2.0'` because that was one less the latest version as of the time of this post at [PowershellGallery](https://www.powershellgallery.com/packages/Az/8.2.0).

   - So Googling this error did not give me any good hits. I guess I'm just unfortuante that my powershell Function App is having issues loading the `Az` module. 

   - This is no surprise to me though, have you ever tried installing it? i.e. run `Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force` on a new machine? This takes like 10+ minutes and downloads like 30 submodules.

   - So I found that you have the option of [uploading](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell?tabs=portal#custom-modules) a Custom Module using the [Kudo Advanced tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#kudu) and uploading, but even that timed out when I was trying to upload my az.zip of all the az modules I had installed on my own machine that I had zipped.

   - This got me thinking, why do I even need that whole thing? So then I commented it out and looked up some recent versions of `Az.Accounts` and `Az.Network` instead and put those in the `requirements.psd1`. Then everything started working.

1. Moral of the story, only import submodules you need your Function App to do. Odd because many sites on the internet freely say to import `Az` parent instead. The easiest way to determine which modules you need is to lookup cmdlets used in your code and see what module they are part of.

   - For example [Set-AzContext](https://learn.microsoft.com/en-us/powershell/module/az.accounts/set-azcontext?view=azps-8.3.0) docs says its part of `Az.Accounts` module.
   - For example [Get-AZVirtualNetwork](https://learn.microsoft.com/en-us/powershell/module/az.network/get-azvirtualnetwork?view=azps-8.3.0) docs says its part of `Az.Network` module. You can see I need this in [line 1020](https://github.com/gerryw1389/PS-FindNextCIDRRange/blob/main/http/run.ps1#L1020) of the `run.ps1` Function App.