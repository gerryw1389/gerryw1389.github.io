---
title: Deploy Jenkins Windows Node
date: 2020-03-23T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/03/deploy-jenkins-windows-node
categories:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

In this post (a continuation of [this](https://automationadmin.com/2020/03/deploy-jenkins-windows-master) post) I will attach 2 WS2019 instances to a WS2019 Jenkins master as a node. I ran into an issue doing it the normal way so I ended up using SSH instead. The main note to know about nodes is that if you have a label in Jenkins for a group of servers, it is a good idea to configure all of the servers the same so that jobs can run on any server at any time. Because of this, I go into details additional to a normal Jenkins setup.

Note, the normal way that you join Windows Servers instances to a Windows Server master is:
   - Do step 6 below, but choose the default connection which is `Let Jenkins Control this Agent As A Windows Service`
   - On the node, go to the masters Web UI and go to Manage Jenkins => Manage Nodes => Click your node name => download the `.jnlp` file. 
   - Open PS as administrator and `cd` to your downloads and run `./jenkins-slave.jnlp` which allows you to click `File - Install as a Windows Service`
   - The agent installs fine, but then fails to start because of memory issues
   - I spent hours googling [the issue](https://duckduckgo.com/?t=ffab&q=jenkins+windows+agent+There+is+insufficient+memory+for+the+Java+Runtime+Environment+to+continue.&ia=web) with no luck until I found a Stack Overflow post where someone suggested using SSH instead. So I did that instead...


This is part of a 3 part series:

   - [1 - Deploy Jenkins Master](https://automationadmin.com/2020/03/deploy-jenkins-windows-master)
   - 2 - Deploy Jenkins Nodes
   - [3 - Connect To Github](https://automationadmin.com/2020/04/connect-windows-to-github)

### To Resolve:

1. First, in azure deploy two WS2019 instances named `schedtasks2-win2019.domain.com` and `schedtasks3-win2019.domain.com`.

   - Attach a 80 GB second disk at deploy time
   - Do NOT modify your network security group to allow any traffic to the nodes, people only need access to the Jenkins master on 443/tcp.

2. Now follow regular windows server deployment tasks:
 
   - Join the computer to your domain
   - Create a security group in AD that will be local admin
   - Create a service account user and add it to that group in AD - `domain.com\svc_windowsJenkins`
   - As the local admin on the box, run `lusrmgr.msc` and add that security group as local admins. Log out and back in as the service account.
   - Ensure that you can open Powershell as administrator as the service account
   - Rest of the post will assume you are that user

3. Setup SSH on `schedtasks2-win2019.domain.com`, `schedtasks3-win2019.domain.com`, and `schedtasks-win2019.domain.com`:

   - On all 3 servers:

   - Run `gpedit.msc` and find `Computer Configuration\Administrative Templates\System\Specify settings for optional component installation and component repair` and `enable` it with the second option of `Bypass WSUS`. Reboot the machine. This is required for the next steps.

   ```powershell
   # install openSSH server
   Add-WindowsCapability -Online -Name $(Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Server*' | Select -ExpandProperty Name)
   # start sshd
   Start-Service sshd
   # enable sshd as a service
   Set-Service -Name sshd -StartupType 'Automatic'
   ```

   - On `schedtasks2-win2019.domain.com` and `schedtasks3-win2019.domain.com` - connect to master `schedtasks-win2019.domain.com` and store the SSH fingerprint in the known_hosts file. Open ps as admin and:

   ```powershell
   ssh svc_windowsJenkins@domain.com@schedtasks-win2019.domain.com
   # enter password
   exit
   cd c:\users\svc_windowsJenkins\.ssh\
   cat known_hosts
   # copy to clipboard
   schedtasks-win2019.domain.com,10.20.20.4 ecdsa-sha2-nistp256 AAAAE2VjZHyui9NoYTItbmlzdHAyNTYAAAAIbmlzd8941NTYAAABBBAfKe3rbQTdwuL3xICPdRVx3rpHEFxDZdLW/LgdDBk2yOmbYICRLkos7iXiNkOR9OflZYcCKm0TjcPyPwesbZfY=
   cd C:\windows\system32\config\systemprofile\.ssh\
   ii known_hosts
   #paste it in
   # just to be safe, you could ssh again, but you should be good
   ```

   - From `schedtasks-win2019.domain.com`, ssh to `schedtasks2-win2019.domain.com` and `schedtasks3-win2019.domain.com` and ensure their ssh fingerprints are in its `known_hosts` file.


4. Add local firewall rules to both of the new nodes:

   - firewall.cpl => Advanced Firewall => Inbound Rules => Add
   - Name: JenkinsMasterNode
   - Ports: 22, 8089
   - Scope: 10.20.20.4

   - See step 6 for why we open 8089

5. Install Java and setup directories:

   - Copy over and install `OpenJDK8U-jdk_x64_windows_hotspot_8u242b08.msi` (if you don't have it, google [https://adoptopenjdk.net/](https://adoptopenjdk.net/) - install with all options
   - create `q:\jenkins`
   - create `q:\powershell` and create a [32 bit key file](https://automationadmin.com/2016/05/using-passwords-with-powershell/) called `aes.key`.
   	- Disable Inheritence and convert to explicit permissions
     - Remove everyone except `svc_windowsJenkins` and `SYSTEM` (NTAuthority\System); Give them full control.
   - Open PS As admin and type: `set-timezone "Central Standard Time"` and `winrm set winrm/config/winrs '@{MaxMemoryPerShellMB="4096"}'`
   - Do Windows Updates and restart

6. Add each node to the jenkins pool:

   - Login to [https://schedtasks-win2019.domain.com](https://schedtasks-win2019.domain.com) 
   - Manage Jenkins => Configure Global Security => TCP port for inbound agents => 8089
   - Manage Jenkins => Configure Nodes => Configure:
   - Name = `schedtasks3-win2019`
   - Number Executors (recommended one per processor) = 2 
   - Remote Directory = `q:/jenkins/`
   - Label = `windows`
   - Usage = Use this node as much as possible
   - Launch Method = Launch agents via SSH
     - Host: `schedtasks3-win2019.domain.com`         
     - Add credentials => `uta\svc_windowsJenkins` and its password
     - Host verification strategy => Manually trusted key Verification Strategy
       - Advanced: `Prefix Start Agent Command = ` set to `G: && `
   - Availability = Keep online as much as possible
   - Save
   - You should see the node 'come online' on the Status screen


7.  Next, in Azure create a public IP address and assign to each NIC so that we can give them vendors for SFTP jobs:  

   - public ip addresses => New
   - name = jenkins-node1
   - type: static
   - dns = blah-node1.southcentralus.cloudapp.azure.com
   - Do the same thing again, but node2 instead of 1
   - After created, Associate => NIC => schedtasks3-win201953
   - verify on VM, open PS: `$ipinfo = Invoke-RestMethod http://ipinfo.io/json; $ipinfo.ip`

8. Setup PS Environment:

   - Install RSAT: Server Manager => Features => Install AD module only
   - PS: `Install-Module -Name Az -AllowClobber -Scope AllUsers`
   - PS: `Install-Module -Name vmware.powercli -AllowClobber -Scope AllUsers`


9. Test load balancing in Jenkins

   - Create job: `Powershell Test` with the following FreeStyle project powershell code:

   ```powershell
   write-output $env:path
   write-output $env:username
   $con = get-content "q:\scripts\key.key"
   write-output "length is $($con.length)"
   ```

   - Ensure Jenkins Master won't run jobs: Login to `schedtasks-win2019.domain.com` => Manage Jenkins => Configure Nodes => Master => Set Executors to `0`
   - Run job `Powershell Test` which make sure powershell is ran as `svc_windowsJenkins` and can read the `aes.key` file
   - Take one node offline and make sure the job still runs
   - Alternate the other node and run the same job, should still work!

10. At this point, there is virtually unlimited settings you can tweak on each of your nodes as now that Jenkins can run scripts.  

   - For example, I created `q:\resources` on my attached disk and then added `winscp` so that I can use its DLL to SCP files from a powershell script. Now, instead of putting that executable in Github and pulling it down on every run, I can just do a quick `Test-Path q:\resources\winscp\winscp.dll` instead and have the script continue if found and error and exit if not. This slims down the run times of jobs even more.
   - Again, the only catch is that you will need to replicate every change you make to all nodes in the cluster. This shouldn't be a big deal though because you only have to do this once!

11. Done - At this point you have joined two nodes to the Jenkins cluster and tested that jobs can load balance between nodes. Next, we will configure Github so that we can build the jobs once and update them anytime after without having to connect to Jenkins Web UI.

