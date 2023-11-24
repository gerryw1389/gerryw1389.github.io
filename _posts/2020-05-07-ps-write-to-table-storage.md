---
title: 'PS: Write To Table Storage'
date: 2020-05-07T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/ps-write-to-table-storage
tags:
  - Azure
tags:
  - Scripting-Powershell
  - Azure-StorageAccounts
  - Scripting-RestAPI
---
<!--more-->

### Description

Azure Storage Accounts can host table storage that scripts can use for temp or long term placement. In the move to replace VRO with Azure Automation, we decided to treat table storage similar to that of Resource Elements in VRO.

### To Resolve

1. Here are functions you can use:

   ```powershell
   Function Get-StorageAccountName
   {
      $cred = Get-AutomationPSCredential -Name 'storage info'
      $val = $cred.UserName
      return $val
   }

   Function Get-StorageAccountKey
   {
      $cred = Get-AutomationPSCredential -Name 'storage info'
      $val = $cred.GetNetworkCredential().Password
      return $val
   }

   $storageAccount = (Get-StorageAccountName)
   $accesskey = (Get-StorageAccountKey)

   
   function Get-AllRows($TableName)
   {
      $version = "2017-04-17"
      $resource = "$tableName"
      $table_url = "https://$storageAccount.table.core.windows.net/$resource"
      $GMTTime = (Get-Date).ToUniversalTime().toString('R')
      $stringToSign = "$GMTTime`n/$storageAccount/$resource"
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Convert]::FromBase64String($accesskey)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($stringToSign))
      $signature = [Convert]::ToBase64String($signature)
      $headers = @{
         'x-ms-date'    = $GMTTime
         Authorization  = "SharedKeyLite " + $storageAccount + ":" + $signature
         "x-ms-version" = $version
         Accept         = "application/json;odata=fullmetadata"
      }
      $item = Invoke-RestMethod -Method GET -Uri $table_url -Headers $headers -ContentType application/json
      return $item.value
   }

   # Write-Output "Getting all rows"
   # $tableItems = Get-AllRows -TableName "Workflows"


   function Get-SingleRow($TableName, $PartitionKey, $RowKey)
   {
      $version = "2017-04-17"
      $resource = "$tableName(PartitionKey='$PartitionKey',RowKey='$Rowkey')"
      $table_url = "https://$storageAccount.table.core.windows.net/$resource"
      $GMTTime = (Get-Date).ToUniversalTime().toString('R')
      $stringToSign = "$GMTTime`n/$storageAccount/$resource"
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Convert]::FromBase64String($accesskey)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($stringToSign))
      $signature = [Convert]::ToBase64String($signature)
      $headers = @{
         'x-ms-date'    = $GMTTime
         Authorization  = "SharedKeyLite " + $storageAccount + ":" + $signature
         "x-ms-version" = $version
         Accept         = "application/json;odata=fullmetadata"
      }
      $item = Invoke-RestMethod -Method GET -Uri $table_url -Headers $headers -ContentType application/json
      return $item.value
   }

   # Write-Output "Getting single row"
   # $tableItem = Get-SingleRow -TableName "Workflows" -RowKey "example-service-now-info" -PartitionKey "REQ00000346"
   
   function New-Row($TableName, $PartitionKey, $RowKey, $Entity)
   {
      $version = "2017-04-17"
      $resource = "$tableName(PartitionKey='$PartitionKey',RowKey='$Rowkey')"
      $table_url = "https://$storageAccount.table.core.windows.net/$resource"
      $GMTTime = (Get-Date).ToUniversalTime().toString('R')
      $stringToSign = "$GMTTime`n/$storageAccount/$resource"
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Convert]::FromBase64String($accesskey)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($stringToSign))
      $signature = [Convert]::ToBase64String($signature)
      $headers = @{
         'x-ms-date'    = $GMTTime
         Authorization  = "SharedKeyLite " + $storageAccount + ":" + $signature
         "x-ms-version" = $version
         Accept         = "application/json;odata=fullmetadata"
      }
      $body = $entity | ConvertTo-Json
      $item = Invoke-RestMethod -Method PUT -Uri $table_url -Headers $headers -Body $body -ContentType application/json
   }

   <#
   Write-Output "Creating a new table entity"
   $body = @{
      RowKey       = "example-service-now-info"
      PartitionKey = "REQ00000346"
      Status       = "waiting"
      Value        = '{ "blah" = "bob"}'
   }
   New-Row -TableName "Workflows" -RowKey "example-service-now-info" -PartitionKey "REQ00000346" -entity $body
   #>

   function Update-Row($TableName, $PartitionKey, $RowKey, $entity)
   {
      $version = "2017-04-17"
      $resource = "$tableName(PartitionKey='$PartitionKey',RowKey='$Rowkey')"
      $table_url = "https://$storageAccount.table.core.windows.net/$resource"
      $GMTTime = (Get-Date).ToUniversalTime().toString('R')
      $stringToSign = "$GMTTime`n/$storageAccount/$resource"
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Convert]::FromBase64String($accesskey)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($stringToSign))
      $signature = [Convert]::ToBase64String($signature)
      $body = $entity | ConvertTo-Json
      $headers = @{
         'x-ms-date'      = $GMTTime
         Authorization    = "SharedKeyLite " + $storageAccount + ":" + $signature
         "x-ms-version"   = $version
         Accept           = "application/json;odata=minimalmetadata"
         'If-Match'       = "*"
         'Content-Length' = $body.length
      }
      $item = Invoke-RestMethod -Method MERGE -Uri $table_url -Headers $headers -ContentType application/json -Body $body
   
   }

   <#
   Write-Output "Merging with an existing table entity"
   $body = @{
      RowKey       = "example-service-now-info"
      PartitionKey = "REQ00000346"
      Status       = "waiting"
      Value        = '{ "blah" = "bob"}'
   }
   Update-Row -TableName "Workflows" -RowKey "example-service-now-info" -PartitionKey "REQ00000346" -entity $body
   #>
   
   function Remove-Row($TableName, $PartitionKey, $RowKey)
   {
      $version = "2017-04-17"
      $resource = "$tableName(PartitionKey='$PartitionKey',RowKey='$Rowkey')"
      $table_url = "https://$storageAccount.table.core.windows.net/$resource"
      $GMTTime = (Get-Date).ToUniversalTime().toString('R')
      $stringToSign = "$GMTTime`n/$storageAccount/$resource"
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Convert]::FromBase64String($accesskey)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::UTF8.GetBytes($stringToSign))
      $signature = [Convert]::ToBase64String($signature)
      $headers = @{
         'x-ms-date'    = $GMTTime
         Authorization  = "SharedKeyLite " + $storageAccount + ":" + $signature
         "x-ms-version" = $version
         Accept         = "application/json;odata=minimalmetadata"
         'If-Match'     = "*"
      }
      $item = Invoke-RestMethod -Method DELETE -Uri $table_url -Headers $headers -ContentType application/http
   
   }
   # Write-Output "Deleting an existing table row"
   # Remove-Row -TableName "Workflows" -RowKey "example-service-now-info" -PartitionKey "REQ00000346"
   ```
