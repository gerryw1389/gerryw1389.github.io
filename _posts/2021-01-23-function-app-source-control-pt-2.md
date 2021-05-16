---
title: Azure Function App With Github Source Control Pt 2
date: 2021-01-23T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/function-app-source-control-pt-2/
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

As a continuation of my [original post](https://automationadmin.com/2020/08/create-azure-function-app-with-github-source-control), this is the steps I do to create a Function App these days. Note: You can see the code for this post at [my Github](https://github.com/gerryw1389/python/tree/main/scripts/azure-function-template-basic).

### To Resolve:

1. First, we have completely went with [Python HTTP](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#http-trigger-and-bindings) as the main Function Apps and nixed Powershell Core.

   - We currently have a single Linux App Service plan P2 that we can bind all new Function Apps to as long as they are Python.

2. The way I develop a Function App is that I start with a template folder like the one I have [on Github](https://github.com/gerryw1389/python/tree/main/scripts/azure-function-template)

   - I first replace the three `READJSON` functions with something easier like:

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

      ### Response
      pastdate = datetime.now() + timedelta(days=0,  hours=-6, minutes=0)
      date = pastdate.strftime("%Y-%m-%d-%r")
      
      rspJson = json.dumps([{ 
               "response": response,
               "date_time": date 
      }])
      return func.HttpResponse(rspJson, status_code=200)

   if __name__ == '__main__':
      main(req)
   else:
      logging.error("Function not called correctly, please try again.")
   ```

   - Note that this Function App doesn't have any input passed in, but if you want just add in:

   ```python
   req_body = req.get_json()

   description = req_body["description"]
   logging.info(f"Extracted description: {description}")
   ```

   - Just replace `description` with whatever JSON key is passed in.

   - And the return this Function App returns is:

   ```python
   rspJson = json.dumps([{ 
      "response": response,
      "date_time": date 
   }])
   ```

3. Once I develop the python script, I rename the folder `READJSON` to the name of the function, like `get_ip` in this case
   - I then modify `host.json` (in the root of the Function App directory) to say `"Function.get_ip": "Information",` instead of `"Function.ReadJSON.User": "Warning",` for instance so that I can get logging in Log Analytics (see below).

4. I then push this to my organization level repo in Github. Keep in mind that at this point it is not in Azure in any way.

5. Next, in Azure, deploy a new Python 3.8 App.

   - Set source as Github
   - Under Organization, choose your organization. This should pop up a separate Window where you link your Github to Azure through an Oauth app called 'Azure App Service' or something.
     - To get Github integration with your Github organization, sign in to Github and go to Settings => Applications => Oauth Apps => Azure App Service => Request access to organization.
     - After our Github Organization owner approved, I had to do the following to get access in Azure:
     - In the Function App blade in Azure => Go to IAM => Roles => Contributor => Add => My email account. This is different than the privileged account I use for Azure access.
     - If I sign in on a new Firefox container with my email account I can see the Function App.
     - Now go to Deployment Center => Github => Authorize. This should bring up a window that will authorize with Github and should disappear quickly giving you the option to now choose your organization and the repo you just created.
     - Now, from your machine, make a change and push it to the repo. Then see if it notices the change in the Function App. Should work!
   - Point to repo and branch. Note that if your organization's repo doesn't show up, try changing the Python version one or two down and it might just magically find your Github repos (had this happen before)
   - If you get this far, great! At this point you have a Function App in source control which is the goal. Now lets do some optional stuff...

6. One optional thing you can do at this point is modify your app to [mount a file share from an Azure Storage Account](https://automationadmin.com/2021/01/azure-functions-mounting-storage) if needed.

7. Another thing I do for all Function Apps is set certain environmental variables inside `Configuration` blade in Azure in order to [access secrets](https://automationadmin.com/2021/01//2021/01/function-apps-get-secrets/)

8. Under `Diagnostics` blade, send their logs to a Log Analytics Workspace. This is mandatory to get the logs for the apps. You can have App Insights forward logs there as well by clicking on the `Properties` blade under App Insights and pointing to your Log Analytics workspace.

9. Optionally, at this point you can import the Function App as an API inside API Management and give it a friendly URL for users to point to.
   - Go to API Management => API’s => Right click one if you already have one => Import => Function Apps => Select the name of our new function, `get_ip`
   - Now, in Logic Apps, just create two actions to call the API Management instance:
     - Azure Keyvault => Get Secret => get the `Ocp-Apim-Subscription-Key` value
     - HTTP => POST => https://`your-instance`.azure-api.net/`your-function-app`/`your-function`
     - Make sure to put the value of the secret as the value in the value field
     - ![logic-app-http-with-api-mgmt](https://automationadmin.com/assets/images/uploads/2021/01/la-http-action.png){:class="img-responsive"}

10. Optionally, have Logic Apps call that API Management endpoint from the previous step. Likewise, you can bypass API Management and call the Function App directly from Logic Apps or many other automation tools.
