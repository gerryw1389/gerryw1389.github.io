---
title: 'PS: Creating Scripts'
date: 2018-04-30T03:05:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-creating-scripts/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Designing
---
<!--more-->

### Description:

This is a general idea of how to go about creating scripts in Powershell.

### To Resolve:

1. Start with a [template](https://automationadmin.com/2016/11/ps-template-script/) script.

2. Almost all functions will need to have a parameter so the user can specify for their environment. You can let it allow multiple by adding &#8220;[]&#8221; in the type declaration

   ```powershell
   [string[]]$ComputerName
   ```

3. Then, in the process block, just loop through each that the user passed. If they only passed one that is fine:

   ```powershell
   ForEach ($Computer in $ComputerName)
   {
   # Do something for each individual computer
   }
   ```

4. The first steps will be fine enough on their own, but sometimes you want to put each iteration into a table and then return that at the end:

   - This is part of my [Get-ComputerInfo](https://github.com/gerryw1389/powershell/blob/master/gwConfiguration/Public/Get-ComputerInfo.ps1) info script

   ```powershell
   Foreach ($Computer in $ComputerName)
               {

                  If (!([String]::IsNullOrWhiteSpace($Computer)))
                  {

                     If (Test-Connection -Quiet -Count 1 -Computer $Computer)
                     {

                           $Progress = @{}
                           $Progress.Activity = "Getting Sytem Information..." 
                           $Progress.Status = ("Percent Complete:" + "{0:N0}" -f ((($i++) / $ComputerName.count) * 100) + "%")
                           $Progress.CurrentOperation = "Processing $($Computer)..."
                           $Progress.PercentComplete = ((($j++) / $ComputerName.count) * 100)
                           Write-Progress @Progress
                     
                     
                           $CimSession = Get-LHSCimSession -ComputerName $Computer -Credential $Credential

                           $computerSystem = Get-CimInstance CIM_ComputerSystem -CimSession $CimSession
                           $computerBIOS = Get-CimInstance CIM_BIOSElement -CimSession $CimSession
                           $computerOS = Get-CimInstance CIM_OperatingSystem -CimSession $CimSession
                           $computerCPU = Get-CimInstance CIM_Processor -CimSession $CimSession
                           $computerHDD = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID = 'C:'" -CimSession $CimSession

                           $ComputerObject = [Ordered]@{}
                           $ComputerObject.ComputerName = $computerSystem.Name
                           $ComputerObject.LastReboot = $computerOS.LastBootUpTime
                           $ComputerObject.OperatingSystem = $computerOS.OSArchitecture + " " + $computerOS.caption
                           $ComputerObject.Model = $computerSystem.Model
                           $ComputerObject.RAM = "{0:N2}" -f [int]($computerSystem.TotalPhysicalMemory / 1GB) + "GB"
                           $ComputerObject.DiskCapacity = "{0:N2}" -f ($computerHDD.Size / 1GB) + "GB"
                           $ComputerObject.TotalDiskSpace = "{0:P2}" -f ($computerHDD.FreeSpace / $computerHDD.Size) + " Free (" + "{0:N2}" -f ($computerHDD.FreeSpace / 1GB) + "GB)"
                           $ComputerObject.CurrentUser = $computerSystem.UserName
                           
                           Write-Output "ComputerName: $($ComputerObject.ComputerName.ToString())"
                           Write-Output "LastReboot: $($ComputerObject.LastReboot.ToString())"
                           Write-Output "OperatingSystem: $($ComputerObject.OperatingSystem.ToString())"
                           Write-Output "Ram: $($ComputerObject.RAM.ToString())"
                           Write-Output "TotalDiskSpace: $($ComputerObject.TotalDiskSpace.ToString())"
                           Write-Output "CurrentUser: $($ComputerObject.CurrentUser.ToString())"
                           Write-Output "####################<Break>####################"

                           $ComputerObjects += $ComputerObject
                           
                           Remove-CimSession -CimSession $CimSession 

                     }

                     Else
                     {
                           Write-Output "Remote computer was not online."
                           $ComputerObject = [Ordered]@{}
                           $ComputerObject.ComputerName = $computer
                           $ComputerObject.LastReboot = "Unable to ping. Make sure the computer is turned on and ICMP inbound ports are opened."
                           $ComputerObject.OperatingSystem = "$null"
                           $ComputerObject.Model = "$null"
                           $ComputerObject.RAM = "$null"
                           $ComputerObject.DiskCapacity = "$null"
                           $ComputerObject.TotalDiskSpace = "$null"
                           $ComputerObject.CurrentUser = "$null"

                           $ComputerObjects += $ComputerObject                     
                     }
                  }

                  Else
                  {
                     Write-Output "Computer name was not in a usable format"
                     $ComputerObject.ComputerName = "Value is null. Make sure computer name is not blank"
                     $ComputerObject.LastReboot = "$Null"
                     $ComputerObject.OperatingSystem = "$null"
                     $ComputerObject.Model = "$null"
                     $ComputerObject.RAM = "$null"
                     $ComputerObject.DiskCapacity = "$null"
                     $ComputerObject.TotalDiskSpace = "$null"
                     $ComputerObject.CurrentUser = "$null"

                     $ComputerObjects += $ComputerObject   
                  }
               }
   ```

5. Ignoring the Cim-Session part, what this is doing is looping through one more computers and logging their results into a log file. The first IF block just makes sure you didn't enter a blank computer name, the second sees if the computer is online, and finally => it processes each computer in the list by connecting to them and putting the results into an object called &#8220;$ComputerObject.

5. But we don't want to stop there because there can be many computers and we want a list at the end. So what we do is place each $ComputerObject into a $ComputerObjects array. So now, we go back to the Begin block and initialize the array:

   ```powershell
   $ComputerObjects = @()
   ```

6. Now in the End block, you can just display the results:

   ```powershell
   $ComputerObjects
   ```

7. This works fine for displaying on a screen, but not to a text file. So we do one last thing instead:

   ```powershell
   $a = $ComputerObjects | Out-String
   Write-Output $a
   ```

8. This is a way to convert an object to a string that way the log will look like what is displayed on the screen.