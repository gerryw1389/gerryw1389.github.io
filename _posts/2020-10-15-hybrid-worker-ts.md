---
title: Hybrid Worker Troubleshooting
date: 2020-10-15T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/10/hybrid-worker-ts
categories:
  - Azure
  - WindowsServer
tags:
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

Not very often I will have to troubleshoot issues on a hybrid worker. My only experience is with Windows Server 2019 and have had little luck in getting into troubleshooting these things. I will add to this post as they happen.

### To Resolve:

1. The only tool I have used so far resides at "C:\Program Files\Microsoft Monitoring Agent\Agent\AgentControlPanel.exe"

   - One time, when we had networking issues, it said: `The agent could not connect to the Microsoft Operations Management service`
   - The fix was to fix the networking issues and then restart `HealthService` ("C:\Program Files\Microsoft Monitoring Agent\Agent\HealthService.exe").
   - Then it changed back to connected.

2. In theory, you could check that `Orchestrator.Sandbox.exe` is running during a runbook execution, but not much to do there. More info on another post [here](https://automationadmin.com/2020/07/azure-automation-new-csonlinesession-maxshell-issue)
