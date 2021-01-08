---
title: Rename Hybrid AD Autopilot Device
date: 2020-06-04T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/rename-hybrid-ad-autopilot-device
categories:
  - Azure
  - Windows
tags:
  - Scripting-RestAPI
  - Scripting-Powershell
  - Azure-Intune
---
<!--more-->

### Description:

So the goal of this post is to clarify what all we tried for renaming devices joined using Hybrid Azure AD Join. [Per Microsoft](https://docs.microsoft.com/en-us/mem/intune/remote-actions/device-rename), renaming hybrid devices is not yet supported:

   - ![Not Supported](https://automationadmin.com/assets/images/uploads/2020/06/intune-3.jpg){:class="img-responsive"}

### To Resolve:

1. First thing I wanted to do is find `Device Name` and `Group Tag` from the Intune portal via code:

   - Image:
   - ![Intune Device Info](https://automationadmin.com/assets/images/uploads/2020/06/intune-1.jpg){:class="img-responsive"}

   - So I installed a bunch of modules and tried a bunch of commands and couldn't find this information anywhere:

   ```powershell
   Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
   Install-Module AzureAD -Force
   Install-Module WindowsAutopilotIntune -Force
   Install-Module Microsoft.Graph.Intune -Force
   #Install:
   #ActiveDirectory
   #MSOnline

   Connect-MSGraph
   Connect-AutopilotIntune
   Connect-MsolService
   Connect-AzureAD

   $device = Get-AutopilotDevice -serial "some-serialnumber"
   $managedDeviceID = $($device.managedDeviceID)
   
   Get-MsolDevice -DeviceID $managedDeviceID
   Get-MsolDevice -DeviceId $device.azureActiveDirectoryDeviceId

   Get-IntunemanagedDevice -managedDeviceId "some-guid" | select *

   Get-AzureADUserRegisteredDevice -ObjectId "some-guid"
   
   $a = Get-AzureADDevice -ObjectId "some-guid"
   $a |select *

   ```

   - None of these would get me that information! So frustrating!


2. I finally decided to open up Network tools in Firefox and see what REST calls my browser was making to get that information and was able to track it down:

   - ![Intune Graph API](https://automationadmin.com/assets/images/uploads/2020/06/intune-2.jpg){:class="img-responsive"}

3. I then translated this into Powershell and tested different device serial numbers. See code below for implementation but for now I needed to find a way to run this on the client device itself. That is where I found [this great post](https://oofhours.com/2020/05/19/renaming-autopilot-deployed-hybrid-azure-ad-join-devices/)


   - First, we have to allow client devices to rename themselves:
     - Right click OU => Delegate Access
     - Add `SELF` and check names, should go to `NT Authority\SELF`
     - Task to Delegate => Create custom
     - Choose "Computer objects" from the list of object types.
     - Check "Read All Properties" and "Write All Properties" to enable renaming.
     - Complete

   - Next, created an application in Azure that can read Device data:

     - App Registrations => ReadData
     - Generate Client Secret => $secretKey
     - Copy Client ID => some guid
     - Add Permissions => 
       - Permission:
       - Device.Read.All - Application - Read all devices
       - DeviceManagementApps.Read.All - Application - Read Microsoft Intune apps
       - DeviceManagementConfiguration.Read.All - Application - Read Microsoft Intune device configuration and policies
       - DeviceManagementManagedDevices.PrivilegedOperations.All - Application - Perform user-impacting remote actions on Microsoft Intune devices
       - DeviceManagementManagedDevices.Read.All - Application - Read Microsoft Intune devices
       - DeviceManagementRBAC.Read.All - Application - Read Microsoft Intune RBAC settings
       - DeviceManagementServiceConfig.Read.All - Application - Read Microsoft Intune configuration
       - User.Read - Delegated - Sign in and read user profile
     - Grant access

   - Lastly, download the [poster's Github](https://github.com/mtniehaus/RenameComputer) locally


4. So the goal is to create a new Intune app and push that to the clients and have them renamed themselves according to the fields in step 1 set by a user manually when onboarding a device. Here are some changes made:


   - At the top, insert the Graph API function

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

   - Under `if $goodtogo` type:

   ```powershell
   Try
   {
      Write-Output "Getting graph token..."
         
      $params = @{
         'ClientID'     = 'someClientID'
         'ClientSecret' = 'someSecret'
         'TenantID'     = 'someTenant'
      }
      $token = New-MSGraphAPIToken @params
   }
   Catch
   {
      Write-Error "Unable to get graph token"
   }

   Try
   {
      $computerName = $env:computername
      Write-Output "Sending request to get serial number"
      $a = 'https://graph.microsoft.com/beta/deviceManagement/managedDevices?$filter=(Notes%20eq%20%27bc3e5c73-e224-4e63-9b2b-0c36784b7e80%27)%20and%20(contains(activationlockbypasscode,%20%27' + $computerName + '%27))'
      $params = @{
         Method      = 'Get'
         Uri         = $a
         Headers     = $token
         ErrorAction = "stop"
      }
      $request = Invoke-RestMethod @params
      $serial = $($request.value.serialnumber.ToString())
      Write-Output "Sending request to get serial number...Serial is $serial "
   }
   Catch
   {
      Write-Output "Sending request to get serial number failed"
   }

   Try
   {
      Write-Output "Sending request to get ID"
      $a = 'https://graph.microsoft.com/beta/deviceManagement/windowsAutopilotDeviceIdentities?$top=25&$filter=contains(serialNumber,' +
      "'" + $serial + "')"
      $params = @{
         Method      = 'Get'
         Uri         = $a
         Headers     = $token
         ErrorAction = "stop"
      }
      $request2 = Invoke-RestMethod @params
      $id = $($request2.value.id)
      Write-Output "Sending request to get ID...ID is $id"
   }
   Catch
   {
      Write-Error "Sending request to get ID failed"
   }

   Try
   {
      Write-Output "Sending request to get variables for rename"
      $a = 'https://graph.microsoft.com/beta/deviceManagement/windowsAutopilotDeviceIdentities/' + $id +
      '?$expand=deploymentProfile,intendedDeploymentProfile'
      $params = @{
         Method      = 'Get'
         Uri         = $a
         Headers     = $token
         ErrorAction = "stop"
      }
      $request3 = Invoke-RestMethod @params
      $groupTag = $($request3.groupTag)
      $displayName = $($request3.displayName)
      Write-Output "Sending request to get variables for rename...Completed"
      Write-Output "Group tag for this device: $groupTag"
      Write-Output "Display name for this device: $displayName"
   }
   Catch
   {
      Write-Error "Sending request to get variables for rename"
   }

   If ( $displayName.Contains("-") )
   {
      $splitDisplay = $displayName.Split("-")
      $newName = $groupTag + "-" + $splitDisplay[-1]
   }
   Else
   {
      $newName = $groupTag + "-" + $displayName
   }
   Write-Output "New name for this device: $newName"

   # Set the computer name
   Write-Output "Renaming computer to $newName"
   Rename-Computer -NewName $newName

   ```

   - Finally, build the app and deploy it => Open PS as administrator => `./makeapp.cmd`

5. Test and see