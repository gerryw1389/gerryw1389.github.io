---
title: 'Azure: Create Powershell App'
date: 2020-01-18T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/azure-create-ps-app/
categories:
  - Azure
tags:
  - Cloud
  - Scripting-RestAPI
---
<!--more-->

### Description:

In order to have a powershell script connect to Azure and perform a task, you must first create an application under your tenant in Azure and give it rights to do so. Then in your powershell scripts, you pass in the `clientSecret` key to use the app to manipulate objects in Azure. The beauty of this is that powershell will require no importing of modules and will use plain REST API's to connect to Azure from any machine. Here is how:

### To Resolve

1. Go to Azure => App Registrations => Create new

   ```escape
   App Registrations = CompanyPowershell
   clientID = store in Keypass
   objectID = store in Keypass
   client secret = store in Keypass
   ```

2. API Permissions => Add A Permission button
   - Microsoft Graph `Delegated` tab => Expand Directory, User, Group and check all options like 'read.writeall' and such
   - Microsoft Graph `Application` tab => Expand Directory, User, Group and check all options like 'read.writeall' and such
   - After they are all added, click the button `Grant admin consent for $Tenant`

3. Onetime - run the following to make sure the app has permissions:

   ```powershell
   # Install-Module MSOnline
   Connect-MSolService
   $ClientWebApp = Get-MsolServicePrincipal -AppPrincipalId "seeKeypassObjectID"
   Add-MsolRoleMember -RoleName "Company Administrator" -RoleMemberType ServicePrincipal -RoleMemberObjectId $ClientWebApp.objectID
   ```

4. Use Powershell to connect and get a token:

   ```powershell
   Function New-MSGraphAPIToken {
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
      [parameter(mandatory=$true)]
      [string]$ClientID,
      [parameter(mandatory=$true)]
      [string]$ClientSecret,
      [parameter(mandatory=$true)]
      [string]$TenantID
      )
      
      $body = @{grant_type="client_credentials";scope="https://graph.microsoft.com/.default";client_id=$ClientID;client_secret=$ClientSecret}
      $oauth = Invoke-RestMethod -Method Post -Uri https://login.microsoftonline.com/$TenantID/oauth2/v2.0/token -Body $body
      $token = @{'Authorization'="$($oauth.token_type) $($oauth.access_token)"}    
      Return $token
   }

   $ClientID = 'seeKeypass'
   $ClientSecret = 'seeKeypass'
   $tenantID= 'seeKeypass'
   $token = New-MSGraphAPIToken -clientID $clientID -clientSecret $clientSecret -tenantID $tenantID

   # example request
   $uri = "https://graph.microsoft.com/v1.0/users/email@domain.com"
   $request = Invoke-RestMethod -Method GET -Uri $uri -Headers $token
   ```

5. At this point, you can script Powershell to do anything you need in Azure using REST APIs only - no modules!

   - Example, add a user to a group

   ```escape
   # Get the ID of the user from previous step  - 7fe12cec-4355-42f5-8355-0e8f58ffd5b5
   # Get the id of the group using Azure Web UI or something: ex => HR d59b713a-0c78-4068-8bb5-648asdlloeb453cb1a
   GET https://graph.microsoft.com/v1.0/groups/d59b713a-0c78-4068-8bb5-648asdlloeb453cb1a
   # Use this Template to add a user to a group:
   POST url: https://graph.microsoft.com/v1.0/groups/{group_id}/members/$ref
   # NOTE: the `$ref` on the end is literal, you don't replace it with anything
   # Content-type: application/json
   # Content BODY string: {"@odata.id": "https://graph.microsoft.com/v1.0/users/{user_id}"}
   # where ... group_id - group object id
   # where user_id - user object id
   ```

6. [Here](https://github.com/gerryw1389/powershell/blob/master/gwNetworking/Public/Add-AzUserToAzGroup.ps1) is a function I have recently used this with.

