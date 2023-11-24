---
title: 'Veeam: Jobs Stuck In Stopping State'
date: 2016-05-24T12:54:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-jobs-stuck-in-stopping-state/
tags:
  - LocalSoftware
tags:
  - Backup
  - Regedit
---
<!--more-->

### Description:

I haven't had this happen to backup jobs, but replications have done this a couple times. Essentially, you want to reboot a replication server but you need to stop the replications on the VBR server first and you get stuck at a screen that shows your jobs are stuck in a stopping state for over 10 minutes. Use the following steps to actually get the jobs to stop.

  <img class="alignnone size-full wp-image-728" src="https://automationadmin.com/assets/images/uploads/2016/09/veeam-stuck-in-a-stopping-state.png" alt="veeam-stuck-in-a-stopping-state" width="708" height="134" srcset="https://automationadmin.com/assets/images/uploads/2016/09/veeam-stuck-in-a-stopping-state.png 708w, https://automationadmin.com/assets/images/uploads/2016/09/veeam-stuck-in-a-stopping-state-300x57.png 300w" sizes="(max-width: 708px) 100vw, 708px" />

### To Resolve:

1. Stop all services that start with &#8220;veeam&#8221;.

2. Open the Windows Task Manager and kill all `Veeam.Backup.Manager` and `VeeamAgent.exe` processes.

3. Restart the services that were stopped in step 1.

4. Remove snapshots from VM(s) that part of the stuck jobs. (If they have not been already removed).

5. If the previous steps didn't work, we need to alter the MySQL database the Veeam uses. To backup the MySQL database:

   - Using SQL Server Management Studio:

     - Open Microsoft SQL Server Management Studio (May need to be installed separately)
     - Connect to the &#8220;ServerName\Instance&#8221; of the server that has the DB you want backed up.
     - Expand the Databases tab to get to the DB you want to back up.
     - Right click the desired DB => Tasks => Back Up
     - Set &#8220;Backup Type&#8221; to &#8220;Full&#8221;
     - Go through the rest of the General and Options tab information to set the options to what you want.
     - Click OK to start the Backup process.

   - Using sqlcmd (preferred):

     - Check the name of the SQL instance and Veeam database in the Windows registry:
     - HKLM\Software\VeeaM\Veeam Backup and Replication\SqlServerName
     - HKLM\Software\VeeaM\Veeam Backup and Replication\SqlInstanceName
     - HKLM\Software\VeeaM\Veeam Backup and Replication\SqlDatabaseName
     - Open Windows Command prompt and connect to SQL instance:
     - SQLCMD -S SERVER\VEEAMSQL2008R2 
     - syntax is `SQLCMD -S (SqlServerName)\SqlInstanceName`
     - Note: In case you have SQL server authentication enabled you may define username using `-U` parameter
     - Back up the Veeam database:
     - BACKUP DATABASE VeeamBackup TO DISK = 'f:\db-backup\veeamdb.bak'  
     - GO
     - Syntax is:  
     - BACKUP DATABASE SqlDatabaseName TO DISK = 'C:\VeeamDB.bak'  
     - GO

6. In a new notepad document, copy/paste the following query:

   ```escape
   UPDATE [Backup.Model.JobSessions]  
   SET [state] = '-1'  
   WHERE [state] != '-1'
   ```

   - Save the script as *.sql file (e.g. script.sql) to local disk.
   - Make sure that no jobs are running.
   - Open an admin command prompt and run the following command:
   - sqlcmd -S SERVER\VEEAMSQL2008R2 -d VeeamBackup -i C:\Scripts\sql-query.sql -o C:\Scripts\sqlresetresults.txt
   - Syntax is:  
   - `sqlcmd -S SqlServerName\SqlInstanceName -d SqlDatabaseName -i PATHTOSCRIPT\script.sql -o c:\resetresult.txt`
   - Using: HKLM\Software\VeeaM\Veeam Backup and Replication\SqlServerName 
   - Using: HKLM\Software\VeeaM\Veeam Backup and Replication\SqlInstanceName
   - Using: HKLM\Software\VeeaM\Veeam Backup and Replication\SqlDatabaseName
   - If the script needs to be applied to EM database, please use:  
   - Using: HKLM\Software\VeeaM\Veeam Backup Reporting\SqlServerName  
   - Using: HKLM\Software\VeeaM\Veeam Backup Reporting\SqlInstanceName  
   - Using: HKLM\Software\VeeaM\Veeam Backup Reporting\SqlDatabaseName

7. Start all the Veeam services, should be good to go!


### References:

["How to forcibly stop jobs that are stuck in 'stopping' status"](https://www.veeam.com/kb1727)