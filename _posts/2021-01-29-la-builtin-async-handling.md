---
title: Logic App Builtin Async Handling
date: 2021-01-29T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/la-builtin-async-handling/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

Follow this guide to create Wrapper Logic Apps to introduce [Async communications](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply#solution) for Azure Functions.

UPDATE 2021-05: I would skip this post and read about [my Durable Functions post](https://automationadmin.com/2021/05/azure-durable-functions) instead. I feel like this may work but it was back when I was first trying to solve a problem I have recently solved with Durable Functions so I would just do that instead. Keeping this here in case someone would rather do this.

### To Resolve:

1. Create a [Function App](https://automationadmin.com/2020/11/azure-function-python-http-template) in python with a `time.sleep(6)`, call it `sleep`

   - Using the template [here](https://github.com/gerryw1389/python/blob/main/scripts/azure-function-template/ReadJSON/__init__.py), add a line before the return that sleeps the app for a few seconds.

2. Create a logic app called `Async`

   - Trigger = Http request
   - Json structure = Paste in the same as the function app, in my case:

   ```json
   {
      "name": "gerry",
      "car": "mustang",
      "birth": {
      "city": "fort worth",
      "state": "Texas"
      }
   }
   ```

   - Action: Function App
     - Request body: `$body` from trigger

   - Action: Response
     - Status Code = 200
     - Headers: Content-Type - application/json
     - Body: `$body` from function `sleep`
   - On the Response action, select the ellipses to go to Settings. Turn `Asynchronous Response` toggle to on.

3. Create a logic app called `Controller`

   - Trigger = Reoccurance to whenever you want
   - Action: Logic App => Async
     - The inputs will auto show up as `city`, `state`, `car`, and `name`. Just fill them in with dummy data.

4. Run and you will get a response! It should take 6 seconds if you did `time.sleep(6)` in step 1. This proves that you can wrap a Logic App around a semi-long running Function App and take advantage of Async HTTP. I have not tested if this goes beyond the [3.9 minutes which will cause it to fail](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-limits-and-config?tabs=azure-portal#http-request-limits).

   ```json
   [
      {
      "response": "Hello, gerry.\n\nYou chose dodge.\n\nYour birth city is fort worth in the state of tx",
      "date_time": "2020-12-09-21-13-26"
      }
   ]
   ```
