---
title: Postman PreRequests and Tests
date: 2020-02-09T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/postman-pre-request-and-tests
tags:
  - LocalSoftware
tags:
  - RestAPI
---
<!--more-->

### Description:

So in Postman, you can use `pre-request scripts` to have Postman run scripts before the connection and `tests` to run after the connection. This works really well with a software like, for example [Netiq Identity Governance](https://www.microfocus.com/en-us/products/netiq-identity-governance/overview#). That particular software requires an Oauth token before the connection and afterwards to revoke the token.

### To Resolve:

1. First create an environment:
   - Set variable: `currentAccessToken` 
   - Set variable: `currentRefreshToken`
   - Remember to place double curly brackets on each end - see [here](https://learning.postman.com/docs/sending-requests/variables/)

2. Set pre-request script:

   ```javascript
   const echoPostRequest = {
      url: 'https://server.domain.com:8443/osp/a/idm/auth/oauth2/token',
      method: 'POST',
      header: {
         'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: {
         mode: 'urlencoded',
         urlencoded: [
            { key: "grant_type", value: "password" },
            { key: "username", value: "myUser" },
            { key: "password", value: "pa55word" },
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

3. Set tests:

   ```javascript
   const echoPostRequest = {
      url: 'https://server.domain.com:8443/osp/a/idm/auth/oauth2/revoke',
      method: 'POST',
      header: {
         'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: {
         mode: 'urlencoded',
         urlencoded: [
            { key: "token", value: pm.environment.get("currentRefreshToken") },
            { key: "client_id", value: "mySuperLongClientID" },
            { key: "client_secret", value: "mySuperLongClientSecret" }
         ]
      }
   };

   pm.sendRequest(echoPostRequest, function (err, response) {
      try {
      console.log(response.json());
      jsonData = JSON.parse(responseBody);
      } catch (err) {
         pm.environment.set('currentRefreshToken', "blank")
         console.log(err); // This must be logging the error on console
         console.log("If error is No data, empty input at 1:1^, that is okay")
      }
   });
   ```

4. Lastly, inside the connection just set `Authorization` tab to:
   - type: Bearer Token
   - Value: `currentAccessToken`

