---
title: Function Apps With Logic Apps
date: 2021-01-19T21:49:19-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/function-apps-with-logic-apps/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
  - Azure-FunctionApps
  - Scripting-Python
---
<!--more-->

### Description:

Azure Function Apps are completely serverless bits of code that you can run. Lately, we have been having Logic Apps pass JSON payloads to Function Apps, have them process something, and return a different payload back to the Logic App and then using a 'condition' action to check the response. To top it off, this can all be integrated with Azure API Management.

### To Resolve:

1. For example, let's first develop a Function App:

   ```python
   #!/usr/bin/python3

   ##################################################
   # This function will return a parsed description from a passed in string
   # {
   #    "description": "something"
   # }

   ##################################################

   import sys
   import logging
   import azure.functions as func
   import os
   import time
   from datetime import datetime, timedelta
   import json
   import requests

   def main(req: func.HttpRequest) -> func.HttpResponse:

      req_body = req.get_json()

      description = req_body["description"]
      logging.info(f"Extracted description: {description}")

      splitDesc = description.split("\n")
      
      split_list = [x.strip() for x in splitDesc[8].split(":")[1].split(',')]
      logging.info(f"Extracted split list: {split_list}")

      department = splitDesc[3].split(":")[1].strip()
      logging.info(f"Extracted department: {department}")

      split_list_string = ','.join(split_list)

      ### Response
      pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
      date = pastdate.strftime("%Y-%m-%d-%r")
      

      rspJson = json.dumps([{ 
               "serial_numbers": split_list_string,
               "department": department,
               "date_time": date 
      }])
      return func.HttpResponse(rspJson, status_code=200)

   if __name__ == '__main__':
      main(req)
   else:
      logging.error("Function not called correctly, please try again.")
   ```

   - Note the input for the Function App is:

   ```python
   req_body = req.get_json()

   description = req_body["description"]
   logging.info(f"Extracted description: {description}")
   ```

   - And the return is:

   ```python
   rspJson = json.dumps([{ 
      "serial_numbers": split_list_string,
      "department": department,
      "date_time": date 
   }])
   ```

2. We can then develop a Logic App with a HTTP Trigger that will call this function and pass in the description as a variable from whatever calls the Logic App.

3. You can optionally import your Function App into [Azure API Management](https://automationadmin.com/2020/08/azure-api-management)

   - What you can do is add the action `Get Secret` which will reach out to Azure Keyvault and get the `Ocp-Apim-Subscription-Key` value
   - Then add a `HTTP` action that calls your API Management endpoint which calls your Function App.
   - Why do this? Central point of API calls for example or maybe you have logging enabled on API Management and track things there. Dunno, we just wanted to centralize API calls from various automation tools.

4. So at this point, you can build a domino affect:

   - You can use Postman on your machine to pass a json payload to the logic app that contains a `description` key.
   - The Logic App can pass that to API Management
   - API Management can pass that to a Function App
   - Function App can respond with some data
   - That response gets sent back to Logic App
   - Logic App can parse that response and send it back to your Postman client directly or come up with its own Response using the `Response` action that is mandatory with HTTP Triggers.
   - You could even add a layer replacing your Postman which could be an Event Grid Event, Service Bus Message, or another Logic App but let's not get too carried away.

5. So what's the point of all this? Well the main thing is we are still learning on how everything fits in the big picture but the idea is that:

   - API Management and Event Grid are event based triggers for Logic Apps.
   - Logic Apps themselves can have reoccurrence triggers or HTTP triggers.
   - Each of these can call Function Apps that will parse JSON payloads and respond back to the calling Logic App usually in sub-second time frames.
   - Much faster than [Azure Automation](https://automationadmin.com/2020/10/using-azure-automation-logic-apps-for-sftp) which is what we were currently using.
