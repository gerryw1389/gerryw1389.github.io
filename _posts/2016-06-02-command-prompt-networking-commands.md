---
title: 'Command Prompt: Networking Commands'
date: 2016-06-02T20:42:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/command-prompt-networking-commands/
tags:
  - Windows
tags:
  - OneLiners-CMD
  - Scripting-CMD
---
<!--more-->

### Description:

The following commands can be ran in the Windows Command Prompt.

### To Detect IP Settings:

   ```powershell
   :: Shows basic IP information
   ipconfig

   :: Used most often, shows extended IP information
   ipconfig /all

   :: Releases an IP address if on DHCP
   ipconfig /release

   :: Renews the IP address if on DHCP
   ipconfig /renew
   ```

### To Disable/Enable A Nic Called "Local Area Connection":

   ```powershell
   netsh interface set interface name="Local Area Connection" admin=disabled

   :: To Re-Enable
   netsh interface set interface name=""Local Area Connection"" admin=enabled
   ```

### To Test Connectivity Between 2 Nodes:

   ```powershell
   :: Sends 4 data packets between two nodes.
   ping (IP address or hostname)
   ```

### To See All Open Files That Are Shared Out:

   ```powershell
   openfile /query
   ```

### To Close All Open Files:

   ```powershell
   for /f "skip=4 tokens=1" %a in ('net files') do net files %a /close
   ```

### To Message A User On The Network:

   ```powershell
   msg "(AdministratorAccountName)" /server:(ComputerName) (message, ex: what's up?)
   :: You can also use an IP without the "\\" in front of it. A message that says whats up?" 
   :: Example: 
   msg "administrator" /server:192.168.1.10 whats up?
   ```

### To fix error `Error 5 getting Session Names` when opening a MMC console:

   ```powershell
   reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v "AllowRemoteRPC" /t REG_DWORD /d 1 /f
   ```

### To Resolve A MAC Address From An IP On Your Subnet:

   ```powershell
   arp -a
   arp -g
   ```

### To map a network drive:

   ```powershell
   net use g: \\ServerComputerName\share P@$$w0rd123 /user:domain.com\user.name /persistent:yes
   ```

   - In this example I mapped a shared drive as the G:\ as a user named "domain.com\user.name" and made it reconnect at logon (persistent)  

### To Delete Mapped Drives:

   ```powershell
   net use /del (drive letter:)
   :: Deletes all mapped drives
   net use /del *
   ```

### To Enable RDP:

   ```powershell
   netsh advfirewall firewall add rule name="Open Port 3389" dir=in action=allow protocol=TCP localport=3389
   reg add "hklm\system\currentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0x0 /f
   sc config TermService start= auto
   net start Termservice
   ```

### To Remove RDP Access:

   ```powershell
   net stop termservice
   sc config termservice start=disabled
   reg add "hklm\system\currentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0x1 /f
   netsh advfirewall firewall delete rule name="Open Port 3389"
   ```

### To Enable Ping Through Windows Firewall:

   ```powershell
   netsh firewall set icmpsetting 8 enable
   ```

### To Install the Windows Firewall:

   ```powershell
   :: Usually during a virus cleanup
   Rundll32 setupapi,InstallHinfSection Ndi-Steelhead 132 %windir%\inf\netrass.inf

   :: Restart the computer

   Netsh firewall reset
   ```

### To Disable the Windows Firewall:

   ```powershell
   netsh advfirewall set currentprofile state off
   ```

### To allow WinRM and WMI through the Windows Firewall:

   ```powershell
   netsh advfirewall set currentprofile settings remotemanagement enable
   ```

### To View Local Account Security Settings:

   ```powershell
   :: Show local accounts
   net accounts

   :: Show domain settings
   net accounts /domain
   ```

### To Change MTU Size:

   ```powershell
   netsh interface ipv4 set subinterface "Local Area Connection" mtu=1458 store=persistent
   netsh interface ipv4 show subinterface
   ```

### To Reset Winsock:

   ```powershell
   netsh int ip reset C:\resetlog.txt
   netsh winsock reset
   ```