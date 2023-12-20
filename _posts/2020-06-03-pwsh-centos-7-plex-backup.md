---
title: Pwsh Centos 7 Plex Backup 
date: 2020-06-03T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/pwsh-centos-7-plex-backup
tags:
  - LocalSoftware
  - Linux
tags:
  - LinuxServer
  - Powershell
---
<!--more-->

### Description:

I had a bash script doing backups on Centos, but wanted to see if I could convert those to the core version of Powershell instead. Sure enough, worked on the first try:

### To Resolve:

1. Create a file called `plex.ps1` and paste / run :

   ```powershell
   <#

   # Register the Microsoft RedHat repository
   #curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
   # Install PowerShell
   #sudo yum install -y powershell
   # create /home/myuser/scripts/plex.ps1

   #>

   #!/usr/bin/env pwsh

   $Date = Get-Date -Format "yyyy-MM-dd"
   $log = "/home/myuser/scripts/logs/plexbackup_" + $date + ".log"

   If (!(Test-Path $log))
   {
         New-Item -Itemtype File -Path $log -Force | Out-Null
   }

   $stop = "systemctl stop plexmediaserver.service"
   $start = "systemctl start plexmediaserver.service"

   $options = "-zavh --exclude={'Cache/','Crash Reports/','Logs/','Plug-in Support/Cache/'}"
   $source = "/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/"
   $destination = "/mnt/plex/backup"
   $rsync = "rsync $options $source $destination" 

   Write-Output "Starting Backup of Plex Database."  | Out-File $log -Append -Encoding "ascii"
   Write-Output "============================================================" | Out-File $log -Append -Encoding "ascii"

   # Stop Plex
   Write-Output "Stopping Plex Media Server" | Out-File $log -Append -Encoding "ascii"
   Write-Output "------------------------------------------------------------" | Out-File $log -Append -Encoding "ascii"
   bash -c $stop | Out-File $log -Append -Encoding "ascii"

   # Backup database
   Write-Output "Starting Backup." | Out-File $log -Append -Encoding "ascii"
   Write-Output "------------------------------------------------------------" | Out-File $log -Append -Encoding "ascii"
   bash -c $rsync | Out-File $log -Append -Encoding "ascii"

   # Restart Plex
   Write-Output "Starting Plex Media Server." | Out-File $log -Append -Encoding "ascii"
   Write-Output "------------------------------------------------------------" | Out-File $log -Append -Encoding "ascii"
   bash -c $start | Out-File $log -Append -Encoding "ascii"

   # Done
   Write-Output "Backup Complete" | Out-File $log -Append -Encoding "ascii"
   Write-Output "============================================================" | Out-File $log -Append -Encoding "ascii"
   ```
