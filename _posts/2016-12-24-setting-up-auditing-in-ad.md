---
title: Setting Up Auditing In AD
date: 2016-12-24T07:37:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/setting-up-auditing-in-ad/
tags:
  - WindowsServer
tags:
  - GroupPolicy
  - ActiveDirectory
  - Powershell
---
<!--more-->

### Description:

So the other day, I was going through the Event Viewer on one of our domain controllers and noticed that we haven't setup Auditing up. Yelp! Follow this post to setup auditing in your environment. 

NOTE: All of our servers are Server2012r2.
{: .notice--success}

### To Resolve:

1. Login to the Domain Controller

2. Create a new domain wide GPO (I placed mine a couple under the default domain policy)

3. Edit it like so:

   ```escape
   Go to Computer Configuration\Policies\Windows Settings\Security Options  
   Enable "Audit: Force audit policy subcategory settings.."

   Now go to Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\DS Access  
   Enable "Audit Directory Service Access" to success  
   Enable "Audit Directory Service Changes" to success

   Now go to Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Logon  
   Enable all four and set them to "failure"
   ```

3. That's it for the GPO. Now open up ADUC and click on View => Advanced Settings. This is so that we can get the Audit tab for the next step.

4. Right-click the top of the domain tree and bring up the properties. Select Security tab "Advanced" Auditing tab. Select the "Everyone" security principal, set Type to Success and Applies to: This object and all descendant objects.  For the permissions set the following:  

   ```escape
   Write all properties  
   Delete  
   Delete subtree  
   Modify permissions  
   Modify owner  
   All validated writes  
   All extended writes  
   Create all child objects  
   Delete all child objects
   ```

5. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `eventvwr.msc`. What I did here was purposely try to login to another server with the wrong password and verified that an event 4776 was recorded. It was. If you want to use a one liner in Powershell you could do something like:

   ```powershell
   Get-EventLog -Logname Security | where { $_.EntryType -eq 'FailureAudit' -and $_.InstanceId -eq '4776' }
   ```

6. Lastly, you are going to want to put something in place that lets you know when these happen. A powershell script as a scheduled task works best. All credit goes to Dean Bunn.

   ```powershell
   #############################################################
   # Script Name: AD_DCs_Failed_Login_Report.ps1
   # Version: 1.0
   # Author: Dean Bunn
   # Last Edited: 07/26/2011
   # Description: Failed Logins Report for DCs
   # Link: https://itadmindev.blogspot.com/2011/07/powershell-ad-dc-failed-logins-report.html
   #############################################################

   #Array for All Failed Login Entries
   $arrFailures = @()
   #Array for Reporting
   $Summary = @()

   #Domain Controller Array
   $DCs = @("dc1","dc2","dc3")

   foreach($DC in $DCs)
   {
   #Retrieve Failed Logins on Each DC for the Last 24 Hours
   $failedLogins = get-eventlog -computername $DC -logname security -after (get-date).adddays(-1) | where-object {$_.instanceID -eq 4625 }

   #Loop Through Each Failed Login
   foreach($failedLogin in $failedLogins)
   {

   #Var for Workstation Name
   $workstation = ""
   #Var for IP Address
   $networkAddress = ""

   #Array of Failed Login Log Entry Message (Split by Line Break)
   $flM = $failedLogin.message.Split("`n")

   #Loop Through Each Line in the Log Entry Message
   foreach($fl in $flM)
   {
   #Check to See if Line has Source Network Address Info
   if($fl.Contains("Source Network Address:"))
   {
   #Remove Unneeded Data from Line
   $fl = $fl.Replace("Source Network Address:","")
   #Clean UP Network Address Info
   $networkAddress = $fl.ToString().Trim()
   }

   #Check to See if Line has Workstation Info
   if($fl.Contains("Workstation Name:"))
   {
   #Remove Unneeded Data from Line
   $fl = $fl.Replace("Workstation Name:","")
   #Clean Up Workstation Info
   $workstation = $fl.ToString().ToUpper().Trim()
   }

   }

   #Format Failed Login Entry Data Before Adding to Array
   $flEntry = $networkAddress + "," + $workstation

   #Quick Check to See if IP And Host Name Weren't Empty
   if($flEntry.length -gt 1)
   {
   #Added Failed Entry to Array
   $arrFailures += $flEntry
   }


   }

   }

   #Create Hashtable for Unique Check
   $htReport = @{}

   #Loop Through Failed Log Entries Array and Count How Many Failed Logins
   foreach($flEntry in $arrFailures)
   {
   #Int for Counting Failed Login Attempts
   $intEC = 0

   if(!$htReport.ContainsKey($flEntry))
   {
   #Loop Again Through Array Looking for IP + Host Name Match
   foreach($item in $arrFailures)
   {
   if($flEntry -eq $item)
   {
   $intEC = $intEC + 1
   }
   }

   #After Determining Matches, See if Entry Count Added To Report Already
   #And Only Report on 10 or Greater Failed Logins for IP + Host Name Pair
   if($intEC -gt 10) #
   {

   #Split Apart IP Host Name Entry to Add It to Report Summary
   $arrFlEntry = $flEntry.Split(",")

   #Create New PowerShell Object and Assign Data to It
   $uEntry = new-Object PSObject
   $uEntry | add-Member -memberType noteProperty -name "IP" -Value $arrFlEntry[0].ToString()
   $uEntry | add-Member -memberType noteProperty -name "Host Name" -Value $arrFlEntry[1].ToString()
   $uEntry | add-Member -memberType noteProperty -name "Failed Logins" -Value $intEC.ToString()
   #Add Entry to Summary Array
   $Summary += $uEntry

   }

   #Add Entry Info to Reporting Hashtable
   $htReport.add($flEntry,"1")

   }

   }

   #Get Current Short Date
   $rptDate = Get-Date -Format d

   #Style for HTML Table in ConvertTo-HTML
   $a = "<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cstyle%3E%22%0D%0A%24a%20%3D%20%24a%20%2B%20%22TABLE%7Bborder-width%3A%201px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3B%7D%22%0D%0A%24a%20%3D%20%24a%20%2B%20%22TH%7Bborder-width%3A%201px%3Bpadding%3A%205px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3Btext-align%3A%20center%3B%7D%22%0D%0A%24a%20%3D%20%24a%20%2B%20%22TD%7Bborder-width%3A%201px%3Bpadding%3A%205px%3Bborder-style%3A%20solid%3Bborder-color%3A%20black%3Btext-align%3A%20left%3B%7D%22%0D%0A%24a%20%3D%20%24a%20%2B%20%22%3C%2Fstyle%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="<style>" title="<style>" />"

   #Message Body (Sorted by Failed Login Attempts)
   $emsg = $Summary | Sort-Object {[int]$_."Failed Logins"} -descending | ConvertTo-Html -head $a | Out-String

   #Settings for Email Message
   $messageParameters = @{
   Subject = "DCs Failed Logins Report for " + $rptDate
   Body = $emsg
   From = "DCAdmins@my.company.com"
   To = "DCAdmins@my.company.com"
   SmtpServer = "smtp.my.company.com"
   }
   #Send Report Email Message
   Send-MailMessage @messageParameters –BodyAsHtml
   ```


