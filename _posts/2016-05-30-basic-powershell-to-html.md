---
title: 'PS: Powershell To HTML'
date: 2016-05-30T06:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/basic-powershell-to-html/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

I used the following guide in learning how to setup Powershell with HTML reporting functionality.



### To Resolve:

1. Create an object.

   ```powershell
   $MyObject = Get-Service

   # or

   $ArrayOfObjects = ForEach ($Address in $Addresses) {
   New-Object -Property @{
   Name = $Name
   Address = $Address
   State = $State
   }
   }
   ```

2. Next, lets see how it looks using the built-in HTML report:

   ```powershell
   $MyObject | ConvertTo-HTML | Out-File C:\test.htm
   ```

3. It looks kinda bland, let's add some CSS:

   ```powershell
   $Header = @"
   Title of my Report 
   "@
   $Pre = "Header"
   $Post = "Footer"
   $MyObject | Select 'Status','name' | ConvertTo-HTML -Head $Header -PreContent $Pre -PostContent $Post | out-file c:\test.htm
   Invoke-item C:\scripts\test.htm
   ```

4. Looks great! Let's see if we can add that to an email instead:

   ```powershell
   Function Send-Email {
   $Mailmessage = New-Object System.Net.Mail.Mailmessage
   $Mailmessage.From = "Email@Domain.Com"
   $Mailmessage.To.Add("Email@Domain.Com")
   $Mailmessage.Subject = "Test"
   $Mailmessage.Body = $Body
   $Mailmessage.Isbodyhtml = $True
   $Smtpclient = New-Object System.Net.Mail.Smtpclient
   $Smtpclient.Host = "Smtpservername"
   $Smtpclient.Send($Mailmessage)
   }
   $Myobject = Get-Service
   $Header = @"
    
   Title Of My Report
    
   "@
   $Pre = "Header"
   $Post = "Footer"
   $Html = $Myobject | Select 'Status','Name' | Convertto-Html -Head $Header -Precontent $Pre -Postcontent $Post
   $Body = $Html | Out-String
   Send-Email $Body
   ```


