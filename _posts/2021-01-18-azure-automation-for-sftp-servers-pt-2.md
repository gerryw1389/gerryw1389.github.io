---
title: Using Logic Apps and Azure Automation for SFTP Pt. 2
date: 2021-01-18T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/azure-automation-for-sftp-servers-pt-2/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-Automation
  - Scripting-Powershell
---
<!--more-->

### Description:

This will be a continuation of my [original post](https://automationadmin.com/2020/10/using-azure-automation-logic-apps-for-sftp) where I use Logic Apps to schedule Azure Automation runbooks to transfer files from our Azure storage accounts to third parties via SFTP. So one of our main services that we offer is the ability to transfer files to third party vendors using Azure Storage and Azure Automation. This works because:

- You can assign a static IP for each Hybrid Worker in a pool and then provide those IPs to vendors.
- You can write runbooks locally in vscode and push to Github which will sync to Azure Automation for you.
- You can write Logic Apps that run the runbooks on whatever schedule you want.

### To Resolve:

1. I use the WinSCP module to write Powershell runbooks that transfer files.

2. First, at the top of my runbooks, I ensure that I can mount the drive which is a file share from my Azure Storage account:

   ```powershell
   Try 
   { 
      Get-PSDrive -Name "Q" -ErrorAction "Stop" | Out-Null 
   }
   Catch
   { 
      Try
      {
            New-PSDrive -Name "Q" -PSProvider "FileSystem" -Root "\\my-organization.file.core.windows.net\data" -ErrorAction "Stop" | Out-Null
      }
      Catch
      {
            Write-Output "Unable to mount T Drive"
            Write-Error "Terminating runbook"
      }
   }
   ```

3. Next, use the WinSCP to transfer files to and from remote SFTP servers. Note that the [WinSCP scripting module](https://winscp.net/eng/docs/library) in this example is placed in `Q:\rsc\WinSCPnet.dll`.

   ```powershell
   Write-Output "Checking for WinSCP..."
   $dll = "Q:\rsc\WinSCPnet.dll"
   If ( -not ( Test-Path $dll ))
   {
      Write-Output "Unable to find WinSCP dll, exiting"
   }
   Write-Output "Checking for WinSCP...Completed"

   $tempPath = 'c:\scripts\'

   # Load WinSCP .NET assembly
   Add-Type -Path $dll

   # ssh hostkey of some.server.company.com
   # can see this by connecting in the GUI and going to Session => Get URL/Code
   # https://winscp.net/eng/docs/library_example_known_hosts
         
   $sftpUser = 'someUser'
   $sftpPass = 'somePass'
   $strSSH = "ssh-ed25519 256 bb7g56Q8//5+aFGvq/wyBJj328emoTslfkoDvQuacGJ1gP/IM="

   $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
      Protocol              = [WinSCP.Protocol]::Sftp
      HostName              = "some.server.company.com"
      UserName              = $sftpUser
      Password              = $sftpPass
      SshHostKeyFingerprint = $strSSH
   }

   $session = New-Object WinSCP.Session
   Try
   {
      $session.Open($sessionOptions)
      
      # Getting files - do remote path then local path
      # $session.GetFiles("/some/path/data*.txt", $tempPath).Check()
      
      # Putting files - do local path and then remote path
      # $session.PutFiles("C:\scripts\test02.txt", "/some/path/*").Check()
      
      # Removing files
      #  $filenames = $session.EnumerateRemoteFiles("/some/path/", "test02*.txt", [WinSCP.EnumerationOptions]::None)
      #  if ($filenames.Count -gt 0)
      #   {
      #     foreach ($fileInfo in $filenames)
      #     {
      #       Write-output "Removing: $($fileInfo.FullName)"
      #       $removalResult = $session.RemoveFiles($($fileInfo.FullName))
      #       if ($removalResult.IsSuccess)
      #       {
      #           Write-Output "Removing of file $($fileInfo.FullName) succeeded"
      #       }
      #       else
      #       {
      #           Write-Output "Removing of file $($fileInfo.FullName) failed"
      #       }
      #     }
      #   }
      #   Else
      #   {
      #     Write-Output "No files found in remote directory"
      #   }

      # Removing files older than 90 days old
      # $fileLastWrite = $($fileInfo.LastWriteTime)
      # #Write-output "File last write time: $($fileInfo.LastWriteTime)"
      # $time = New-TimeSpan -Start $fileLastWrite -End (Get-Date)
      # If ( $($time.days) -gt 90 )
      # {
      # Write-output "Filename: $($fileInfo.FullName)"
      # Write-output "File last write time GREATER than 90 days: true"
      # Write-output "Removing: $($fileInfo.FullName)"
      # <#
      #       $removalResult = $session.RemoveFiles($($fileInfo.FullName))
      #       if ($removalResult.IsSuccess)
      #       {
      #         Write-Output "Removing of file succeeded: $($fileInfo.FullName)"
      #       }
      #       else
      #       {
      #         Write-Output "Removing of file failed: $($fileInfo.FullName)"
      #       }
      #       #>
      # }
      # Else
      # {
      # #Write-output "File last write time GREATER than 90 days: false"
      # }
      
      # Rename remote items - provide current name and new name then do MoveFile. Put in a foreach loop if needed.
      # $fullName = [WinSCP.RemotePath]::Combine("/some/path/", "test02.txt")
      # $fullNewName = [WinSCP.RemotePath]::Combine("/some/path/", "test02-modified.txt")
      # $session.MoveFile($fullName, $fullNewName)
   }
   Catch
   {
      Write-Output "Unable to SFTP file to the destination"
      Write-Error "Terminating runbook"
   }
   Finally
   {
      $session.Dispose()
   }
   ```

4. I spend a lot of time moving files to and from temp folders as well:

   ```powershell
   Write-Output "Creating temp path..."
   $guid = New-Guid
   $tempFolder = "c:\scripts\Temp\" + $($guid.guid)
   If ( Test-Path $tempFolder )
   {
      New-Item -Itemtype "Directory" -Path $tempFolder -Force | Out-Null
   }
   Else
   {
      New-Item -Itemtype "Directory" -Path $tempFolder | Out-Null 
   }
   Write-Output "Creating temp path...Completed: $tempfolder"

   Write-Output "Copying files from Q drive to local C drive for file transfer"
   $today = Get-Date -Format "yyyy-MM-dd"
   $destPath = "Q:\my-files\" + $today
   If ( Test-Path $destPath)
   {
      $files = Get-ChildItem $destPath
   }
   Else
   {
      Write-Output "Unable to find files from last job"
      Write-Error "Terminating Runbook"
   }

   foreach ( $file in $files)
   {
      Try
      {
         Copy-Item $($file.fullname) -Destination ( $tempFolder + '\' + $($file.name) ) -ErrorAction "Stop"
      }
      Catch
      {
         Write-Output "Unable to move file from T drive to local C drive for transfer"
         Write-Error "Terminating Runbook"
      }
   }
   Write-Output "Copying files from T drive to local C drive for file transfer...Completed"
   ```

5. Using this method, you can transfer files to and from Azure Storage to third party SFTP servers.
