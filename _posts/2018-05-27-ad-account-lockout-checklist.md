---
title: AD Account Lockout Checklist
date: 2018-05-27T03:42:58+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/ad-account-lockout-checklist/
tags:
  - Windows
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Checklist for finding out why an account keeps locking out of AD.

### To Resolve:

1. Check event ID's: 529, 539, 644, 671, 675, 676, 681, 4771, 4625, 4740 

2. Scripts  

3. Credential Manager  

4. Scheduled tasks  

5. System Credential Manager (run psexec to open the system user, and check there),  

6. SQL agent jobs  

7. Third party RDP programs like RDTabs and Terminals.  

8. If none of the above, then turn on [AD debug logging](https://automationadmin.com/2016/12/setting-up-auditing-in-ad/), netlogon issues can present themselves in wonky ways.