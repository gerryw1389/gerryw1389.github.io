---
title: 'PS: Software Commands'
date: 2016-06-02T20:56:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ps-software-commands/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

This section is for Powershell itself and any software on the OS.

#### To See how Powershell developers coded an internal function (Out-File in this example):

   ```powershell
   $command = Get-Command Out-File -CommandType Cmdlet
   $metadata = New-Object System.Management.Automation.CommandMetaData($command)
   $proxyCode = [System.Management.Automation.ProxyCommand]::Create($metadata)
   $proxyCode
   ```

   - NOTE: Almost all command prompt commands work just as well in Powershell. Search the &#8220;batch&#8221; label to see examples of them.

#### To Launch PS As Admin:

   ```powershell
   Start-Process powershell.exe -verb runas
   ```

#### To Launch ISE As Admin:

   ```powershell
   Start-Process powershell_ise -verb runas
   ```

#### To Start An EXE As Admin:

   ```powershell
   cmd /c "runas /profile /user:server\administrator "C:\Program Files (x86)\Google\Drive\googledrivesync.exe""
   ```

#### To Make A Shortcut Run As Admin

   ```powershell
   $fullpath = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative Tools\Event Viewer.lnk'
   $fileBytes = [System.IO.File]::ReadAllBytes($fullpath)
   $fileBytes[0x15] = $fileBytes[0x15] -bor 0x20
   [System.IO.File]::WriteAllBytes($fullpath, $fileBytes)
   ```

#### To Start A Program Normally:

   ```powershell
   C:\Windows\System32\calc.exe
   # or
   cmd /c "start C:\Windows\System32\calc.exe"
   # or 
   & C:\Windows\System32\calc.exe
   ```

#### To Bulk Install Programs (Change the path of the executables relative to scripts running path)

   ```powershell
   Write-Output "Installing PDF" 
   If (!(Test-Path "C:\Program Files (x86)\PDF"))
   {
      Set-Location -Path "$PSScriptRoot\..\Private\Bin\pdf"
      Invoke-Item -Path "$PSScriptRoot\..\Private\Bin\pdf\setup.exe"
      cmd /c "pause"
   }
   Else
   {
      Write-Output "PDF already installed, moving on" 
   }
   ```

#### To Get OS Version

   ```powershell
   # To get the Server OS Version:

   $Counter = 0
   [string]$OsName = Get-Ciminstance -ClassName Win32_OperatingSystem -Property Caption | Select-Object -ExpandProperty Caption

   Switch -Regex ($osName)
   {
      '7'
      {
         Log $osName; $Counter = 1; Break 
      }
      # Had to put R2 first because if it matches 2008, it would just break and not keep the correct counter. Nested elseif's could be another option.
      '2008 R2'
      {
         Log $osName; $Counter = 3; Break 
      }
      '2008'
      {
         Log $osName; $Counter = 2; Break 
      }
      '2012 R2'
      {
         Log $osName; $Counter = 5; Break 
      }
      '2012'
      {
         Log $osName; $Counter = 4; Break 
      }
      '10'
      {
         Log $osName; $Counter = 6; Break 
      }
      '2016'
      {
         Log $osName; $Counter = 7; Break 
      }
   }

   # Then, if older than 2012r2, you can run this:

   If ($Counter -le 4)
   {
      # Do something in older versions of Powershell (Versions 2, 3)
   }
   Else
   {
      # Do something in newer versions of Powershell (4+)
   }

   ```

#### To Interact With COM Objects (Outlook in this example)

   ```powershell
   # New Outlook object
   $ol = new-object -comobject "Outlook.Application";

   # MAPI namespace
   $mapi = $ol.getnamespace("mapi");

   $folder =  $mapi.Folders.Item('name@gmail.com').Folders.Item('Inbox')

   # Get the items in the folder
   $contents = $folder.Items

   # Sort the items in the folder by the metadata, in this case ReceivedTime
   $contents.Sort("ReceivedTime")

   # Get the first item in the sorting; in this case, you will get the oldest item in your inbox.
   $item = $contents.GetFirst()
   echo $item

   # If instead you wanted to get the newest item, you could do the same thing but do $item = $contents.GetLast()

   ```

