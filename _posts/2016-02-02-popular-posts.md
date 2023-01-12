---
title: Popular Posts
date: 2016-02-02T04:53:02+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/02/popular-posts/
categories:
  - SysAdmin
---
<!--more-->

#### Posts:

1. Azure:
   - [Every call to Azure has a REST API Backend - Azure is just a giant REST Webapp!](https://automationadmin.com/2022/10/tf-using-az-preview-features)
   - It doesn't matter if you are using the portal GUI, powershell, az cli, or pythin SDKS, they all just pass data types to Rest API endpoints in the background.
   - It is important to learn this!!

1. Terraform Setup:
   - [Setup Azure Devops For Terraform](https://automationadmin.com/2022/05/setup-azdo-terraform/)
   - [Terraform: Setup New Subscription](https://automationadmin.com/2022/10/tf-new-subscription)

1. Terraform Main Strategy:
   - [Terraform: Calling Remote Modules](https://automationadmin.com/2022/08/calling-remote-modules)
   - [Git Tagging](https://automationadmin.com/2022/08/git-tagging)

2. Terraform:
   - [Terraform: Introduction](https://automationadmin.com/2022/07/tf-intro)
   - [Terraform: Read Multiple Subscriptions](https://automationadmin.com/2022/08/tf-read-multiple-subs)
   - Just read all the posts under the [Infrastructure Provisioning](https://automationadmin.com/tags/#infrastructureprovisioning) tag :)

3. Git:
   - [Connecting To Private Github Repo](https://automationadmin.com/2018/02/connect-to-github-private-repo/)
   - [Git Tagging](https://automationadmin.com/2022/08/git-tagging)
   - [VSCode Remote Explorer Setup](https://automationadmin.com/2022/08/vscode-remote-explorer-setup)
   - [Notes on Git](https://automationadmin.com/2019/06/notes-on-git/)

4. Powershell:
   - [New To Powershell?](https://automationadmin.com/2018/02/new-to-powershell/)
   - [Template](https://automationadmin.com/2016/11/ps-template-script/)
   - [Logging](https://automationadmin.com/2017/09/ps-why-I-use-my-template-for-logging/)
   - [PS Remoting GPO](https://automationadmin.com/2019/05/gpo-enable-psremoting-over-https/)
   - [Modules](https://automationadmin.com/2018/01/ps-moving-to-modules-pt-2/)
   - [Single Commands](https://automationadmin.com/tags/#ps-one-liners)
   - [Using Passwords In Scripts](https://automationadmin.com/2016/05/using-passwords-with-powershell/)
   - Download my latest Powershell module:

   ```powershell
   $URI = "https://api.github.com/repos/gerryw1389/powershell/releases/latest"

   # Prevent "Invoke-RestMethod : The request was aborted: Could not create SSL/TLS secure channel."
   # This is because Powershell uses 1.0 and most sites require 1.2
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
   $Response = Invoke-RestMethod -Method Get -Uri $URI
   $ZipUrl = $Response.zipball_url

   # Download the file to the current location
   $OutputPath = "$((Get-Location).Path)\$($Response.name.Replace(" ","-")).zip"
   Invoke-RestMethod -Method Get -Uri $ZipUrl -OutFile $OutputPath
   ```

5. Python:
   - [New To Python](https://automationadmin.com/2020/11/new-to-python)
   - [Running Python On Windows](https://automationadmin.com/2020/02/setup-portable-python-scripts-on-windows)
   - [Intermediate Snippets](https://automationadmin.com/2020/06/python-intermediate-snippets)

6. General:
   - [How to be a Linux SysAdmin](https://automationadmin.com/2016/05/how-to-become-a-linux-sysadmin/) 
   - [How to be a Windows SysAdmin](https://automationadmin.com/2016/06/how-to-be-a-windows-sysadmin/) 
   - [3 Part Quiz](https://automationadmin.com/2018/05/general-knowledge-quiz/)
   - [Setting Up A Test Lab](https://automationadmin.com/2016/12/setting-up-a-lab-using-only-virtual-box/)
   - [Setup A New Computer](https://automationadmin.com/2020/07/chocolatey-computer-refresh)

7. Specific actions:
   - [Breaking Into SA Jobs](https://automationadmin.com/2016/05/breaking-into-sa-jobs/)
   - [PS: Get Emails From All Users On A Share](https://automationadmin.com/2018/11/common-workflow-get-email-addresses-for-all-users-on-a-share/)
   - [PS: Servers List To CSV](https://automationadmin.com/2019/06/servers-list-to-csv/)
   - [Logic App Expressions](https://automationadmin.com/2020/05/logic-app-expressions)
   - [Regex Examples](https://automationadmin.com/2017/02/regex-examples/)

8. Other:
   - [Top Xkcd's](https://automationadmin.com/2018/08/top-xkcds/)
   - [Meta - Categories and Tags for this site](https://automationadmin.com/2016/01/categories-tags/)
