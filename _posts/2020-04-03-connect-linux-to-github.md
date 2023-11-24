---
title: Connect Windows Server To Github
date: 2020-04-03T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/connect-windows-to-github
tags:
  - WebSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

Here are the steps I did to connect my Jenkins Windows servers to Github. For now, instead of integrating Github directly into Jenkins, I installed Git on each server and scripted a way for them to pull down just their specific folder using [sparse checkout](https://www.git-scm.com/docs/git-sparse-checkout) ad hoc when the job is ran. While Jenkins can probably do this natively, I haven't got there yet.

This is part of a 3 part series:

   - [1 - Deploy Jenkins Master](https://automationadmin.com/2020/03/deploy-jenkins-windows-master)
   - [2 - Deploy Jenkins Nodes](https://automationadmin.com/2020/03/deploy-jenkins-windows-node)
   - 3 - Connect To Github

Update: It looks like if I wanted, I could set Jenkins to use [sparse-checkout](https://www.decodingdevops.com/checkout-a-directory-from-git-by-using-jenkins/) by just clicking Additional Options => Sparse Checkout Paths => Enter path and then entering `. "$ENV:WORKSPACE\script name.ps1"` as the build step. I will continue to use what I have for now but keep this mind for my next Jenkins setup.


### To Resolve:

1. On each node (not needed on master server), install Git and connect to a private repo for your company's Github (if applicable):

   - First, in Azure AD create a service account, have it bypass 2FA (Security => Conditional Access => Policy Name => Exclude)
   - Now, in Github, join that user to your organization.
   - Login as that user and go to Settings => Developer Settings => Personal Access tokens => Create one with rights "repo" (full control)
   - Authorize it for SSO by hitting the drop down menu next to the token. Very important!
   - On each server, download and install 64 bit git. Make sure to 'Use Git and optional Unix tools from the Command Prompt' during install
   - Open ps not as admin:

   ```powershell
   cd ~./Documents
   mkdir test-git
   cd test-git
   git init .
   git config --global user.name "Service Windows Jenkins"
   git config --global user.email "svc_windowsJenkins@domain.com"   
   git remote add origin https://github.com/yourCompany/YourJenkinsRepo
   git config core.sparsecheckout true
   Write-Output "root/folder1/example-sub-folder" | out-file -encoding utf8 .\.git\info\sparse-checkout
   git pull origin master
   # enter user name and personal access token in the window that pops up
   git config --global credential.helper manager
   ```

   - We will use something like this in our jenkins jobs going forward. It's really neat because instead of checking out a single `jenkinsfile` like I do with my [previous install](https://automationadmin.com/2020/02/jenkins-source-job-in-gitlab/), I just have each server to a git pull but just for that specific job's folder at run time!

2. At this point in the walkthrough, you should have a service account in Github tied to your organization and your repo and you have a personal access token stored on each Windows node in the credential manager.

   - Ensure that you can see your token in credential manager:
   - RDP to each Windows server and run `control /name Microsoft.CredentialManager` and look for your github entry
   - If you have lots of different entries or bulk, just delete everything and do the Git steps again. Here is what to run to clear CredMan:

   ```powershell
   cmd /c "cmdkey /list" | ForEach-Object {if ($_ -like "*Target:*")
   {
   cmdkey /del:($_ -replace " ", "" -replace "Target:", "")
   }}
   ```

3. Using your account which should be admin in Github, create a repo 'windows-jenkins' as a private repo initialized with a README and set the owner to your organization.

   - Add the `svc_windowsJenkins@domain.com` from the [previous post](https://automationadmin.com/2020/03/deploy-jenkins-windows-node) as a maintainer under Repo Settings => Manage Access.

4. OK, now we will do the final step which is to setup a job that will create powershell scripts on whatever host it runs on. These scripts will pull down from github specifically tied to the job (so they don't download the whole repo on every run), they will move to the directory and execute whatever the scripts purpose is.

   - Create job: Freestyle project named 'powershell-test2'
   - No schedule, no nothing - just a simple `powershell` step under build that contains

   ```powershell
   # create powershell script

   $ScriptFile = "q:\jenkins\workspace\powershell-test2\script.ps1"

   $text = @'
   If ( Test-Path "q:\jenkins\workspace\powershell-test2\temp" )
   {
      Remove-Item "q:\jenkins\workspace\powershell-test2\temp" -Recurse -Force
      New-Item -ItemType Directory -Path "q:\jenkins\workspace\powershell-test2\temp" | Out-Null
   }
   Else
   {
      New-Item -ItemType Directory -Path "q:\jenkins\workspace\powershell-test2\temp" | Out-Null
   }
   Set-Location "q:\jenkins\workspace\powershell-test2\temp"
   git init . 
   git remote add origin https://github.com/yourCompany/YourJenkinsRepo
   git config core.sparsecheckout true
   Write-Output "powershell-test" | out-file -encoding utf8 .\.git\info\sparse-checkout
   git pull origin master
   exit
   '@

   If ( -not ( Test-Path $ScriptFile))
   {
      New-Item -ItemType File -Path $ScriptFile -Value $text | Out-Null
   }
   Else
   {
      Remove-Item $ScriptFile -Force
      New-Item -ItemType File -Path $ScriptFile -Value $text | Out-Null
   }

   # create the second launcher

   $ScriptFile2 = "q:\jenkins\workspace\powershell-test2\script2.ps1"

   $text2 = @'
   $ScriptFile = "q:\jenkins\workspace\powershell-test2\temp\powershell-test\test.ps1"

   Function Get-ObfPass
   {
      $s = '76492d1116743f0423413b16050a5345MgB8AF'
      $s += 'IAMwA2AHYAQgAyAEEAcQB2AC8AZABnAFkAQgBL'
      $s += 'AHcAQQA9iHIARwBEAHcAPQA9AHwAMQA0ADcAZg'
      $s += 'AwAGQANAA5ADkAOQA1ADAAZgA2AGQAZQAyADEA'
      $s += 'YgAzAGUANQA89AGQAYwA3ADEAMwA1AGQAZQBmAG'
      $s += 'MAMQA2ADUANQA5ADkAYgBhAGYANAA2ADgAYgA4'
      $s += 'ADAAMAAyADAANwAyADIAYgAwADgANABjADgANg'
      $s += 'AyADcANwABBq2='
      $Key = Get-Content "q:\scripts\key.key"
      $user = 'blank'
      $pass = $s | ConvertTo-SecureString -Key $Key
      $cred = New-Object -Typename System.Management.Automation.PSCredential -Argumentlist $user, $pass
      $val = $cred.GetNetworkCredential().Password
      return $val
   }

   Write-Output "Running second script - inside"

   $Username = "domain.com\svc_windowsJenkins"
   $Password = Get-ObfPass
   $SecurePassword = ConvertTo-SecureString -String $Password -AsPlainText -Force
   $Credential = New-Object System.Management.Automation.PSCredential( $Username, $SecurePassword)

   $Start = @{ 
      'FilePath'         = 'powershell.exe'
      'Credential'       = $Credential
      'WorkingDirectory' = 'q:\jenkins\workspace\powershell-test2\temp\powershell-test'
      'ArgumentList'     = @( '-f', $ScriptFile,
         '-ExecutionPolicy', 'Bypass',
         '-NoProfile', '-Verb', 'RunAs'
      )
   }
   Start-Process @Start -Wait
   Write-Output "Running second script - inside - completed"

   exit
   '@

   If ( -not ( Test-Path $ScriptFile2))
   {
      New-Item -ItemType File -Path $ScriptFile2 -Value $text2 | Out-Null
   }
   Else
   {
      Remove-Item $ScriptFile -Force
      New-Item -ItemType File -Path $ScriptFile2 -Value $text2 | Out-Null
   }


   # launch the first script

   Function Get-ObfPass
   {
      $s = '76492d1116743f0423413b16050a5345MgB8AF'
      $s += 'IAMwA2AHYAQgAyAEEAcQB2AC8AZABnAFkAQgBL'
      $s += 'AHcAQQA9iHIARwBEAHcAPQA9AHwAMQA0ADcAZg'
      $s += 'AwAGQANAA5ADkAOQA1ADAAZgA2AGQAZQAyADEA'
      $s += 'YgAzAGUANQA89AGQAYwA3ADEAMwA1AGQAZQBmAG'
      $s += 'MAMQA2ADUANQA5ADkAYgBhAGYANAA2ADgAYgA4'
      $s += 'ADAAMAAyADAANwAyADIAYgAwADgANABjADgANg'
      $s += 'AyADcANwABBq2='
      $Key = Get-Content "q:\scripts\key.key"
      $user = 'blank'
      $pass = $s | ConvertTo-SecureString -Key $Key
      $cred = New-Object -Typename System.Management.Automation.PSCredential -Argumentlist $user, $pass
      $val = $cred.GetNetworkCredential().Password
      return $val
   }

   Write-Output "Running first script"

   $Username = "domain.com\svc_windowsJenkins"
   $Password = Get-ObfPass
   $SecurePassword = ConvertTo-SecureString -String $Password -AsPlainText -Force
   $Credential = New-Object System.Management.Automation.PSCredential( $Username, $SecurePassword)
   $Start = @{ 
      'FilePath'         = 'powershell.exe'
      'Credential'       = $Credential
      'NoNewWindow'      = $true
      'WorkingDirectory' = 'q:\jenkins\workspace'
      'ArgumentList'     = @( '-f', $ScriptFile,
         '-ExecutionPolicy', 'Bypass',
         '-NoProfile', '-Verb', 'RunAs'
      )
   }
   Start-Process @Start -Wait

   Write-Output "Running first script - Completed"
   Write-Output "Running second script"

   $Start2 = @{ 
      'FilePath'         = 'powershell.exe'
      'Credential'       = $Credential
      'NoNewWindow'      = $true
      'WorkingDirectory' = 'q:\jenkins\workspace'
      'ArgumentList'     = @( '-f', $ScriptFile2,
         '-ExecutionPolicy', 'Bypass',
         '-NoProfile', '-Verb', 'RunAs'
      )
   }
   Start-Process @Start2 -Wait
   Write-Output "Running second script - Completed"

   Write-Output "completed O_o"
   ```

   - Let me explain what this does:
     - At runtime, it will create two files under `q:\jenkins\workspace\powershell-test2` called `script.ps1` and `script2.ps1`
     - Since the nodes run as `NT Authority\System`, we have them launch a process as the service account that pulls down from Github (script.ps1)
       - As you can see, this is where that key file comes into play that we created in the previous post. Alternatively, you could try to have Jenkins inject the credential at run time.
     - We then do the same thing for `script2.ps1` which will launch a script from the newly pulled down Github repo.

5. Now that we have everything setup, the real power comes from the fact that from now on, you only have to use something like vscode to pull from github, make changes locally by `git commit` and then push the changes back to Github without even touching Jenkins or any of its nodes!

