---
title: Azure Function Python HTTP Template
date: 2020-11-22T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/azure-function-python-http-template
tags:
  - Azure
tags:
  - Python
  - Azure-FunctionApps
---
<!--more-->

### Description:

So in one of the first steps to convert powershell functions to python functions, this is the basic Http Trigger template to use with Azure Functions that I came up with:

### To Resolve:

1. Scripts will be maintained [on Github](https://github.com/gerryw1389/python/tree/main/scripts/azure-function-template), but mainly if I send:

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

   - The endpoint responds back with:
  
   ```escape
   Hello, gerry.

   You chose mustang.

   Your birth city is fort worth in the state of Texas
   ```

2. What this template demonstrates is that I can send a two-level json payload and it can extract those into variables. In addition, I create a `helpers.py` that it will import so I can create functions in a separate file and have the main function and controller. This is huge! Can't wait to get started and expand on this!