#### To Make Sure A Script Is Running As Admin, And If Not – Restart As Admin With All Parameters Passed:

   ```powershell
   If (-Not ([Security.Principal.Windowsprincipal][Security.Principal.Windowsidentity]::Getcurrent()).Isinrole([Security.Principal.Windowsbuiltinrole] "Administrator"))
   {
   $Arguments = "& '" + $Myinvocation.Mycommand.Definition + "'"
   Start-Process Powershell -Verb Runas -Argumentlist $Arguments
   Break
   }
   ```

#### To Clear The Credential Manager:

   ```powershell
   cmd /c "cmdkey /list" | ForEach-Object {if ($_ -like "*Target:*")
   {
   cmdkey /del:($_ -replace " ", "" -replace "Target:", "")
   }}
   ```

#### To Stop A Process If It Is Running:

   ```powershell
   $process = Get-Process -Name "powershell.exe" -ErrorAction SilentlyContinue
   If ($process -eq $null)
   {
   Write-Output "$($process.name) is not running, continuing…"
   }
   Else
   {
   Stop-Process $process
   Write-Output "$($process.name) is running, closing"
   }
   ```

#### To Restart A Computer Into Advanced Startup Mode:

   ```powershell
   cmd /c "shutdown /o /r /t 02"
   ```

#### To Add An Environmental Variable:

   ```powershell
   $X = "C:\_Gwill\Google\Scripts\_Other-Langs\Python\Python27"
   $Env:Path+= ";" + $X + ";"
   [Environment]::Setenvironmentvariable("Path",$Env:Path, [System.Environmentvariabletarget]::User)
   Write-Output "Path Updated Permanently!!"
   ```

#### To Enable System Restore and Create A Checkpoint:

   ```powershell
   Enable-ComputerRestore -Drive $env:systemdrive -Verbose
   Checkpoint-Computer -Description "Default Config" -RestorePointType "MODIFY_SETTINGS" -Verbose
   ```

