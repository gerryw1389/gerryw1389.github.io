---
title: Learning Rest API Examples
date: 2020-02-20T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/learning-rest-api-examples
tags:
  - LocalSoftware
tags:
  - Scripting-RestAPI
  - Scripting-Powershell
---
<!--more-->

### Description:

So in my [Previous post on Yealink](https://automationadmin.com/2019/10/yealink-rest-api), I was uploading devices to Yealink Management console which is great, but what if you just want to see if a device exists? Well here is how I would go from knowing nothing about how to accomplish the task to resolving it:


### To Resolve:

1. As always, start by reading the official API documents. In my experience, these are hit-or-miss in how helpful they are. Many times they define the API but don't give full examples like my site so it's hard to picture what they are asking.

2. A more common approach is to do as follows:

   - In firefox, open the developer tools - Usually `F12` key
   - Login to Yealink management portal via web UI and do a search by the MAC Address of a device
   - Go to networking tab and grab the URI and the params 'body'
   - Now that we have that info, create a powershell script to do it by looping through an array:

   ```powershell
   function get-device ($mac)
   {
      Write-output "processing $mac"
      $baseUri = 'https://api-dm.yealink.com:8445/'
      $apiUri = 'api/open/v1/manager/device/getList'
         
      $accessKeyId = 'seeKeePass'
      $accessKeySecret = 'seeKeePass'
                     
      # Generate header params
      $guid = [GUID]::NewGuid().ToString().Replace('-', '')
      $epochStart = New-Object DateTime 1970, 1, 1, 0, 0, 0, ([DateTimeKind]::Utc)
      $timeStamp = [int64](([DateTime]::UtcNow) - $epochStart).TotalMilliseconds
      
      # Build Headers hashtable
      $headers = @{ }
      $headers.Add('X-Ca-Key', $accessKeyId)
      $headers.Add('X-Ca-Nonce', $guid)
      $headers.Add('X-Ca-Timestamp', $timeStamp)
      
      # Build Body Object
      $body = @{
         "key"       = $mac
         "searchKey" = $mac
      }
      
      # Add signature to header hashtable
      $jsonBody = $body | ConvertTo-Json
      $md5hash = New-Object System.Security.Cryptography.MD5CryptoServiceProvider
      $sig = $md5hash.ComputeHash( [System.Text.Encoding]::UTF8.GetBytes($jsonBody) )
      $bodyB64Hash = [Convert]::ToBase64String( $sig )
      $headers.Add('Content-MD5', $bodyB64Hash)
      
      # Convert headers hashtable into array (sig requires array, invoke-restmethod requires hashtable)
      $headerArray = @()
      foreach ($key in $headers.keys)
      {
         $headerArray += "{0}:{1}" -f $key, $headers[$key]
      }
      
      # Build out string for signing. Values need to be sorte
      # TODO: Identify if whole block needs to be sorted after X-Ca headers, or just each section
      $strToSign = "POST`n"
      $strToSign += $(($headerArray | Sort-Object ) -join "`n") + "`n"
      $strToSign += $apiUri
      
      # Build out HMACSHA256 Signature
      $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
      $hmacsha.key = [Text.Encoding]::ASCII.GetBytes($accessKeySecret)
      $signature = $hmacsha.ComputeHash([Text.Encoding]::ASCII.GetBytes($strToSign))
      $signature = [Convert]::ToBase64String($signature)
      
      # Add signature to headers hashtable
      $headers.Add('X-Ca-Signature', $signature)
      
      # Build out URI to call, including parameters #
      $uri = $baseUri + $apiUri
      $Response = Invoke-RestMethod -Uri $uri -Headers $headers -ContentType 'application/json;charset=UTF-8' -Body $jsonBody -method Post
      
      #$Response
      #$Response.error.fieldErrors.msg
      # a lack of teh require parameter in the interface
      
      If ( $Response.ret -gt 0)
      {
         #Write-Output "success: $mac"
      }
      Else
      {
         Write-Output "failed: $mac"
      }
   }
      
   $array = @(
      '806BC05E414C',
      '806BC05E4101',
      '806BC0784A95'
   )
      
   foreach ($a in $array)
   {
      Write-Output "working: $a"
      get-device -mac $a
      Start-Sleep -seconds 1
   }
   ```

   - To me, the hardest part about Rest APIs is finding out how to create the authorization headers for the API. If you can get successful responses once from an API endpoint, then it's just a matter of reading what API to hit and what to send.