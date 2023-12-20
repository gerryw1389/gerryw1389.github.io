---
title: Using Powershell To Access Gmail API
date: 2018-01-21T16:08:50+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/01/using-powershell-to-access-gmail-api/
tags:
  - WebSoftware
tags:
  - Powershell
  - RestAPI
---
<!--more-->

### Description:

Follow this guide to connect to Gmail API using OAuthv2 working as of 2020-08-26. What I did was:

### To Resolve:

1. Delete my current 'posh' application and created a new one called 'powershell'

   - Go to [Google Project Console](https://console.developers.google.com/iam-admin/projects?)
   - Create a new project
   - Enable the Gmail API by selecting the API and selecting `enable API` , after creating your project.
   - Click Credentials
   - Create OAuth Client ID Credentials
   - Select Web Application as product type
   - Configure the Authorized Redirect URI to `https://developers.google.com/oauthplayground` must not have a ending `/` in the URI
   - Save your client ID and Secret
   - Browse to [Oauth Playground](https://developers.google.com/oauthplayground)
   - This saves us time from generating an OAuth request in PowerShell. This is where we will authorize our Project to our Google Account using our provided  - Client ID and Client Secret.
   - Click the gear in the right-hand corner and select `Use your own OAuth credentials`
   - Choose `Gmail API v1` and copy the `refresh_token` and `access_token` to notepad

2. Now in my [Gmail API script](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Send-CreditBalance.ps1) I just use the following snippet to connect to Gmail and read/delete my messages:

   ```powershell
   $clientId = "31262ipuu5.apps.googleusercontent.com"
   $clientSecret = "RRak"
   $refreshToken = '1//04DXqtu2S'
   $headers = @{ 
      "Content-Type" = "application/x-www-form-urlencoded" 
   } 
   $body = @{
      client_id     = $clientId
      client_secret = $clientSecret
      refresh_token = $refreshToken
      grant_type    = 'refresh_token'
   }
   $params = @{
      'Uri'         = 'https://accounts.google.com/o/oauth2/token'
      'ContentType' = 'application/x-www-form-urlencoded'
      'Method'      = 'POST'
      'Headers'     = $headers
      'Body'        = $body
      'Verbose'     = $true
   }
   $accessTokenResponse = Invoke-RestMethod @params
   $accesstoken = $($accessTokenResponse.access_token)
   
   $headers = @{ 
      "Content-Type" = "application/json" 
   }
   $params = @{
      'Uri'         = "https://www.googleapis.com/gmail/v1/users/me/messages?access_token=$accesstoken"
      'ContentType' = 'application/json'
      'Method'      = 'GET'
      'Headers'     = $headers
      'Verbose'     = $true
   }
   $getMessagesResponse = Invoke-RestMethod @params
   $messages = $($getMessagesResponse.messages)
   ```

   - So `access_token` only has a one hour use time while the `refresh_token` should be good until you change your account's password, you do this regularly right?

3. Feel free to ignore past this step - keeping here for any readers that need more info:

### Older

1. I couldn't get this working before because I was running into an issue with the fact that I had to open a browser to get the $code variable like this:

   - Create `c:/scripts/1.ps1`

   ```powershell
   # 1 - fill in
   $clientId = "883355tlpc.apps.googleusercontent.com"
   $clientSecret = "fOYop"

   # 2 - Do this one time, note that you have to run this each time you move past this step, will see about automating somehow
   # $scopes = "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/gmail.send"
   $scopes = "https://mail.google.com/"
   Start-Process "https://accounts.google.com/o/oauth2/v2/auth?client_id=$clientId&scope=$([string]::Join("%20", $scopes))&access_type=offline&response_type=code&redirect_uri=urn:ietf:wg:oauth:2.0:oob"  

   cmd /c pause
   ```

   - Create `c:/scripts/2.ps1`

   ```powershell
   $clientId = "883355tlpc.apps.googleusercontent.com"
   $clientSecret = "fOYop"
   $refreshToken = '1//04dniS4GdT9DXqtu2S'
   $headers = @{ 
      "Content-Type" = "application/x-www-form-urlencoded" 
   } 
   $body = @{
      client_id     = $clientId
      client_secret = $clientSecret
      refresh_token = $refreshToken
      grant_type    = 'refresh_token'
   }
   $params = @{
      'Uri'         = 'https://accounts.google.com/o/oauth2/token'
      'ContentType' = 'application/x-www-form-urlencoded'
      'Method'      = 'POST'
      'Headers'     = $headers
      'Body'        = $body
   }
   $accessTokenResponse = Invoke-RestMethod @params
   $accesstoken = $($accessTokenResponse.access_token)
   # Write-Output "Access token: " $accesstoken

   $headers = @{ 
      "Content-Type" = "application/json" 
   }
   $params = @{
      'Uri'         = "https://www.googleapis.com/gmail/v1/users/me/messages?access_token=$accesstoken"
      'ContentType' = 'application/json'
      'Method'      = 'GET'
      'Headers'     = $headers
      'Body'        = $body
   }
   $getMessagesResponse = Invoke-RestMethod @params
   $messages = $($getMessagesResponse.messages)

   Write-Output $messages

   cmd /c pause
   ```

2. So I would run `c:/scripts/1.ps1` and paste the code from the browser window into `$refresh_token` in `c:/scripts/2.ps1`.

   - After this it would work perfectly, but I can't be logging in interactively if this is going to be a scheduled task!
   - What I was missing was the redirect URI and Oauth Playground steps from above.

3. That is all for now, but in summary, once you have the $AccessToken, you can access Gmail API pretty easily:

   - **All emails:**  
   `Invoke-WebRequest -Uri "https://www.googleapis.com/gmail/v1/users/me/messages?access_token=$accesstoken" -Method Get`

   - **Individual Email (Where $a = $($message.id) (see above)):**  
   `Invoke-WebRequest -Uri ("https://www.googleapis.com/gmail/v1/users/me/messages/$a" + "?access_token=$accesstoken") -Method Get`

   - **Trash an email (Where $a = $($message.id) (see above)):**  
   `Invoke-WebRequest -Uri ("https://www.googleapis.com/gmail/v1/users/me/messages/$a/trash" + "?access_token=$accesstoken") -Method Post`

   - Found this on [StackExchange](https://stackoverflow.com/questions/39728767/new-gmail-api-support-for-powershell). If you just want to get the most recent emails header, you can use this function:

   ```powershell
   Function Get-SubjectLine
   {
   #Acquires most recent message ID using access token.
   $messageIDjson = Invoke-WebRequest -Uri "https://www.googleapis.com/gmail/v1/users/me/messages?access_token=$accessToken" -Method Get | ConvertFrom-Json;
   #Converts JSON message and thread ids into string.
   $messageID = ($messageIDjson | Out-String);
   #Seperates string on first message ID, places messageID into $result.
   $start = $messageID.indexOf("=") + 1;
   $end = $messageID.indexOf(";", $start);
   $length = $end - $start;
   $result = $messageID.substring($start, $length);
   #Acquires most recent message, using ID stored in result and access token.
   $messages = Invoke-WebRequest -Uri ("https://www.googleapis.com/gmail/v1/users/me/messages/$result" + "?access_token=$accessToken") -Method Get | ConvertFrom-Json;

   return $messages.snippet;
   }
   ```

   - I'm sure there are millions of other things you can do once you are at this step. Enjoy!
