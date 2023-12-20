---
title: 'PS: Rest APIs'
date: 2020-01-24T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/ps-rest-api/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So as I move more into Automation, I'm finding that many software vendors build their software with Rest API first, then CLI, then a web UI on top. This post is a way to interact with Rest API's from Powershell. I usually use this in combination with [PostMan](https://automationadmin.com/2019/10/postman-get-token/) when trying to code workflows in [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/).

When interacting with REST API's, you have multiple parts of a request but the main two are headers and body. For a `GET` request, you usually just need headers because you are just requesting information and not providing information. For `PUT` and `POST` requests, you almost always need something in the body. Body's can be JSON or x-www-form-urlencoded or other types. A good way to learn this is to play around with different software in your environment that offers Rest API's and use PostMan as a client on your machine.

Either way, in Powershell, you should mostly use not hashtables like you would think, but a `System.Collections.Generic.Dictionary` object which is very similar:

   ```powershell
   Connect-AzureAD
   $d = Get-AzureADUser -ObjectId "user@domain.com"
   $d | Select -ExpandProperty ExtensionProperty 

   # type is System.Collections.Generic.Dictionary, so we reference like a hashtable
   $d.ExtensionProperty["employeeUniqueId"]

   # to create one from scratch
   $d = New-Object 'system.collections.generic.dictionary[string,string]'

   $d.gettype()
   # IsPublic IsSerial Name                                     BaseType
   # -------- -------- ----                                     --------
   # True     True     Dictionary`2                             System.Object

   # to add a key
   $d["foo"] = "bar"

   $d | Format-Table -auto
   # Key   Value
   # ---   -----
   # foo   bar

   # as usual, see your different options by running `$d | gm`
   ```

Anyways, here are some examples:




### To Resolve

1. To just interact with a web service, do something like:
   
   ```powershell
   $text = ((Invoke-Webrequest -Uri "https://uselessfacts.jsph.pl/random.json?language=en" -UseBasicParsing).content | ConvertFrom-Json).text
   ```

2. To interact with a web service and pass a parameter, you can do something like (assuming you want 5 responses):

   ```powershell
   $text = ((Invoke-Webrequest -Uri "https://uinames.com/api/?amount=5" -UseBasicParsing).content | ConvertFrom-Json).name
   ```

3. Both of these work well since you don't have to have any headers in your request. Most APIs require authentication. In order to do that, they will have different standards. Here is an example with Basic Authentication which is real common:

   ```powershell
   $user = 'myUser'
   $pass = 'seeKeypass'
   $pair = "$($user):$($pass)"
   $encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
   $basicAuthValue = "Basic $encodedCreds"
   $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
   $headers.Add("Authorization", $basicAuthValue)
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
   $req = Invoke-RestMethod -Method GET -Uri "https://test.service-now.com/api/now/table/sc_request?sysparm_query=short_description%3DAccess%20Request&sysparm_limit=100&state=1" -Headers $headers
   $req | ConvertTo-Json
   ```

   - This is will return a JSON object from service now using the credentials for the user `myUser` and the password of `seeKeypass`

4. What you will see more often is Oauth 2.0 REST API's. They provide two main things in their response: an `access_token` and a `refresh_token`. I still need to read more on their meanings but for accessing them via code, use the following:

   - So Step 1 is to get a token:

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

   $ClientSecret = 'seeKeypass'
   $ClientID = 'your-application-client-id'
   $TenantID = 'your-tenant-in-azure'
   $token = New-MSGraphAPIToken -clientID $clientID -clientSecret $clientSecret -tenantID $tenantID -Username "myUser@domain.com" -Password $password
   ```
    
   - Next, use the `$token` variable ( a System.Collections.Generic.Dictionary object) to make one or more requests:

   ```powershell
   # example - adding user to group in Azure AD via Rest API
   $posturi = "https://graph.microsoft.com/v1.0/groups/$groupID/members/" + '$ref'
   $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
   $headers.Add("Authorization", $token["Authorization"])
   $headers.Add("Content-Type", "application/json")
   $jsonBody = @{ "@odata.id" = "https://graph.microsoft.com/v1.0/users/$userID" } | ConvertTo-Json
   Try
   {
      Invoke-RestMethod -Method Post -Uri $posturi -Headers $headers -Body $jsonBody
      Write-output "Adding user to group: Succeeded - $groupID"
   }
   Catch
   {
      Write-Output "Unable to complete the request"
   }
   ```

   - Finally, when reading the [WSDL](https://en.wikipedia.org/wiki/Web_Services_Description_Language) for a REST API, check and see if you have to `revoke` an API token after each call as well. This is not that uncommon, for example:

   ```powershell
   $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
   $headers.Add("Content-Type", "application/x-www-form-urlencoded")
   $refreshToken = "a;sdlfkjalk;dfja;lksf"
   $clientId = "myClient"
   $clientSecret = "mySecret"
   $body = "token=$refreshToken&client_id=$clientId&client_secret=$clientSecret"
   $response = Invoke-RestMethod 'https://some.endpoint.com/api/auth/oauth2/revoke' -Method 'POST' -Headers $headers -Body $body
   $response | ConvertTo-Json
   ```

   - Usually you will only have to request a token and then make one or more calls, but sometimes you may have to revoke it after each call as well if you are running API calls very often.

5. I have another example [here](https://automationadmin.com/2020/02/ps-upload-csv-to-teams-sharepoint-site)