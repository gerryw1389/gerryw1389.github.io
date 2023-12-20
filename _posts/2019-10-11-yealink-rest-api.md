---
title: Yealink Rest API
date: 2019-10-11T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/yealink-rest-api
tags:
  - WebSoftware
tags:
  - RestAPI
---
<!--more-->

### Description:

Yealink is a Voip Phone manufacturer that my organization uses. The following is a guide on how to use Postman or Powershell to add a device to their management console.

### To Resolve:

1. Example, to use GET in Postman to get a device's details

   - In Postman, in the top right corner is the environment section
   - Create yourself a new environment for the Yealink Device Manager, and add the AccessKeyID and AccessKeySecret.
   - Next, in the GET request, fill in the following pre-request script but change the `'id=exampleID'` to an ID from a phone in that you can get in the URL of the web GUI for an individual device:

   ```javascript
   // Get key/secret
   var MyKey = pm.environment.get('AccessKeyID');
   var MySecret = pm.environment.get('AccessKeySecret');

   // Set API URI variable
   var myURI = 'api/open/v1/manager/device/getDetail'

   // Generate UUID
   var uuid = require('uuid');
   var MyGUID = uuid().replace(/-/g,'');
   pm.environment.set('MyGUID', MyGUID);

   // Get unix timestamp in ms
   var curDate = Date.now();
   pm.environment.set("MyTimestamp", curDate);

   // Generate string for signing
   var mySigString = 'GET\n' + 
      'X-Ca-Key:' + MyKey + '\n' +
      'X-Ca-Nonce:' + MyGUID + '\n' +
      'X-Ca-Timestamp:' + curDate + '\n' +
      myURI + '\n' +
      'id=exampleID';

   var hash = CryptoJS.HmacSHA256( mySigString, MySecret);
   var hashInB64 = CryptoJS.enc.Base64.stringify(hash);
   pm.environment.set('MySig', hashInB64);
   ```

   - Now, select the drop down on the top right as whatever environment name you gave in step 1 and choose the environment.

   - Next go to the Headers tab and add the following:

   ```javascript
   X-Ca-Key: {{AccessKeyID}}
   X-Ca-Nonce: {{MyGUID}}
   X-CA-Signature: {{MySig}}
   X-Ca-Timestamp: {{MyTimestamp}}
   Content-Type: application/json;charset=UTF-8
   ```

   - Now, place in a GET api link and hit send. For example: 'https://api-dm.yealink.com:8445/api/open/v1/manager/device/getDetail?id=exampleID'

   - This returns:

   ```json
   {
      "ret": 1,
      "data": "[{(lots of info)"}]}]",
      "error": null
   }
   ```

   - Success!

