---
title: Setting Up Cron Job Using Crontab
date: 2018-02-24T05:12:27+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/setting-up-cron-job-using-crontab/
categories:
  - Linux
tags:
  - Scripting-Bash
---
<!--more-->

### Description:

Follow this guide to using crontab in Linux. The following is a list of cron directories:  
   - /etc/cron.hourly  
   - /etc/cron.daily  
   - /etc/cron.weekly  
   - /etc/cron.monthly

### To Resolve:

1. If you don't want to worry about when your script runs and just want it to run hourly, daily, weekly, or monthly then just copy your script to one of those directories with a permission of `755` and it will run:
   - Example:
   - Open a terminal and copy your shell script `script.sh` into one of the directories above. If you need to run the script hourly, place your script file in the `cron.hourly` folder. For daily, place it inside the `cron.daily` and so forth.

   - Give the shell script the correct permission. For example, if script is called `script.sh`, set permission as follows:

   ```shell
   cd /etc/cron.daily/
   chmod 755 script.sh
   ```

   - Then, later in the logs you can see it ran:

   ```escape
   cat /var/log/cron* # specifically cron-20200106
   Jan  6 11:32:01 servername run-parts(/etc/cron.daily)[11043]: starting script.sh
   Jan  6 11:32:01 servername run-parts(/etc/cron.daily)[11051]: finished script.sh
   ```

2. If you prefer to have a more dynamic and explicit way to run a job, use crontab:

   ```shell
   crontab –e
   ```

   - This opens vi editor for you. Create the cron command using the following syntax:

     - The number of minutes after the hour (0 to 59)  
     - The hour in military time (24 hour) format (0 to 23)  
     - The day of the month (1 to 31)  
     - The month (1 to 12)  
     - The day of the week(0 or 7 is Sun, or use name)       - The command to run

   - An example command would be `0 0 * * * /etc/cron.daily/script.sh`. This would mean that the shell script will exactly execute at midnight every night. I personally would use an [online generator](https://crontab-generator.org/) to learn the syntax.

   - To save the changes to the crontab that you just made, hit ESC key, and then type :w followed by :q to exit.

3. After exiting crontab, the scheduled task (Windows equivalent) will run. If you want to check the jobs, check first as your normal user and then check as root (run `ls -l` to see the script's owner) :

   ```shell
   # To list existing cron jobs:
   crontab -l
   crontab -u username -l

   # To remove an existing cron job:
   crontab –e
   # Delete the line that contains your cron job
   # Save and quit => Type :wq!
   ```

