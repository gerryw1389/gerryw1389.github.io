---
title: Setup Work Laptop
date: 2022-03-15T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/03/setup-work-laptop
tags:
  - SysAdmin
tags:
  - PersonalSoftware
  - Tweaks
---
<!--more-->

### Description:

So at each place I work, I like to setup a folder structure on my Windows Laptop that keeps my files locally under the `C:\scripts` folder directory while also backing them up to my company's Onedrive and my home PC for offline backup. Here is how I set it up. Obviously I would remove the offline backup part if company policies do not allow any data to leave the company laptop. See my [dot files post](https://automationadmin.com/2022/01/dot-files) for some references to these settings.

### To Resolve:

1. Create folder `c:\scripts` and under that create `c:\scripts\sync.bat` with the following contents:

   ```powershell
   @ECHO OFF
   PowerShell.exe -NoProfile ^
   -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""'}"
   Pause
   ```

   - and then create `c:\scripts\sync.ps1` with the following contents:

   ```powershell
   robocopy "C:\scripts\company" "C:\Users\myuser\OneDrive - My Company\company" /mir /xd '.git'
   robocopy "C:\Users\myuser\OneDrive - My Company\company" "\\192.168.50.50\backup" /mir /np /ndl /log:"c:\scripts\robocopy.log"
   ```

1. Now create a folder called `C:\scripts\company` replacing company with a short version of the company name. Under that folder we will store all documents that will be backed up to OneDrive:

   - `apps` - This just holds config information for any apps I install. Similar to `/etc`
   - `docs-personal` - Documents I don't want others to see but still back up to Onedrive. Stuff like paycheck info, any communications between me and one other person meant to be personal, or just sensative info in general.
   - `docs-work` - All work related documents, not afraid to share. This is the folder I will share with a Team sharepoint when I leave the company.
   - `repo` - Any/all code repos. The idea is to have different workspaces point to these folders based on what I'm working on.
      - Workspaces can be found under `C:\scripts\company\apps\vscode\*.code-workspace`

1. Now that folders are setup. I would then install all the software needed (assuming you have admin rights to your laptop - might be able to do this without it though):

   ```powershell
   Set-ExecutionPolicy RemoteSigned
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

   $packages = ( 
      "7zip",
      "azure-cli",
      "everything",
      "git",
      "greenshot",
      "k9s",
      "keepass",
      "kubernetes-cli",
      "kubernetes-helm",
      "microsoftazurestorageexplorer",
      "notepadplusplus",
      "terraform",
      "vscode"
   )

   choco feature disable -n=showDownloadProgress

   foreach ($package in $packages)
   {
      choco install $package -y --limitoutput
   }

   # Install the OpenSSH Client
   Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
   ```

1. After installing programs, I would then configure them like [I usually do](https://automationadmin.com/2018/08/setup-a-new-computer/). Here is a list of extensions in VSCode I would then install as well as my default [user settings](https://github.com/gerryw1389/misc/blob/main/vscode/settings-sync.json):

   ```powershell
   $extensions = @(
      "hashicorp.terraform",
      "liwei.relax-eyes-theme",
      "ms-vscode-remote.remote-ssh",
      "ms-vscode.powershell",
      "redhat.vscode-yaml",
      "vscode-icons-team.vscode-icons",
      "yzane.markdown-pdf"
   )

   foreach ($ext in $extensions)
   {
      Write-Output "Installing extension: $ext ..."
      code --install-extension $ext
      Write-Output "Installing extension: $ext ...Completed"
   }
   ```

1. That's about it. I would then normally pin VSCode to my taskbar and edit it's target location to point to a workspace at `C:\scripts\company\apps\vscode\default.code-workspace` which points to a folder at `C:\scripts\company\repo\notes` for example where I store all my notes. I would then create other workspaces depending on the languages I work on such as:

   - `C:\scripts\company\apps\vscode\powershell.code-workspace` which points to `C:\scripts\company\repo\powershell`
   - `C:\scripts\company\apps\vscode\python.code-workspace` which points to `C:\scripts\company\repo\python`
   - `C:\scripts\company\apps\vscode\terraform.code-workspace` which points to `C:\scripts\company\repo\terraform`
   - and so on...

   - When I say points to, I mean these workspace files are super basic and just look like this:

   ```json
   {
      "folders": [
         {
               "path": "C:\\scripts\\company\\repo\\notes"
         }
      ],
      "settings": {}
   }
   ```

   - I still keep all my config at the User Settings level for Vscode, but use Workspaces to logically seperate what I'm working on because I don't like to see long trees of folders so I use workspaces alot.

   - Lastly, I usually have a function in my [PSProfile](https://github.com/gerryw1389/misc/blob/main/dot-files/Microsoft.Powershell_profile.ps1) that will start workspaces on demand since somedays I just stay in my default workspace all day and don't need to launch all my workspaces.

   ```powershell
   Function Start-Workspaces
   {
      [Cmdletbinding()]
      Param
      (
         [Parameter(Mandatory = $false, ValueFromPipeline = $false, ValueFromPipelineByPropertyName = $false, Position = 0)]
         [Switch]$All
      )  

      If ( $all )
      {
         code C:\scripts\company\repo\powershell
         code C:\scripts\company\repo\python
         code C:\scripts\company\repo\terraform
      }
      Else
      {
         code C:\scripts\company\repo\powershell
      }
   }
   Set-Alias -Name "sw" -Value "Start-Workspaces"
   ```

1. Since I use SSH Client on my Windows Laptop to connect to a remote linux server where I do most of my git interactions, I usually run this script to ensure my service is running and my keyfiles are added to my ssh auth agent:

   ```powershell
   $Service = Get-Service -Name "SSH-Agent"

   If ( $Service.Status -eq "Stopped" )
   {
      Write-Output "SSH Agent service was stopped, starting..."
      Start-Service $Service
      Write-Output "SSH Agent service was stopped, starting...Completed"
   }

   Write-Output "Running ssh-add..."
   ssh-add -l
   Write-Output "Running ssh-add...Completed"
   ```