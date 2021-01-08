---
title: 'PS: AutoLaunch Cisco AnyConnect VPN'
date: 2018-04-30T05:14:42+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-autolaunch-cisco-anyconnect-vpn/
categories:
  - Windows
  - Networking
tags:
  - Scripting-Powershell
  - Router
---
<!--more-->

### Description:

Follow this guide to have Anyconnect start after the user signs in on their computer. I couldn't ever get this to officially work because what it does is &#8220;hijack&#8221; Windows explorer as the landing pad and runs a batch file instead and essentially holds the desktop hostage unless the user signs into the VPN. The problem is a couple things:

  1. The network stack doesn't always completely load so sometimes it will throw weird errors.
  2. Sometimes it works perfectly, other times it doesn't?

DISCLAIMER: This was abandoned because we want to go the official route using Cisco Anyconnect SBL => Start Before Logon. Just fun in a lab.

### To Resolve:

1. So start by creating the following in `C:\scripts` on a laptop you want to test this with:

   ```powershell
   c:\scripts\start-vpn\private  
   c:\scripts\start-vpn\private\helpers.psm1 - See [here](https://automationadmin.com/2018/01/ps-helper-functions/).

   c:\scripts\start-vpn\public  
   c:\scripts\start-vpn\public\create-info.bat  
   c:\scripts\start-vpn\public\create-info.ps1  
   c:\scripts\start-vpn\public\create-sched.bat  
   c:\scripts\start-vpn\public\create-sched.ps1  
   c:\scripts\start-vpn\public\startup.bat  
   c:\scripts\start-vpn\public\startup.ps1  
   c:\scripts\start-vpn\public\script.bat
   ```

2. All the bat files just need:

   ```powershell
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -Windowstyle Hidden -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
   ```

   - Except script.bat, it should have:

   ```powershell
   cd "C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client"
   vpncli.exe -s < c:\scripts\Start-VPN\Public\info.dat
   ```

3. Now populate create-info.ps1:

   ```powershell
   If (!(Test-Path $PSScriptRoot\info.dat))
   {
      $User = Read-Host -Prompt "Please enter VPN Username"
      $Pass = Read-Host -Prompt "Please enter VPN Password"
      $val = @"
   connect vpn.yourcompany.com
   $User
   $Pass
   "@
      New-Item -ItemType File -Path $PSScriptRoot -Name info.dat -Value $val
   }
   ```

   - This is to be ran once, it just saves the username and password to a file in c:\scripts\start-vpn\public\ called &#8220;info.dat&#8221;. I know, not secure, but this is just testing. We will eventually need to find a way to store in Credential Manager or encrypt somehow.

4. Now populate &#8220;create-sched.ps1&#8221;:

   ```powershell
   $tName = "VPNStatup"
   $tCommand = "C:\scripts\Start-VPN\Public\startup.bat"
   $tAction = New-ScheduledTaskAction -Execute "$tCommand"
   $uName = "$env:userdomain" + "\" + "$env:username"
   $tTrigger = New-ScheduledTaskTrigger -AtLogOn -User $uName
   Register-ScheduledTask -Action $tAction -Trigger $tTrigger -TaskName $tName -User $uName
   ```

   - This just creates a scheduled task at login to run startup.bat.

