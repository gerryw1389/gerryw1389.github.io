---
title: 'Veeam: To Recover A File'
date: 2016-05-24T12:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-to-recover-a-file/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Follow these steps to recover a file from a Veeam backup.

### To Resolve:

1. Click on &#8220;Backup & Replication&#8221; in the left hand navigation pane.

   - ![veeam-1](https://automationadmin.com/assets/images/uploads/2016/09/veeam-1.png){:class="img-responsive"}

1. On the main screen, expand the MainServer server backup node.

1. Right click the &#8220;ServerName&#8221; VM and select &#8220;Restore guest files (Windows)…&#8221;

   - ![veeam-2](https://automationadmin.com/assets/images/uploads/2016/09/veeam-2.png){:class="img-responsive"}

4. Highlight the date of the backup that you would like to grab the file from and select Next => Finish.

5. You can now browse the file system in the previous state and grab the needed file. (D:Data)

   - ![veeam-3](https://automationadmin.com/assets/images/uploads/2016/09/veeam-3.png){:class="img-responsive"}


