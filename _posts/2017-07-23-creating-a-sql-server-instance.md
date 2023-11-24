---
title: Creating A SQL Server Instance
date: 2017-07-23T03:04:35+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/creating-a-sql-server-instance/
tags:
  - WindowsServer
tags:
  - SQL
---
<!--more-->

### Description:

Follow these steps to install a SQL Server named instance.

### To Resolve:

1. Insert the iso and start the setup installer.

2. From the left menu, click Installation.

3. Click New SQL Server stand-alone installation or add features to an existing installation.

4. Wait for the installation wizard to search for the latest updates. Click Next.

5. The installation will now run the Setup Support Rules wizard. Click OK when the operation is completed.

6. In the Installation Type screen, select Perform a new installation of SQL Server 2012.

7. In the Product Key screen, enter your license key. Unless your organization requires something different for licensing compliance, this should be the same key as the license key for the original instance of SQL server installed.

8. Read the EULA, click I accept the license terms and click Next.

9. Select SQL Server Feature Installation and click Next.

10. Select features to install: In the Feature Selection screen select the components that are going to be installed:

   - Database Engine Services
   - SQL Server Replication
   - Full-Text and Semantic Extractions for Search
   - Data Quality Services

11. Click Next. The wizard runs through another rule check for the Installation Rules. Click Next.

12. Select Named instance and enter a name for the new SQL server instance. This should be something informative and easy to recognize. This name will be used to access the instance created. For example, NEW_INSTANCE. Click Next.

13. Wait for the installation wizard to complete the Disk Space Requirements check. Click Next.

14. The Server Configuration dialogue box allows you to configure what services of this instance you would like to automatically start. Change all of the services to Automatic. Click Next.

15. In the database engine configuration screen, select Mixed Mode (SQL Server authentication and Windows authentication).

16. (Optional) Specify a password for the SQL Server system administrator (sa).

17. Click the Add Current User to add the user you are logged in as, or the Add… button to add a specific account for this purpose. Once complete, click Next.

18. In the Error Reporting screen, click Next.

19. The last rule checking window ensures all previous information entered will allow the installation for the new SQL server instance to complete successfully. Review any required information and click Next.

20. Click Install. Installation process takes some time depending on the available resources.

21. When the installation is complete, click Close.