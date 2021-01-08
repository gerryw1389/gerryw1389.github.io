---
title: Random PS Snippets
date: 2019-06-05T00:40:27-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/06/random-ps-snippets/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

Just a random list of snippets that I use often. Can mostly be found on different pages throughout this site.



#### To create Batch files:

   ```powershell
   For functions:
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command ". "%~dpn0.ps1"; Clean-tempfiles "' -Verb RunAs}"
   popd

   For scripts:
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
   popd
   ```

#### To Compare two files:

   ```powershell
   # Shows same between 1 and 2
   # This shows all the servers that are the same between the vuln.txt and prod.txt.
   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content  "c:\_gwill\temp\prod.txt" ) -IncludeEqual -ExcludeDifferent
   # Shows what is in 2 that is not in 1.
   # Shows all the servers that are in prod.txt, but not in vuln.txt
   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content "c:\_gwill\temp\prod.txt" ) | 
   Where-Object -Property SideIndicator -eq '=>'
   # Shows what is in 1 that is not in two
   # Shows all the servers that are in vuln.txt, but not in prod.txt 
   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content "c:\_gwill\temp\prod.txt" ) | 
   Where-Object -Property SideIndicator -eq '<='
   ```

#### To To create a CSV:

   ```powershell
   # Begin
   $Objects = [System.Collections.Generic.List[PSObject]]@()
   $Intro = 'Netid,Full Name,Email' # Enter column names
   [void]$Objects.Add($Intro)
   # Process
   foreach ($item in $collection)
   {
      $item = 0 # something with an item
      [void]$Objects.Add($Item)
   }
   # End
   $Objects | Out-File "c:\scripts\objects.csv" -Encoding ascii
   ```

#### To To modify a CSV:

   ```powershell
   $lines = Import-csv 'C:\scripts\list.csv' 
   $newcsv = foreach ( $line in $lines )
   {
      $line.action = 'update'
      if ( $line.sex -eq 'Male')
      {
      $line.sex = 'M'
      }
      Else
      {
      $line.sex = 'F'
      }
      [datetime]$date = $line.dateofbirth
      $line.dateofbirth = $date.tostring("yyyy/MM/dd")
      $line
   }
   $NewCSV |export-csv c:\scripts\modified.csv -NoTypeInformation
   ```

#### To create a Hashtable

   ```powershell
   $Params = @{
      'Path' = "HKCU:\Some\Path"
      'Name' = "Category"
      'Value' = "1" 
      'Type' = "DWORD"
   }
   SetReg @Params
   ```

#### To create Arrays (Actually Lists which are more efficient)

   ```powershell
   $Array = [System.Collections.Generic.List[PSObject]]@()
   foreach ($I in $Items)
   {
      [void]$Array.Add($Item)
   }
   ```

#### To get values from a parameter list: For example to equate HardwareInventory to '{00000000-0000-0000-0000-000000000001}'

   ```powershell
   Param
   (
   [Parameter(Mandatory = $true,
   ValueFromPipeline = $true,
   ValueFromPipelineByPropertyName = $true)]
   [string[]]$ComputerName = $env:COMPUTERNAME,

   [Parameter(Mandatory = $true)]
   [ValidateSet('MachinePolicy',
   'DiscoveryData',
   'ComplianceEvaluation',
   'AppDeployment', 
   'HardwareInventory',
   'UpdateDeployment',
   'UpdateScan',
   'SoftwareInventory')]
   [string]$ClientAction
   )

   Begin
   {
   $ScheduleIDMappings = @{
      'MachinePolicy' = '{00000000-0000-0000-0000-000000000021}'
      'DiscoveryData' = '{00000000-0000-0000-0000-000000000003}'
      'ComplianceEvaluation' = '{00000000-0000-0000-0000-000000000071}'
      'AppDeployment' = '{00000000-0000-0000-0000-000000000121}'
      'HardwareInventory' = '{00000000-0000-0000-0000-000000000001}'
      'UpdateDeployment' = '{00000000-0000-0000-0000-000000000108}'
      'UpdateScan' = '{00000000-0000-0000-0000-000000000113}'
      'SoftwareInventory' = '{00000000-0000-0000-0000-000000000002}'
   }
   $ScheduleID = $ScheduleIDMappings[$ClientAction]
   # Schedule ID is used to map a value to a key from a hashtable. You can use this
   }
   Process
   {
      [void] ([wmiclass] "\\$ComputerName)\root\ccm:SMS_Client").TriggerSchedule($ScheduleID)
   }
   ```


### Active Directory

#### To Get members of a group:

   ```powershell
   Get-ADGroupMember -Identity $group -ErrorAction stop			
   ```

#### To Get groups that a member is a part of (memberOf tab):

   ```powershell
   Get-ADPrincipalGroupMembership williamsg | select name
   ```

#### To Get all servers in a certain OU:

   ```powershell
   Get-ADComputer -Filter * -SearchBase "OU=Test,DC=domain,DC=com" | Select-Object -Property "DNSHostName"
   ```

#### To Add user to group:

   ```powershell
   Add-ADGroupMember -Identity "VPN" -Members $name
   ```

#### To See nested groups:

   ```powershell
   Import-Module Activedirectory; Get-ADGroupmember 'Domain Admins' -Recursive | Select-Object -Property Name 
   ```

#### To Get DistinguishedName:

   ```powershell
   (Get-ADComputer -Identity $Computername).DistinguishedName
   ```

#### To Get password expiration:

   ```powershell
   Get-ADUser $user –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" |  Select-Object -Property "Displayname", @{Name = "ExpiryDate"; Expression = { [datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed") } } 
   ```

