---
title: Migrating Email Scheduled Task
date: 2021-01-17T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/migrating-email-sched-tasks
categories:
  - Windows
tags:
  - Scripting-Python
  - Scripting-Powershell
---
<!--more-->

### Description:

These are the steps I used to migrate my "send email if bitcoin is trending down" [scheduled task to python](https://github.com/gerryw1389/python/tree/main/scripts/check_bitcoin).

### To Resolve:

1. Read the [README](https://github.com/gerryw1389/python/blob/main/scripts/check_bitcoin/readme.md)

2. In Windows task scheduler, setup the task to run on whatever schedule needed and point to the batch file.
   - The batch file will call the powershell script
   - The powershell script will activate the venv and call the python script
   - The python script will query the REST API and create a 'logs' folder that will tell me if the price doesn't drop and will email me when the price does drop
   - Script will be maintained [on my Github](https://github.com/gerryw1389/python/tree/main/scripts/check_bitcoin)
     - If you have time, look at the `helpers.py` file and how it uses functions to start logging and sending emails
     - Look at the log file to see the format
     - Check the [check_mutual_funds](https://github.com/gerryw1389/python/tree/main/scripts/check_mutual_funds) repo and see a foreach loop with this API and a different endpoint!
     - Try to replicate on your machine, this is a good first project!
