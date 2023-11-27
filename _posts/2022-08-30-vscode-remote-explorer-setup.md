---
title: VSCode Remote Explorer Setup
date: 2022-08-30T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/vscode-remote-explorer-setup
tags:
  - Azure
tags:
  - VersionControl
  - Scripting-Bash
  - LinuxServer
  - NoteTaking
  - PKI
  - VsCode
---
<!--more-->

### Description:

Continuing from my [previous post](https://automationadmin.com/2022/03/setup-work-laptop) about setting up a laptop, this post is how I setup SSH connections from a remote server to our organizations Azure Devops instance using [VSCode's Remote Explorer](https://code.visualstudio.com/docs/remote/ssh) extension.

### To Resolve:

1. So by the end of that post, you should have:
   - `choco` installed user programs
   - OpenSSH Client installed
   - VScode configured with `ms-vscode-remote`

1. Now, generate a SSH key pair and copy the public portion to your clipboard

   ```shell
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ssh-add ~/.ssh/id_rsa
   # copy ~/.ssh/id_rsa.pub to clipboard
   ```

   - Add the ssh key to your AzDo account.

1. After getting access to your server add this to your `.ssh/config`:

   ```escape
   Host computer.domain.com
      HostName computer.domain.com
      User myuser
      ForwardAgent yes
   ```

1. Before connecting remote, make sure SSH keys added locally to your SSH Auth agent:

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

   - I had done a few things locally before connecting that may or may not be required:

   - Set service to automatic:

   ```powershell
   Set-Service ssh-agent -StartupType Automatic
   Start-Service ssh-agent
   ```

   - Also, I had created a fake service so I don't have to install ssh server on windows (not sure if this is needed): `sc.exe create sshd binPath=C:\Windows\System32\OpenSSH\ssh.exe`

   - Also I had connected one time manually through powershell before setting everything up through VScode by using the `-A` switch which forwards SSH Auth: `ssh me@computer.domain.com -A`

1. Once I have my SSH keys added locally to my SSH Auth agent and have SSH'd into the remote server using VSCode's Remote Explorer extension, I have a few tasks I need to setup:

   - Create a directory `/home/myuser/repo/`
   - Create a `.gitconfig` with a `user.name` and `user.email` set so I can start pulling repos without providing that information every time.
   - After changing to that directory, I then start pulling down repos from my Azure Devops instance:

   ```shell
   cd /home/myuser/repo/
   git clone git@ssh.dev.azure.com:v3/MyOrg/MyProject/MyRepo1
   # creates folder MyRepo1
   git clone git@ssh.dev.azure.com:v3/MyOrg/MyProject/MyRepo2
   # creates folder MyRepo2
   ```

   - Then I create a script called `/home/myuser/pull.sh` like this:

   ```shell
   cd /home/myuser/repo/myrepo1
   git checkout main
   git remote prune origin
   git pull origin main

   cd /home/myuser/repo/myrepo2
   git checkout master
   git remote prune origin
   git pull origin master

   # ommiting many others

   cd /home/myuser/

   ```

   - I know I can create a list of repos where my trunk branch is `main` and another where my trunk branch is `master` and then do a `for loop` but I don't mind just copy/paste/tweaking the scripts sometimes.

1. Next, after I have all my repos synced to the linux box, I wanted a way to SSH directly into a specific folder on the remote server instead of my `/home/myuser/repo/` folder which has like 20+ repos and will generate a long tree in my VScode's Explorer view. Here is how I added "shortcuts" in my Remote Explorer:
   - First I ssh'd to my remote server to the `/home/myuser/` folder the same as before.
   - Next, in the remote SSH Vscode window, I went to `File => Open Folder` and pointed to the path of one of my repos `/home/myuser/repo/myrepo1`
   - Next, it prompted me for the password again and it opened up a window scoped to just that path.
   - Now, you can exit all vscode windows from your local machine and it will just "show up" in the Remote Explorer view under your target server.
   - Cool, but like I said, I have 20+ repos, do I have to do this for all of them? I think so :/ , at the time of this writing I don't know of [any other way](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings) to bulk add a bunch of remote folders.

1. But I did find a way to make it somewhat faster, you just keep 'looping' from one folder to the next once you connect to the Remote SSH vscode window:
   - SSH into your remote server and from that SSH session:
   - Click on `File => Open Folder` and then put in a full path like `/home/myuser/repo/myrepo1`
   - Enter your credentials
   - Then from THAT window, click on `File => Open Folder` and then put in a full path like `/home/myuser/repo/myrepo2`
   - And keep doing this over and over ...
   - When you are done, your host computer's Remote Explorer should have a "shortcut" for all folders you looped through instead of repeating the previous step 20+ times.