5. Now we populate startup.ps1:

   ```powershell
   <#######<Script>#######>
   <#######<Header>#######>
   # Name: Start-VPN
   # Copyright: Gerry Williams (https://automationadmin.com)
   # License: MIT License (https://opensource.org/licenses/mit)
   # Script Modified from: n/a
   <#######</Header>#######>
   <#######<Body>#######>
   Function Start-VPN
   {
      <#
   .Synopsis
   Starts a VPN connection assuming you have internet and are not already connected to internal network.
   .Description
   More thorough description.
   .Parameter Logfile
   Specifies A Logfile. Default is $PSScriptRoot\..\Logs\Scriptname.Log and is created for every script automatically.
   .Example
   Start-VPN
   Usually same as synopsis.
   .Notes
   2017-09-08: v1.0 Initial script 
   .Functionality
   Please see https://automationadmin.com/2017/09/running-ps-scripts-against-multiple-computers/ on how to run against multiple computers.
   #>

      [Cmdletbinding()]
      Param
      (
      )
      
      Begin
      {       
      }
      
      Process
      {   
         Try
         {
               
               $A = Test-Connection -Computername 10.0.0.1 -Quiet -Count 2
               $B = Test-Connection -Computername 8.8.8.8 -Quiet -Count 2
         
               If ($A)
               {
                  $Internal = 1
                  $Justinternet = 0
                  $Notconnected = 0
                  Write-Output "Connected to internal network already"
               }
               Elseif ($B)
               {
                  $Internal = 0
                  $Justinternet = 1
                  $Notconnected = 0
                  Write-Output "Connected to internet, but not internal network. Need to start VPN!"
               }
               Else
               {
                  $Internal = 0
                  $Justinternet = 0
                  $Notconnected = 1
                  Write-Output "Not connected to the internet"
               }

               If ($Justinternet -Eq 1)
               {
                  Get-Process | Foreach-Object `
                  {
                     If ($_.Processname.Tolower() -Eq "Vpnui")
                     {
                           $Id = $_.Id; Stop-Process $Id
                     }
                  }
                  Get-Process | Foreach-Object `
                  {
                     If ($_.Processname.Tolower() -Eq "Vpncli")
                     {
                           $Id = $_.Id; Stop-Process $Id
                     }
                  }
                  Start-Process -Filepath C:\Scripts\Start-VPN\Public\script.Bat -Windowstyle Hidden -Wait
                  Start-Process -Filepath "C:\Program Files (X86)\Cisco\Cisco Anyconnect Secure Mobility Client\Vpnui.Exe"
               }
               Else
               {
                  # Do nothing
               }
         }
         Catch
         {
            Write-Error -Message $($_.Exception.Message)
         }
      }

      End
      {
         
      }

   }

   Start-VPN
   <#######</Body>#######>
   <#######</Script>#######>
   ```

   - Modify line 46 to an IP on your internal network. The idea here is to check their connection status and if they are not connected to the internet at all or connected to your internal network => do nothing. If they have internet and are not connected => launch VPN.

   - We could just stop here, but as I said => sometimes works, sometimes doesn't. So we go a step further&#8230;

