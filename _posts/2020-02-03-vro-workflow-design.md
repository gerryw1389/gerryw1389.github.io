---
title: 'VRO: Workflow Design'
date: 2020-02-01T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/vro-workflow-design/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

Inside [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) when you build a workflow, there are a couple of things I have learned that make the job easier:

1. Keep a consistent name for variables and their respective Inventory [hosts and operations](https://automationadmin.com/2020/01/vro-add-rest-host-and-ops/)

2. Add default error handler elements and have them catch errors that your workflow throws:

   - So on the workflow schema, instead of your regular `Start => Scriptable Taks => End`, you will now have two rows:
   - Start => Scriptable Taks => End
   - Default error handler => Scriptable Taks => End
   - Pic:

   ![trap-error](https://automationadmin.com/assets/images/uploads/2020/02/trap-error.jpg){:class="img-responsive"}


### To Resolve

1. On the scripting element, add an output variable of "strError"

2. Then drag and drop a "Default error handler" element and choose "strError" as the default 'Output exception binding'

3. Drag and drop a new scriptable task and insert it between the error handler and the automatically placed 'end' element.

   - Make sure to bind "strError" to its input parameters.

   - In the scriptable task Scripting pane, type out:

   ```javascript
   //System.log("error is: " + strError)
   var strVerbiage = "Currently there are no requests in the queue"
   var strSplit = strError.split("(")
   var strErrorVerbiage = strSplit[0].trim();
   if (strErrorVerbiage == strVerbiage) {
      System.log("this error was trapped successfully")
   }
   else
   {
      System.log("this error was NOT trapped successfully: " + strErrorVerbiage)
   }
   ```

   - Make sure you have what you want `strVerbiage` to be in your main script as a `thow` statement. For example:

   ```javascript
   try {
      // This will cause the workflow to error when there are 0 tickets.
      var requestNumber = openRequests["result"][0]["number"]
      System.log("Request Number: " + requestNumber)
   }
   catch (e) {
      strError = "Currently there are no requests in the queue"
      throw "Currently there are no requests in the queue"
   }
   ```

4. Run the workflow again and you will see that it will throw an error, and then this element will still allow the workflow to complete successfully.


5. For making sure variables are consistent, I add keep a variables.md file that I reference and copy what is needed to the top of my workflows in a multiline comment:

   ```javascript
   /*

   Purpose: This workflow will connect to Service Now and parse new requests of a certain type, extract information, and send the information to software for approval. It then records this information for another workflow to pick up.

   Add Variables to workflow:
   { 
      "variable-name": "snGetRequest", 
      "type": "REST:RESTOperation", 
      "value": "SERVICE_NOW - getRequest: GET api/now/table/",
      "rest-host": "SERVICE_NOW: https://test.service-now.com/"
   }
   { 
      "variable-name": "snPutRequest", 
      "type": "REST:RESTOperation", 
      "value": "SERVICE_NOW - putRequest: PUT api/now/table/sc_request/", 
      "data-type": "application/json",
      "rest-host": "SERVICE_NOW: https://test.service-now.com/"
   }
   { 
      "variable-name": "softwareGetUserInfo", 
      "type": "REST:RESTOperation", 
      "value": "SOME_SOFTWARE - getSpecificUser: GET api/users?q={id}",
      "rest-host": "SOME_SOFTWARE: https://somehost.domain.com/"
   }
   { 
      "variable-name": "softwareGetRequests", 
      "type": "REST:RESTOperation", 
      "value": "SOME_SOFTWARE - getUserRequests: GET api/requests",
      "rest-host": "SOME_SOFTWARE: https://somehost.domain.com/"
   }
   { 
      "variable-name": "softwarePostToken", 
      "type": "REST:RESTOperation", 
      "value": "SOME_SOFTWARE - postToken: POST /api/oauth2/token", 
      "data-type": "application/x-www-form-urlencoded",
      "rest-host": "SOME_SOFTWARE: https://somehost.domain.com/"
   }
   { 
      "variable-name": "softwarePostRequest", 
      "type": "REST:RESTOperation", 
      "value": "SOME_SOFTWARE - postRequest: POST api/request", 
      "data-type": "application/json",
      "rest-host": "SOME_SOFTWARE: https://somehost.domain.com/"
   }
   { 
      "variable-name": "rscTask", 
      "type": "ResourceElement", 
      "value": "my-json-file.txt",
      "rest-host": "VRO_RESOURCE_ELEMENTS"
   }
   { 
      "variable-name": "softwarePostTokenRevoke", 
      "type": "REST:RESTOperation", 
      "value": "SOME_SOFTWARE - postTokenRevoke: POST /api/oauth2/revoke", 
      "data-type": "application/x-www-form-urlencoded",
      "rest-host": "SOME_SOFTWARE: https://somehost.domain.com/"
   }
   */
   ```

   - Each of these variables are added to the workflows variables tab and again in the scriptable tasks as input variables. They are then called in my javascript code to perform operations (REST API calls). Responses are usually stored and recorded in [its own json file](https://automationadmin.com/2020/01/vro-attachments/) and passed between workflows.