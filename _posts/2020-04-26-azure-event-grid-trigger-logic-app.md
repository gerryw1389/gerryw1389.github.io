---
title: Azure Event Grid Trigger Logic App
date: 2020-04-26T08:06:24-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/azure-event-grid-trigger-logic-app
tags:
  - Azure
tags:
  - Orchestration
  - Azure-LogicApps
  - Azure-EventGrid
  - RestAPI
---
<!--more-->

### Description:

Having a runbook [run every minute](https://automationadmin.com//2020/04/azure-function-app-run-every-minute) in one way to automate things. But it just feels wrong. Why not make things event based instead? Well this is my first attempt at using Azure Event Grid to do just that.

### To Resolve:

1. Create a new Event Grid Domain:
   - Go to Event Grid Domains and create a new one `MyTestEG`
   - Note the endpoint it creates - `https://mytesteg.southcentralus-1.eventgrid.azure.net/api/events`

2. Create a new topic:
   - Go to Event Grid Topics and create a new one `MyTestTopic`
   - Add a new Event Subscription: `MyTestSubscription`
   - Have the subscription call a logic app: Paste in URL for HTTP webook
     - If you haven't already, create a logic app
     - Set its trigger to be `When a HTTP Request is Received`
     - Request body json: Paste in body (from next step): It generates json schema for you.
     - Now add a step to 'Send An Email (v2)' - have it send you an email so you can see when successful
     - Hit save
     - After it saves the first time, copy its `HTTP POST URL`

3. Send test payload:

   - First, go back to Event Grid Domains => MyTestEG => Access Keys => Copy the first key => Put in Keepass (optional)
   - It will be used in the header under `aeg-sas-key`

   - Headers:

   ```escape
   POST https://mytesteg.southcentralus-1.eventgrid.azure.net/api/events
   Content-Type: application/json
   aeg-sas-key: seekeepass
   Content-Type: text/plain
   ```

   - Body:

   ```escape
   [
   {
      "id": "REQ12345678",
      "subject": "someRequest",
      "topic": "myTestTopic",
      "eventType": "Service Now",
      "eventTime": "2019-02-13T18:41:00.9584103Z",
      "data": {
         "otherdata": "something"
         },
      "dataVersion": "1.0",
      "metadataVersion": null
   }
   ]
   ```

4. Did this trigger your logic app which resulted in an email to you (per step 2)? This may not work because I have removed my domain specific stuff and I know we got it working but it may not work since it's been sanitized - let me know in the comments.

5. So this is good and all, but we need a way to filter events in case we get more than a few of these. You can do this with `Subject filtering`:

   - Go back to Event Topics. Click `MyTestTopic` and `+ Event Subscription`
   - Name = TESTLogicApp
   - Event Schema: Event Grid Schema
   - Endpoint Type: Web Hook
   - Endpoint: (webhook from above)
   - Topic Type: Event Grid Domain
   - Topic Resource: MyTestEG
   - Domain Topic: MyTestTopic
   - Generate random guid from [https://guidgenerator.com/online-guid-generator.aspx](https://guidgenerator.com/online-guid-generator.aspx)
   - Filter tab = Check the box to enable subject filtering and choose 'subject begins with' and paste in '6a99c7e2-5dab-4036-b1fc-2a74b65967ef'
   - Save / Exit

6. Test from your machine using Postman
   - Headers: Same
   - Body:

   ```escape
   [
      {
         "id": "REQ12345678",
         "subject": "s6a99c7e2-5dab-4036-b1fc-2a74b65967ef",
         "topic": "myTestTopic",
         "eventType": "Service Now",
         "eventTime": "2019-02-13T18:41:00.9584103Z",
         "data": {
            "otherdata": "something"
            },
         "dataVersion": "1.0",
         "metadataVersion": null
      }
   ]
   ```
