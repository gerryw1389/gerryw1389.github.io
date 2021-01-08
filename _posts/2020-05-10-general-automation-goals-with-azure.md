---
title: General Automation Goals With Azure
date: 2020-05-10T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/general-automation-goals-with-azure
categories:
  - WebSoftware
tags:
  - Cloud
---
<!--more-->

### Description:

The following is a general idea of how my team will attempt to use Azure for generic automation tasks.

### To Resolve:

1. A request will be sent from some application somewhere to an Event Grid Domain with a specific Event Subscription.
   - In order to set this up, create an Event Grid Domain => add an Event Grid Topic Subscription => Then go inside that and create a webhook that calls a Logic App. Note that the Logic App needs to be created first with a trigger of 'when a HTTP request is received' and an example json payload that would expect from Event Grid like:

   ```json
   [
   {
      "id": "REQ0246",
      "subject": "c09b47416-4bfd7e4c947",
      "topic": "testServiceNowPub",
      "eventType": "testServiceNow",
      "eventTime": "2019-05-21T18:41:00.9584103Z",
      "data": {
         "sysid": "956db97bcd4504f99eae9619e8",
         "number": "REQ02446",
         "u_ut_id": "1001544",
         "description": "test"},
      "dataVersion": "1.0",
      "metadataVersion": null
   }
   ]
   ```

   - After you paste in an example payload, it will generate the json schema and once you hit 'save' on the Logic App, it will give you the HTTP endpoint for Event Grid.

2. Based on the subject filter, the Event Grid Topic will call a Logic App via HTTP Webhook
   - In the example above, if I send a POST to my Event Grid Domain with the topic of `testServiceNowPub` and a subject of `c09b47416-4bfd7e4c947`, then Event Grid will automatically trigger my Logic App from the step above. I can do this from Postman first, but then I can do this from within Service Now for a Catalog Item workflow.

3. The Logic App will do one of the following:

   - First, try to complete the automation goal itself without calling anything except maybe another Logic App
   - Second, send to an Azure Function if `all` of the conditions are met:
     - Doesn't require fixed drives or shared File drives
     - Doesn't require specific source IP Address (for connecting to systems that whitelist a specific IP range)
     - Will be less than 10 minute runtime
   - Third/Last, send to Azure Automation Runbook (catch all - any automation not completed at this point will end up here):
     - Requires fixed drives or shared File drives
     - Needs specific source IP Address (for connecting to systems that whitelist a specific IP range)
     - Will be over than 10 minute runtime
