---
title: 'PS: Multiline Inputbox'
date: 2019-08-10T00:25:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/08/ps-multiline-inputbox/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So using VMWare Orchestrator we were able to get VMs to deploy that send a json string via email to the person who submits the request. 

I then wrote a quick powershell script that a user can copy and paste the json string into and it will return a list of properties in a `result` table for them.

The generic code can be found below but the gist of it is that you would then use `json | gm` to see the properties and then store those in a hashtable. 

### To Resolve:

1. For example, you would first map the json properties to easier names:

   ```powershell
   # Map to easy names
   $server = [ordered] @{
      # About the host
      'Hostname'                   = $json.machine.name
      'FQDN'                       = $json.machine.name + '.domain.com'
      'HostIPAddress'              = $json.machine.properties.'VirtualMachine.Network0.Address'
      'ComputerOU'                 = $json.machine.properties.'ext.policy.activedirectory.orgunit'
      'UserGeneratedPartofName'    = $json.machine.properties.'COMPANY.ApplicationName'
      'OSType'                     = $json.machine.properties.'COMPANY.OSType'
      'Type'                       = $json.machine.properties.textField_fbaea404
      'ServerType'                 = $json.machine.properties.'COMPANY.ServerType'
      'Environment'                = $json.machine.properties.'COMPANY.Environment'
      # Vmware
      'HardwareSpecs'              = $json.machine.properties.textArea_a0b98a8f
      'Size'                       = $json.machine.properties.size
      'VcenterUUID'                = $json.machine.properties.'VirtualMachine.Admin.UUID'
      'VeeamBackupGroup'           = $json.machine.properties.'PpS.CategoryTag.VMTag.Veeam-Backup-Groups'
      'reservationid'              = $json.machine.properties.ReservationPolicyID
      'VMtaggingID'                = $json.machine.properties.'Extensibility.Workflows.vmTagging.Id'
      # other
      'ServiceNowTicketNo'         = $json.machine.properties.'COMPANY.ServiceNowTicketNo'
      'CostCenter'                 = $json.machine.properties.'PpS.CategoryTag.VMTag.Cost Center'
      'BackupRequired'             = $json.machine.properties.'COMPANY.IsBackupRequired'
      'NeedCNAME'                  = $json.machine.properties.'COMPANY.NeedCNAME'
      'CNAME'                      = $json.machine.properties.'COMPANY.CNAME'
      #Inventory
      'SupportLevel'               = $json.machine.properties.'COMPANY.SupportLevel'
      'NameofApplicationRunning'   = $json.machine.properties.'COMPANY.NameofApplicationRunning'
      'NameApplicationsSupporting' = $json.machine.properties.'COMPANY.NameApplicationsSupporting'
      'PrimarySystemAdmin'         = $json.machine.properties.'COMPANY.PrimarySystemAdmin'
   }
   ```

2. You can then fix any discrepencies:

   ```powershell
   # Conversions
   If ( $($server.Environment) -eq 'p' )
   {
      $serverEnvironment = 'Production'
   }
   Elseif ( $($server.Environment) -eq 't')
   {
      $serverEnvironment = 'Test'
   }
   Elseif ( $($server.Environment) -eq 'd')
   {
      $serverEnvironment = 'Development'
   }
   Else
   {
      $serverEnvironment = 'Unknown'
   }
   ```

3. Finally, you would send those results to the screen, a text file, or another email, or whatever:

   ```powershell
   Write-Output "######## SysAdmin Info #################"
   $sysAdmin = [ordered] @{
      'Canonical FQDN'              = $($server.FQDN)
      'IPAddress'                   = $($server.HostIPAddress)
      'Computer OU'                 = $($server.ComputerOU)
      'User Generated Part of Name' = $($server.UserGeneratedPartofName)
      'OS Type'                     = $serverOS
      'Server Type'                 = $serverType
      'Environment'                 = $serverEnvironment
   }
   Write-Output $sysAdmin
   ```

4. Source is maintained under [gwMisc](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Read-MultiLineInputBox.ps1).
