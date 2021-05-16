---
title: Setup NAT Gateway For Azure Functions
date: 2020-12-27T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/setup-nat-gateway-for-azure-functions
categories:
   - WebSoftware
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

3. Tie the Function App to the VNET:
   - Function App => Networking => VNET Integration => Configure => Add VNET/Subnet that has NAT GW
   - Verify that it can see the subnet by click on the subnet name which should show the NAT gateway as well
   - Force all outgoing traffic to go through the VNET by:
     - Go to configuration => New App Setting => `WEBSITE_VNET_ROUTE_ALL = 1`. This will force the traffic going to the internet to be routed through public IP address associated to the NAT Gateway.
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

4. Do your push to Github which should sync with Azure's Function App and then test with Postman. Did it work? Didn't for me, I didn't get any errors, but I ended up getting one of the IP's of the Function App instead of that of the Gateway.

5. I currently have a case open with Microsoft on this but my guess is that this will work fine for Windows App service plans and Windows Powershell functions like in the posts above. Reason for this assumption is that they seem to always support Windows things first and then python later...

   - For Troubleshooting:
   - At first, I had read something like mounting storage wasn't supported and I had done this in the past Per [docs](https://docs.microsoft.com/en-us/azure/azure-functions/scripts/functions-cli-mount-files-storage-linux):

   ```shell
   az webapp config storage-account add \
      --resource-group myResourceGroup \
      --name $functionAppName \
      --custom-id $shareId \
      --storage-type AzureFiles \
      --share-name $shareName \
      --account-name $AZURE_STORAGE_ACCOUNT \
      --mount-path $mountPath \
      --access-key $AZURE_STORAGE_KEY
   ```

   - So I deleted the storage by typing `az webapp config storage-account delete --custom-id CustomId --name MyWebApp --resource-group MyResourceGroup` per [docs](https://docs.microsoft.com/en-us/cli/azure/webapp/config/storage-account?view=azure-cli-latest#az_webapp_config_storage_account_delete), still didn't change anything, Function App was still displaying an IP in the list from the output of `az webapp show --resource-group MyResourceGroup --name MyWebApp --query outboundIpAddresses --output tsv` and not the NAT Gateway.

   - I deleted the NAT Gateway multiple times and recreated, no change
   - I deployed a new Function App, no change
   - Will update this if I have a resolution...
