---
title: SQL Installion Error
date: 2016-05-26T22:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/sql-installion-error/
tags:
  - WindowsServer
tags:
  - SQL
---
<!--more-->

### Description:

You will get Error code 0x84B40000 when installing SQL Server 2008 Express. It will say:

&#8220;SQL Server Setup has encountered the following error: Attributes do not match. Present attributes (Directory, Compressed) , included attributes (0), excluded attributes (Compressed, Encrypted). Error code 0x84B40000.&#8221;

### To Resolve:

1. Open &#8220;My Computer&#8221; and right click on the OS Drive's Properties. If the checkbox is checked under &#8220;compress this drive to save disk space&#8221;, uncheck it. SQL will not install on drives that are compressed.