---
title: 'Github Actions: Unable To Read Private Key'
date: 2023-09-10T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/09/unable-to-load-priv-key-from-akv
tags:
  - Azure
  - Terraform
  - Azure-KeyVault
  - PKI
---
<!--more-->

### Description

A key goal I wish to accomplish with Github Actions is to set all the secrets I can in an Azure Key Vault and then only get them at run time to populate all the other secrets needed. I have been doing this for years with [Function Apps](https://automationadmin.com/2021/01/function-apps-get-secrets/) and other Azure services and wish to continue this strategy. Basically, the strategy works like this: `"Only store Azure Credentials as Env secrets and use those at runtime to populate more secrets"`. This way you can create a Service Principal with limited rights like ["Key Vault Secrets User"](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#key-vault-secrets-user) at the AKV level and then monitor it in Azure Active Directory to ensure it is only being used to access AKVs. 

Using that logic, I tried that in Github Actions since there is a way to store a Private Key in AKV under the secrets blade, but unfortunately, it gives various errors. So I ended up just leaving private keys as repo secrets and everything is working as expected. See below with what I tried:

### Steps

1. First, I uploaded secrets to AKV like usual for private key files:

   ```powershell
   function Add-Secret
   {
      param (
         [string][Parameter(Mandatory = $true)] $KeyVaultName = $(throw "The path to the file is required."),
         [string][Parameter(Mandatory = $true)] $SecretName = $(throw "The path to the file is required."),
         [string][Parameter(Mandatory = $true)] $FilePath = $(throw "The path to the file is required."),
         [System.Nullable[System.DateTime]][Parameter(Mandatory = $false)] $Expires,
         [switch][Parameter(Mandatory = $false)] $Base64 = $false
      )

      $isFileFound = Test-Path -Path $FilePath -PathType Leaf
      if ($false -eq $isFileFound)
      {
         Write-Error "No file could containing the secret certificate at '$FilePath'"
         return;
      }

      Write-Output "Creating KeyVault secret..."

      $secretValue = $null
      if ($Base64)
      {
         $content = Get-Content $filePath -AsByteStream -Raw
         $contentBase64 = [System.Convert]::ToBase64String($content)
         $secretValue = ConvertTo-SecureString -String $contentBase64 -Force -AsPlainText
      }
      else
      {
         $rawContent = Get-Content $FilePath -Raw
         $secretValue = ConvertTo-SecureString $rawContent -Force -AsPlainText
      }

      $secret = $null
      if ($Expires -ne $null)
      {
         $secret = Set-AzKeyVaultSecret -VaultName $KeyVaultName -SecretName $SecretName -SecretValue $secretValue -Expires $Expires -ErrorAction Stop
      }
      else
      {
         $secret = Set-AzKeyVaultSecret -VaultName $KeyVaultName -SecretName $SecretName -SecretValue $secretValue -ErrorAction Stop
      }

      $version = $secret.Version
      Write-Output "Secret '$SecretName' (Version: '$version') has been created."
   }


   Add-Secret -KeyVaultName "aa-prd-scus-hub-akv-v1" -SecretName "module-cosmosdb-key" -FilePath "C:\scripts\cosmosdb.txt"
   Add-Secret -KeyVaultName "aa-prd-scus-hub-akv-v1" -SecretName "oci-source-provider-key" -FilePath "C:\scripts\oci.txt"
   Add-Secret -KeyVaultName "aa-prd-scus-hub-akv-v1" -SecretName "module-rg-key" -FilePath "C:\scripts\rg.txt"
   ```

1. When it got to the [get-secrets](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L111) task, it then gave this error:

   ```escape
   9s
   Run az account set --subscription "prd-hub"
   b3BlbnNzaC1rZXktdjEAAA..Dd2U5fnIAAAAKmdpdEBnaXRodWIuY29tOkRlbHRhRGVudGFsQ0EvbW9kdW
   xlLnJnLmdpdAECAw==
   -----END OPENSSH PRIVATE KEY-----
   b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
   QyNTUxOQAAACDPVUYMyfZGzvmIZuH2c92s7xuAmsY46R3K3Quo4DC+2AAAALj5yik6+cop
   OgAAAAtzc2gtZW..QF
   -----END OPENSSH PRIVATE KEY-----
   Error: Unable to process file command 'output' successfully.
   Error: Invalid format 'b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
   ```

1. So then I thought, maybe it's the `--output tsv` option and I found online that there is a better switch, `none`, [that you can use for raw output](https://learn.microsoft.com/en-us/cli/azure/format-output-azure-cli#none-output-format):

1. Unfortunately, this gave a different set of errors:

   ```escape
   Run az account set --subscription "prd-hub"
   
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   Warning: Can't add secret mask for empty string in ##[add-mask] command.
   ```

   - And eventually:

   ```escape
   Run cd $GITHUB_WORKSPACE
   # github.com:22 SSH-2.0-babeld-f8b1fc6c
   # github.com:22 SSH-2.0-babeld-f8b1fc6c
   # github.com:22 SSH-2.0-babeld-f8b1fc6c
   # github.com:22 SSH-2.0-babeld-f8b1fc6c
   # github.com:22 SSH-2.0-babeld-f8b1fc6c
   Error loading key "/home/runner/.ssh/module_rg": error in libcrypto
   Error: Process completed with exit code 1.
   ```

1. One thing I have noticed is that in many circumstances, the `error in libcrypto` comes from the loading of the private key incorrectly. For example, I also got this when I had a shell script like:

   ```shell
   # Create key files from Repo Secrets:
   echo $SSH_KEY_MODULE_RG > ~/.ssh/module_rg
   echo $SSH_KEY_MODULE_COSMOSDB > ~/.ssh/module_cosmosdb
   ```
  
   - where the action was like:

   ```yaml
   - name: "Setup SSH Keys and known_hosts"
         run: |
            cd $GITHUB_WORKSPACE
            chmod +x ./.github/scripts/update_ssh_agent.sh
            ./.github/scripts/update_ssh_agent.sh
         env:
            SSH_AUTH_SOCK: /tmp/ssh_agent.sock
            SSH_KEY_MODULE_RG: ${/{ secrets.ssh_key_module_rg }}
            SSH_KEY_MODULE_COSMOSDB: ${/{ secrets.ssh_key_module_cosmosdb }}
   ```

   - NOTE: [Jekyll Liquid Filters](https://jekyllrb.com/docs/liquid/filters/) clash with [Github Variables](https://docs.github.com/en/actions/learn-github-actions/variables#using-contexts-to-access-variable-values) so replace all instances of `${/{` by removing the forward slash :)


   - The fix was to surround them in quotes after getting that `libcrypto` error:

   ```shell
   # Create key files from Repo Secrets:
   echo "$SSH_KEY_MODULE_RG" > ~/.ssh/module_rg
   echo "$SSH_KEY_MODULE_COSMOSDB" > ~/.ssh/module_cosmosdb
   ```

1. Anyways, I haven't spent too much energy on this so there may be an easy fix but for now I'm just going to set my PEM files as repo secrets. Just would prefer to follow my standard if possible.