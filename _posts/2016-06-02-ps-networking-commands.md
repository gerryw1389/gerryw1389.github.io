---
title: 'PS: Networking Commands'
date: 2016-06-02T20:58:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ps-networking-commands/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

I still mainly use CMD commands for these, but this is a list of networking related commands you can do from Powershell:

#### To Check If A Port Is Open (Quit using Telnet! It's 2018!!)

   ```powershell
   Test-NetConnection myserver.domain.com -port 445
   # Look for the TCPTestSucceeded to be "True"
   # This shows that TCP packets can traverse as opposed to just ICMP packets
   # I use this one almost daily

   # Test-NetConnection for Server2008r2:
   $tcp = New-Object Net.Sockets.TcpClient 
   $tcp.Connect("10.45.23.109", 443)
   ```

#### To Interact With REST API's

   ```powershell
   # Rest method examples
   Invoke-RestMethod -Uri 'https://api.chucknorris.io/jokes/random' -Method Get | 
   Select-Object -ExpandProperty Value
   Invoke-RestMethod -Uri 'https://catfact.ninja/fact' -Method Get | 
   Select-Object -ExpandProperty Fact
   ```

#### Or Just Regular Sites Like SS64:

   ```powershell
   Function Get-Help2
   {
      <# 
   .Synopsis
   Launches a window in SS64.com for a selected command.
   .Description
   Launches a window in SS64.com for a selected command.
   .Example
   Get-Help Get-Process
   Opens a window in your default internet browser to ss64's page on get-process.
   .Notes
   2017-10-19: v1.0 Initial script 
   #>
      param
      (
         [string]$command
      )
      $command = $command.ToLower()
      Start-process -filepath "https://ss64.com/ps/$command.html"
   }
   ```

#### To Disable DHCP On A NIC (W8/Server 2012):

   ```powershell
   Get-NetAdapter -Name "Local Area Connection" | Set-NetIPInterface -DHCP Disabled
   ```

#### To Set A Static IP and Default Gateway (W8/Server 2012):

   ```powershell
   Get-NetAdapter -Name "Local Area Connection" | New-NetIPAddress -AddressFamily IPv4 -IPAddress 10.0.1.100 -PrefixLength 24 -Type Unicast -DefaultGateway 10.0.1.1
   ```

#### To Configure DNS Server Address (W8/ Server 2012):

   ```powershell
   Get-NetAdapter -Name "Local Area Connection" | Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 10.0.1.10
   ```

#### To Map A Network Drive:

   ```powershell
   New-PSDrive -Name S -Root \Server01Scripts -Persist -PSProvider FileSystem
   ```

   - This creates a S: visible in Windows Explorer that is a permanent mapped drive.

#### To Get Public IP:

   ```powershell
   $publicIP = (Invoke-WebRequest -uri http://www.icanhazip.com).Content
   # $publicIP can now be used to see your WAN IP.
   ```

#### To Install Exe's:

   ```powershell
   Foreach ($Computer In $Computers)
   {
   Copy-Item "C:\Yourlocalscript.Ps1" -Destination "\\$Computer\c$\Temp"
   Invoke-Command -Scriptblock { Powershell.Exe C:\Tempcscript.Ps1 } -Computername $Computer -Asjob
   }
   ```

#### To Download A File:

   ```powershell
   Invoke-Webrequest 'https://github.com/example.Zip' -Outfile $Env:Userprofile\Downloads\Example.Zip
   ```

#### To Download To Temp Directory

   ```powershell
   Function DownloadFileToTemp
   {
      param
      (
         [Parameter()]
         [String]$Url
      )

      $fileName = [system.io.path]::GetFileName($url)
      $tmpFilePath = [system.io.path]::Combine($env:TEMP, $fileName)

      $wc = new-object System.Net.WebClient
      $wc.DownloadFile($url, $tmpFilePath)
      $wc.Dispose()

      return $tmpFilePath
   }
   ```

#### To Get Computer/ Domain Names:

   ```powershell
   (Get-Wmiobject Win32_Computersystem).Name
   (Get-Wmiobject Win32_Computersystem).Domain
   ```