2. Example, to use GET in Powershell to get a device's details

   ```powershell
   ## Setup Variables
   $baseUri = 'https://api-dm.yealink.com:8445/'
   $accessKeyId = 'Key'
   $accessKeySecret = 'SECRET'

   $epochStart = New-Object DateTime 1970,1,1,0,0,0,([DateTimeKind]::Utc)

   $deviceId = 'exampleID'
   $apiUri = 'api/open/v1/manager/device/getDetail'

   # Generate GUID
   $guid = [GUID]::NewGuid().ToString().Replace('-','')

   # Get milliseconds since epoch
   $timeStamp = [int64](([DateTime]::UtcNow) - $epochStart).TotalMilliseconds

   # Build Headers hashtable
   $headers = @{}
   $headers.Add('X-Ca-Key', $accessKeyId)
   $headers.Add('X-Ca-Nonce', $guid)
   $headers.Add('X-Ca-Timestamp',$timeStamp)

   # Build parameters array
   $params = @()
   $params += 'id=' + $deviceId

   # Convert headers hashtable into array (sig requires array, invoke-restmethod requires hashtable)
   $headerArray = @()
   foreach($key in $headers.keys) {
      $headerArray += "{0}:{1}" -f $key, $headers[$key]
   }

   # Build out string for signing. Values need to be sorted
   $strToSign = "GET`n"
   $strToSign += $(($headerArray | Sort-Object )-join "`n") + "`n"
   $strToSign += $apiUri + "`n"
   $strToSign += $(($params | Sort-Object) -join "`n")

   # Build out HMACSHA256 Signature
   $hmacsha = New-Object System.Security.Cryptography.HMACSHA256
   $hmacsha.key = [Text.Encoding]::ASCII.GetBytes($accessKeySecret)
   $signature = $hmacsha.ComputeHash([Text.Encoding]::ASCII.GetBytes($strToSign))
   $signature = [Convert]::ToBase64String($signature)

   # Add signature to headers hashtable
   $headers.Add('X-Ca-Signature', $signature)

   # Build out URI to call, including parameters #
   $uri = $baseUri + $apiUri + '?' + $($params -join '&')

   # Execute REST call
   $res = Invoke-RestMethod -Uri $uri -Headers $headers -ContentType 'application/json;charset=UTF-8' -Method Get
   ```

3. Example, to use POST in Postman to add a device

   - Using the same environment from above (with the access key and secret key)
   - Go to the pre-request script and paste in (without changing anything):

   ```javascript
   // Get key/secret
   var MyKey = pm.environment.get('AccessKeyID');
   var MySecret = pm.environment.get('AccessKeySecret');

   // Set API URI variable
   var myURI = 'api/open/v1/manager/device/add'

   // Generate UUID
   var uuid = require('uuid');
   var MyGUID = uuid().replace(/-/g,'');
   pm.environment.set('MyGUID', MyGUID);

   // Get unix timestamp in ms
   var curDate = Date.now();
   pm.environment.set("MyTimestamp", curDate);

   // Generate Content MD5
   var myBody = pm.request.body.raw;
   var ContentMD5 = CryptoJS.enc.Base64.stringify( CryptoJS.MD5(myBody) );
   pm.environment.set('ContentMD5',ContentMD5);

   // Generate string for signing
   var mySigString = 'POST\n' + 
      'Content-MD5:' + ContentMD5 + '\n' +
      'X-Ca-Key:' + MyKey + '\n' +
      'X-Ca-Nonce:' + MyGUID + '\n' +
      'X-Ca-Timestamp:' + curDate + '\n' +
      myURI;

   var hash = CryptoJS.HmacSHA256( mySigString, MySecret);
   var hashInB64 = CryptoJS.enc.Base64.stringify(hash);
   pm.environment.set('MySig', hashInB64);
   ```

   - Now in the body, put in information that is required:

   ```json
   {
      "mac": "12345",
      "machineId": "12345",
      "modelId": "12345",
      "phone": "Test",
      "regionId": "12345"
   }
   ```

   - Lastly, put the following headers:

   ```json
   Content-MD5: {{ContentMD5}}
   X-Ca-Key: {{AccessKeyID}}
   X-Ca-Nonce: {{MyGUID}}
   X-CA-Signature: {{MySig}}
   X-Ca-Timestamp: {{MyTimestamp}}
   Content-Type: application/json;charset=UTF-8
   ```

4. Example, to use POST in Powershell to add a device

   ```powershell
   ## Setup Variables
   $baseUri = 'https://api-dm.yealink.com:8445/'
   $accessKeyId = 'Key'
   $accessKeySecret = 'SECRET'

   $epochStart = New-Object DateTime 1970,1,1,0,0,0,([DateTimeKind]::Utc)

   $apiUri = 'api/open/v1/manager/device/add'

   # Generate GUID
   $guid = [GUID]::NewGuid().ToString().Replace('-','')

   # Get milliseconds since epoch
   $timeStamp = [int64](([DateTime]::UtcNow) - $epochStart).TotalMilliseconds

   # Build Headers hashtable
   $headers = @{}
   $headers.Add('X-Ca-Key', $accessKeyId)
   $headers.Add('X-Ca-Nonce', $guid)
   $headers.Add('X-Ca-Timestamp',$timeStamp)

   # Build Body Object
   $body = New-Object psobject -Property @{
      'mac' = '12345'
      'machineId' = '12345'
      'modelId' = '12345'
      'phone' = 'Test'
      'regionId' = '12345'
   }

   $jsonBody = $body | ConvertTo-Json
   $md5hash = New-Object System.Security.Cryptography.MD5CryptoServiceProvider
   $sig = $md5hash.ComputeHash( [System.Text.Encoding]::UTF8.GetBytes($jsonBody) )
   $bodyB64Hash = [Convert]::ToBase64String( $sig )

   $headers.Add('Content-MD5', $bodyB64Hash)

   # Convert headers hashtable into array (sig requires array, invoke-restmethod requires hashtable)
   $headerArray = @()
   foreach($key in $headers.keys) {
      $headerArray += "{0}:{1}" -f $key, $headers[$key]
   }

   # Build out string for signing. Values need to be sorted
   $strToSign = "POST`n"
   $strToSign += $(($headerArray | Sort-Object )-join "`n") + "`n"
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
   $res = Invoke-RestMethod -Uri $uri -Headers $headers -ContentType 'application/json;charset=UTF-8' -Body $jsonBody -method Post
   ```


