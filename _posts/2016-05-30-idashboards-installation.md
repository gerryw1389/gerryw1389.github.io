---
title: iDashboards Installation
date: 2016-05-30T05:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/idashboards-installation/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

These are the steps I followed in installing iDashboard server. [iDashboards](https://www.idashboards.com) is a Java application that displays dashboards views of Excel or SQL Server data. It falls under reporting type applications used heavily in management positions.

### To Resolve:

1. I created a new Server 2012 VM, installed MS SQL Server 2008r2, and moved over the iDashboards installer, Java SQL installer, and the license file.

2. Before running the .exe for iDashbaords, I had to open SQL Server Management Studio.

3. Under Databases, I right clicked => New => DataBaseName

4. Under Security => Logins => Right Click => New Login => Filled out the info below:

   - Name: DBUser # Note: I created the same user and added them to the local admin account (`lusrmgr.msc`). On this screen, I selected the option to &#8220;search..&#8221; and pointed to the user.
   - Select the SQL Server authentication and input the password you want the user to have.
   - Move to the Server Roles tab => check &#8220;sysadmin&#8221; to give the database user sysadmin rights.
   - Move to the user mapping tab and select all the options. Also add &#8220;dbo&#8221; under the default schema:

   <img class="size-full wp-image-669 aligncenter" src="https://automationadmin.com/assets/images/uploads/2016/09/idashboards-user-mapping.png" alt="idashboards-user-mapping" width="559" height="570" srcset="https://automationadmin.com/assets/images/uploads/2016/09/idashboards-user-mapping.png 559w, https://automationadmin.com/assets/images/uploads/2016/09/idashboards-user-mapping-294x300.png 294w" sizes="(max-width: 559px) 100vw, 559px" />

   - Leave the rest default and click OK. Finished the installation. iDashboards can now be accessed via web GUI.

5. Website links:

  <img class="alignnone size-full wp-image-668" src="https://automationadmin.com/assets/images/uploads/2016/09/idashboard-links.png" alt="idashboard-links" width="521" height="167" srcset="https://automationadmin.com/assets/images/uploads/2016/09/idashboard-links.png 521w, https://automationadmin.com/assets/images/uploads/2016/09/idashboard-links-300x96.png 300w" sizes="(max-width: 521px) 100vw, 521px" />