#### To Send Mail:

   ```powershell
   Function Sendmailmessage
   {
   Param(
   $From = ""
   $To = ""
   $Mailserver = ""
   [String]$Subject,
   [String]$Body
   )
   Send-Mailmessage -Smtpserver $Mailserver -From $From -To $To -Subject $Subject -Body $Body
   }
   # Be Sure That Your Mail Server Accepts Mails From The Host
   ```

#### To Disable and Enable a NetAdapter

   ```powershell
   Disable-NetAdapter -Name "Wireless Network Connection"
   Enable-NetAdapter -Name "Wireless Network Connection"
   ```

#### To Set a static IP

   ```powershell
   New-NetIPAddress -InterfaceAlias "Wireless" -IPv4Address 10.0.1.95 -PrefixLength "24" -DefaultGateway 10.0.1.1
   # or if existing
   Set-NetIPAddress -InterfaceAlias "Wireless" -IPv4Address 192.168.12.25 -PrefixLength "24"
   Set-NetIPInterface -InterfaceAlias "Wireless" -Dhcp Enabled
   ```

#### To Check for a port opening:

   ```powershell
   Test-NetConnection -ComputerName www.thomasmaurer.ch -Port 80
   Test-NetConnection -ComputerName www.thomasmaurer.ch -CommonTCPPort HTTP
   ```

#### To SMB Information:

   ```powershell
   Get-SmbClientConfiguration
   Get-SmbConnection
   Get-SmbOpenFile
   Get-SmbMutlichannelConnection
   ```

#### To Set Hyper-V Settings:

   ```powershell
   Get-NetAdapterVmq

   # Disable VMQ
   Set-NetAdapterVmq -Enabled $false

   # Enable VMQ
   Set-NetAdapterVmq -Enabled $true

   # For a specific VM
   Get-VMNetworkAdapter -VMName Server01

   # Get VM Network Adapter IP Addresses
   (Get-VMNetworkAdapter -VMName NanoConHost01).IPAddresses

   # Get VM Network Adapter Mac Addresses
   (Get-VMNetworkAdapter -VMName NanoConHost01).MacAddress
   ```

### PS Remoting

#### To Use local variables in Remote Commands

   ```powershell
   LocalVar = "test"
   Invoke-Command -ComputerName ms2 -ScriptBlock {Write-host "The localvar value $using:LocalVar"}

   # Map a drive in a remote session:
   $getcred = Get-Credential 'myuser'
   $servers = "myserver"
   $jsession = New-PSSession -ComputerName $servers -Credential $getcred
   Invoke-Command -ScriptBlock {
      # You will have to enable CredSSP if you don't use the $Using variable here.
      New-PSDrive -name share1 -psprovider FileSystem -root \\ServerComputerName\directory -Credential $using:getcred;
      dir share1:
   };
   ```

#### To Install Remote MSI

   ```powershell
   Import-Csv -Path "C:\temp\New_relicInst.csv" | ForEach-Object {
      $vmhost = $_.Name
      $dest = "\\" + $vmhost + "\C$\Windows\temp"
      copy-item " WindowsAzureVmAgent.2.7.1198.778.rd_art_stable.160617-1120.fre.msi" -Destination $dest -Force
      Invoke-Command -ComputerName $vmhost -ScriptBlock {
         $Exp = "cmd.exe /c C:\windows\temp\WindowsAzureVmAgent.2.7.1198.778.rd_art_stable.160617-1120.fre.msi /q /l* C:\windows\temp\azureagentinst.log"
         Invoke-Expression $Exp
      }
   }
   ```

