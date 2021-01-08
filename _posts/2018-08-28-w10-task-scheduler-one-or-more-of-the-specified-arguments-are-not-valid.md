---
title: 'W10 Task Scheduler: One or more of the specified arguments are not valid'
date: 2018-08-28T15:43:57+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/w10-task-scheduler-one-or-more-of-the-specified-arguments-are-not-valid/
categories:
  - Windows
---
<!--more-->

### Description:

I had an issue where if you have an account running under `domainName\Username` and changed something to an existing task, the Task Scheduler would throw up the error `One or more of the specified arguments are not valid`. This was particularly annoying because you could spend 10 minutes trying to find out what you did wrong.

### To Resolve:

1. The fix is to open the properties, go to the user it is running as, and point to the user in the directory again. In my case with went from `gerry` to `testlab.test\gerry` and it worked. It's like it needs to refresh the user who is running the task to have the `domainName\UserName` format.