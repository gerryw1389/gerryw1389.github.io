---
title: Logic Apps Loop MS Bookings Results
date: 2020-12-17T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/la-loop-bookings-results
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Scripting-RestAPI
---
<!--more-->

### Description:

In this example, my coworker developed a Logic App that will reach out to Microsoft Bookings and query Graph API to get a list of values. It then loops over and over and builds a JSON file that it eventually places in Azure Blob storage.

I think this is the first Logic App I have worked on that uses Oauth so that's neat!

### To Resolve:

1. Source code is [here](https://github.com/gerryw1389/terraform-examples/tree/main/logic-apps/oauth-example-loop-bookings-results/oauth-example-loop-bookings-results.json)

2. Be sure to find/replace for `double open brackets` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

3. Pics

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/booking1.jpg){:class="img-responsive"}

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/booking2.jpg){:class="img-responsive"}

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/booking3.jpg){:class="img-responsive"}
