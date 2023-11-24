---
title: 'IDG: Create New App For Approvals'
date: 2020-02-20T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/idg-create-app-for-approvals
tags:
  - LocalSoftware
tags:
  - Scripting-RestAPI
---
<!--more-->


### Description

[Netiq Identity Governance](https://www.microfocus.com/en-us/products/netiq-identity-governance/overview#) (shortened to IDG) is a software that can pull in Identities and applications from your organization and determine if a user has too many permissions. One of the things we are currently using it for is an approval process for Service Now Catalog Items. The software is too complex to explain in a simple post, but start with reading [the admin guide](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/front.html) for more information.

So the workflow goes like this:
   - Azure Automation has two runbooks that run every minute:
     - One that scans Service Now table for a new request that matches a specific short description
     - One that scans IDG every minute for approval statuses

   - So a user fills out a Catalog Item in Service Now and a record is generated to the Request Table
   - Azure Automation detects the request and parses it
   - Azure Automation will send relevant details to IDG and to Table Storage tracking the status of the request
   - Another runbook is ran every minute that is completely unaware of the first runbook that scans the Table Storage for a request that has a status of 'not complete'. It then gets the IDG approval number and checks its status.
     - If the approver approved the request, it fulfills whatever action you want it to: Add user to group in AD, add user to Group in Azure, send a XML payload with information, send a REST API call with information, whatever you want
     - If the approver denied the request, go back to Service Now and close the request letting the ticket submitter know the request was denied.

So now that we know the workflow, we just need to connect Service Now to IDG using what is called 'permissions'. So IDG has the concept of 'Applications' which can be just about anything that it will parse and read in as a group of permissions. These permissions have unique GUIDs that IDG generates which is how we know to map Service Now to IDG. In this post, I will explain how to create a new CSV "Application" that IDG will read in. 

The reason for creating a CSV application is that we need some dummy data that IDG can approve and then once approved, we can do something with the approval. In this example, we have group membership in Azure AD that users can request to be added to in order to get a license assigned:

1. User requests to be added to the group 'mySpecialApp' in Azure AD by filling out a Service Now Catalog Item
2. Azure Automation will scan this and send it to IDG
3. IDG has an approval policy to lookup the user's manager. That person then approves the request
4. Azure Automation will scan this and connect to Azure AD and add the user to group 'mySpecialApp' which will assign them the license.

In our example, we will ssh to the app server running RHEL 7 and create a new application:

### To Resolve

1. On the server itself type `vi /csv/mySpecialApp.csv` and paste in:

   ```
   "PermissionID", "parentPermissionID", "PermissionOwner", "childPermissionId"
   "mySpecialAppSandbox","parentmySpecialAppSandbox", "gerryw", "childmySpecialAppSandbox"
   "mySpecialAppTest","parentmySpecialAppTest", "gerryw", "childmySpecialAppTest"
   "mySpecialAppProduction","parentmySpecialAppProduction", "gerryw", "childmySpecialAppProduction"
   ```

2. Inside IDG, go to Applications => Create New => mySpecialApp_Environment
   - Use CSV Permission Collector template
   - Collector name = mySpecialApp_Environment_Permissions
   - Fill in the information [guide](https://www.netiq.com/documentation/identity-governance-35/admin-guide/data/b1e5gtiu.html):

   ```
   Unique ID = parentPermissionId
   Permission ID from Source = PermissionId
   Permission Name = displayName
   Permission Description = description
   Permission Type = Type
   Assignable Permission = assignable
   Permission-owners mapping = PermissionOwner / Map to attribute "CN"
   Parent Permission ID = parentPermissionId
   Link to Child Permission(s) = childPermissionId
   clear out everything else
   ```

   - Save and run collection + publish collection

3. Go to Catalog => Permissions and paste in the owner 'Gerry' for each permission. While there, write down the `Internal Permission ID` by clicking on `more`. This is the unique GUID we will need when we send the request

4. Go to Policy => Access Request Policy => Request Policies
   Requestors = Check the box for all users
   Permissions tab => Add => Search and filter on "mySpecialApp_Environment" then add all the permissions

5. Go to Policy => Access Request Policy => Approval Policies
   - Approval Step #1 = Select Users and Groups => Gerry 
   - NOTE: This is only for testing, once this goes into production, you can map it to the requestors manager which it will look up because it is reading in from [Netiq Identity Manager](https://www.microfocus.com/en-us/products/netiq-identity-manager/overview) and Active Directory.
   - Permissions => Add => Search and filter on "mySpecialApp_Environment" then add all the permissions

6. Go to Fulfillment => Configuration => Fulfillment Targets => + => Call it `WriteToCSV` and have it write to `/csv/` locally.

7. Go to Fulfillment => Configuration => Application Setup tab => mySpecialApp Environment => WriteToCSV

8. Do a test in the GUI: Access Request => Request/Browse => Applications/mySpecialApp_Environment => mySpecialAppProduction => Add to Cart => Submit => YOu can confirm it works by checking `/csv/changeset_001.csv`  (number may be different) on the server and by seeing no error messages in the GUI!

9. Now that we know it works and we have the GUIDs, we can send POST requests to create approvals.

   - Incomplete example that shows the general idea:


   ```powershell
   Function New-IDGReqAddPerm
   {
      [CmdletBinding()]
      param (
         [string]$ReasonRequestNumber, 
         [string]$UniquePermValue, 
         [string]$ReasonDiscription, 
         [string]$PermDisplayName, 
         [string]$UniqueUserValue, 
         [string]$UserDisplayName
      )
      $token = Get-IDGToken
      $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
      $headers.Add("Content-Type", "application/json")
      $headers.Add("Accept", "application/json")
      $headers.Add("Authorization", "Bearer $($token.access_token)")
      $URI = 'https://server.domain.com:8443/api/request/request'
      $body = [ordered]@{
         "requestSource"        = "REQUEST"
         "requester"            = "502a94b79f2364d47688b9015364764d457173"
         "requesterDisplayName" = "myUser"
         "reason"               = $ReasonRequestNumber
         "requestItems"         = @( [ordered]@{
               "showSodViolations"              = $false
               "hideSodViolationsForSelected"   = $false
               "hideSodViolationsForAllPending" = $false
               "requestItem"                    = $UniquePermValue
               "reason"                         = $ReasonDiscription
               "displayName"                    = $PermDisplayName
               "type"                           = "PERMISSION"
               "recipient"                      = $UniqueUserValue
               "recipientDisplayName"           = $UserDisplayName
               "indexInCart"                    = 0
               "requestType"                    = "ADD_PERMISSION_TO_USER"
               "img"                            = "images/icon_permission.png"
               "violationsForAllPending"        = "[]"
               "violationsForSelected"          = "[]"
            })
      }
      $strBody = $body | ConvertTo-Json
      $params = @{
         "Headers" = $headers
         "Body"    = $strBody
         "Method"  = "Post"
         "URI"     = $URI
      }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      $req = Invoke-RestMethod @params
      Clear-IDGToken -RefreshToken $($token.refresh_token)
      return $req
   }
      
   Function New-IDGReqRemovePerm
   {
      [CmdletBinding()]
      param (
         [string]$ReasonRequestNumber, 
         [string]$UniquePermValue, 
         [string]$ReasonDiscription, 
         [string]$PermDisplayName, 
         [string]$UniqueUserValue, 
         [string]$UserDisplayName
      )
      $token = Get-IDGToken
      $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
      $headers.Add("Content-Type", "application/json")
      $headers.Add("Accept", "application/json")
      $headers.Add("Authorization", "Bearer $($token.access_token)")
      $URI = 'https://server.domain.com:8443/api/request/request'
      $body = [ordered]@{
         "requestSource"        = "REQUEST"
         "requester"            = "502a94b79f2364d47688b9015364764d457173"
         "requesterDisplayName" = "myUser"
         "reason"               = $ReasonRequestNumber
         "requestItems"         = @( [ordered]@{
               "showSodViolations"              = $false
               "hideSodViolationsForSelected"   = $false
               "hideSodViolationsForAllPending" = $false
               "requestItem"                    = $UniquePermValue
               "reason"                         = $ReasonDiscription
               "displayName"                    = $PermDisplayName
               "type"                           = "PERMISSION"
               "recipient"                      = $UniqueUserValue
               "recipientDisplayName"           = $UserDisplayName
               "indexInCart"                    = 0
               "requestType"                    = "REMOVE_PERMISSION_ASSIGNMENT"
               "img"                            = "images/icon_permission.png"
               "violationsForAllPending"        = "[]"
               "violationsForSelected"          = "[]"
            })
      }
      $strBody = $body | ConvertTo-Json
      $params = @{
         "Headers" = $headers
         "Body"    = $strBody
         "Method"  = "Post"
         "URI"     = $URI
      }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      $req = Invoke-RestMethod @params
      Clear-IDGToken -RefreshToken $($token.refresh_token)
      return $req
   }
   ```

   - You can see what endpoints to call by navigating to your IDG server's Swagger UI `https://server.domain.com:8443/doc/`