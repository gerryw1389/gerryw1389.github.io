---
title: Setup NAT Gateway For Azure Functions
date: 2020-12-27T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/setup-nat-gateway-for-azure-functions
categories:
   - Azure
tags:
   - Cloud
   - Azure-FunctionApps
   - Azure-NATGateways
   - Scripting-Python
---
<!--more-->

### Description:

In this post, I will setup a NAT Gateway and then connect my Function App (linux app Service Plan) to that gateway so that all outbound requests go through a single IP. I mostly followed [this post](https://notetoself.tech/2020/11/21/azure-functions-with-a-static-outbound-ip-address/) and the associated [Microsoft Blog post](https://azure.github.io/AppService/2020/11/15/web-app-nat-gateway.html).

### To Resolve:

1. Create a brand new resource group. Inside that resource group, create a VNET:
   - Create a `/24` address space and then create 4 `/26` subnets

2. Create NAT Gateway:
   - Create a public IP for it
   - Tie to one subnet
     - I selected this in the wizard but it didn't stick on creation. To fix just go to the gateway => Subnets => Assign to a subnet

3. Create a [Function App](https://automationadmin.com/2021/01/function-app-source-control-pt-2/) in Azure and set the source as Github.

   - Add `requests==2.25.0` to your `requirements.txt` Function App
   - Copy/paste the following into one of your functions `__init__.py` files:

   ```python
   #!/usr/bin/python3

   import sys
   import logging
   import azure.functions as func
   from . import helpers
   import os
   import time
   from datetime import datetime
   import json
   import requests

   def main(req: func.HttpRequest) -> func.HttpResponse:
      logging.info("Python HTTP trigger function processed a request.")

      url = "https://ifconfig.me/ip"
      payload = {}
      headers = {
      'Content-Type': 'application/json',
      }
      r = requests.request("GET", url, headers=headers, data=payload)
      
      response = r.text
      logging.info(f"Response: {response}")

      rspJson = json.dumps([{ 
               "response": response,
               "date_time": date 
      }])
      return func.HttpResponse(rspJson, status_code=200)

   if __name__ == '__main__':
      main(req)
   else:
      print("function not called correctly")
   ```

   - Push this to Github and it will sync with Azure.
   - Before binding with the gateway, do a test to get the public IP. You can do this in the portal by going to Function App => Functions => `get_ip` => Code/Test.
   - It should return with one of the IP's which are listed on Function App => Properties blade (Outbound IP addresses).

4. Tie the Function App to the VNET:
   - Function App => Networking => VNET Integration => Configure => Add VNET/Subnet that has NAT GW. Click on the subnets name and verify that is has the gateway listed as a NAT gateway.
   - Force all outgoing traffic to go through the VNET by:
     - Go to configuration => New App Setting => `WEBSITE_VNET_ROUTE_ALL = 1`. This will force the traffic going to the internet to be routed through public IP address associated to the NAT Gateway.

5. Test with Postman (or the Code/Test in the portal like before). Did it work? As of 2021-06-01 this is now working for me!

6. To verify we could use this as a way to transfer files, I also added in a response that will give me output of the files in a directory for a [mounted Azure File Share](https://automationadmin.com/2021/01/azure-functions-mounting-storage/). This worked as well. Code:

   ```python
   #!/usr/bin/python3

   ##################################################
   # This function will return the public ip of the function app

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

      url = "https://ifconfig.me/ip"
      payload = {}
      headers = {
      'Content-Type': 'application/json',
      }
      r = requests.request("GET", url, headers=headers, data=payload)
         
      response = r.text
      logging.info(f"Response: {response}")

      files_in_share = os.listdir("/data")
      logging.info(f"Files in mounted share: {files_in_share}")

      ### Response
      pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
      date = pastdate.strftime("%Y-%m-%d-%r")
      
      rspJson = json.dumps([{ 
               "response": response,
               "date_time": date,
               "files": files_in_share
      }])
      return func.HttpResponse(rspJson, status_code=200)

   if __name__ == '__main__':
      main(req)
   else:
      logging.error("Function not called correctly, please try again.")
   ```

   - I then get the expected response: `[{"response": "x.x.x.x (public ip of NAT Gateway)", "date_time": "2021-06-01-02:16:18 PM", "files": ["file1.csv", "file2.csv", "file3.csv"]}]`
