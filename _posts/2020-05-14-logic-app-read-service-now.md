---
title: 'Logic App: Read Service Now'
date: 2020-05-14T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/logic-app-read-service-now
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

So while working with Service Now developers to move to [an Event Based setup](https://automationadmin.com/2020/05/general-automation-goals-with-azure), I wrote a Logic App in the interim that scans Service Now for new requests every minute and calls an Azure Automation job if a new record was created. Here are the steps:


### To Resolve:

1. Trigger => Reoccurrence set to `1 week`, then `M-F` every minute between `8am and 5pm`

2. HTTP Action:
   - Method: GET
   - URI: (You will need to tweak this in Postman but the idea is filter on the short description. Example `https://yourcompany.service-now.com/api/now/table/sc_request?sysparm_query=short_description%3DSomething&sysparm_limit=10&state=1` this will get 'Something' with a state of 'New' from the request table.
   - Headers: Authorization (your authorization method)

3. Store the `Body` of the response in a variable named `Get-SNResponse`.

4. Initialize an integer variable with `0`

5. Store the length of the first variable in another variable `length(variables('Get-SNResponse'))`

6. Add a condition that if length is greater than `13`, call an automation job. Or as I did, have it increment the first integer variable and then create another condition that says if that variable is greater than 0, create an automation job - same thing.