#### To create a server group:

   ```powershell
   # Have RSAT installed and have $computername populated
   Import-Module ActiveDirectory
   $GroupName = $ComputerName + '.domain.com Administrators'
   New-ADGroup -Name $GroupName -GroupScope "Global" -GroupCategory "Security" -Path 'OU=Servers,DC=domain,DC=com'
   Add-ADGroupMember -Identity $GroupName -Members 'veeam'
   Add-ADGroupMember -Identity $GroupName -Members 'SysAdmins'
   ```

#### To blank out property

   ```powershell
   $users = @(
   'ashleyh-admin',
   'studere-admin',
   'williamsg-admin')
   Import-module activedirectory
   foreach ($user in $users)
   {
   $u = Get-ADUser -Identity $user
   Set-ADuser -Identity $u -EmailAddress $null
   Write-Output "Set email to null: $user"
   }
   ```

#### To To view group gidNumbers

   ```powershell
   $properties = @{ 
   'LDAPFilter' = "(&(objectCategory=group)(gidNumber=*))" 
   'SearchBase' = 'OU=AdminAccounts,OU=VP for Information Technology,OU=President,OU=Departments,DC=uta,DC=edu' 
   'Properties' = 'gidNumber' 
   }
   $groups = Get-ADObject @Properties| Select-Object @{Name = "DN"; Expression = {$_.DistinguishedName}}, @{Name = "gid"; Expression = {$_.gidNumber}}
   ```

   #### To view user gidNumbers
   
   ```powershell
   $properties = @{ 
   'LDAPFilter' = "(&(objectCategory=user)(gidNumber=*))" 
   'SearchBase' = 'OU=AdminAccounts,OU=VP for Information Technology,OU=President,OU=Departments,DC=uta,DC=edu' 
   'Properties' = 'gidNumber' 
   }
   $users = Get-ADObject @Properties| Select-Object @{Name = "DN"; Expression = {$_.DistinguishedName}}, @{Name = "gid"; Expression = {$_.gidNumber}}
   ```


### Parameters:

#### To add common parameters

   ```powershell
   [Cmdletbinding()]
      Param
      (
         [Parameter(Mandatory=$true, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, Position=0)]
         [String[]]$RegistryKey,
         
         [Parameter(Mandatory=$true, Position=1)]
         [String]$Username,
         
         [String]$Logfile = "$PSScriptRoot\..\Logs\Set-RegistryPermission.log"
      )
   ```

#### To add Requires statements

   ```powershell
   #Requires -Version <N>[.<n>]
   #Requires -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
   #Requires -Modules { <Module-Name> | <Hashtable> }
   #Requires -PSEdition <PSEdition-Name>
   #Requires -ShellId <ShellId>
   #Requires -RunAsAdministrator
   ```

#### To Use -Whatif:

   ```powershell
   Function Restart-Computers
   {
      [CmdletBinding(SupportsShouldProcess = $true)]
      param(
         [string[]]$ComputersToRestart
      )

      ForEach ($Computer in $ComputersToRestart)
      {
         # If the user uses the -Whatif parameter, this will show: 
         # What if: Performing the operation "Rebooting the server" on target "Server01", but won't actually do it.
         If ($pscmdlet.ShouldProcess("$Computer", "Rebooting the server"))
         {
               # Put code here for code you want to run if the user DOESN'T USE the -WhatIf parameter
               Write-Output "Restarting computer $Computer"
               Restart-Computer $Computer 
         }
      }
   }
   Restart-Computers -ComputersToRestart "Server01", "Server02" -WhatIf
   ```

#### To reference ISE Advanced Function - Full:

   ```powershell
   <#
      .Synopsis
         Short description
      .DESCRIPTION
         Long description
      .EXAMPLE
         Example of how to use this cmdlet
      .EXAMPLE
         Another example of how to use this cmdlet
      .INPUTS
         Inputs to this cmdlet (if any)
      .OUTPUTS
         Output from this cmdlet (if any)
      .NOTES
         General notes
      .COMPONENT
         The component this cmdlet belongs to
      .ROLE
         The role this cmdlet belongs to
      .FUNCTIONALITY
         The functionality that best describes this cmdlet
      #>
      function Verb-Noun
      {
            [CmdletBinding(DefaultParameterSetName='Parameter Set 1', 
                        SupportsShouldProcess=$true, 
                        PositionalBinding=$false,
                        HelpUri = 'http://www.microsoft.com/',
                        ConfirmImpact='Medium')]
            [Alias()]
            [OutputType([String])]
            Param
            (
               # Param1 help description
               [Parameter(Mandatory=$true, 
                           ValueFromPipeline=$true,
                           ValueFromPipelineByPropertyName=$true, 
                           ValueFromRemainingArguments=$false, 
                           Position=0,
                           ParameterSetName='Parameter Set 1')]
               [ValidateNotNull()]
               [ValidateNotNullOrEmpty()]
               [ValidateCount(0,5)]
               [ValidateSet("sun", "moon", "earth")]
               [Alias("p1")] 
               $Param1,
      
               # Param2 help description
               [Parameter(ParameterSetName='Parameter Set 1')]
               [AllowNull()]
               [AllowEmptyCollection()]
               [AllowEmptyString()]
               [ValidateScript({$true})]
               [ValidateRange(0,5)]
               [int]
               $Param2,
      
               # Param3 help description
               [Parameter(ParameterSetName='Another Parameter Set')]
               [ValidatePattern("[a-z]*")]
               [ValidateLength(0,15)]
               [String]
               $Param3
            )
      
            Begin
            {
            }
            Process
            {
               if ($pscmdlet.ShouldProcess("Target", "Operation"))
               {
               }
            }
            End
            {
            }
      }
      End
      {

      }

   }
   ```

