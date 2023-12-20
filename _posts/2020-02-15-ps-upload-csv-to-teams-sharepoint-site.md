---
title: 'PS: Upload CSV To Teams Sharepoint Site'
date: 2020-02-15T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/ps-upload-csv-to-teams-sharepoint-site
tags:
  - Windows
tags:
  - Powershell
  - RestAPI
---
<!--more-->

### Description:

As the title suggests, put the following snippets in a script if you want to upload a file to a Sharepoint Teams folder. Note that I have a service account added to my team in Teams and had to use the `connect as user` instead of `connect as application` method to Graph API which is not what I usually do. For it, you use the same `New-MSGraphAPIToken` function, but it is slightly tweaked:

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
         [string]$TenantID,
         [parameter(mandatory = $true)]
         [string]$Username,
         [parameter(mandatory = $true)]
         [string]$Password

      )
      $body = @{
         Grant_Type    = "Password"
         client_Id     = $clientID
         Client_Secret = $clientSecret
         Username      = $Username
         Password      = $Password
         Scope         = "https://graph.microsoft.com/.default"
      }
      $oauth = Invoke-RestMethod -Method Post -Uri https://login.microsoftonline.com/$TenantID/oauth2/v2.0/token -Body $body
      $token = @{'Authorization' = "$($oauth.token_type) $($oauth.access_token)" }    
      Return $token
   }
   ```

For reference, here is how you would connect as an application

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
   ```


### To Resolve:

1. Using the first function above, put it in your `Begin{}` block and then in your process block, put the following:

   - As always [Read the API first](https://docs.microsoft.com/en-us/graph/api/driveitem-put-content?view=graph-rest-1.0&tabs=http)

   ```powershell
   $token = New-MSGraphAPIToken -clientID $clientID -clientSecret $clientSecret -tenantID $tenantID -Username "myUser@domain.com" -Password $password

   # Perform the upload
   $uri = "https://graph.microsoft.com/v1.0/drives/drive-id/items/item-id:/phoneNumbers.csv:/content" 

   $ContentType = "text/plain"
   Invoke-RestMethod -Method Put -headers $token -Uri $uri -InFile $file -ContentType $ContentType
   ```

2. To change the upload from `csv` or `txt` to use an Excel document, change `text/plain` to `application/octet-stream`. This has been tested and confirmed to work.

