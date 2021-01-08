---
title: 'Azure Function App: Run Every Minute'
date: 2020-04-16T08:06:24-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/azure-function-app-run-every-minute
categories:
  - Azure
tags:
  - Cloud
  - Orchestration
  - Azure-FunctionApp
---
<!--more-->

### Description:

So if you ever have a runbook that you need to run often, like once a minute often, here is the workaround since the Web UI will only allow once an hour at most

### To Resolve:

1. Go to Automation Account => Runbooks => YourRunbook => Webhooks => Add Webhook
   - Create a web hook, copy URL - you only get one chance to see this so write it down
   - Make sure that it is set to run on your hybrid workers

2. Using Postman, use a Microsoft Graph API call to the webook and see if it works. Ensure that whatever user or application you are using has the permissions to execute runbooks. Honestly not sure what permissions are needed since this worked with [my generic Powershell Rest API application](https://automationadmin.com/2020/01/azure-create-ps-app/) and that app has no rights in my Azure subscription

3. Go to Function Apps => New 

   - Name: `run-every-minute`
   - Publish `code`, Runtime stack `powershell core`, version `6`
   - New Function => 'timer trigger'
	- Name: `default`
	- Schedule: `0 */1 * * * *`
   - Click on the function name above the word functions => Platform Features => Configuration
   - Add in the following environmental variables: `AzClientID = blah` and `AzClientSecret = blah` replacing `blah` with a clientID and clientSecret for an Azure app that has the ability to start runbooks via Rest API (as always, test this in Postman first!)

4. Then set your code, under the provided code:

   - Default code provided by Azure:

   ```powershell
   # Input bindings are passed in via param block.
   param($Timer)

   # Get the current universal time in the default string format
   $currentUTCtime = (Get-Date).ToUniversalTime()

   # The 'IsPastDue' porperty is 'true' when the current function invocation is later than scheduled.
   if ($Timer.IsPastDue) {
      Write-Host "PowerShell timer is running late!"
   }

   # Write an information log with the current time.
   Write-Host "PowerShell timer trigger function ran! TIME: $currentUTCtime"
   ```

   - Your code under it:

   ```powershell
   Function New-MSGraphAPIToken
   {
      <#
   .SYNOPSIS
   Acquire authentication token for MS Graph API
   .DESCRIPTION
   If you have a registered app in Azure AD, this function can help you get the authentication token
   from the MS Graph API endpoint. Each token is valid for 60 minutes.
   .PARAMETER ClientID
   This is the registered ClientID in AzureAD
   .PARAMETER ClientSecret
   This is the key of the registered app in AzureAD
   .PARAMETER TenantID
   This is your Office 365 Tenant Domain
   .EXAMPLE
   $graphToken = New-MSGraphAPIToken -ClientID <ClientID> -ClientSecret <ClientSecret> -TenantID <TenantID>
   The above example gets a new token using the ClientID, ClientSecret and TenantID combination
   .NOTES
   General notes
   #>
      param(
         [parameter(mandatory = $true)]
         [string]$ClientID,
         [parameter(mandatory = $true)]
         [string]$ClientSecret,
         [parameter(mandatory = $true)]
         [string]$TenantID
      )
      $body = @{grant_type = "client_credentials"; scope = "https://graph.microsoft.com/.default"; client_id = $ClientID; client_secret = $ClientSecret }
      $oauth = Invoke-RestMethod -Method Post -Uri https://login.microsoftonline.com/$TenantID/oauth2/v2.0/token -Body $body
      $token = @{'Authorization' = "$($oauth.token_type) $($oauth.access_token)" }    
      Return $token
   }

   $clientID = $env:AzClientID
   $clientSecret = $env:AzClientSecret
   $TenantId = 'your-org-guid-for-tenant-id'
   $token = New-MSGraphAPIToken -clientID $clientID -clientSecret $clientSecret -tenantID $tenantID

   $uri = "https://s5events.azure-automation.net/webhooks?token=someToken"

   Try
   {
      Write-Output "Sending request to run azure job"
      Invoke-RestMethod -Method POST -Uri $uri -Headers $token -ErrorAction Stop
      Write-Output "Sending request to run azure job - completed"
   }
   Catch
   {
      Write-Output "Unable to send request"
   }
   ```

5. Set your function app execution to run every minute: Go to Integrate tab and choose schedule: `0 */1 * * * *`

6. Just a note that if you set it to something like `0 */1 8-17 * * 1-5` which will run every minute between 8-5 M-F, it will not work if your timezone is not exactly UTC. You have to go to your function app => App Settings (Configuration) and add `WEBSITE_TIME_ZONE` with the value of `Central Standard Time` for instance.
