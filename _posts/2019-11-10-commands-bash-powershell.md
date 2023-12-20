---
title: 'Commands: Bash vs. Powershell'
date: 2019-11-10T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/11/commands-bash-powershell/
tags:
  - Linux
  - Windows
tags:
  - Powershell
  - Bash
  - OneLiners-Powershell
  - OneLiners-Bash
---
<!--more-->

### Description:

When doing Systems administration between RHEL 7 and Windows Server 2016, here are the two ways to accomplish similar tasks (linux fist, then Windows):

### To Resolve:

### To see services set to start on startup that are not running:

   ```shell
   # lin
   systemctl list-units --state=failed
   # win
   Get-Wmiobject -Class Win32_Service | Where { $_.State -Ne 'Running' -And $_.Startmode -Eq 'Auto' } | Convertto-Html | Out-File Serviceerrors.Html
   ```

### To add rules to the firewall:

   ```shell
   # lin
   firewall-cmd --zone=public --add-port=22/tcp --permanent
   firewall-cmd --zone=public --add-service=ssh --permanent
   # - more specific rules
   firewall-cmd --permanent --add-rich-rule='rule='rule family="ipv4" source address="10.254.24.12/32" port port="3306" protocol="tcp" accept
   firewall-cmd --reload
   # win
   Import-Module NetSecurity
   Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
   New-NetFirewallRule -Name Allow_RDP -DisplayName "Allow RDP" -Description "RDP Rule" -Protocol TCP -LocalPort 3389 -Enabled True -Profile Any -Action Allow
   New-NetFirewallRule -Name Allow_Ping -DisplayName "Allow Ping" -Description "Packet Internet Groper ICMPv4" -Protocol ICMPv4 -IcmpType Any -Enabled True -Direction Outbound -Profile Any -Action Allow
   Set-NetFirewallRule -DisplayGroup "Windows Management Instrumentation (WMI)" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Network Discovery" -Profile Any
   Set-NetFirewallRule -DisplayGroup "File and Printer Sharing" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Windows Firewall Remote Management" -Profile Any
   Set-NetFirewallRule -DisplayGroup "Core Networking" -Profile Any
   # To Create Custom Firewall Rules
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


### To map a network drive:

   ```shell
   # lin
   sudo mount -t cifs -o username=homeUser //192.168.0.90/share /home/gerry/data
   sudo mount -t cifs -o username=windowsuser,password=WindowsUserPassword,uid=1000,gid=976 //192.168.0.30/winshare /mnt/shared
   # for NFS
   mkdir -p /mnt/nfs/home
   mount 192.168.0.32:/home /mnt/nfs/home
   # win
   New-PSDrive -Name G -Root \\Server01\Scripts -Credential domain\user -Persist -PSProvider FileSystem
   ```

### To create a new user and add to Admins on local machine:

   ```shell
   # lin
   adduser username
   passwd username
   usermod -aG wheel username
   # to test
   su - username
   # sudo command_to_run
   sudo ls -la /root
   # win
   $Password = Read-Host -AsSecureString
   New-LocalUser "User03" -Password $Password -FullName "Third User" -Description "Description of this account."
   Add-LocalGroupMember -Group "Administrators" -Member "Admin02"
   ```

### To get latest events from event log:

   ```shell
   # lin
   tail -f /var/log/syslog
   less /var/log/syslog
   # see others at https://www.eurovps.com/blog/important-linux-log-files-you-must-be-monitoring/
   # win
   Get-Eventlog -Logname System -Newest 5 | Select -Property Eventid, Timewritten, Message | Sort Timewritten -Descending | Convertto-Html | Out-File C:\scripts\Error.Htm
   Invoke-Command -Computername (Get-Content C:\Servers.Txt) -Scriptblock {Get-Eventlog -Logname System | Where {$_Leveldisplayname -Eq "Critical"}}
   ```

### To enable remote management:

   ```shell
   # lin
   sudo systemctl enable sshd
   # - ensure it allows connections the way you want
   sudo vim /etc/ssh/sshd_config
   # win
   enable/disable remote management
   netsh advfirewall firewall add rule name="Open Port 3389" dir=in action=allow protocol=TCP localport=3389
   reg add "hklm\system\currentControlSet\Control\Terminal Server" /v "fDenyTSConnections" /t REG_DWORD /d 0x0 /f
   sc config TermService start= auto
   net start Termservice
   ```

### To get free disk space :

   ```shell
   # lin
   df -h
   # win
   Get-Ciminstance Win32_Logicaldisk -Filter "Deviceid='C:'" | Select @{N='Freegb' ; E={$_.Freespace / 1gb -As [Int]}}
   ```

### To rename files in bulk :

   ```shell
   # lin
   rename 's/.txt/.ps1/' *
   # win
   Get-Childitem "C:\Scripts" | Rename-Item -Newname { $_.Name -Replace ".txt",".ps1" }
   ```

### To Set Everyone Full Permissions For A File:

   ```shell
   # lin
   chmod 777 /home/gerry/myfile.txt
   # win
   Function Set-Permissions($File)
   {
   $Acl = Get-Acl $File
   $Accessrule= New-Object System.Security.Accesscontrol.Filesystemaccessrule("Everyone", "Fullcontrol", "Allow")
   $Acl.Setaccessrule($Accessrule)
   $Acl | Set-Acl $File
   }
   Set-Permissions c:\scripts\myfile.txt
   ```

### To Give Admins Full Control Of A Folder:

   ```shell
   # lin
   chown -R root:root /root
   chmod -R 744 /root
   # win
   Function Takeown-Folder($Path)
   {
   Takeown.Exe /A /F $Path
   $Acl = Get-Acl $Path
   # Get Administraor Group
   $Admins = New-Object System.Security.Principal.Securityidentifier("S-1-5-32-544")
   $Admins = $Admins.Translate([System.Security.Principal.Ntaccount])

   # Add Nt Authority\System
   $Rule = New-Object System.Security.Accesscontrol.Filesystemaccessrule($Admins, "Fullcontrol", "None", "None", "Allow")
   $Acl.Addaccessrule($Rule)

   Set-Acl -Path $Path -Aclobject $Acl
   }
   Takeown-Folder c:\scripts
   ```

### To add an environmental variable permanently (survives reboot) :

   ```shell
   # lin
   vi /etc/profile
   # add to end
   PATH="$PATH:/opt/puppetlabs/bin";export PATH
   # see path - it's not there?
   echo $PATH
   # oh ya, now it is
   source /etc/profile
   echo $PATH
   # or rhel
   echo 'pathmunge /opt/puppetlabs/puppet/bin' > /etc/profile.d/puppet.sh
   chmod +x /etc/profile.d/puppet.sh
   . /etc/profile
   # win
   $X = "C:\scripts\python27"
   $Env:Path+= ";" + $X + ";"
   [Environment]::Setenvironmentvariable("Path",$Env:Path, [System.Environmentvariabletarget]::User)
   ```

### To Set A Daily Task (Daily/2AM) :

   ```shell
   # lin
   crontab -e
   0 2 * * * /root/scripts/clean.sh
   # or
   cp /root/scripts/clean.sh /etc/cron.daily
   chmod 755 clean.sh
   # see if job was ran
   /var/log/cron*
   # Sometimes you can find specific info from job in:
   /var/spool/mail/root
   # win
   $taskName = "ExampleDailyChocolateyUpgrade"
   $taskAction = New-ScheduledTaskAction –Execute C:\programdata\chocolatey\choco.exe -Argument "upgrade all -y"
   $taskTrigger = New-ScheduledTaskTrigger -At 2am -Daily
   $taskUser = "System"
   Register-ScheduledTask –TaskName $taskName -Action $taskAction –Trigger $taskTrigger -User $taskUser
   ```

### To set computer to never sleep :

   ```shell
   # lin
   sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
   # - to re-enable
   sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
   # win
   cmd /c "powercfg -change -monitor-timeout-ac 0"
   cmd /c "powercfg -change -monitor-timeout-dc 0"
   cmd /c "powercfg -change -standby-timeout-ac 0"
   cmd /c "powercfg -change -standby-timeout-dc 0"
   cmd /c "powercfg -change -disk-timeout-ac 0"
   cmd /c "powercfg -change -disk-timeout-dc 0"
   cmd /c "powercfg -change -hibernate-timeout-ac 0"
   cmd /c "powercfg -change -hibernate-timeout-dc 0"
   ```

### To rename a server:

   ```shell
   # lin
   sudo hostnamectl set-hostname MyServer01
   # win
   Rename-Computer "newName"
   Restart-Computer -Force
   ```

### To get logged on user :

   ```shell
   # lin
   w
   # or
   who -a
   # win
   Get-WmiObject Win32_LogonSession -ComputerName localhost -Filter 'LogonType=2 OR LogonType=10' |
   Foreach-Object { $_.GetRelated('Win32_UserAccount') } |
   Select-Object Caption -Unique
   ```

### To get the last reboot time:

   ```shell
   # lin
   who -b
   last reboot | less
   last reboot | head -1
   # - for shutdown
   last -x|grep shutdown | head -1
   # win
   $RebootTime = [System.DateTime]::ParseExact((Get-WmiObject Win32_OperatingSystem -ComputerName localhost| foreach{$_.LastBootUpTime}).split('.')[0],'yyyyMMddHHmmss',$null)
   $RebootTime
   ```

### To find largest files on a system:

   ```shell
   # lin
   find / -type f -printf '%s %p\n'| sort -nr | head -10
   # - folders
   du -sh /* 2>/dev/null | sort -h
   du -sh /* | sort -rh | head -5
   find / -type d -exec du -Sh {} + | sort -rh | head -n 5
   # win
   gci -r|
      sort -descending -property length | 
      select -first 10 fullname, name, @{Name="Gigabytes";Expression={[Math]::round($_.length / 1GB, 2)}} |
      Out-GridView
   ```

### To delete files older than 30 days:

   ```shell
   # lin
   # - to see them
   find /home/user/*.log -mtime +30 -print
   # - to delete them
   find /home/user/*.log -mtime +30 | xargs rm -f
   find /home/user/*.log -mtime +30 -delete
   # win
   Get-ChildItem –Path "C:\path\to\folder" -Recurse | Where-Object {($_.LastWriteTime -lt (Get-Date).AddDays(-30))} | Remove-Item
   ```

