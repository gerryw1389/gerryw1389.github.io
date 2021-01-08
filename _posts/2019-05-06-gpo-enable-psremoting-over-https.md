---
title: 'GPO: Enable-PSRemoting Over HTTPS'
date: 2019-05-06T12:30:48+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/05/gpo-enable-psremoting-over-https/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - GroupPolicy
---
<!--more-->

### Description:

This script will be similar to my regular allow PS remoting script, but this is for environments that want HTTPS remoting.

### To Resolve:

1. First, [go the domain's PDC and edit  the GPOs Firewall](https://automationadmin.com/2019/04/gpo-cannot-edit-setting-in-windows-firewall-with-advanced-security/) rule:

   - `Computer Configuration\Policies\Windows Settings\Security Settings\Windows Firewall with Advanced Security`
   - Inbound Rules => Allow 5986 => specify IP addresses

2. Turn on logging:

   - `Computer Configuration\Policies\Windows Settings\Security Settings\Administrative Templates\Windows Components/Windows Powershell\`  
   - Turn on Module Logging  
   - Turn on Powershell Script Block logging  
   - Turn on script execution => Allow local scripts and remote signed scripts

3. Allow remote access:

   - `Computer Configuration\Policies\Windows Settings\Security Settings\Administrative Templates\Windows Components/Windows Remote Shell`  
   - Allow Remote Shell Access => Enabled

4. Finally,  set the service to startup automatically

   - `Computer Configuration\Preferences\Control Panel\Services\`  
   - WinRM => Set to automatic startup

5. Done! Wait, where is the listener? Well unfortunately, you have to set that up yourself. Fortunately, this is easy to script! Here is the following script I ran to remove our regular HTTP remoting and then create a HTTPS listener by binding to a cert that was issued by a third party CA:

   ```powershell
   $Counter = 0
         
   [string]$OsName = Get-WmiObject -Query 'SELECT Caption FROM Win32_OperatingSystem' -Namespace ROOT\Cimv2 | Select-Object -ExpandProperty Caption
   Switch -Regex ($osName)
   {
      '7'
      {
         Write-output $osName; $Counter = 1; Break 
      }
      # Had to put R2 first because if it matches 2008, it would just break and not keep the correct counter. Nested elseif's could be another option.
      '2008 R2'
      {
         Write-output $osName; $Counter = 3; Break 
      }
      '2008'
      {
         Write-output $osName; $Counter = 2; Break 
      }
      '2012 R2'
      {
         Write-output $osName; $Counter = 5; Break 
      }
      '2012'
      {
         Write-output $osName; $Counter = 4; Break 
      }
      '10'
      {
         Write-output $osName; $Counter = 6; Break 
      }
      '2016'
      {
         Write-output $osName; $Counter = 7; Break 
      }
   }
         
   function Enable-PSScriptBlockLogging
   {
      [CmdletBinding()]
      param ()
      $BasePath = "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"

      if (-not (Test-Path $BasePath))
      {
         Write-Verbose "ScriptBlockLogging registry key doesn't exist. Creating now."
         $null = New-Item $BasePath –Force

         Write-Verbose "Setting registry key value to 1 of type DWORD."
         $null = New-ItemProperty $BasePath -Name EnableScriptBlockLogging -Value "1" -PropertyType DWORD
      }
      else
      {
         if ((Get-ItemProperty -Path $BasePath).EnableScriptBlockLogging.getType().Name -eq 'Int32')
         {
               Write-Verbose "Key exists, updating value to 1."
               Set-ItemProperty $BasePath -Name EnableScriptBlockLogging -Value "1"
         }
         else
         {
               Write-Verbose "Key exists of wrong data type, removing existing entry."
               Remove-ItemProperty $BasePath -Name EnableScriptBlockLogging

               Write-Verbose "Setting new registry key value to 1 of type DWORD."
               $null = New-ItemProperty $BasePath -Name EnableScriptBlockLogging -Value "1" -PropertyType DWORD
         }
      }
   }

   If ($Counter -eq 7)
   {
      Enable-PSScriptBlockLogging
      Write-Output "Enabling script block logging since this is Server 2016"
   }

   Function Enable-PSOverHTTPS
   {
      $Cert = Get-Childitem Cert:\LocalMachine\My | Where-Object { $_.Issuer.StartsWith("CN=InCommon") -and $_.notafter -gt (get-date) }

      If ($cert.thumbprint.length -gt 10)
      {
         New-Item -Path WSMan:\LocalHost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $Cert[-1].Thumbprint –Force
         Get-NetFirewallRule -DisplayName "Windows Remote Management (HTTP-In)" | Remove-NetFirewallRule
         Get-ChildItem WSMan:\Localhost\listener | Where-Object -Property Keys -eq "Transport=HTTP" | Remove-Item -Recurse 
         Write-Output " $env:Computername : Successfully enabled HTTPS listener" | Out-File -FilePath "\\fileserver\https-success.txt" -Append -Encoding ASCII
      }
      Else
      {
         Write-Output " $env:Computername : Unable to find computers certificate" | Out-File -FilePath "\\fileserver\https-fail.txt" -Append -Encoding ASCII
      }
   }

   Enable-PSOverHTTPS
   ```

NOTE: Ensure that computer objects can write to the share `\\fileserver` for the logging. Also `$cert[-1]` is used to grab the last cert in case the $cert object returns more than one.
{: .notice--success}
