---
title: 'Veeam Error: Processing ServerName'
date: 2016-05-24T12:40:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-error-processing-servername/
tags:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Veeam error will look like `Processing (ServerName) Error: Microsoft SQL server hosting the configuration database is currently unavailable. Possible reasons are heavy load, networking issue, server reboot, or hot backup`

### To Resolve:

1. This has only been seen on VM's with "Application Aware Processing" in their options and connected to a SQL database.

2. Try changing from Windows Authentication to SQL Authentication. Either way, make sure the Windows account credentials can access the SQL instance and if you use SQL authentication, make sure that user has access to the database.

3. I have also fixed this by pausing my replications during the peak backup times and resuming them later, outlined [here](https://automationadmin.com/2016/05/veeam-replication-startstop-scripts/)

### References:

["Step 2. Specify Connection Settings"](http://helpcenter.veeam.com/backup/80/vsphere/dbconfig_connection_settings.html?zoom_highlightsub=sql%2Bauthentication)