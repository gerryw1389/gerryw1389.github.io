---
title: 'Graph API: Read Extension Attributes'
date: 2020-08-21T14:27:17-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/graph-api-read-extension-attributes
categories:
  - WebSoftware
  - Azure
tags:
  - Scripting-RestAPI
---
<!--more-->

### Description:

So I had a goal to query Azure Graph API to answer something like: "Get me all users like `(user.extensionAttribute3 -eq "Employee") -and (user.accountEnabled -eq True) -and -not (user.jobtitle -eq "Retired")`". This is how I did it:

### To Resolve:

1. [Create an application](https://automationadmin.com/2020/01/azure-create-ps-app/) in Azure with Application permissions to Graph API and `User.Read.All`.
   - Copy its application ID and client secret to notepad.

2. Open Postman, create a collection, add the following request:

   - `GET https://graph.microsoft.com/v1.0/users/user@domain.com`
   - Pre-request script

   ```js
   const echoPostRequest = {
      url: 'https://login.microsoftonline.com/5cdc5b43-d7be-4eee2-8173-729e3b0a62d9/oauth2/v2.0/token',
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
            { key: "client_id", value: "id" },
            { key: "client_secret", value: "my-secret" }
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

   - In the Pre-Request script above, replace `id` with your application ID and `my-secret` with your client secret.

3. After running it, you will see that it doesn't get your user's `onPremisesExtensionAttributes`, for that, just change to the beta API `GET https://graph.microsoft.com/beta/users/user@domain.com`





