---
title: 'Veeam Error: Guest Processing Skipped'
date: 2016-05-24T12:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-error-guest-processing-skipped/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Veeam will be failing on the backups with the following log event: `"Guest processing skipped, check guest OS VSS state and integration components version..."`

  <img class="alignnone size-full wp-image-724" src="https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest.png" alt="veeam-failed-to-prepare-guest" width="1344" height="68" srcset="https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest.png 1344w, https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-300x15.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-768x39.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-1024x52.png 1024w" sizes="(max-width: 1344px) 100vw, 1344px" />

### To Resolve:

1. After Googling the error, I found the official answer at [http://www.veeam.com/kb1855](https://www.veeam.com/kb1855). First step is to make sure you have the newest &#8220;Integration Services Setup Disk&#8221; installed. To install, just go to action on the Hyper-V menu and install it.

  <img class="alignnone size-full wp-image-725" src="https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-2.png" alt="veeam-failed-to-prepare-guest-2" width="377" height="519" srcset="https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-2.png 377w, https://automationadmin.com/assets/images/uploads/2016/09/veeam-failed-to-prepare-guest-2-218x300.png 218w" sizes="(max-width: 377px) 100vw, 377px" />


2. Login to the VM with the issue => Run => `diskmgmt.msc` => Right click => Properties => Shadow Copies => Settings => Point to a location to store shadow copies => and then Enable. It will create a snapshot automatically. If you have the space, go into the Settings on this tab and select &#8220;no limit&#8221; for the size of the snapshots.

  <img class="alignnone size-full wp-image-4641" src="https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped.jpg" alt="" width="661" height="578" srcset="https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped.jpg 661w, https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped-300x262.jpg 300w" sizes="(max-width: 661px) 100vw, 661px" />

3. From an elevated command prompt, run &#8220;vssadmin list writers&#8221; and look for any States or errors that look wrong like &#8220;offline&#8221; or similar.

  <img class="alignnone size-full wp-image-4642" src="https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped-2.jpg" alt="" width="736" height="517" srcset="https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped-2.jpg 736w, https://automationadmin.com/assets/images/uploads/2017/08/guestprocessingskipped-2-300x211.jpg 300w" sizes="(max-width: 736px) 100vw, 736px" />