6. Modified &#8220;startup.ps1&#8221;:

   ```powershell
   <#######<Script>#######>
   <#######<Header>#######>
   # Name: Start-VPN
   # Copyright: Gerry Williams (https://automationadmin.com)
   # License: MIT License (https://opensource.org/licenses/mit)
   # Script Modified from: n/a
   <#######</Header>#######>
   <#######<Body>#######>
   Function Start-VPN
   {
      <#
      .Synopsis
      This function will start the VPN client before the user can see their desktop.
      #>

      Begin
      {       
         $Vpnui = "C:\Program Files (X86)\Cisco\Cisco Anyconnect Secure Mobility Client\Vpnui.Exe"
         
         Function Continue-ToDesktop
         {
               Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell" -Value "explorer.exe" -Type String
               Start-Process Explorer.Exe
               Start-Sleep 1
               Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell" -Value "c:\scripts\startup.bat" -Type String
         }
         
         Function Show-MessageFullScreenWithBackground ($message)
         {

               Add-Type -AssemblyName System.Windows.Forms

               $Screens = [system.windows.forms.screen]::AllScreens
               $i = 0;
               foreach ($Screen in $Screens)
               {
                  $i++;
                  if ( $Screen.Primary )
                  {
                     $w = $Screen.Bounds.Width #$Screen.WorkingArea.Width if you don't want to go full fullscreen 
                     $h = $Screen.Bounds.Height #$Screen.WorkingArea.Height if you don't want to go full fullscreen
                  }
               }
      
               $objForm = New-Object System.Windows.Forms.Form
               $objForm.StartPosition = "CenterScreen"
               $objForm.Size = New-Object System.Drawing.Size($w, $h)
               $font = New-Object System.Drawing.Font("arial", 22, [System.Drawing.Fontstyle]::Regular)
               $objForm.Font = $font
               $text = New-Object System.Windows.Forms.Label
               $text.Text = "$message"
               $text.Size = New-Object System.Drawing.Size($w, $h)
               $text.TextAlign = "MiddleCenter"
               $objForm.Controls.Add($text)
               $objForm.Autosize = $true
               $objForm.MinimizeBox = $false
               $objForm.MaximizeBox = $false
               $objForm.ShowIcon = $false
               $objForm.BackColor = "#000000"
               $objForm.ForeColor = "#00FF00"
               $objForm.SizeGripStyle = "Hide"
               $objForm.FormBorderStyle = "None"

               $objForm.Show()
               Start-Sleep -Seconds 2

               $text = New-Object System.Windows.Forms.Label
               $text.Text = "please"
               $text.Size = New-Object System.Drawing.Size($w, $h)
               $text.TextAlign = "MiddleCenter"
               $objForm.Controls.Add($text)

               $objForm.Close()
         }
            
      Process
      {   
         
         $a = Test-Connection -ComputerName 10.0.0.1 -Quiet -Count 2
         $b = Test-Connection -ComputerName 8.8.8.8 -Quiet -Count 2
         
         If ($a)
         {
               $Internal = 1
               $JustInternet = 0
               $NotConnected = 0
         }
         Elseif ($b)
         {
               $Internal = 0
               $JustInternet = 1
               $NotConnected = 0
         }
         Else
         {
               $Internal = 0
               $JustInternet = 0
               $NotConnected = 1
         }

         If ($Internal -eq 1)
         {
               Show-MessageFullScreenWithBackground -Message "Connected to internal network, continuing to desktop"
               Continue-ToDesktop
         }
         Elseif ($JustInternet -eq 1)
         {
               Show-MessageFullScreenWithBackground -Message "Please connect to the VPN"
               
               Get-Process | ForEach-Object `
               {
                  if ($_.ProcessName.ToLower() -eq "vpncli")
                  {
                     $Id = $_.Id; Stop-Process $Id
                  }
               }
               
               Do 
               {
                  [string]$vpncli = 'C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exe'
                  Start-Process -WindowStyle Minimized -FilePath $vpncli -ArgumentList "-s < c:\scripts\info.dat"
                  Start-Sleep -Seconds 5
                  Show-MessageFullScreenWithBackground -Message "Please connect to the VPN..."
               }
               Until ($a)

               Continue-ToDesktop
         }
         Else 
         {
               Show-MessageFullScreenWithBackground -Message "No internet detected, continuing to desktop"
               Continue-ToDesktop
         }

      }
      
      End
      {
      
      }

   }

   Start-VPN
   ```

   - This does the same thing, but it will hijack Windows Explorer after the user logs in and instead show a message that they need to connect to the VPN if the conditions of the previous step are met. Lines 20-26 are what hijacks the desktop. They allow the user to the desktop, but change it afterwards to the startup script for the next reboot.  

   - Lines 28-74 are just the function to show the fullscreen message.  

   - Lines 118-125 is the main part it's supposed to keep looping until they connect to the VPN. It's supposed to use the credentials from step 2. You could also look at the Event Viewer here which is how I initially coded it, but it wasn't as reliable as just a ping to an internal device.

7. Well, as I mentioned, this is as far as I got in my lab => if you are working on this => good luck! 

8. Some other resources you could try:

   - [Cisco_Anyconnect.ps1](https://gist.github.com/jhorsman/88321511ce4f416c0605)  

   - [AnyConnect Login Script](https://community.spiceworks.com/scripts/show/4087-automated-anyconnect-login-script)  