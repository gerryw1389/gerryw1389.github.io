---
title: System Center Configuration Manager
date: 2016-05-29T04:49:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/system-center-configuration-manager/
categories:
  - WindowsServer
tags:
  - ConfigManagement
---
<!--more-->

### Description:

System Center Configuration Manager (SCCM) is a management application that monitors and controls various aspects of multiple computers. Follow these steps to install System Center Configuration Manager.

NOTE: I did these steps in a Windows Server 2012 Standard VM in my home lab. My company is not large enough to warrant a purchase of this amazing software so I have barely any experience with it at this time. This is just from a DreamSpark subscription at my college.

### To Resolve:

1. First, install the .NET 3.5 feature by Server Manager or by PS running: Install-WindowFeature -Name NET-Framework-Core.

   - I kept getting a `dismapi_error__cbs_download_failure microsoft.windows.servermanager` error, so I just mounted my install ISO and added a `-source D:\sources\sxs\` parameter and it was finally successful.

2. SCCM requires a SQL Server instance, so I installed SQL Server 2012. In the feature selection I &#8220;selected all&#8221; options and added my domain admin as a user for all admin stuff. From what I read, you have to choose the same SQL Server year as SCCM.

3. Run the installer, enter the product key, combine with the SQL instance it populates, create a management group name/ administrator, and finish the install.