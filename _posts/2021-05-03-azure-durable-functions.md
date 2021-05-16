---
title: Azure Durable Functions
date: 2021-05-03T21:49:19-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2021/05/azure-durable-functions/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

This will be a post of me following along with [the quickstart](https://docs.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode#create-your-functions). Durable Functions are just like regular functions except they consist of three functions instead of one. Here are their roles:

- Orchestrator function - describes a workflow that orchestrates other functions.
- Activity function - called by the orchestrator function, performs work, and optionally returns a value.
- Client function - a regular Azure Function that starts an orchestrator function. This example uses an HTTP triggered function.

Note: You can see the code for this post at [my Github](https://github.com/gerryw1389/python/tree/main/scripts/azure-durable-functions-basic).

### To Resolve:

1. First, create a new project inside the `/dev` folder following [my local development post](https://automationadmin.com/2021/04/functions-local/) using the Azure Functions VSCode Extension.

2. Add `azure-functions-durable` to `requirements.txt` then install by running `.venv\scripts\activate` followed by `python -m pip install -r requirements.txt`.

3. Next, create each of the functions:

   - First, create a function using template 'Durable Functions orchestrator'. Called it `MyOrchestrator`.
   - Next, create a function using template 'Durable Functions activity'. Called it `MyActivity`.
   - Last, create a function using template 'Durable Functions HTTP starter'. Called it `MyHTTP`.

4. Now edit `MyOrchestrator` to call `MyActivity` instead of the default `Hello`

   ```python
   import logging
   import json
   import azure.functions as func
   import azure.durable_functions as df


   def orchestrator_function(context: df.DurableOrchestrationContext):
      result1 = yield context.call_activity('MyActivity', "Tokyo")
      result2 = yield context.call_activity('MyActivity', "Seattle")
      result3 = yield context.call_activity('MyActivity', "London")
      logging.info("completed!")
      return [result1, result2, result3]

   main = df.Orchestrator.create(orchestrator_function)
   ```

   - Also edit `MyHTTP` to add in logs to say it is starting:

   ```python
   import logging

   import azure.functions as func
   import azure.durable_functions as df


   async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
      client = df.DurableOrchestrationClient(starter)
      instance_id = await client.start_new(req.route_params["functionName"], None, None)

      logging.info("starting...")
      logging.info(f"Started orchestration with ID = '{instance_id}'.")


      return client.create_check_status_response(req, instance_id)
   ```

5. Edit `MyActivity` to import sleep and add a 3 minute pause. Since this will be called 3 times we ensure this bypasses Function App default 5 minute intervals.

   ```python
   import logging
   from time import sleep

   def main(name: str) -> str:
      logging.info("processing...")
      sleep(180)
      return f"Hello {name}!"
   ```

6. Edit logging in `host.json` to include our functions so that we can see the output of `logging.info()` statements:

   ```json
   {
      "version": "2.0",
      "logging": {
         "fileLoggingMode": "debugOnly",
         "logLevel": {
            "Function.MyActivity": "Information",
            "Function.MyHTTP": "Information",
            "Function.MyOrchestrator": "Information",
            "default": "None"
         },
         "applicationInsights": {
            "httpAutoCollectionOptions": {
               "enableHttpTriggerExtendedInfoCollection": true,
               "enableW3CDistributedTracing": true,
               "enableResponseHeaderInjection": true
            }
         }
      }
   }
   ```

7. Type `func start host`.
   - First it gave the error: `Missing value for AzureWebJobsStorage in local.settings.json. This is required for all triggers other than httptrigger, kafkatrigger. You can run 'func azure functionapp fetch-app-settings <functionAppName>' or specify a connection string in local.settings.json.`
   - So I went into one of my already running Function App settings and grabbed the `AzureWebJob` value and pasted it in like it said to. This is because durable functions need storage accounts to keep track of requests.
   - Now we trigger it through Postman by calling `http://localhost:7071/api/orchestrators/MyOrchestrator`
   - Grab its `statusQueryGetUri` or click on it. Either way, do a GET against it:

   ```json
   {
      "name": "MyOrchestrator",
      "instanceId": "c712394922604d48a474f851b5cb43ea",
      "runtimeStatus": "Running",
      "input": null,
      "customStatus": null,
      "output": null,
      "createdTime": "2021-05-07T12:51:54Z",
      "lastUpdatedTime": "2021-05-07T12:51:54Z"
   }
   ```

   - You can keep clicking Send in Postman against that GET URL a couple times until it finishes 9 minutes later.

   ```json
   {
      "name": "MyOrchestrator",
      "instanceId": "c712394922604d48a474f851b5cb43ea",
      "runtimeStatus": "Completed",
      "input": null,
      "customStatus": null,
      "output": [
         "Hello Tokyo!",
         "Hello Seattle!",
         "Hello London!"
      ],
      "createdTime": "2021-05-07T12:51:54Z",
      "lastUpdatedTime": "2021-05-07T13:00:56Z"
   }
   ```

   - Finally look at the logs and we see how it took 9 minutes to execute (see the processing statements at 51, 54, and 57?):

   ```escape
   [2021-05-07T12:51:47.357Z] Host lock lease acquired by instance ID '00000000000000000000000096ED6998'.
   [2021-05-07T12:51:54.452Z] Executing 'Functions.MyHTTP' (Reason='This function was programmatically called via the host APIs.', Id=bf10f167-c8e2-48d3-b0f0-d01bdcb2bff8)
   [2021-05-07T12:51:54.630Z] starting...
   [2021-05-07T12:51:54.633Z] Started orchestration with ID = 'c712394922604d48a474f851b5cb43ea'.
   [2021-05-07T12:51:54.679Z] Executed 'Functions.MyHTTP' (Succeeded, Id=bf10f167-c8e2-48d3-b0f0-d01bdcb2bff8, Duration=257ms)
   [2021-05-07T12:51:54.736Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=60a04ce5-4aa7-47c8-968a-57dd235844c2)
   [2021-05-07T12:51:54.809Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=60a04ce5-4aa7-47c8-968a-57dd235844c2, Duration=78ms)
   [2021-05-07T12:51:54.931Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=6823bec4-6098-4267-a272-bec27ba9f1fb)
   [2021-05-07T12:51:54.937Z] processing...
   [2021-05-07T12:54:54.940Z] Executed 'Functions.MyActivity' (Succeeded, Id=6823bec4-6098-4267-a272-bec27ba9f1fb, Duration=180011ms)
   [2021-05-07T12:54:55.310Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=a5681bf8-1ae1-417a-9bc0-d31c92f0d1cc)
   [2021-05-07T12:54:55.322Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=a5681bf8-1ae1-417a-9bc0-d31c92f0d1cc, Duration=14ms)
   [2021-05-07T12:54:55.391Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=4a5826e3-a285-4fed-9b07-1bb4414c71a8)
   [2021-05-07T12:54:55.396Z] processing...
   [2021-05-07T12:57:55.398Z] Executed 'Functions.MyActivity' (Succeeded, Id=4a5826e3-a285-4fed-9b07-1bb4414c71a8, Duration=180006ms)
   [2021-05-07T12:57:55.798Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=e31b5b4f-5c5f-4e2a-806e-12a360f5ffd4)
   [2021-05-07T12:57:55.808Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=e31b5b4f-5c5f-4e2a-806e-12a360f5ffd4, Duration=12ms)
   [2021-05-07T12:57:55.880Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=7ab3a58f-b143-443d-90a3-57b84e86fbb5)
   [2021-05-07T12:57:55.886Z] processing...
   [2021-05-07T13:00:55.888Z] Executed 'Functions.MyActivity' (Succeeded, Id=7ab3a58f-b143-443d-90a3-57b84e86fbb5, Duration=180008ms)
   [2021-05-07T13:00:56.250Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=7b7eefdc-65f0-4014-96e3-c388a5c61efc)
   [2021-05-07T13:00:56.262Z] completed!
   [2021-05-07T13:00:56.270Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=7b7eefdc-65f0-4014-96e3-c388a5c61efc, Duration=21ms)
   ```

8. Now let's see what happens if we do one step, but make it 10 minutes long.

   - First, edit `MyOrchestrator` to look like this:

   ```python
   import logging
   import json

   import azure.functions as func
   import azure.durable_functions as df


   def orchestrator_function(context: df.DurableOrchestrationContext):
      result1 = yield context.call_activity('MyActivity', "Tokyo")
      result2 = 'blah2'
      result3 = 'blah3'
      #result2 = yield context.call_activity('MyActivity', "Seattle")
      #result3 = yield context.call_activity('MyActivity', "London")
      logging.info("completed!")
      return [result1, result2, result3]

   main = df.Orchestrator.create(orchestrator_function)
   ```

   - Then edit `MyActivity` to pause for 10 minutes instead of 3

   ```python
   import logging
   from time import sleep

   def main(name: str) -> str:
      logging.info("processing...")
      sleep(600)
      return f"Hello {name}!"
   ```

   - Now run it

   ```json
   {
      "name": "MyOrchestrator",
      "instanceId": "4ed961d7558a4dad9a36001f19f542da",
      "runtimeStatus": "Running",
      "input": null,
      "customStatus": null,
      "output": null,
      "createdTime": "2021-05-06T22:05:02Z",
      "lastUpdatedTime": "2021-05-06T22:05:02Z"
   }
   ```

   - Looks good. Let's wait again.

   ```json
   {
      "name": "MyOrchestrator",
      "instanceId": "4ed961d7558a4dad9a36001f19f542da",
      "runtimeStatus": "Completed",
      "input": null,
      "customStatus": null,
      "output": [
         "Hello Tokyo!",
         "blah2",
         "blah3"
      ],
      "createdTime": "2021-05-06T22:05:02Z",
      "lastUpdatedTime": "2021-05-06T22:15:07Z"
   }
   ```

   - Nice, one step and it took 10 minutes! Let's check the logs:

   ```escape
   [2021-05-06T22:05:02.304Z] Executing 'Functions.MyHTTP' (Reason='This function was programmatically called via the host APIs.', Id=464c8589-20a0-48b5-93c7-a76b372c2607)
   [2021-05-06T22:05:02.487Z] starting...
   [2021-05-06T22:05:02.491Z] Started orchestration with ID = '4ed961d7558a4dad9a36001f19f542da'.
   [2021-05-06T22:05:02.496Z] Executed 'Functions.MyHTTP' (Succeeded, Id=464c8589-20a0-48b5-93c7-a76b372c2607, Duration=192ms)
   [2021-05-06T22:05:05.803Z] Host lock lease acquired by instance ID '00000000000000000000000096ED6998'.
   [2021-05-06T22:05:06.956Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=049f9e11-704d-47f9-80e3-a58fa124dc1f)
   [2021-05-06T22:05:06.990Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=049f9e11-704d-47f9-80e3-a58fa124dc1f, Duration=36ms)
   [2021-05-06T22:05:07.092Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=08c054f0-3822-4b0c-9482-aa90a434e51a)
   [2021-05-06T22:05:07.098Z] processing...
   [2021-05-06T22:15:07.101Z] Executed 'Functions.MyActivity' (Succeeded, Id=08c054f0-3822-4b0c-9482-aa90a434e51a, Duration=600010ms)
   [2021-05-06T22:15:07.456Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=6d783445-bafa-4624-9838-3d738c0cde26)
   [2021-05-06T22:15:07.467Z] completed!
   [2021-05-06T22:15:07.479Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=6d783445-bafa-4624-9838-3d738c0cde26, Duration=25ms)
   ```

9. Now let's see what happens if we do 3 steps, but pass in a `dict` object instead of string.

   - First, edit `MyOrchestrator` to look like this:

   ```python
   import logging
   import json

   import azure.functions as func
   import azure.durable_functions as df


   def orchestrator_function(context: df.DurableOrchestrationContext):

      name = { "firstname": "Darth", "lastname": "Vader"}
      employee = {
      'name': {
         'firstname': 'Darth',
         'lastname': 'Vader'
         },
      'dateofjoining': {
         'day': 1,
         'month': 5,
         'year': 2017
         }
      }


      result1 = yield context.call_activity('MyActivity', name)
      #result2 = 'blah2'
      #result3 = 'blah3'
      result2 = yield context.call_activity('MyActivity', employee)
      result3 = yield context.call_activity('MyActivity', employee["dateofjoining"])
      logging.info("completed!")
      return [result1, result2, result3]

   main = df.Orchestrator.create(orchestrator_function)
   ```

   - Then edit `MyActivity` to accept input of type `dict` and return a type of `dict`

   ```python
   import logging
   from time import sleep

   def main(name: dict) -> dict:
      logging.info("processing...")
      sleep(1)
      return f"Dict: {name}!"
   ```

   - Now run it. No need to wait since it will do 3 iterations one second each

   ```json
   {
      "name": "MyOrchestrator",
      "instanceId": "5cfebaf36ba848dd8b6d70adeb7b7979",
      "runtimeStatus": "Completed",
      "input": null,
      "customStatus": null,
      "output": [
         "Dict: {'firstname': 'Darth', 'lastname': 'Vader'}!",
         "Dict: {'name': {'firstname': 'Darth', 'lastname': 'Vader'}, 'dateofjoining': {'day': 1, 'month': 5, 'year': 2017}}!",
         "Dict: {'day': 1, 'month': 5, 'year': 2017}!"
      ],
      "createdTime": "2021-05-07T13:12:29Z",
      "lastUpdatedTime": "2021-05-07T13:12:33Z"
   }
   ```

   - Logs:

   ```escape
   [2021-05-07T13:12:29.629Z] Executed 'Functions.MyHTTP' (Succeeded, Id=6ec469fd-b2db-4b01-90f5-f9e43af3c4f0, Duration=262ms)
   [2021-05-07T13:12:29.953Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=59ccd413-7010-4d50-b104-409e823940fd)
   [2021-05-07T13:12:29.994Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=59ccd413-7010-4d50-b104-409e823940fd, Duration=48ms)
   [2021-05-07T13:12:30.093Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=338277bc-7ceb-48ae-8b0a-b826d996b9f5)
   [2021-05-07T13:12:30.099Z] processing...
   [2021-05-07T13:12:31.110Z] Executed 'Functions.MyActivity' (Succeeded, Id=338277bc-7ceb-48ae-8b0a-b826d996b9f5, Duration=1019ms)
   [2021-05-07T13:12:31.260Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=e91cd494-4f90-4561-b940-7d04d5598eec)
   [2021-05-07T13:12:31.275Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=e91cd494-4f90-4561-b940-7d04d5598eec, Duration=16ms)
   [2021-05-07T13:12:31.344Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=75037eb1-1ac4-4d7c-9df5-20479ac41b2a)
   [2021-05-07T13:12:31.353Z] processing...
   [2021-05-07T13:12:32.360Z] Executed 'Functions.MyActivity' (Succeeded, Id=75037eb1-1ac4-4d7c-9df5-20479ac41b2a, Duration=1015ms)
   [2021-05-07T13:12:32.536Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=e76d8f7d-ff82-4b42-abad-31be37dfbfe6)
   [2021-05-07T13:12:32.548Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=e76d8f7d-ff82-4b42-abad-31be37dfbfe6, Duration=12ms)
   [2021-05-07T13:12:32.616Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=948cdc07-6b02-4be7-b556-7ba261ef8782)
   [2021-05-07T13:12:32.622Z] processing...
   [2021-05-07T13:12:33.629Z] Executed 'Functions.MyActivity' (Succeeded, Id=948cdc07-6b02-4be7-b556-7ba261ef8782, Duration=1013ms)
   [2021-05-07T13:12:33.759Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=bc478630-de35-4483-84ec-77009a12a895)
   [2021-05-07T13:12:33.769Z] completed!
   [2021-05-07T13:12:33.776Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=bc478630-de35-4483-84ec-77009a12a895, Duration=17ms)
   ```

   - What have we learned?
     - Passing `name = { "firstname": "Darth", "lastname": "Vader"}` to the Activity function results in `"Dict: {'firstname': 'Darth', 'lastname': 'Vader'}!",`
     - Passing `employee = { 'name': { 'firstname': 'Darth', 'lastname': 'Vader' }, 'dateofjoining': { 'day': 1, 'month': 5, 'year': 2017 } }` results in `"Dict: {'name': {'firstname': 'Darth', 'lastname': 'Vader'}, 'dateofjoining': {'day': 1, 'month': 5, 'year': 2017}}!",`
     - Finally, passing `employee["dateofjoining"]` results in `"Dict: {'day': 1, 'month': 5, 'year': 2017}!"`
     - Since all my HTTP functions receive JSON payloads and return JSON payloads, this is almost all I need for now. Last thing is to see if we can get the json payload from the body of the HTTP trigger from the user when they call `MyHTTP`.

10. Now let's see what happens if we pass in a `dict` in the initial call and pass it along to the Activity function.

    - So, first, I'm going to pass in the following payload to my function

    ```python
    import requests
    import json

    url = "http://localhost:7071/api/orchestrators/MyOrchestrator"

    payload = json.dumps({
    "firstname": "Darth",
    "lastname": "Vader"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    ```

    - To capture this, I need to edit my `MyHTTP` function like so:

    ```python
    import logging

    import azure.functions as func
    import azure.durable_functions as df


    async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
      
      req_body = req.get_json()
      #logging.info(f"Request body as json: {req_body}")

      first_name = req_body["firstname"]
      logging.info(f"Extracted First Name: {first_name}")

      last_name = req_body["lastname"]
      logging.info(f"Extracted Lastname: {last_name}")

      payload = {
         "first_name" : first_name,
         "last_name" : last_name
      }

      client = df.DurableOrchestrationClient(starter)
      instance_id = await client.start_new(req.route_params["functionName"], None, payload)

      logging.info("starting...")
      logging.info(f"Started orchestration with ID = '{instance_id}'.")


      return client.create_check_status_response(req, instance_id)
    ```

    - How did I know to pass `payload` as the third param? I read [the docs](https://docs.microsoft.com/en-us/python/api/azure-functions-durable/azure.durable_functions.durableorchestrationclient?view=azure-python#start-new-orchestration-function-name--str--instance-id--typing-union-str--nonetype----none--client-input--typing-union-typing-any--nonetype----none-----str)

    - Next, edit `MyOrchestrator` to look like this:

    ```python
    import logging
    import json

    import azure.functions as func
    import azure.durable_functions as df


    def orchestrator_function(context: df.DurableOrchestrationContext):

    input = context.get_input()
    payload = dict(input)
    result1 = yield context.call_activity('MyActivity', payload)
    result2 = yield context.call_activity('MyActivity', payload)
    result3 = yield context.call_activity('MyActivity', payload)
    logging.info("completed!")
    return [result1, result2, result3]

    main = df.Orchestrator.create(orchestrator_function)
    ```

    - How did I know to get the payload `context.get_input()` as the input param? I read [the docs](https://docs.microsoft.com/en-us/python/api/azure-functions-durable/azure.durable_functions.durableorchestrationcontext?view=azure-python#get-input------typing-union-typing-any--nonetype-)

    - Then edit `MyActivity` to accept input of type `dict` and return a type of `dict`

    ```python
    import logging
    from time import sleep

    def main(name: dict) -> dict:
    logging.info("processing...")
    sleep(1)
    return f"Dict: {name}!"
    ```

    - Now run it. No need to wait since it will do 3 iterations one second each

    ```json
    {
    "name": "MyOrchestrator",
    "instanceId": "c37f9889f28442d98bf7a29faa4415ce",
    "runtimeStatus": "Completed",
    "input": "{\"first_name\": \"Darth\", \"last_name\": \"Vader\"}",
    "customStatus": null,
    "output": [
      "Dict: {'first_name': 'Darth', 'last_name': 'Vader'}!",
      "Dict: {'first_name': 'Darth', 'last_name': 'Vader'}!",
      "Dict: {'first_name': 'Darth', 'last_name': 'Vader'}!"
    ],
    "createdTime": "2021-05-07T13:43:31Z",
    "lastUpdatedTime": "2021-05-07T13:43:36Z"
    }
    ```

    - Logs:

    ```escape
    [2021-05-07T13:43:31.812Z] Executing 'Functions.MyHTTP' (Reason='This function was programmatically called via the host APIs.', Id=c4c4a50e-6e26-49f5-9081-4f9438c512ae)
    [2021-05-07T13:43:31.821Z] Extracted First Name: Darth
    [2021-05-07T13:43:31.823Z] Extracted Lastname: Vader
    [2021-05-07T13:43:32.125Z] starting...
    [2021-05-07T13:43:32.129Z] Started orchestration with ID = 'c37f9889f28442d98bf7a29faa4415ce'.
    [2021-05-07T13:43:32.131Z] Executed 'Functions.MyHTTP' (Succeeded, Id=c4c4a50e-6e26-49f5-9081-4f9438c512ae, Duration=319ms)
    [2021-05-07T13:43:32.157Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=71f9937f-1cd9-4e64-bf4f-ebd5ec0c074a)       
    [2021-05-07T13:43:32.163Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=71f9937f-1cd9-4e64-bf4f-ebd5ec0c074a, Duration=6ms)
    [2021-05-07T13:43:32.455Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=5409e172-3074-4d2b-8788-5f2c8e5355c5)
    [2021-05-07T13:43:32.460Z] processing...
    [2021-05-07T13:43:33.462Z] Executed 'Functions.MyActivity' (Succeeded, Id=5409e172-3074-4d2b-8788-5f2c8e5355c5, Duration=1007ms)
    [2021-05-07T13:43:33.593Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=c849d364-d8a7-4947-99f2-ad59857cd877)       
    [2021-05-07T13:43:33.601Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=c849d364-d8a7-4947-99f2-ad59857cd877, Duration=8ms)
    [2021-05-07T13:43:33.669Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=bcb9d51d-4387-4614-8a0c-dc1f70607655)
    [2021-05-07T13:43:33.674Z] processing...
    [2021-05-07T13:43:34.680Z] Executed 'Functions.MyActivity' (Succeeded, Id=bcb9d51d-4387-4614-8a0c-dc1f70607655, Duration=1011ms)
    [2021-05-07T13:43:34.865Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=bb625d76-3ad5-4078-ba5e-0db7a8fd24fd)
    [2021-05-07T13:43:34.875Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=bb625d76-3ad5-4078-ba5e-0db7a8fd24fd, Duration=9ms)
    [2021-05-07T13:43:34.941Z] Executing 'Functions.MyActivity' (Reason='(null)', Id=62032eb3-4791-4c44-8c07-910b8039a943)
    [2021-05-07T13:43:34.948Z] processing...
    [2021-05-07T13:43:35.950Z] Executed 'Functions.MyActivity' (Succeeded, Id=62032eb3-4791-4c44-8c07-910b8039a943, Duration=1008ms)
    [2021-05-07T13:43:36.079Z] Executing 'Functions.MyOrchestrator' (Reason='(null)', Id=ef56cbbd-f1b9-4352-993e-69525c800967)
    [2021-05-07T13:43:36.088Z] completed!
    [2021-05-07T13:43:36.091Z] Executed 'Functions.MyOrchestrator' (Succeeded, Id=ef56cbbd-f1b9-4352-993e-69525c800967, Duration=12ms)
    ```

    - One more thing, let's change `name` to `payload` by updating the `function.json` associated with the function:

    ```json
    {
    "scriptFile": "__init__.py",
    "bindings": [
      {
         "name": "payload",
         "type": "activityTrigger",
         "direction": "in"
      }
    ]
    }
    ```

    - Now we can update our passed in param name:

    ```python
    import logging
    from time import sleep

    def main(payload: dict) -> dict:
    logging.info("processing...")
    sleep(1)
    return f"Dict: {payload}!"
    ```

    - What have we learned?
      - I can now pass in a JSON payload and have the function process the data. This is all I need for now. Will update later with more stuff.

11. Lastly, I just follow my post on [creating a Function App](https://automationadmin.com/2021/01/function-app-source-control-pt-2/)
