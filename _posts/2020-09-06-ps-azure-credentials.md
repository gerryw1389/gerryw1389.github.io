---
title: 'PS: Azure Credentials'
date: 2020-09-06T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/ps-azure-credentials
tags:
  - Azure
tags:
  - Powershell
  - Azure-KeyVault
  - Azure-Automation
---
<!--more-->

### Description:

Currently, I have to write to different functions depending on where I'm pulling passwords from, feel free to use!

### To Resolve:

1. From Azure Key Vault (make sure the script is running as an Azure AD user who has access):

   ```powershell
   function Get-SNUserName
   {
      $v = Get-AzKeyVaultSecret -VaultName 'my-vault' -Name 'My-Credential'
      $p = $v.SecretValue
      $val = [System.Net.NetworkCredential]::new("", $p).Password
      return $val
   }
      
   function Get-SNPass
   {
      $v = Get-AzKeyVaultSecret -VaultName 'my-vault' -Name 'My-Credential'
      $p = $v.SecretValue
      $val = [System.Net.NetworkCredential]::new("", $p).Password
      return $val
   }
   ```

2. Inside the credentials blade inside an Azure Automation Account:

   ```powershell
   Function Get-AzureAdminUser
   {
      $cred = Get-AutomationPSCredential -Name 'My-Credential'
      $val = $cred.UserName
      return $val
   }

   Function Get-AdminPass
   {
      $cred = Get-AutomationPSCredential -Name 'My-Credential'
      $val = $cred.GetNetworkCredential().Password
      return $val
   }
   ```
