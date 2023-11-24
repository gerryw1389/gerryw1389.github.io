---
title: 'VRO: Parse REST Responses'
date: 2020-01-21T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-parsing-responses/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

I use the following with [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) to parse REST responses (json objects thus far):

### To Resolve

1. REST API's that I have been interacting with so far have all been responding with JSON when you send a request. So part of your functions in your code should iterate through a response and grab the needed variables. Here is an example response:


   ```json
   {
      "arraySize": 1,
      "users": [
         {
               "userId": 32421798732,
               "attributes": [
                  {
                     "attributeId": 11,
                     "attributeKey": "department",
                     "attributeType": "COLLECTED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Information Technology"
                  },
                  {
                     "attributeId": 3,
                     "attributeKey": "displayDescription",
                     "attributeType": "ARC_MANAGED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Systems Administrator"
                  },
                  {
                     "attributeId": 2,
                     "attributeKey": "displayName",
                     "attributeType": "ARC_MANAGED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Gerry Williams"
                  }
               ],
               "link": "/api/data/users/32421798732",
               "supervisorId": 32421798798,
               "linkSupervising": "/api/data/users/32421798732/supervising",
               "linkAffiliations": "/api/data/users/32421798732/affiliations",
               "linkGroups": "/api/data/users/3242179/groups",
               "linkPermissions": "/api/data/users/3242179/permissionsBoundComposite",
               "linkAccounts": "/api/data/users/32421798732/accounts",
               "uniqueUserId": "41f6fghew6c2dd5413a87251370aa6a2041"
         }
      ],
      "buildTag": false
   }
   ```

   - So in code, we would loop through and grab the values for `attributeID` of `3` and `2` and store those in a variable

   ```javascript
   var nameAttVal = ""
   var uniqueUserId = ""
   // assuming REST API response is stored in contentAsStringSoftware
   var softwareJson = JSON.parse(contentAsStringSoftware)
   for (i = 0; i < softwareJson.users[0].attributes.length; i++) {
      System.log("This is an attribute: " + softwareJson.users[0].attributes[i].attributeId)
      if (softwareJson.users[0].attributes[i].attributeId == "2") {
         nameAttVal = softwareJson.users[0].attributes[i].attributeValue
      }
      if (softwareJson.users[0].attributes[i].attributeId == "3") {
         jobAttVal = softwareJson.users[0].attributes[i].attributeValue
      }
   }
   System.log("This is the Name: " + nameAttVal)
   System.log("This is the Job title: " + jobAttVal)
   ```

   - In this case `nameAttVal` would be `Gerry Williams` and `jobAttVal` would be `Systems Administrator`

2. The main thing to look for is that if the response contains an array, you need to store it in an array as well:

   ```json
   {
      "arraySize": 1,
      "users": [
         {
               "userId": 3242179,
               "attributes": [
                  {
                     "attributeId": 11,
                     "attributeKey": "department",
                     "attributeType": "COLLECTED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Information Technology"
                  },
                  {
                     "attributeId": 3,
                     "attributeKey": "displayDescription",
                     "attributeType": "ARC_MANAGED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Systems Administrator"
                  },
                  {
                     "attributeId": 2,
                     "attributeKey": "displayName",
                     "attributeType": "ARC_MANAGED",
                     "attributeDataType": "STRING",
                     "attributeValue": "Gerry Williams"
                  },
                  {
                     "attributeId": 9,
                     "attributeKey": "emails",
                     "attributeType": "COLLECTED",
                     "attributeDataType": "STRING",
                     "attributeValues": [
                        "gerry.williams@domain.com"
                     ]
                  }
               ],
               "link": "/api/data/users/32421798732",
               "supervisorId": 32421798798,
               "linkSupervising": "/api/data/users/32421798732/supervising",
               "linkAffiliations": "/api/data/users/32421798732/affiliations",
               "linkGroups": "/api/data/users/3242179/groups",
               "linkPermissions": "/api/data/users/3242179/permissionsBoundComposite",
               "linkAccounts": "/api/data/users/32421798732/accounts",
               "uniqueUserId": "41f6fghew6c2dd5413a87251370aa6a2041"
         },
         ],
      "buildTag": false
   }
   ```

   - The code is basically the same, just make sure you declare an array before hand and then add the array value to the array.

   ```javascript
   var nameAttVal = ""
   var uniqueUserId = ""
   var uniqueUserEmail = []
   // assuming REST API response is stored in contentAsStringSoftware
   var SoftwareJson = JSON.parse(contentAsStringSoftware)
   for (i = 0; i < SoftwareJson.users[0].attributes.length; i++) {
      System.log("This is an attribute: " + SoftwareJson.users[0].attributes[i].attributeId)
      if (SoftwareJson.users[0].attributes[i].attributeId == "2") {
         nameAttVal = SoftwareJson.users[0].attributes[i].attributeValue
      }
      if (SoftwareJson.users[0].attributes[i].attributeId == "3") {
         jobAttVal = SoftwareJson.users[0].attributes[i].attributeValue
      }
      if (softwareJson.users[0].attributes[i].attributeId == "9") {
      uniqueUserEmail.push(softwareJson.users[0].attributes[i].attributeValues);
   }
   }
   System.log("This is the Name: " + nameAttVal)
   System.log("This is the Job title: " + jobAttVal)
   ```

   - In this case `nameAttVal` would be `Gerry Williams` and `jobAttVal` would be `Systems Administrator` and `uniqueUserEmail` would be `["gerry.williams@domain.com"]`

   - You could then later in the code loop through the array and do something with each email address as needed.

