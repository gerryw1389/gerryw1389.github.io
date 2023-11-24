---
title: 'Veeam: SureBackup'
date: 2017-08-26T05:30:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/veeam-surebackup/
tags:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Veeam SureBackup is a way to tests your backup jobs automatically. You set them up like regular jobs and they do a restore in a test environment that Veeam creates.

### To Resolve:

1. Open the Veeam GUI and go to Backup Infrastructure => Sure Backup => Create => Name:Whatever => Point to a folder on whatever VM host you want for testing (one that is not being used a lot) => Leave all settings default => Next, Next, Next, Finish

2. Backup Infrastructure => Sure Backup => Application Groups => Create => I just chose a single W8.1 machine to test

3. Go to Backup & Replication tab => New Sure Backups Job => Point to Sure backup job, Point to sure backup application group (Make sure to check the checkbox to &#8220;keep the application group running after job completes&#8221;) => Next, Next, Next, Finish (check Run the job when finished).

4. Now we get to see it in action! RDP to your VM host and connect to the appliance via Hyper v  

   ```escape
   login: root / SureBackupJobName_r # see ["How to log in to the Virtual Proxy Appliance"](https://www.veeam.com/kb1447) for your password
   ```

5. Connect to your VM, should be good to go.

   <img class="alignnone size-full wp-image-4627" src="https://automationadmin.com/assets/images/uploads/2017/08/surebackup.png" alt="" width="1049" height="875" srcset="https://automationadmin.com/assets/images/uploads/2017/08/surebackup.png 1049w, https://automationadmin.com/assets/images/uploads/2017/08/surebackup-300x250.png 300w, https://automationadmin.com/assets/images/uploads/2017/08/surebackup-768x641.png 768w, https://automationadmin.com/assets/images/uploads/2017/08/surebackup-1024x854.png 1024w" sizes="(max-width: 1049px) 100vw, 1049px" /> 


### References:

["SureBackup Job"](https://helpcenter.veeam.com/docs/backup/hyperv/surebackup_job.html?ver=95)  