#### To Set UAC Setting To Third Bar Down (Notify When Apps Make Changes… Don't Dim):

   ```powershell
   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "ConsentPromptBehaviorAdmin"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "EnableInstallerDetection"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "PromptOnSecureDesktop"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
   $Name = "FilterAdministratorToken"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Set A Daily Task (Daily/2AM):

   ```powershell
   $taskName = "ExampleDailyChocolateyUpgrade"
   $taskAction = New-ScheduledTaskAction –Execute C:\programdata\chocolatey\choco.exe -Argument "upgrade all -y"
   $taskTrigger = New-ScheduledTaskTrigger -At 2am -Daily
   $taskUser = "System"
   Register-ScheduledTask –TaskName $taskName -Action $taskAction –Trigger $taskTrigger -User $taskUser
   ```

#### To Set Power Settings To "Never Sleep":

   ```powershell
   cmd /c "powercfg -change -monitor-timeout-ac 0"
   cmd /c "powercfg -change -monitor-timeout-dc 0"
   cmd /c "powercfg -change -standby-timeout-ac 0"
   cmd /c "powercfg -change -standby-timeout-dc 0"
   cmd /c "powercfg -change -disk-timeout-ac 0"
   cmd /c "powercfg -change -disk-timeout-dc 0"
   cmd /c "powercfg -change -hibernate-timeout-ac 0"
   cmd /c "powercfg -change -hibernate-timeout-dc 0"
   ```

#### To Allow Pings, RDP, WMI, and File and Printer Sharing Through Firewall:

   ```powershell
   Import-Module NetSecurity
   Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
   New-NetFirewallRule -Name Allow_RDP -DisplayName "Allow Ping" -Description "Packet Internet Groper ICMPv4" -Protocol ICMPv4 -IcmpType Any -Enabled True -Profile Any -Action Allow
   New-NetFirewallRule -Name Allow_Ping -DisplayName "Allow Ping" -Description "Packet Internet Groper ICMPv4" -Protocol ICMPv4 -IcmpType Any -Enabled True -Direction Outbound -Profile Any -Action Allow
   Set-NetFirewallRule -DisplayGroup "Windows Management Instrumentation (WMI)" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Network Discovery" -Profile Any
   Set-NetFirewallRule -DisplayGroup "File and Printer Sharing" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Windows Firewall Remote Management" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Core Networking" -Profile Any
   ```

#### To Create Custom Firewall Rules

   ```powershell
   $Params = @{
      'DisplayName' = "AllowRDP"
      'Description' = "Allow Remote Desktop"
      'Profile' = "Any"
      'Direction' = "Inbound"
      'LocalPort' = "3389"
      'Protocol' = "TCP"
      'Action' = "Allow"
      'Enabled' = "True"
   }
   New-NetFirewallRule @Params | Out-Null
   ```

#### To Disable Firewall

   ```powershell
   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
   # or
   netsh advfirewall set allprofiles state off
   ```

#### To Enable Remote Desktop With Network Level Authentication:

   ```powershell
   $registryPath = "HKLM:\System\CurrentControlSet\Control\Terminal Server"
   $Name = "fDenyTSConnections"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null

   $registryPath = "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"
   $Name = "UserAuthentication"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Remote Assistance:

   ```powershell
   $registryPath = "HKLM:\System\CurrentControlSet\Control\Remote Assistance"
   $Name = "fAllowToGetHelp"
   $value = "0"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Disable Windows Update Automatic Restart:

   ```powershell
   $registryPath = "HKLM:\Software\Microsoft\WindowsUpdate\UX\Settings"
   $Name = "UxOption"
   $value = "1"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   ```

#### To Export/Import Start Menu Layouts:

   ```powershell
   Export-StartLayout –path c:\_gwill\startmenu.xml
   Import-StartLayout -LayoutPath c:\software\startmenu.xml -MountPath c:
   ```

#### To Disable Windows Defender:

   ```powershell
   # Get information about Server roles and features that are available or installed
   Get-WindowsFeature
   # Turn-off real-time protection
   Set-MpPreference -DisableRealtimeMonitoring $true
   # Check real-time protection status
   Get-MpPreference | FL *RealtimeMonitoring
   # Turn-on real-time protection
   Set-MpPreference -DisableRealtimeMonitoring $false
   # Install Windows Defender GUI (no restart required)
   Install-WindowsFeature Windows-Defender-GUI
   # Uninstall Windows Defender and its GUI (restart required)
   Remove-WindowsFeature Windows-Defender, Windows-Defender-GUI
   ```

#### To disable Windows defender another way:

   ```powershell
   $registryPath = "HKLM:\System\CurrentControlSet\Services\SecurityHealthService"
   $name = "Start"
   $value = "4"
   IF(!(Test-Path $registryPath))
   {
   New-Item -Path $registryPath -Force | Out-Null
   }
   New-ItemProperty -Path $registryPath -Name $name -Value $value -PropertyType DWORD -Force | Out-Null
   Restart-Computer
   ```

#### To Enable PS Remoting:

   ```powershell
   Enable-Psremoting -Force
   # Make sure to hit "a" yes to all on the prompts
   ```

#### To Update Help (One of the First Tasks To Do):

   ```powershell
   Update-Help
   ```

#### To Create A Text File of A Command's Help:

   ```powershell
   Get-Help (Commandname) -Full >(Commandname Or Whatever).Txt
   ```

#### To Get A Pop-Up Window In Finding Help:

   ```powershell
   Get-Help Invoke-Item -ShowWindow
   ```

#### To Run A &#8220;What-If&#8221; Analysis For A Command. You Can Also Use &#8220;-confirmation&#8221; For A Pop-Up Confirmation Prompt:

   ```powershell
   Restart-Computer -WhatIf
   #or
   Restart-Computer -Confirm
   ```

#### To Find the Properties/Method of A Command. Pipe To Get-Member or &#8220;gm&#8221;:

   ```powershell
   Get-Process | Gm
   ```

#### To Start A Transcript Of All Commands and Their Output For A PS Session:

   ```powershell
   Start-Transcript (Pathname)
   ```

#### To Change The Background of the PS GUI:

   ```powershell
   (Get-Host).Ui.Rawui.Backgroundcolor = "Red"
   ```

#### To Check The Execution Policy and Change It To Remote Signed:

   ```powershell
   # Must Run-As Admin

   # Gets Current Execution Policy
   Get-Executionpolicy
   Set-Executionpolicy Remotesigned
   ```

#### To Get The Version of PS Running:

   ```powershell
   $PSVersionTable
   ```

#### To Open Your Current Directory In Windows Explorer Using Invoke-Item:

   ```powershell
   ii .
   ```

   - Stands for Invoke-Item -Path $currentDirectory

#### To See If A Command Has An Alias:

   ```powershell
   Get-Alias -Definition (Commandname)
   ```

#### To Create Your Own Alias:

   ```powershell
   New-Alias -Name (Shortname) -Val (Realcommandname) -Desc (Not Mandatory But You Can Add A Description)
   ```

#### To Search Help On SS64.com From PS:

   ```powershell
   Function Get-Help2
   {
   param([string]$command)
   $lcommand = $command.ToLower()
   Start-process -filepath "http://ss64.com/ps/$lcommand.html"
   }
   ```

#### To AutoLoad Scripts (Usually Placed In PS Profile):

   ```powershell
   $autodir="C:\Scripts\_Autoload"
   Get-ChildItem "${autodir}\*.ps1" | ForEach-Object {. $_}
   Write-Output "Scripts in " + $autodir + " loaded"
   ```

#### To Add All Clients To Trusted Hosts

   ```powershell
   Set-Item wsman:\localhost\Client\TrustedHosts -value *
   ```

#### To Learn Begin, Process, End:

   ```powershell
   Function Test-BPEPowershell
   {
   Begin
   {
   $i = 0
   Write-Host "Setting `$i in Begin to $i"
   }
   Process
   {
   $i++
   Write-Host "Setting `$i in Begin to $i"
   }
   End
   {
   Write-Host "Setting `$i in Begin to $i"
   }
   }
   '1', '2', '3' |Test-BPEPowershell
   ```

#### To Learn &#8220;-WhatIf&#8221;:

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

#### To Create A Collection Of Objects In A Single Variable:

   ```powershell
   [System.Management.Automation.Scriptblock]$Scriptblock = {
   $Lastboottime = (Get-Ciminstance -Classname Win32_Operatingsystem | Select-Object -Property Lastbootuptime).Lastbootuptime
   Return [Datetime]$Lastboottime
   }

   Process
   {
   Foreach ($Computer In $Computername)
   {
   $Lastboottime = Invoke-Command -Scriptblock $Scriptblock
   }
   $table = [Pscustomobject] @{
   Computername = $Computer
   Lastboottime = $Lastboottime
   }
   ```

   - Info we need:  
   - For Each $computer in $computername – builds the computer name table  
   - $lastboottime = main information we want to get from each computer  
   - $table = Variable that will hold the values for each computer processed

### More Advanced:

#### To Make Your Computer Talk Using MS Speech:

   ```powershell
   Add-Type -AssemblyName System.speech
   $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
   $speak.Speak('Ohhh Baby Ohh Yeah Do Me Harder')
   ```

#### To Make Sure Your Script Runs As Administrator:

   ```powershell
   If (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
   [Security.Principal.WindowsBuiltInRole] "Administrator"))
   {
   Write-Warning "You do not have Administrator rights to run this script!`nPlease re-run this script as an Administrator!"
   Break
   }

   ```

#### To Disable Screensaver:

   ```powershell
   Set-ItemProperty -Path 'HKCU:SoftwarePoliciesMicrosoftWindowsControl PanelDesktop' -Name ScreenSaveTimeOut -Value 0
   Set-ItemProperty -Path 'HKCU:SoftwarePoliciesMicrosoftWindowsControl PanelDesktop' -Name ScreenSaveActive -Value 0
   Set-ItemProperty -Path 'HKCU:SoftwarePoliciesMicrosoftWindowsControl PanelDesktop' -Name ScreenSaverIsSecure -Value 0
   ```

#### To Enable Task Manager (post virus cleanup):

   ```powershell
   Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\System' -Name DisableTaskMgr -Value 0
   ```

#### To Disable Windows 7 Automatic Driver Installation:

   ```powershell
   Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching -Name SearchOrderConfig -Value 0
   ```

#### To Add A GUI To Server 2012 Core: to uninstall type &#8220;uninstall&#8221; at the beginning

   ```powershell
   Install-WindowsFeature -ComputerName Server-Gui-Mgmt-Infra, Server-Gui-Shell -Restart
   ```

#### To Get All Scheduled Tasks and Export Them To CSV:

   ```powershell
   schtasks /query /v /fo csv | out-file tasks.csv
   ```

#### To Create A Pop-Up Window:

   ```powershell
   $wshell = New-Object -ComObject Wscript.Shell -ErrorAction Stop
   $wshell.popup("Text",0,"Message",48+4)
   #or
   (new-object -ComObject wscript.shell).Popup("Text",3,"Message") 
   # Change the 3 to however long you want to message to appear. 0 will leave it up until user intervention.
   ```

#### To Change The Hostname:

   ```powershell
   # From Elevated CMD:
   $computerName = Get-WmiObject Win32_ComputerSystem
   $newName = Read-Host -Prompt "Please enter new hostname:"
   $computerName.Rename($newName)
   # For PSv3+:
   Rename-Computer "newName"
   Restart-Computer -Force
   ```

#### To Get Logged On User:

   ```powershell
   Get-WmiObject Win32_LogonSession -ComputerName localhost -Filter 'LogonType=2 OR LogonType=10' |
   Foreach-Object { $_.GetRelated('Win32_UserAccount') } |
   Select-Object Caption -Unique
   ```

#### To Get Last Reboot Time:

   ```powershell
   $RebootTime = [System.DateTime]::ParseExact((Get-WmiObject Win32_OperatingSystem -ComputerName localhost| foreach{$_.LastBootUpTime}).split('.')[0],'yyyyMMddHHmmss',$null)
   $RebootTime
   ```

#### To Run Remote .BAT file Using PS Remoting:

   ```powershell
   copy c:\test.bat \\test\c$\test.bat
   invoke-command -script {c:\test.bat} -computer test
   ```

#### To have a service start automatically:

   ```powershell
   $A = get-service Wuauserv
   if ($A.Status -eq "Stopped") {$A.start()} elseIf ($A.status -eq "Running") {Write-Output -Verbose $A.name "is running"}
   ```

#### To unblock scripts you download:

   ```powershell
   gci C:\path\to\scripts -recurse | unblock-file -Verbose
   ```

#### To Save To SQL Database

   ```powershell
   <#
   Saving data to SQL Server - versus Excel or some other contraption - is easy.

   Assume that you have SQL Server Express installed locally. You've created in it a database called MYDB, and in that a table called MYTABLE. 
   The table has ColumnA and ColumnB, which are both strings (VARCHAR) fields. And the database file is in c:\myfiles\mydb.mdf. 
   This is all easy to set up in a GUI if you download SQL Server Express "with tools" edition. And it's free!

   $cola = "Data to go into ColumnA"
   $colb = "Data to go into ColumnB"

   $connection_string = "Server=.\SQLExpress;AttachDbFilename=C:\Myfiles\mydb.mdf;Database=mydb;Trusted_Connection=Yes;"
   $connection = New-Object System.Data.SqlClient.SqlConnection
   $connection.ConnectionString = $connection_string
   $connection.Open()
   $command = New-Object System.Data.SqlClient.SqlCommand
   $command.Connection = $connection

   $sql = "INSERT INTO MYTABLE (ColumnA,ColumnB) VALUES('$cola','$colb')"
   $command.CommandText = $sql
   $command.ExecuteNonQuery()

   $connection.close()
   You can insert lots of values by just looping through the three lines that define the SQL statement and execute it:

   $cola = @('Value1','Value2','Value3')
   $colb = @('Stuff1','Stuff2','Stuff3')

   $connection_string = "Server=.\SQLExpress;AttachDbFilename=C:\Myfiles\mydb.mdf;Database=mydb;Trusted_Connection=Yes;"
   $connection = New-Object System.Data.SqlClient.SqlConnection
   $connection.ConnectionString = $connection_string
   $connection.Open()
   $command = New-Object System.Data.SqlClient.SqlCommand
   $command.Connection = $connection

   for ($i=0; $i -lt 3; $i++) {
   $sql = "INSERT INTO MYTABLE (ColumnA,ColumnB) VALUES('$($cola[$i])','$($colb[$i])')"
   $command.CommandText = $sql
   $command.ExecuteNonQuery()
   }

   $connection.close()
   It's just as easy to run UPDATE or DELETE queries in exactly the same way. SELECT queries use ExecuteReader() instead of ExecuteNonQuery(), and return a SqlDataReader object that you can use to read column data or advance to the next row.
   #>

   ```

