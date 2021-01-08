---
title: 'PS: Send Email When Bitcoin Price Is X pt 2'
date: 2020-09-04T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/ps-send-email-bitcoin
categories:
  - LocalSoftware
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Here is the updated function (to [this](https://automationadmin.com/2020/01/ps-send-email-bitcoin/)) that I use to send me emails when to buy certain stocks and bitcoin. It runs daily and uses Alpha Vantage API.

### To Resolve:

1. See below:

   ```powershell
   function Send-Email
   {
      [CmdletBinding()]
      Param 
      (
         [string]$fundName
      )
      $usernameXML = Import-Clixml -Path "$PSScriptRoot\username.xml"
      $username = $usernameXML.GetNetworkCredential().Password

      $passwordXML = Import-Clixml -Path "$PSScriptRoot\password.xml"
      $password = $passwordXML.GetNetworkCredential().Password

      # Creds for sending email
      $pw = ConvertTo-SecureString -String $password -AsPlainText -Force
      $Creds = New-Object -Typename System.Management.Automation.PSCredential -Argumentlist $username, $pw

      $From = "me@gmail.com"
      $To = "me@gmail.com"
      $Subject = "Buy Fund: $fund"
      $Body = "Records indicate this fund is on decline for more than 3 days"
      $SMTPServer = "smtp.gmail.com"
      $SMTPPort = "587"
      $params = @{
         "From"       = $From
         "To"         = $To
         "Subject"    = $Subject
         "Body"       = $Body
         "SmtpServer" = $SMTPServer
         "Port"       = $SMTPPort
         "Credential" = $Creds
         "BodyAsHTML" = $true
         "UseSsl"     = $true
         "Verbose"    = $true
      }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      Send-MailMessage @params
   }

   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"  
   $funds = @( "VFIFX", "VWUSX", "VTSAX", "BTC-USD")

   foreach ($fund in $funds)
   {
      Write-Log "fund: $fund"

      $uri = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + $fund + "&apikey=PNFmyKey"
      $response = Invoke-RestMethod $uri -Method 'GET' -Headers $headers -Body $body
      #$response | ConvertTo-Json

      $last3 = $response.'Time Series (Daily)'.PSObject.Properties | Sort-Object -Descending | Select-Object -First 5 
      $first = $last3[0].name
      $firstvalue = $last3[0].value.'5. adjusted close'
      $second = $last3[1].name
      $secondvalue = $last3[1].value.'5. adjusted close'
      $third = $last3[2].name
      $thirdvalue = $last3[2].value.'5. adjusted close'
      $fourth = $last3[3].name
      $fourthvalue = $last3[3].value.'5. adjusted close'
      $fifth = $last3[4].name
      $fifthvalue = $last3[4].value.'5. adjusted close'

      Write-Log "$first - $firstvalue"
      Write-Log "$second - $secondvalue"
      Write-Log "$third - $thirdvalue"
      Write-Log "$fourth - $fourthvalue"
      Write-Log "$fifth - $fifthvalue"

      $count = 0
      if ($firstvalue -lt $secondvalue)
      {
         $count += 1
      }
      if ($secondvalue -lt $thirdvalue)
      {
         $count += 1
      }
      if ($thirdvalue -lt $fourthvalue)
      {
         $count += 1
      }
      if ($fourthvalue -lt $fifthvalue)
      {
         $count += 1
      }
      Write-Log "Value of count: $count"
      If ( $count -lt 4)
      {
         Write-Log "Dont buy: $fund"
         #Send-Email -fundName $fund
      }
      Else
      {
         Write-Log "Buy $fund"
         Send-Email -fundName $fund
      }
      Start-Sleep -Seconds 3
   }
   ```

2. This can be found on my [gwMisc](https://github.com/gerryw1389/powershell/tree/main/gwMisc) section on my Github