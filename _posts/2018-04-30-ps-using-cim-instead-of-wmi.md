---
title: 'PS: Using CIM instead of WMI'
date: 2018-04-30T04:09:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-using-cim-instead-of-wmi/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So as I'm going through scripts and adding them to my GitHub repo, I'm seeing quite a few of my functions using WMI instead of CIM. So I'm now going through and correcting them.

### To Resolve:

1. WMI => CIM Notes:

   Get-CimInstance => Gets instances of a class.  
   New-CimInstance => Creates a new instance of a class.  
   Remove-CimInstance => Removes one of more instances of a class.  
   Set-CimInstance => Modifies one or more instances of a class.  
   Get-CimAssociatedInstance => Gets all the associated instances for a particular instance.  
   Invoke-CimMethod => Invokes instance or static method of a class.  
   Get-CimClass => Gets class schema of a CIM class.  
   Register-CimIndicationEvent => Helps subscribe to events.  
   New-CimSession => Creates a CIM Session with local or a remote machine  
   Get-CimSession => Gets a list of CIM Sessions that have been made.  
   Remove-CimSession => Removes CimSessions that are there on a machine.  
   New-CimSessionOption => Creates a set of options that can be used while creating a CIM session.

   Commands = Old => New  
   Get-WmiObject => Get-CimInstance  
   Get-WmiObject -list => Get-CimClass  
   Set-WmiInstance => Set-CimInstance  
   Set-WmiInstance –PutType CreateOnly => New-CimInstance  
   Remove-WmiObject => Remove-CimInstance  
   Invoke-WmiMethod => Invoke-CimMethod

   WSMan:  
   Test-WSMan  
   Get-WSManInstance  
   Set-WSManInstance  
   New-WSManInstance  
   Remove-WSManInstance  
   Invoke-WSManAction

   Cmdlets for Configuring WSMan Session:  
   Connect-WSMan  
   Disconnect-WSMan  
   New-WSManSessionOption  
   Set-WSManQuickConfig  
   Get-WSManCredSSP  
   Enable-WSManCredSSP  
   Disable-WSManCredSSP

1. To find older WMI methods that CIM doesn't appear to offer (but it does):

   ```powershell
   (Get-CIMClass win32_operatingsystem).CimClassMethods
   ```

   For example, this finds the same Win32Shutdown method that WMI has and tells me it needs an argument called &#8220;@{ Flags = [int] }&#8221;. So from here, I just sub in my $_action variable for my [Restart-ComputerWin32](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Restart-ComputerWin32.ps1) script.

1. One thing you can place in your scripts is:

   ```powershell
   Try
   {
      $Options = New-CimSessionOption -Protocol WSMAN
      $CimSession = New-CimSession -ComputerName $Computer -Credential $Credential -SessionOption $Options -ErrorAction Stop
      Write-Output "Using protocol: WSMAN"
   }
   Catch
   {
      $Options = New-CimSessionOption -Protocol DCOM
      $CimSession = New-CimSession -ComputerName $Computer -Credential $Credential -SessionOption $Options
      Write-Output "Using protocol: DCOM"
   }
   ```

   This will try and connect to computers using the preferred WSMAN protocol and then, if it fails, go back to DCOM. Then to query specific things, you just build a table:

   ```powershell
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

   $ComputerObjects += $ComputerObject

   Remove-CimSession -CimSession $CimSession
   ```

   This assumes you are using a foreach loop to loop through multiple computers. The goal is build a table and then display that in the End{} block.