5. Lastly, we will download a HTML script [here](https://gallery.technet.microsoft.com/scriptcenter/PowerShell-Collect-Server-089f1da3) and tweak it to meet our needs. For example:

   ```powershell
   # User Variables
   $ComputerName = "my-pc"
   $HTMLFile = "c:\scripts\test.htm"

   # Initialize HTML
   $htmlreport = @()
   $htmlbody = @()
   $spacer = "<br />"

   # Build first row
   Write-Verbose "Collecting computer system information"
   $subhead = "<h3>Computer System Information</h3>"
   $htmlbody += $subhead
   $csinfo = Get-WmiObject Win32_ComputerSystem -ComputerName $ComputerName |
                     Select-Object Name,Manufacturer,Model,
                     @{Name='Physical Processors';Expression={$_.NumberOfProcessors}},
                     @{Name='Logical Processors';Expression={$_.NumberOfLogicalProcessors}},
                     @{Name='Total Physical Memory (Gb)';Expression={$tpm = $_.TotalPhysicalMemory/1GB;"{0:F0}" -f $tpm}},
                     DnsHostName,Domain
   $htmlbody += $csinfo | ConvertTo-Html -Fragment
   $htmlbody += $spacer

   # Second row
   Write-Verbose "Collecting operating system information"
   $subhead = "<h3>Operating System Information</h3>"
   $htmlbody += $subhead

   $osinfo = Get-WmiObject Win32_OperatingSystem -ComputerName $ComputerName -ErrorAction STOP | 
            Select-Object @{Name='Operating System';Expression={$_.Caption}},
                     @{Name='Architecture';Expression={$_.OSArchitecture}},
                     Version,Organization,
                     @{Name='Install Date';Expression={
                        $installdate = [datetime]::ParseExact($_.InstallDate.SubString(0,8),"yyyyMMdd",$null);
                        $installdate.ToShortDateString()
                     }},
                     WindowsDirectory

   $htmlbody += $osinfo | ConvertTo-Html -Fragment
   $htmlbody += $spacer

   # Third Row

   Write-Verbose "Collecting physical memory information"

   $subhead = "<h3>Physical Memory Information</h3>"
   $htmlbody += $subhead

   $memorybanks = @()
         $physicalmemoryinfo = @(Get-WmiObject Win32_PhysicalMemory -ComputerName $ComputerName -ErrorAction STOP |
            Select-Object DeviceLocator,Manufacturer,Speed,Capacity)

         foreach ($bank in $physicalmemoryinfo)
         {
            $memObject = New-Object PSObject
            $memObject | Add-Member NoteProperty -Name "Device Locator" -Value $bank.DeviceLocator
            $memObject | Add-Member NoteProperty -Name "Manufacturer" -Value $bank.Manufacturer
            $memObject | Add-Member NoteProperty -Name "Speed" -Value $bank.Speed
            $memObject | Add-Member NoteProperty -Name "Capacity (GB)" -Value ("{0:F0}" -f $bank.Capacity/1GB)

            $memorybanks += $memObject
         }

         $htmlbody += $memorybanks | ConvertTo-Html -Fragment
         $htmlbody += $spacer

   # End of Headings, you get the point.

   # HTML report

   Write-Verbose "Producing HTML report"
   $reportime = Get-Date

   #Common HTML head and styles
   $htmlhead="<html>
   <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cstyle%3E%0D%0ABODY%7Bfont-family%3A%20Arial%3B%20font-size%3A%208pt%3B%7D%0D%0AH1%7Bfont-size%3A%2020px%3B%7D%0D%0AH2%7Bfont-size%3A%2018px%3B%7D%0D%0AH3%7Bfont-size%3A%2016px%3B%7D%0D%0ATABLE%7Bborder%3A%201px%20solid%20black%3B%20border-collapse%3A%20collapse%3B%20font-size%3A%208pt%3B%7D%0D%0ATH%7Bborder%3A%201px%20solid%20black%3B%20background%3A%20%23dddddd%3B%20padding%3A%205px%3B%20color%3A%20%23000000%3B%7D%0D%0ATD%7Bborder%3A%201px%20solid%20black%3B%20padding%3A%205px%3B%20%7D%0D%0Atd.pass%7Bbackground%3A%20%237FFF00%3B%7D%0D%0Atd.warn%7Bbackground%3A%20%23FFE600%3B%7D%0D%0Atd.fail%7Bbackground%3A%20%23FF0000%3B%20color%3A%20%23ffffff%3B%7D%0D%0Atd.info%7Bbackground%3A%20%2385D4FF%3B%7D%0D%0A%3C%2Fstyle%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="<style>" title="<style>" />
   <body>
   <h1 align=""center"">Server Info: $ComputerName</h1>
   <h3 align=""center"">Generated: $reportime</h3>"

   $htmltail = "</body></html>"
   $htmlreport = $htmlhead + $htmlbody + $htmltail
   $htmlreport | Out-File $htmlfile -Encoding Utf8
   Invoke-Item C:\scripts\test.htm

   <#
   To center the report, just change:
   <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cstyle%3E%0D%0ATABLE%20%7Bborder-width%3A%201px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3Bborder-collapse%3A%20collapse%3Bmargin-left%3A%20auto%3B%20margin-right%3A%20auto%3B%20width%3A%20100px%3B%20text-align%3A%20center%3B%7D%0D%0ATH%20%7Bborder-width%3A%201px%3Bpadding%3A%203px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3Bbackground-color%3A%20%236495ED%3B%7D%0D%0ATD%20%7Bborder-width%3A%201px%3Bpadding%3A%203px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3B%7D%0D%0ATR%3ANth-Child(Even)%20%7BBackground-Color%3A%20%23dddddd%3B%7D%0D%0ATR%3ANth-Child(odd)%20%7BBackground-Color%3A%20%23ffffff%3B%7D%0D%0ATR%3AHover%20TD%20%7BBackground-Color%3A%20%23C1D5F8%3B%7D%0D%0AH3%20%7Btext-align%3A%20center%3B%7D%0D%0A%3C%2Fstyle%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="<style>" title="<style>" />
   #>
   ```

6. This should be enough to get you started. From here, it's all about switching out information and learning up on HTML/CSS.

### References:

[http://thesurlyadmin.com/2013/01/21/how-to-create-html-reports/#more-817](https://thesurlyadmin.com/2013/01/21/how-to-create-html-reports/#more-817)