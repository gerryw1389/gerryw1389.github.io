---
title: 'PS: AD Replication Health Checks'
date: 2016-12-03T01:33:27+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/ps-ad-replication-health-checks/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - ActiveDirectory
---
<!--more-->

### Description:

AD health checks are a must have task for Windows Systems Administrators. I set the following first two scripts up that email me every morning at 5 AM and the third script as ran as a continous task on my PDC.

### To Resolve:

1. Copy and paste these scripts to your domain controller. Set as .ps1 files and setup scheduled tasks with them.

   - [Send-ADDCDiagReport](https://github.com/gerryw1389/powershell/blob/main/gwActiveDirectory/Public/Send-ADDCDiagReport.ps1)
   - [Send-ADHealthReport](https://github.com/gerryw1389/powershell/blob/main/gwActiveDirectory/Public/Send-ADHealthReport.ps1)
   - [Watch-ADReplicationStatus](https://github.com/gerryw1389/powershell/blob/main/gwActiveDirectory/Public/Watch-ADReplicationStatus.ps1)