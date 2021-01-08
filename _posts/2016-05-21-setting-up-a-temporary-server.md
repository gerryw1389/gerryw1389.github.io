---
title: Setting Up A Temporary Server
date: 2016-05-21T23:05:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-a-temporary-server/
categories:
  - WindowsServer
tags:
  - Setup
---
<!--more-->

### Description:

If you have an application that is ran from the server for the network and the server crashes for any reason, sometimes you may need to setup a &#8220;Temporary Server&#8221; until the real server gets repaired or replaced. In a smaller network, you might be able to get away with doing this on a workstation.

### To Resolve:

1. First figure out, is it worth the effort? Most of the time it isn't. If you run on a SQL DB then it could take hours, on the other hand, if you are using a flat file system, this could be fairly quick. The only time its really appropriate is if your server went down and you are not getting it replaced for a couple weeks.

2. Look at your most recent backup- What's the last modified date? Try to run one if possible. Make sure to understand that once you restore from a backup, there is no going back. This is due to database conflicts that can arise.

3. Restore the relevant database to another workstation. Doesn't matter which one, but look for a W7 workstation, XP has a limit of 10 computers that can map drives to a shared folder from it.

4. Point all software to the new location if it's a network application.

5. Share out the database by placing it in a shared folder or drive partition if you have one. Set the permissions to how the server had them. If you have specific users in specific groups, set those up. I typically allow Full Control to Everyone at the share level and the restrict at the NTFS level by AD security groups.

6. Map a network drive on all the computers to the new temp server. Don't delete the original mapped drives for when the server does come back. See [Mapped Network Drive Issues](https://automationadmin.com/2016/05/mapped-network-drives-issues/) for how to do this.