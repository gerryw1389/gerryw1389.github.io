---
title: 'VRO: Read/Write Service Now'
date: 2020-01-20T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-read-write-service-now/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

I use the following snippets to have [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) connect to Service Now and perform read and write operations.

### To Resolve

1. So let's pretend you have a workflow you want to run every minute that scans Service Now for a certain Catalog Item response. First you would [add your ServiceNow REST HOST and add the GET operation](https://automationadmin.com/2020/01/vro-add-rest-host-and-ops/) to VRO's inventory.

2. You would then add the rest operations for Service Now as variables to your workflow. We will add `snGetRequest` and `snPutRequest` to an example workflow.

3. Then, pull over a scripting element and add them as 'inputs' to the script. Now paste in:

   ```javascript
   function restAPICall(restOperation, content, defaultContentType, acceptHeaders, urlTemplateCustom) {
      System.log("==========Generic Rest API call==========");
      var inParamtersValues = [];
      var headerParams = [];
      var acceptHeadersValue = "";
      restOperation.urlTemplate = urlTemplateCustom;
      System.log(restOperation.getHeaderParameters());
      var request = restOperation.createRequest(inParamtersValues, content);
      //set the request content type
      if (System.getModule("com.vmware.library.http-rest.configuration").hasHttpMethodHasBodyPayload(request.getMethod())) {
         System.log("Setting defaut content type to:  " + defaultContentType);
         request.contentType = defaultContentType;
      }
      var headerParamNames = restOperation.getHeaderParameters();
      //System.log(" acceptHeaders " + acceptHeaders );
      if (acceptHeaders && acceptHeaders.length > 0) {
         for (var k in acceptHeaders) {
            acceptHeadersValue = acceptHeadersValue + acceptHeaders[k] + ",";
         }
         var acceptHeadersStringSize = acceptHeadersValue.length - 1;
         acceptHeadersValue = acceptHeadersValue.substring(0, acceptHeadersStringSize);

      }
      for (var k in headerParamNames) {
         System.log(" SET headers: " + headerParamNames[k] + " : " + headerParams[k]);
         request.setHeader(headerParamNames[k], headerParams[k]);
      }
      System.log("Request: " + request);
      System.log("Request URL: " + request.fullUrl);
      var response = request.execute();
      System.log("Response: " + response);
      statusCode = response.statusCode;
      statusCodeAttribute = statusCode;
      System.log("Status code: " + statusCode);
      contentLength = response.contentLength;
      headers = response.getAllHeaders();
      contentAsString = response.contentAsString;
      //System.log("Content as string: " + contentAsString);
      System.log("****Headers****");
      for (var header in headers) {
         System.log(header.toString());
      }
      return contentAsString;
   }

   System.log("==========Get Example Requests from Service Now and needed fields==========")
   var content = ""
   var defaultContentType = "application/json"
   var acceptHeaders = "application/json"
   function get() {
      //URL that can be custom
      urlTemplate = "https://test.service-now.com/api/now/table/sc_request?sysparm_query=short_description%3DExample%20Request&sysparm_limit=10&state=1"
      restAPICall(snGetRequest, content, defaultContentType, acceptHeaders, urlTemplate)
      System.log("Preparing JSON Response: ")
      System.log("this is the content " + content)
      //PARSE JSON INTO A VARIABLE
      var response = JSON.parse(contentAsString)
      //SHOW TOTAL NUMBER OF REQUESTS
      System.log("Total number of Example Requests: " + response["result"].length)
      return response
   }

   // Set variables from Service Now
   var openExampleRequests = get()
   // This will cause the workflow to error when there are 0 Service Now Requests. That is okay because we trap it below. See bottom of this file
   var requestNumber = openExampleRequests["result"][0]["number"]
   System.log("Request Number: " + requestNumber)

   var utaID = openExampleRequests["result"][0]["u_ut_id"]
   System.log("EmplID of the requestor: " + utaID)
   var sys_ID = openExampleRequests["result"][0]["sys_id"]
   System.log("SysID of the Service Now Service Now Request: " + sys_ID)

   var description = openExampleRequests["result"][0]["description"]
   var splitDesc = description.split("\n")

   ```

4. The code above does a couple of things:

   - First it defines a generic REST API function that you can use to pass custom calls
   - Then in another function, it calls the first function (line 53) and it specifically searches for: 'short description = Example Request' with a limit of 10 entries and a state=1 which is 'new'
   - Lastly, it starts to parse the fields from ServiceNow and put them into variables (line 64+). In order to see what you are working with, it is highly advised to first make this call in [Postman](https://automationadmin.com/2019/10/postman-get-token/) or Powershell and work from there.
   - Notice this (line 53) is where it uses the variable `snGetRequest` which is defined in step 1.

5. Now, you perform whatever actions you want. Then towards the end of the workflow, you can update the Service Now Request like so:

   ```javascript
   System.log("==========Update the Service Now Request in Service Now==========")
   var content4 = {
      "state": "12",
      "assigned_to": "c86bf948db9a0058d48b6sd887e65ce961979"
   }
   var changeContent4 = JSON.stringify(content4)
   var defaultContentType4 = "application/json"
   var acceptHeaders4 = "application/json"
   var snowURLTemplate = "https://test.service-now.com/api/now/table/sc_request/" + sys_ID
   restAPICall(snPutRequest, changeContent4, defaultContentType4, acceptHeaders4, snowURLTemplate)
   ```

   - This will update the Service Now Request to "waiting for other tasks"
   - Notice this (line 10) is where it uses the variable `snPutRequest` which is defined in step 1.

6. If you want to close the Service Now Request, just change the `state` to the needed code to close the Service Now Request and do the same PUT request with that code int the body instead of code `12`.