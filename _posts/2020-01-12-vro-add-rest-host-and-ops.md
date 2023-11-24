---
title: 'VRO: Add Rest Host and Operations'
date: 2020-01-12T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-add-rest-host-and-ops/
tags:
  - LocalSoftware
tags:
  - Orchestration
  - Scripting-RestAPI
---
<!--more-->

### Description:

So I've started working more heavily with [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) recently and I have found that it is going to be too difficult to blog about due to how it works like building blocks. That said, I will give a brief overview of how to get started with it (at least the way I have):

Update: Here is a post I did on basic [Javascript syntax in VRO](https://automationadmin.com/2020/01/vro-javascript-syntax/)

### To Resolve

1. The first thing you start to do when you work with VRO is add hosts in its inventory as REST Hosts.

   - What this allows you to do is to then call actions on these hosts like:

   ```javascript
   function getOauthToken() {
      System.log("==========This is the API Call to get the token==========")
      var content1 = {
         "grant_type": "password",
         "username": "myUser",
         "password": "pa55word",
         "client_id": "someClientID",
         "client_secret": "someSecret"
      }
      var formBody = []
      for (var property in content1) {
         var encodedKey = encodeURIComponent(property)
         var encodedValue = encodeURIComponent(content1[property])
         formBody.push(encodedKey + "=" + encodedValue)
      }
      formBody = formBody.join("&")
      var inParameterValues = []
      var request = restPostToken.createRequest(inParameterValues, formBody)
      request.contentType = "application/x-www-form-urlencoded"
      System.log("Request: " + request)
      System.log("Request URL: " + request.fullUrl)
      request.setHeader("Accept", "application/x-www-form-urlencoded")
      var response = request.execute()
      System.log("Response: " + response)
      statusCode = response.statusCode
      System.log("Status Code: " + statusCode)
      contentLength = response.contentLength
      headers = response.getAllHeaders()
      contentAsString = response.contentAsString
      //System.log("Content As String: " + contentAsString)
      var json = JSON.parse(contentAsString)
      var tokenID = json["access_token"]
      System.log("This is the token: " + tokenID)
      return tokenID
   }
   ```

   - It's hard to see, but in that code there is a line: `var request = restPostToken.createRequest(inParameterValues, formBody)`, what we are talking about here is `restPostToken`. So VRO doesn't just magically know anything about the host you are connecting to => You have to add it first in Inventory as a REST HOST! You then have to add operations to that host. Finally you add it to a workflow as an input variable so that VRO knows which operation you are performing (and on what host).

2. So in the previous example I have a variable in my workflow called `restPostToken`. As mentioned, the way it got there was I did the following steps:

   - Login to VRO via Web UI and go to Inventory - See that there is no Rest Host for the server I want to connect to. For example, a server that requires an Oauth 2.0 token for all requests sent to it.
   - I then go to the Workflows tab and run one called `Add A Rest Host`. See my [previous post](https://automationadmin.com/2019/12/vro-run-jenkins-ps/) for an example.
   - I then go to the Workflows tab and run one called `Add A Rest Operation`. See my [previous post](https://automationadmin.com/2019/12/vro-run-jenkins-ps/) for an example. The gist is that you point to your host and then you add as many GET, POST, PUT's or whatever that you will ever need to use in Workflows. Give them good names, for example I always put the operation as the first part of the word. For example "postToken", "getUser", "putSNTicket", ect.
   - I then create a blank workflow and add a new input variable in 2 places `<= pay attention`. First, on the variables screen as a data type `REST:RestOperation` and then on the schema tab under the scriptable task element under 'inputs'.
   - Now, when I put the code above in the script - VRO knows about the host to reach out to and the operation to perform just by the variable in the script.
   - In that same script, you would then have other operations and calls to that host where you attach the Oauth Token as a header. For example:

   ```javascript
   var primaryToken = getOauthToken()
   System.log("==========This is the call to get Information for a user==========")
   var authorizationToken = "Bearer " + primaryToken
   var dynamicURL = "api/data/users?q=" + utaID
   var inParms = []
   softwareGetUserInfo.urlTemplate = dynamicURL
   var requestSoftware = softwareGetUserInfo.createRequest(inParms, "/api/data/users?q=" + uniqueID, null)
   requestSoftware.contentType = "application/json"
   System.log("Request: " + requestSoftware)
   System.log("Request full url: " + requestSoftware.fullUrl)
   requestSoftware.setHeader("Accept", "application/json")
   requestSoftware.setHeader("Authorization", authorizationToken)
   var responseSoftware = requestSoftware.execute()
   System.log("Response: " + responseSoftware)
   var statusCodeSoftware = responseSoftware.statusCode
   var statusCodeAtt = statusCodeSoftware
   System.log("Status Code: " + statusCodeSoftware)
   var contentLengthSoftware = responseSoftware.contentLength
   var headersSoftware = responseSoftware.getAllHeaders()
   var contentAsStringSoftware = responseSoftware.contentAsString
   System.log("Content As String: " + contentAsStringSoftware)
   ```

   - Couple of notes:
   - 1. `softwareGetUserInfo` is another operation to that host when you are using the `primaryToken` variable from the function above.
   - 2. The `softwareGetUserInfo` is dynamic in that you can pass variable to it in the request itself. This is covered in my [Part 2](https://automationadmin.com/2020/01/vro-run-jenkins-pt-2/) post. `uniqueID` is a variable that was defined somewhere else but picture it as a way to search for a specific user, hence the 'GetUserInfo' part of the name

3. So all of this to say, be careful about how you name Rest hosts, rest operations, and input variables. I have taken to put multi-line comment blocks in the top of my workflows that re-use the same variable names so that I don't ever get confused on to what is doing what:

   ```javascript
   /*
   Add Variables to Workflow:
   { 
      "variable-name": "snGetRequest", 
      "type": "REST:RESTOperation", 
      "value": "SERVICENOW_TEST - getRequest: GET api/now/table/",
      "rest-host": "SERVICENOW_TEST: https://company.service-now.com/"
   }
   { 
      "variable-name": "snPutRequest", 
      "type": "REST:RESTOperation", 
      "value": "SERVICENOW_TEST - putRequest: PUT api/now/table/sc_request/", 
      "data-type": "application/json",
      "rest-host": "SERVICENOW_TEST: https://company.service-now.com/"
   }
   { 
      "variable-name": "softwareGetRequestInfo", 
      "type": "REST:RESTOperation", 
      "value": "SOFTWARE_TEST - getSpecificRequestInfo: GET api/request/requestItem/{requestID}/info",
      "rest-host": "SOFTWARE_TEST: https://software.domain.com:8443/"
   }
   { 
      "variable-name": "softwarePostToken", 
      "type": "REST:RESTOperation", 
      "value": "SOFTWARE_TEST - postToken: POST /auth/oauth2/token", 
      "data-type": "application/x-www-form-urlencoded",
      "rest-host": "SOFTWARE_TEST: https://software.domain.com:8443/"
   }
   { 
      "variable-name": "rscTask", 
      "type": "ResourceElement", 
      "value": "task.txt",
      "rest-host": "VRO_RESOURCE_ELEMENTS"
   }
   */
   ```

   - This way, just looking at this workflow I know: It is going to read/write to Service Now, it is going to use a resource element, and it is going to do a GET operation to our software that requires an Oauth Token.

4. Note that I haven't tested this although I use Postman daily now, but if you are a [Postman](https://automationadmin.com/2019/10/postman-get-token/) user - you should be able to export a collection and then [import it directly into VRO!](https://www.vcoteam.info/articles/learn-vco/304-postman-vro-http-rest-plug-in-operations.html) This will save lots of time that you would have to be defining REST operations!
