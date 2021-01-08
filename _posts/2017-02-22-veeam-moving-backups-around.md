---
title: 'Veeam: Moving Backups Around'
date: 2017-02-22T04:47:09+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/02/veeam-moving-backups-around/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

I recently started moving Veeam backups around. For security, I wanted my shares to be accessible only from a specific domain account so I had to setup a server with USB3 ports and plugin drives there. I didn't want to lose my recent backups so I followed Veeam's guide on moving repo's. Example: Moving from USB drive on one server (USB1) to USB drive on another server (USB2)

### To Resolve:

1. Go to Backups => Disk => Job Name => Remove From Configuration. This removes the job from the Veeam database but doesn't actually affect the backup. This would be all the backups that go to USB1.

2. Copy the backups from USB1 to USB2.

3. Create a new backup repo under Backup Infrastructure => Backup Repo's that points to USB2. When adding the repo, Veeam will scan and import the backups automatically, also make sure to specify credentials and anything else needed for the new repo in this step.

4. Lastly, just go to Backups and modify your jobs to now point to USB2's repo. What's really neat is you can &#8220;map backup&#8221; and it will pick up where it left off on the previous repo and automatically move the &#8220;disks => backup&#8221; from &#8220;imported&#8221; over to the completed section for you once you do this.

   - This was a very simplified example, but you get the idea => Remove the repo metadata, add new repo, point your jobs to new repo, then map to old data on new repos.

### References:

["How to Move Veeam Backup & Replication Backup Files"](https://www.veeam.com/kb1729)  