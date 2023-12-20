---
title: 'PS: SkypeOnline Depreciated Finally'
date: 2021-07-05T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/07/ps-skype-online-connector-depreciated
tags:
  - SysAdmin
tags:
  - Powershell
---
<!--more-->

### Description

One of my Azure Automation Runbooks started failing due to SkypeOnlineConnector being depreciated:

   ```escape
   Processing data from remote server admin1a.online.lync.com failed with the following error 
   message: Skype for Business Online PowerShell connections are blocked. Please replace the Skype for Business Online 
   PowerShell connector module with the Teams PowerShell Module.  Please visit https://aka.ms/sfbocon2tpm for supported 
   options. For more information, see the about_Remote_Troubleshooting Help topic.

   Install-Module MicrosoftTeams

   Install the latest Teams PowerShell module. For steps, see Install Microsoft Teams PowerShell.

   Uninstall Skype For Business Online Connector. To do this, in Control Panel, go to Programs and Features, select Skype for Business Online, Windows PowerShell Module, and then select Uninstall.

   In your PowerShell scripts, change the module name that's referenced in Import-Module from

   SkypeOnlineConnector or LyncOnlineConnector to MicrosoftTeams.

   For example, change Import-Module -Name SkypeOnlineConnector to Import-Module -Name MicrosoftTeams.

   When using Teams PowerShell Module 2.0 or later, update your scripts that refers New-CsOnlineSession to Connect-MicrosoftTeams. Import-PsSession is no longer required to establish a Skype for Business Online Remote PowerShell Session as that is done implicit when using Connect-MicrosoftTeams.
   ```

### To Resolve:

1. As the fix says, just uninstall the old SkypeOnlineConnector executable and do an `Import-Module -Name MicrosoftTeams` instead.

2. Normally, this something I wouldn't write a post on, but what makes this awesome is that I have [had issues with SkypeOnline module automation in the past with my Azure Hybrid Workers](https://automationadmin.com/2020/07/azure-automation-new-csonlinesession-maxshell-issue). With this new fix, I was able to move the script from a scheduled task that ran on my Hybrid Worker to my Azure Automation source controlled `runbooks` directory in Github. Heck yes!