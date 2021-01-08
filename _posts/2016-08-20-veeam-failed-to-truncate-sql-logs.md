---
title: 'Veeam Error: Failed To Truncate SQL Logs'
date: 2016-08-20T04:41:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/veeam-failed-to-truncate-sql-logs/
categories:
  - LocalSoftware
tags:
  - SQL
  - Backup
---
<!--more-->

### Description:

You will be getting errors/warnings stating:

   ```escape
   Failed to truncate Microsoft SQL Server transaction logs. Details: Error code: 0x80004005 Failed to invoke func [TruncateSqlLogs]: Unspecified error. Failed to process TruncateSQLLog command. Failed to truncate SQL server transaction logs for instances: . See guest helper log. . Error code: 0x80004005 Failed to invoke func [TruncateSqlLogs]: Unspecified error. Failed to process TruncateSQLLog command. Failed to truncate SQL server transaction logs for instances: See guest helper log.
   ```

### To Resolve:

1. On the SQL server with this error, navigate to `C:\ProgramData\Veeam\Backup` and view the log:

   ```escape
   WARN                            Cannot truncate SQL logs for database: (DBNAME)  Code = 0x80040e31  
   6/22/2016 1:12:46 AM   4640  WARN                             Code meaning = IDispatch error #3121  
   6/22/2016 1:12:46 AM   4640  WARN                             Source = Microsoft OLE DB Provider for SQL Server  
   6/22/2016 1:12:46 AM   4640  WARN                             Description = Query timeout expired  
   6/22/2016 1:12:46 AM   4640  WARN                            No OLE DB Error Information found: hr = 0x80004005
   ```

2. Open up SQL Server Management Studio and add the following user to the database that is failing the credentials:

   ```escape
   User type: SQL user with login  
   User name: System  
   Login name: NT AUTHORITY\SYSTEM  
   Default_schema: db_backupoperator
   ```

3. Next add the following regkeys on the SQL server:

   ```escape
   Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\VeeaM\Veeam Backup and Replication  
   and HKEY_LOCAL_MACHINE\SOFTWARE\VeeaM\Veeam Backup and Replication

   Name: SqlExecTimeout  
   Type: DWORD  
   Value: 600

   Name: SqlLogBackupTimeout  
   Type: DWORD  
   Value: 3600

   Name: SqlConnectionTimeout  
   Type: DWORD  
   Value: 300
   NOTE: These values are decimal values.  
   I also had to add the following keys to the Wow6432Node hive: VeeaMVeeam Backup and Replication  
   **Yes that is how it is supposed to be spelled with a capital M on the VeeaM key, according to support.
   ```

### References:

["Failed to Truncate transaction logs on ONE db in instance"](https://forums.veeam.com/veeam-backup-replication-f2/failed-to-truncate-transaction-logs-on-one-db-in-instance-t33181.html)  
["Job reports warning "Failed to truncate transaction logs for SQL instances..."](https://www.veeam.com/kb2027)  