#### To Spawn Remote Session In New Window

   ```powershell
   Start-Process -FilePath 'PowerShell.exe' -ArgumentList '-NoExit',"-command `"Enter-PSSession -ComputerName $ComputerName`""
   ```

#### To Get A Remote Reg Value

   ```powershell
   Invoke-Command -ComputerName myserver -Credential (Get-Credential) -ScriptBlock {
      [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey("LocalMachine",$env:COMPUTERNAME).OpenSubKey("System\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile").GetValue("EnableFirewall")
   }

   #1 means enabled.
   ```

---

1. 2018-04: Adding additional notes here&#8230;

2. Commands:

   - IPCONFIG => PowerShell: Get-NetIPConfiguration or Get-NetIPAddress

   ```powershell
   Get-NetIPConfiguration
   Get-NetIPAddress | Sort InterfaceIndex | FT InterfaceIndex, InterfaceAlias, AddressFamily, IPAddress, PrefixLength -Autosize
   Get-NetIPAddress | ? AddressFamily -eq IPv4 | FT –AutoSize
   Get-NetAdapter Wi-Fi | Get-NetIPAddress | FT -AutoSize
   ```

   - IPCONFIG /FLUSHDNS and IPCONFIG /REGISTERDNS => PowerShell:

   ```powershell
   Clear-DNSClientCache
   Register-DNSClient
   ```

   - IPCONFIG/RELEASE and IPCONFIG /RENEW => I would place in a function like:

   ```powershell
   $DHCPAdapters = Get-WmiObject –Class Win32_NetworkAdapterConfiguration | Where { $_.IpEnabled -eq $true -and $_.DhcpEnabled -eq $true } 
   foreach ($DHCP in $DHCPAdapters)
   {
   $DHCP.ReleaseDHCPLease() | Out-Null
   Start-Sleep -Seconds 1
   $DHCP.RenewDHCPLease() | Out-Null
   }
   ```

   - PING => PowerShell: Test-NetConnection

   ```powershell
   Test-NetConnection www.microsoft.com
   Test-NetConnection -ComputerName www.microsoft.com -InformationLevel Detailed
   Test-NetConnection -ComputerName www.microsoft.com | Select -ExpandProperty PingReplyDetails | FT Address, Status, RoundTripTime
   1..10 | % { Test-NetConnection -ComputerName www.microsoft.com -RemotePort 80 } | FT -AutoSize
   ```

   - Get some more details from the Test-NetConnection

   ```powershell
   Test-NetConnection -ComputerName www.thomasmaurer.ch -InformationLevel Detailed
   ```

   - Ping multiple IP using PowerShell

   ```powershell
   1..99 | % { Test-NetConnection -ComputerName x.x.x.$_ } | FT -AutoSize
   ```

   - NSLOOKUP => PowerShell: Resolve-DnsName

   ```powershell
   Resolve-DnsName www.microsoft.com
   Resolve-DnsName microsoft.com -type SOA
   Resolve-DnsName microsoft.com -Server 8.8.8.8 –Type A
   ```

   - Bulk NSLOOKUP

   ```powershell
   $servers = Get-Content "c:\_gwill\prod2.txt"

   Foreach ($s in $servers)
   {
      Write-Output "checking $s"
      $cmd = nslookup $s
      If ($Cmd.Length -eq 3)
      {
      Write-Output $s | Out-file "c:\_gwill\err.txt" -Encoding ascii -Append
      }
      Start-Sleep -Milliseconds 10
   }
   ```

   - ROUTE => PowerShell: Get-NetRoute (also New-NetRoute and Remove-NetRoute)

   ```powershell
   Get-NetRoute -Protocol Local -DestinationPrefix 192.168*
   Get-NetAdapter Wi-Fi | Get-NetRoute
   ```

   - TRACERT => PowerShell: Test-NetConnection –TraceRoute

   ```powershell
   Test-NetConnection www.microsoft.com –TraceRoute
   Test-NetConnection outlook.com -TraceRoute | Select -ExpandProperty TraceRoute | % { Resolve-DnsName $_ -type PTR -ErrorAction SilentlyContinue }
   ```

   - NETSTAT => Powershell Get-NetTCPConnection

   ```powershell
   Get-NetTCPConnection | Group State, RemotePort | Sort Count | FT Count, Name –Autosize
   Get-NetTCPConnection | ? State -eq Established | FT –Autosize
   Get-NetTCPConnection | ? State -eq Established | ? RemoteAddress -notlike 127* | % { $_; Resolve-DnsName $_.RemoteAddress -type PTR -ErrorAction SilentlyContinue }
   ```

   - [Source](https://blogs.technet.microsoft.com/josebda/2015/04/18/windows-powershell-equivalents-for-common-networking-commands-ipconfig-ping-nslookup/)
