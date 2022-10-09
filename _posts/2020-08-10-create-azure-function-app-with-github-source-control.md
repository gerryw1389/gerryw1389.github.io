---
title: Create Azure Function App With Github Source Control
date: 2020-08-10T11:10:16-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2020/08/create-azure-function-app-with-github-source-control
categories:
  - Azure
tags:
  - Cloud
  - Azure-FunctionApps
  - VersionControl
---
<!--more-->

### Description:

Follow this basic tutorial to setup an Azure Function with Github as the source control. Be advised that when you do this, almost all screens in the web UI will say 'View is set to Read Only since the App is in Source Control' or something of that nature.

### To Resolve:

1. In Github, Create a repo as a service account repo - not organization level called 'azure-function-http'

2. Create the following files but don't put any data in them just yet:

   - Repo name: azure-function-http
   - my-http-function
     - function.json
     - run.ps1
   - host.json
   - profile.ps1
   - requirements.psd1

   - Note: Make sure `my-http-function`, `host.json`, `profile.ps1`, and `requirements.psd1` are at the root of your repo or the next steps will fail!
   {: .notice--danger}

3. In azure: Create app service plan - Create app 'my-function-app' - Add function 'httptrigger1' and it will include some default powershell in `run.ps1`.

   - Test it by opening Postman and doing a post to your endpoint (which you get by clicking 'Get Function URL' under the function app in code view)

   - body of post:

   ```json
   {
   "name": "Gerry"
   }
   ```

   - response:
   - `Hello, Gerry. This HTTP triggered function executed successfully.`

4. In Azure, under the function app => Go to Source Control => Github => Sign in with your service account => Choose Kudo integration/build => Select your repo 'azure-function-http'

   - In Azure, go to App Files and copy/paste each of the contents to vscode locally. To get to `function.json`, you should go to your function and then hit the drop down under 'code/test' to see its contents.

   - After mirroring with the Web UI and your local vscode repo, do a push to Github.

   - Back in Azure, you should see the sync happen automatically. Now just make a small change:

   - I changed line 18 from:

   - `$body = "Hello, $name. This HTTP triggered function executed successfully."`
   - to:
   - `$body = "Hello, $name. Testing new response. This HTTP triggered function executed successfully."`
   - Commit and push

5. Back to Postman:

   - Body of post:

   ```json
   {
   "name": "Gerry"
   }
   ```

   - Response:
   - `Hello, Gerry. Testing new response. This HTTP triggered function executed successfully.`
