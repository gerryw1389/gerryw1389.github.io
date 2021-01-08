---
title: iDashboards
date: 2016-05-23T12:54:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/idashboards/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

[iDashboards](https://www.idashboards.com) is a server software that we use to generate Flash based reports for your executive team.

### To Resolve:

1. Idashboard has a client that you can install. It allows you to pick a server to connect to.

2. You can download different plugins:

   - Set states into regions = county maps  
   - Chart example pack  
   - Visibility pack = IT metrics  
   - Dsapi = To create custom connections to idashboards API.

3. iDashboards has an auto-discover directory located on the severs's idashboard program files location. You can change this if needed.

   - Rules for Excel:  
   - You have to &#8220;Name&#8221; a set of data = press ctrl+a on the cells and name it something.  
   - Column names shouldn't have trailing spaces.  
   - Do all formatting in iDashboards. Make Excel as plain as possible.

4. iDashbords limitations: For queries = 1000 rows / 3000 for pivots. Files: All photo formats, only .flv for video. * Always drill back up before saving. If you don't it will override the top level one you had previously saved.

### The Actual Program:

1. Designer => Dashboards => Frames = Where you insert Charts/ Panels/ Pictures,Txt

2. GUI Rules: Right click driven menu, You have to manually save, right arrow is to keep and continue, left error is to discard and not save.

3. Terms and features:

   - Dataset => Axis list => Chart type => Chart Preview Properties => Drilldown  
   - Drill down => chart pivots => match column names  
   - Input parameters = textbox, dropdowns, functions  
   - Dashobard paramters = can be applied to all chart paramters as long as the column names match  
   - Picklist = Create picklist from iDashboard menu => create parameter => drop down => picklist  
   - Create filter to parameter

4. Lastly:

   - Report schedules = Sends reports automatically. We configured the smtp server.  
   - Chart alerts = when something happens, send an email.  
   - Dashboard reports = Exports chart data to a PDF.

5. Tips in creating a dashboard:

   - Add the columns as dashboard parameters from the data source. For your own columns, you have to use calculated parameters:  
   - For dates, do ${currdate-90} as the beginning value and ${currdate} as the ending value  
   - For drop down list, you have to manually type all available options in the &#8220;initial value&#8221; for each option. This is only if you want to filter multiple charts on multiple points.  
   - Remember to use thresholds when available  
   - Remember to make all charts look similar in size. If you have to, under &#8220;force grid boundaries&#8221; => check that to set a cutoff