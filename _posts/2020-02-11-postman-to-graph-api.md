---
title: Postman To Graph API
date: 2020-02-11T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/postman-to-graph-api
categories:
  - LocalSoftware
tags:
  - Scripting-RestAPI
---
<!--more-->

### Description:

So in my [previous post](https://automationadmin.com//2020/02/postman-pre-request-and-tests) I talked about using Postman to run pre-request scripts so that it can get an Oauth Token and attach it to each request. Here we are going to do the same thing but instead we will connect to Microsoft Graph API. This assumes that you created [an application](https://automationadmin.com/2020/01/azure-create-ps-app/) before (although will work for user as well (see below):


### To Resolve:

1. First you will need to replace `some-tenant-id`, `client_id`, `client_secret`, `username`, and `password` in the examples to come - make sure you have them. Go into your connection, and edit the `pre-request` script to be like: 

   - To connect as an `application`:

   ```javascript
   const echoPostRequest = {
      url: 'https://login.microsoftonline.com/some-tenant-id/oauth2/v2.0/token',
      method: 'POST',
      header: {
         'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: {
         mode: 'urlencoded',
         urlencoded: [
            { key: "grant_type", value: "client_credentials" },
            { key: "scope", value: "https://graph.microsoft.com/.default" },
            { key: "client_id", value: "mySuperLongClientID" },
            { key: "client_secret", value: "mySuperLongClientSecret" }
         ]
      }
   };

   pm.sendRequest(echoPostRequest, function (err, response) {
      console.log(response.json());
      var responseJson = response.json();
      pm.environment.set('currentAccessToken', responseJson.access_token)
      pm.environment.set('currentRefreshToken', responseJson.refresh_token)
   });
   ```

   - To connect as as a `user`:

   ```javascript
   const echoPostRequest = {
      url: 'https://login.microsoftonline.com/some-tenant-id/oauth2/v2.0/token',
      method: 'POST',
      header: {
         'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: {
         mode: 'urlencoded',
         urlencoded: [
            { key: "grant_type", value: "Password" },
            { key: "scope", value: "https://graph.microsoft.com/.default" },
            { key: "client_id", value: "mySuperLongClientID" },
            { key: "client_secret", value: "mySuperLongClientSecret" },
            { key: "Username", value: "myUser@company.com" },
            { key: "Password", value: "seeKeePass" }
         ]
      }
   };

   pm.sendRequest(echoPostRequest, function (err, response) {
      console.log(response.json());
      var responseJson = response.json();
      pm.environment.set('currentAccessToken', responseJson.access_token)
      pm.environment.set('currentRefreshToken', responseJson.refresh_token)
   });
   ```
   
2. Inside the connection just set `Authorization` tab to:
     - type: Bearer Token
     - Value: `currentAccessToken`

3. For requests that don't use `application/x-www-form-urlencoded` (untested):

   ```javascript
   header: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
   },
   body: {
      mode: 'raw',
      raw: JSON.stringify({ 
         grant_type : "client_credentials"
         scope : "https://graph.microsoft.com/.default"
         client_id : "seeKeePass"
         client_secret : "seeKeePass" 
         })
   }
   ```

   - If that doesn't work, check this [Gist](https://gist.github.com/madebysid/b57985b0649d3407a7aa9de1bd327990) for other options 

4. I have powershell example [here](https://automationadmin.com/2020/02/ps-upload-csv-to-teams-sharepoint-site)

