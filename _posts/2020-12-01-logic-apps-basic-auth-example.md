---
title: Logic Apps Basic Auth Example
date: 2020-12-01T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/logic-apps-basic-auth-example
tags:
  - Azure
tags:
  - Azure-LogicApps
---
<!--more-->

### Description:

In this example, I use Logic Apps to reach out to a Service Now instance using Basic Auth. This is kind of old as we use Oauth now, but the example can still be useful!

### To Resolve:

1. Source code is [here](https://github.com/gerryw1389/terraform-examples/tree/main/2020-12-01-logic-apps-basic-auth-example/basic-auth-example-read-sn/basic-auth-example-read-sn.json)

2. Be sure to find/replace for `double open brackets` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

3. Pics

   - ![basic-auth1](https://automationadmin.com/assets/images/uploads/2020/12/basic-auth1.jpg){:class="img-responsive"}

   - ![basic-auth-2](https://automationadmin.com/assets/images/uploads/2020/12/basic-auth-2.jpg){:class="img-responsive"}
