---
title: Migrating Email Scheduled Task
date: 2021-01-17T18:22:38-06:00
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

These are the steps I used to migrate my "send email if bitcoin is trending down" [scheduled task to python](https://github.com/gerryw1389/python/blob/main/learning/requests/alphavantage-bitcoin.py).

### To Resolve:

1. Create a folder under my private python repo called `check_bitcoin`:

   ```powershell
   cd C:\repo\schedtasks\check_bitcoin
   
   # create an active venv
   python -m venv ./venv
   .\venv\Scripts\activate

   # upgrade pip
   c:\repo\schedtasks\check_bitcoin\venv\scripts\python.exe -m pip install --upgrade pip

   # install stuff
   pip install requests
   pip install python-dotenv
   ```

   - Create a `.gitignore` with `.env` and `venv` so that it is not tracked with git.
   - Develop script and test with `python main.py`
   - Once done, create `requirements.txt` by typing `python -m pip freeze > requirements.txt`
   - Deactivate venv: `deactivate`

2. To have powershell run the python script, I will largely follow my [older post](https://automationadmin.com/2020/02/setup-portable-python-scripts-on-windows)

   - Create a powershell script [check_bitcoin.ps1](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/assets/code/check_bitcoin/check_bitcoin.ps1)

   - Create a [check_bitcoin.bat](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/assets/code/check_bitcoin/check_bitcoin.bat)

3. In Windows task scheduler, setup the task to run on whatever schedule needed and point to the batch file.
   - The batch file will call the powershell script
   - The powershell script will activate the venv and call the python script
   - The python script will query the REST API and create a 'logs' folder that will tell me if the price doesn't drop and will email me when the price does drop
   - Script will be maintained [on my Github](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/assets/code/check_bitcoin)
     - If you have time, look at the `helpers.py` file and how it uses functions to start logging and sending emails
     - Look at the log file to see the format
     - Check the [check_mutual_funds](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/assets/code/check_bitcoin/check_mutual_funds.py) and see a foreach loop with this API and a different endpoint!
     - Try to replicate on your machine, this is a good first project!
