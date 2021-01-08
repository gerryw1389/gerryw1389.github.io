---
title: 'Veeam: Backup Files Unavailable'
date: 2019-04-09T15:17:51+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/veeam-backup-files-unavailable/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Upon looking at a tape job, you will get a warning like &#8220;11 backup files to be excluded from the job because they are unavailable.&#8221;

### To Resolve:

1. Rescan the backup repo and try again

2. Check if the job it depends on is still running.

3. See if there is a merge taking place if you have synthetic fulls going periodically.

4. See if the backup repo is doing a health check.

5. Click Disks => Properties => Verify that the backup points don't have a red X next to them.