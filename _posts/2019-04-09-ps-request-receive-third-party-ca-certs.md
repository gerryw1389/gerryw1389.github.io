---
title: 'PS: Request/Receive Third Party CA Certs'
date: 2019-04-09T16:56:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/ps-request-receive-third-party-ca-certs/
tags:
  - Networking
  - Windows
tags:
  - Scripting-Powershell
  - Scripting-RestAPI
---
<!--more-->

### Description:

Needed to find a way to automate certificate issuing and retrieval, here is a rought first draft based on [Incommon Rest API Guide](https://spaces.at.internet2.edu/display/ICCS/InCommon+CM+RESTful+API)

### 

### To Resolve:

1. To see the types of certs to request

   ```powershell
   curl 'https://cert-manager.com/api/ssl/v1/types/' -i \
   -H 'Content-Type: application/json' \
   -H 'login: email@yourdomain.com' \
   -H 'password: Psswd' \
   -H 'customerUri: InCommon'
   ```

   Example response:

   ```powershell
   {"id":224,"name":"InCommon SSL (SHA-2)","terms":[365,730]},
   ```

2. To Request a cert:

   ```powershell
   curl 'https://cert-manager.com/api/ssl/v1/enroll?' -i -X POST -H 'Content-Type: application/json' -H 'login: email@yourdomain.com' -H 'password: Psswd' -H 'customerUri: InCommon' -d '{"orgId":001,"csr":"-----BEGIN NEW CERTIFICATE REQUEST----- MIIEJDCCAwwCAQAwgacxHDAaBgNVBAMME29pdC1qeHE5cnEyLnV0YS5lZHUxLTAr BgNVBAsMJFRoZSBVbml2ZXJzaXR5IE9mIFRleGFzIEF0IEFybGluZ3RvbjEnMCUG A1UECgweVGhlIFVuaXZlcnNpdHkgT2YgVGV4YXMgU3lzdGVtMRIwEAYDVQQHDAlB cmxpbmd0b24xDjAMBgNVBAgMBVRleGFzMQswCQYDVQQGEwJVUzCCASIwDQYJKoZI hvcNAQEBBQADggEPADCCAQoCggEBAMMNDnhJBf+F10EmNxfR2F2WOMjq6Fh00ceM EJptn0dObBtg8BW+YF3yhqNRG94mbOjGNljAQNdtGsIqZm9s78GR5csH8YYKoqGB HNORToTaFVSvP5LXkxFpoGuJUvVsx5v59raF9WPTs+VAbYfY+yk3kzWaNksGByvu xo+LeSj6DUFDrCne44L4tIJ56STpq9YgPc3oH8Oeb8lSiRDegszD72rvjlio1RaP aokslX1tMyA+crvnBslQI6LrRIotY19DgX1jaSo43vFo3vJKUYYUCbZThMdL9Lc4 X4Xi6gS8uItcSMGtm7O1ruQWWjZaQYX++MA2MqETYDpR+JVzWs0CAwEAAaCCATUw HAYKKwYBBAGCNw0CAzEOFgwxMC4wLjE3MTM0LjIwTAYJKwYBBAGCNxUUMT8wPQIB CQwTT0lULUpYUTlSUTIudXRhLmVkdQwWT0lULUpYUTlSUTJcZ3dpbGxhZG1pbgwL Y2VydHJlcS5leGUwUwYJKoZIhvcNAQkOMUYwRDAOBgNVHQ8BAf8EBAMCBaAwEwYD VR0lBAwwCgYIKwYBBQUHAwEwHQYDVR0OBBYEFNYt8ml/x4q2q8iRiRr5Bsr4ewpv MHIGCisGAQQBgjcNAgIxZDBiAgEBHloATQBpAGMAcgBvAHMAbwBmAHQAIABSAFMA QQAgAFMAQwBoAGEAbgBuAGUAbAAgAEMAcgB5AHAAdABvAGcAcgBhAHAAaABpAGMA IABQAHIAbwB2AGkAZABlAHIDAQAwDQYJKoZIhvcNAQEFBQADggEBADd+vPez4HpO LFmFQUp4/gQJXCG6MgxnloBWKpDVI019OUKxr2mba27kd3+1/seF5xqVhleQxi3G 2rzfWIwiJrU= -----END NEW CERTIFICATE REQUEST-----","subjAltNames":"","certType":224,"numberServers":1,"serverType":14,"term":730,"comments":"SSL Cert Request"}'
   ```

   Response:

   ```powershell
   {"renewId":"cM8m8zbDqepsdfsdfsdfm0PjtqyZG","sslId":123546549245461}
   ```

3. To download a cert

   ```powershell
   curl 'https://cert-manager.com/api/ssl/v1/collect/123546549245461/base64' -i -H 'Content-Type: application/json' -H 'login: email@yourdomain.com' -H 'password: Psswd' -H 'customerUri: InCommon'
   ```

   Response:

   It should allow it. In my case, we have them set to manual approval so I was hit with:

   ```powershell
   {"code":-23,"description":"The certificate hasn't been approved yet!"}
   ```

   But I will get that corrected in the Admin portal.

   The Powershell version of this is:

   ```powershell
   # see available
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
   $URI = 'https://cert-manager.com/api/ssl/v1/types/'
   $request = Invoke-WebRequest -URI $uri -Method GET -Headers @{
   "Content-Type" = "application/json"
   "login" = "email@yourdomain.com"
   "password" = "Psswd"
   "customerUri" = "InCommon"
   }

   # request
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
   $URI = 'https://cert-manager.com/api/ssl/v1/enroll'
   $cert = '-----BEGIN NEW CERTIFICATE REQUEST----- MIIEJDCCAwwCAQAwgacxHDAaBgNVBAMME29pdC1qeHE5cnEyLnV0YS5lZHUxLTAr BgNVBAsMJFRoZSBVbml2ZXJzaXR5IE9mIFRleGFzIEF0IEFybGluZ3RvbjEnMCUG aokslX1tMyA+crvnBslQI6LrRIotY19DgX1jaSo43vFo3vJKUYYUCbZThMdL9Lc4 X4Xi6gS8uItcSMGtm7O1ruQWWjZaQYX++MA2MqETYDpR+JVzWs0CAwEAAaCCATUw HAYKKwYBBAGCNw0CAzEOFgwxMC4wLjE3MTM0LjIwTAYJKwYBBAGCNxUUMT8wPQIB CQwTT0lULUpYUTlSUTIudXRhLmVkdQwWT0lULUpYUTlSUTJcZ3dpbGxhZG1pbgwL Y2VydHJlcS5leGUwUwYJKoZIhvcNAQkOMUYwRDAOBgNVHQ8BAf8EBAMCBaAwEwYD VR0lBAwwCgYIKwYBBQUHAwEwHQYDVR0OBBYEFNYt8ml/x4q2q8iRiRr5Bsr4ewpv MHIGCisGAQQBgjcNAgIxZDBiAgEBHloATQBpAGMAcgBvAHMAbwBmAHQAIABSAFMA QQAgAFMAQwBoAGEAbgBuAGUAbAAgAEMAcgB5AHAAdABvAGcAcgBhAHAAaABpAGMA IABQAHIAbwB2AGkAZABlAHIDAQAwDQYJKoZIhvcNAQEFBQADggEBADd+vPez4HpO LFmFQUp4/gQJXCG6MgxnloBWKpDVI019OUKxr2mba27kd3+1/seF5xqVhleQxi3G vvc4ATywT1GmeYa4GCJLfc7LnhziPAUOhxBkF/muGblG2vT0w2tLb59k/cTnJdcy K4alTV6Cb0Npcj/nmx86nmHdQIhNirkrXFiPlyXlSFx049n6kcQhzVJyiMu5Oh2+ UGEHtGDhEVfu3bgQf21hD7DDICs1EoC8zhIZPpx4z/zCC/niWBFPufVsYTTbVPYt nq6sdToEs1hiojnVEx7N0vMU/4vcbsRt2PmzpvDMhaqQajDjM6KtnU9qSNlUq6dU 2rzfWIwiJrU= -----END NEW CERTIFICATE REQUEST-----'
   $json = @"
   {
   "orgId":001,
   "csr":"$cert",
   "subjAltNames":"",
   "certType":224,
   "numberServers":1,
   "serverType":14,
   "term":730,
   "comments":"SSL Cert Request"
   }
   "@
   $request = Invoke-RestMethod -URI $uri -Method Post -Body $json -Headers @{
   "Content-Type" = "application/json"
   "login" = "email@yourdomain.com"
   "password" = "Psswd"
   "customerUri" = "InCommon"
   }

   # Download
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
   $SSL_ID = '1239564561261'
   $URI = "https://cert-manager.com/api/ssl/v1/collect/$SSL_ID/base64"
   $request = Invoke-WebRequest -URI $uri -Method GET -Headers @{
   "Content-Type" = "application/json"
   "login" = "email@yourdomain.com"
   "password" = "Psswd"
   "customerUri" = "InCommon"
   }
   $content = $request.RawContent
   $begin_index = $content.indexof("-----BEGI", 1600)
   $key = $content.substring($begin_index, (($content.Length -1) - $begin_index))
   $servername = $env:computername + 'mydomain.com'
   If (-not (Test-Path "c:\scripts"))
   {
      New-Item -ItemType Directory -Path "c:\scripts" | Out-Null
   }
   If (-not (Test-Path "c:\scripts\$servername.crt"))
   {
      New-Item -ItemType File -Path "c:\scripts\$servername.crt" -Value $key | Out-Null
   }
   ```


