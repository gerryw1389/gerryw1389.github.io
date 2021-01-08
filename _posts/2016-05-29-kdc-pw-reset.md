---
title: KDC PW Reset
date: 2016-05-29T04:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/kdc-pw-reset/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

If you ever run `repadmin /showrepl` and find errors, one troubleshooting step you can try is to reset the KDC password and clear the ticket cache. The following exchanges should be made between Server1 (your PDC) and Server2 (the server with replication issues):

### To Resolve:

1. Stop the Key Distribution Center (KDC) service on Server2: [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `net stop kdc`

2. Load Kerbtray.exe: Run => `c:\program files\resource kit\kerbtray.exe`

3. Purge the ticket cache on Server2: Right-click the green ticket icon in your system tray, and then click Purge Tickets. You should receive a confirmation that your ticket cache was purged. Click OK.

4. Reset the Server domain controller account password on Server1 (the PDC emulator): [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `netdom /resetpwd /server:server2 /userd:domain.com\administrator /passwordd:password`

5. Synchronize the domain on Server1: [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `repadmin /syncall`

6. Start the KDC service on Server2: [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) Type: `net start KDC`

### References:

["Replication Issues - Think I know why, But ...."](https://www.reddit.com/r/sysadmin/comments/4eb33p/replication_issues_think_i_know_why_but/)  
["Secure channel between the DC's broken"](https://sandeshdubey.wordpress.com/page/2/)  