---
title: Moving To Azure Automation
date: 2020-04-12T08:06:24-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/moving-to-azure-automation
tags:
  - Azure
tags:
  - Orchestration
  - Azure-Automation
  - VersionControl
---
<!--more-->

### Description:

Instead of using Jenkins, we wanted to test with Azure Automation instead. The way it works is that your 'jenkins master' is now becomes an automation account in Azure, and 'jenkins nodes' become ['hybrid workers'](https://docs.microsoft.com/en-us/azure/automation/automation-hybrid-runbook-worker).

### To Resolve:

1. Inside Azure, create at least a '/28' subnet (11 IPs) and create an 'Automation Account' and a 'Log Analytics Workspace'
   - It is very important that when you setup the Automation account, you setup a `runas` account in the window when it asks you. What Azure will do is create an app inside your Resource Group and generate a certificate that you will use in a later step. When repeating this post for a test automation account I skipped this step and got stuck until I went back and did this!

2. On-prem, deploy a WS2019 and run:

   - First, turn off 'IE Enhanced Security'

   - Open PS as administrator and run the template [here](https://docs.microsoft.com/en-us/azure/automation/automation-windows-hrw-install):  

   ```powershell
   Install-Script -Name New-OnPremiseHybridWorker 

   New-OnPremiseHybridWorker.ps1 -AutomationAccountName "automation" -AAResourceGroupName "myAutomationRG"`
   -OMSResourceGroupName "myAutomationRG" -HybridGroupName "automation-workers" `
   -SubscriptionID "697e3b15-da99" -WorkspaceName "automation-logs"

   # It ends by dumping you to 'C:\Program Files\Microsoft Monitoring Agent\Agent\AzureAutomation\7.3.702.0\HybridRegistration>'
   ```

3. Created credential under the automation account called 'domain\svc_jenkins' from before.

   - Open the Automation account in the Azure portal => Select the Hybrid Worker Groups tile, and then select the group => Select All settings, followed by Hybrid worker group settings. => Change the value of Run As from Default to Custom. => Select the credential and click Save.

4. Following [the guide](https://docs.microsoft.com/en-us/azure/automation/automation-hrw-run-runbooks), it says that if you are running workers as a domain user, you have to import a cert on the worker. Seems pretty easy, I created a ps1 file locally and pasted in content from the article and saved as  `Export-RunAsCertificateToHybridWorker.ps1`. I changed the password (on line 33) to a password that I knew. From there I uploaded to the automation account and ran it. It failed during the run, but I was able to see the `.pfx` file from the logs saying it was in `%APPDATA%`.

   - So I went to the machine and double clicked the pfx so it would import. I chose 'local machine' and typed in the password and it worked.

5. Now I created a new runbook called 'test' and pasted in:

   ```powershell
   write-output "starting test"
   write-output (cmd /c whoami)

   new-item -itemtype file -path c:\script -name myfile.txt -value "hello world"

   add-content -path c:\scripts\myfile.txt -value (cmd /c whoami)

   $dll = "c:\scripts\rsc\WinSCPnet.dll"
   If ( -not ( Test-Path $dll ))
   {
   Write-Error "Unable to find WinSCP dll, exiting"
   Exit 1
   }

   New-PSDrive -Name T -PSProvider FileSystem -Root "\\server.domain.com\serviceAccount"
   New-Item -Path "t:" -Name "azure-dir" -ItemType Directory
   New-Item -Path "t:\azure-dir" -Name "something.txt" -ItemType File
   Remove-PSDrive -Name T

   ```

   - Obviously, I made sure that `c:\scripts\rsc\WinSCPnet.dll` existed prior and that a share was created with share permissions and NTFS permissions to allow `domain.com\svc_jenkins` to be able to access it.

   - Test was successful!

6. Next, I made sure the service account user was able to create resources in that specific resource group:

   - Since we use AD sync, I just selected the user principle on the 'Azure Subscriptions' pane and added the account as a 'contributor'
  
7. Next, I had that same account as a user on our company Github. From within Github, I created a repo called `azure-automation` and gave that service account Contributor access. I then created a PAT (Personal Access token).

   - Personal Access Token rights = `repo` all the boxes and `admin:repo_hook`

   - Following [the guide](https://docs.microsoft.com/en-us/azure/automation/source-control-integration#source-control-types), I connected Github to the Automation account using cloud shell in the portal and running (because the portal wouldn't show any repos):

   ```powershell
   $s = ConvertTo-SecureString "5832personalAccessToken5a1ffc5f23ab9c981" -AsPlainText -Force
   New-AzAutomationSourceControl -Name "azure-github" -RepoUrl "https://github.com/mycompany/azure-automation.git" -SourceType GitHub -FolderPath "/runbooks" -Branch master -AccessToken $s -ResourceGroupName "myRG" -AutomationAccountName "automation"
   ```

8. Now add the repo to my machine and create a similar test script and watch it automatically sync and publish (as long as you chose those options under Automation Account => Source Control => AutoSync = True / Publish Runbook = True.

9. If you want to forward your logs, you will have to enable MS Insights at the subscription level and then run from cloudshell:

   ```powershell
   Get-AzResource -ResourceType "Microsoft.OperationalInsights/workspaces"
   # copy output from previous command
   $l = '/subscriptions/longpath/log-analytics'
   Get-AzResource -ResourceType "Microsoft.Automation/automationAccounts"
   # copy output from previous command
   $a = '/subscriptions/longpath/automation'
   Set-AzDiagnosticSetting -ResourceId $a -WorkspaceId $l -Enabled 1

   # Verify
   Get-AzDiagnosticSetting -ResourceId $automationAccountId
   ```

10. I have [another post](https://automationadmin.com/2020/04/use-log-analytics-with-azure-automation-for-alerts) on this if you want to continue reading
