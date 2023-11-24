---
title: Run Azure Functions Locally
date: 2021-04-21T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/04/functions-local/
tags:
  - Azure
tags:
  - Azure-FunctionApps
---
<!--more-->

### Description:

Here are the steps I did to test Azure functions locally following the [quickstart](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python).

### To Resolve:

1. Install the [Azure Core Tools](https://www.npmjs.com/package/azure-functions-core-tools)

2. Install the `Azure Functions` extension in VSCode

3. In Azure Functions blade in vscode, create a new project called 'my-http-test' inside a new folder in my workspace called 'local'.

4. Copy the module names from `requirements.txt` in my other function folder to local.

5. Copy the `__init__.py` from my other function to local. Press F5 to run in debug. This generates an error:

   ```powershell
   The terminal process "C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -Command .venv\Scripts\python -m pip install -r requirements.txt" terminated with exit code: 1.
   ```

   - The fix was to `cd` to the directory and then `./.venv/Scripts/activate` and then `pip install -r path/to/requirements.txt`

6. I tried the previous steps a few times and kept running into errors. What eventually fixed it was:

   - Using azure functions extension, create a new project under a new folder
   - Then, `cd` to the root directory in vscode and run `func host start`
   - Fix all errors until you get just a screen that says `http: [GET,POST] http://localhost:7071/api/http` replace `http` with your function name.

7. From here, you should be able to use Postman to send requests to your example function, except... environmental vars! Uggh... In Azure, these are setup per function app and contain secrets used to connect to Azure Key Vault. Instead, we will use `.env` files:

   - In the local project folder, in your `requirements.txt` add `python-dotenv==0.15.0`
   - Then in `helpers.py` add `from dotenv import load_dotenv` followed by `load_dotenv()` somewhere
   - Now create your `.env` file with environmental vars
   - Lastly, make sure `.env` is in your `.gitignore` or you risk exposing credentials! I also delete this file every day when I'm done testing just to be safe.
