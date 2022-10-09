---
title: Using Azure Key Vault
date: 2020-05-22T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/using-azure-key-vault
categories:
  - Azure
tags:
  - Cloud
  - Azure-KeyVault
---
<!--more-->

### Description:

So inside an Azure Automation Account, you can call credentials securely but what about if you are using other services in Azure? For example, I have [a data gateway](https://automationadmin.com/2020/05/automation-with-azure-data-gateway) that needs to run automation but I need to connect to systems securely. Enter Azure Keyvault. This is how I set it up:

### To Resolve:

1. Create the Key Vault in the GUI => create it to where only one user and one app can access (mine was set to the Azure Data Gateway user from that post). Set it to public selected networks and that means only a VM within that network can do anything.

2. On a VM within the private network you selected, install the `Az` powershell module ( `Install-Module Az -AllowClobber` )

3. Send CliXML credentials to file system:

   ```powershell
   # Encryption using same computer same account (using DPAPI)
   $username = "domain\myUser"
   $password = ConvertTo-SecureString -AsPlainText -Force "Pa$$word"
   New-Object System.Management.Automation.PSCredential($username,$password ) | 
   Export-CliXml "c:\scripts\admin.xml"
   ```

4. Now, using any Logic Apps or Powershell scripts on that server, you just put the following in the begin block:

   - To get a plain text password:

   ```powershell
   Import-Module Az.KeyVault

   $cred = Import-Clixml -Path "c:\scripts\admin.xml"
   Connect-AzAccount -Credential $cred

   Function Get-MyKey
   {
   $v = Get-AzKeyVaultSecret -VaultName 'my-vault' -Name 'test-api'
   $val = $($v.SecretValueText)
   return $val
   }

   # $apiKey = Get-Mykey
   ```

   - To get a SecureString do the same thing but use `$($v.SecretValue)` instead.

5. To set a new password in the Key Vault, you have two options:

   - Inside a VM on the network you restricted to, login to Azure Portal and do stuff in GUI

     - NOTE: I kept getting '403 forbidden' when I went to portal.azure.com from the VM in IE and found that the private network endpoint I created didn't stick. I added it again and clicked save. Seems to work now.
     {: .notice--success}

   - Use Powershell:

   ```powershell
   Import-Module Az.KeyVault
         
   $cred = Import-Clixml -Path "c:\scripts\admin.xml"
   Connect-AzAccount -Credential $cred

   $s = 'blah'
   $secretValue = ConvertTo-SecureString -String $s -AsPlainText -Force
   $Params = @{
      'VaultName'     = 'my-vault'
      'Name'          = 'my-api'
      'SecretValue'   = $secretValue
   }
   Set-AzKeyVaultSecret @params 
   # creates 'my-api' with value of 'blah'
   ```
