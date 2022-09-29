---
title: 'Logic Apps: Using Queue Messages For Tracking'
date: 2020-10-06T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/10/logic-apps-use-queue-messages-for-tracking
categories:
  - Azure
tags:
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

So if you have a chain of Logic Apps and you want to be able to track where they are in the chain, one method you can use is having each one write to a queue storage queue and then having the final Logic App clear it.

### To Resolve:

1. Source code is [here](https://github.com/gerryw1389/terraform-examples/tree/main/2020-10-06-logic-apps-use-queue-messages-for-tracking/queue-storage/queue-storage.json)

2. Be sure to find/replace for `double open brackets` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

3. Pics

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/queue1.jpg){:class="img-responsive"}

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/queue2.jpg){:class="img-responsive"}
