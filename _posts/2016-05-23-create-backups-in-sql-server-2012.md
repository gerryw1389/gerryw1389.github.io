---
title: Create Backups In SQL Server 2012
date: 2016-05-23T12:25:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/create-backups-in-sql-server-2012/
tags:
  - WindowsServer
tags:
  - SQL
---
<!--more-->

### Description:

Follow these steps to create a backup plan in SQL Server 2012. Note this is not a &#8220;one size fits all solution&#8221; so YMMV.

### To Resolve:

1. Open SQL Management Studio and sign in with a user with Sys Admin rights.

2. Navigate down to SQL Server Agent and select &#8220;start&#8221;

3. Go to Management => Maintenance Plans => Follow the Wizard. Make sure to check the &#8220;verify backup integrity&#8221; option.

4. A good source of SQL Server information can be found [here](https://www.mssqltips.com/sql-server-dba-resources/)