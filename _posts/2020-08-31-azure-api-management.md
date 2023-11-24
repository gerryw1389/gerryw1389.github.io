---
title: Azure API Management
date: 2020-08-31T14:27:17-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/azure-api-management
tags:
  - Azure
tags:
  - Azure-ApiManagement
---
<!--more-->

### Description:

So my organization needed a way to send API calls to a third party application that required a static IP from us `outbound` so they could whitelist inbound. We ended up using Azure API management to accomplish this. To further clarify, you can have Azure Logic Apps, Azure Functions, Azure $x call this API management endpoint and it will forward the API calls to a third party. This is a huge win since most organizations I work with will want a single IP to whitelist. This allows me to send API payloads from many Azure tools and only provide a single IP to a third party vendor. If only there was a way to do this with binary files (SFTP transfers without a virtual machine) as well...

### To Resolve:

1. First, deploy an instance in the Azure portal.
2. This takes a while. After it is done, in the Azure Portal go to:
   - API's blade => Echo API => Settings tab => Take note of `Web Service: http://echoapi.cloudapp.net/api`.
3. For your organizations API's, you will replace this with the base URI of the endpoint you want to connect to. For example, for Service Now this is `yourcompany.service-now.com/api`. Let's go ahead and create it:
   - In API's blade => Click `Add API` => Type
     - `SN Test` as display name
     - `SN-Test` as name
     - `https://yourcompany.service-now.com/api` for Web Service URL
     - `/sn-test/` as the API URL Suffix. This is the first part of the URL you will hit to go to SN Test e.g. `https://my-org.azure-api.net/sn-test/`
   - On the same blade, go to Design tab. This lists all the operations you can perform on your API.
     - Click `Add Operation` => Name it `Get Request` => On Front End => Edit => URL `GET /now/table/sc_request` => Save
   - On the same blade, go to the Test tab. Click on `Get Request` and click on the eye icon in bottom right to get the `Ocp-Apim-Subscription-Key` under the HTTP Request section. We will need this to test from Postman.

4. Now inside Postman:
   - Set operation to `GET`
   - Set URL to `https://my-org.azure-api.net/sn-test/now/table/sc_request?sysparm_query=sys_id%3D1e04601adb2ad0106b29d411ce96199e`
     - First part `https://my-org.azure-api.net/sn-test/` is your API Management instance which redirects to the API you just created
     - Second part `/now/table/sc_request` is how to hit SN Request table via API.
     - Last part `?sysparm_query=sys_id%3D1e04601adb2ad0106b29d411ce96199e` is a query put in any SN sys Id you want.
   - Under `Authorization` tab, setup what your organization uses. We use Basic so I put in Username/Password of our API user.
   - Under `Headers` tab, put in `Ocp-Apim-Subscription-Key` and `Ocp-Apim-Trace` as keys and values are what you copied as the key and `true`.
   - Send it. Should be good to go!

5. At this stage, you can keep adding API endpoints and operations as you see fit. But what if you already have some as Postman collections? Well that is where you need to use [OpenMan](https://github.com/codeasashu/openman) to convert Postman 2.1 collections to OpenAPI spec for Azure API Management. I had to do this so this is what I did:
   - Export v2.1 in Postman to `c:\scripts`
   - In wsl:
     - Type: `pip3 install openman`
     - Type: `openman convert /mnt/c/scripts/p.json /mnt/c/scripts/spec2.yaml`
   - Inside Azure API Management portal, go to API's => Add API => OpenAPI Spec => Browse => Upload the yml file, ignore errors

6. At this point, you should be good to go but wanted to include some additional info: To learn more about API Management, what I did was click on `Echo API` and went to Design tab => `Post Create Resource` => FrontEnd => Edit =>  Then looked at bottom sections: Template, Query, Headers, Request, Responses.
   - These are similar to Postman tabs. Inside each one you put a key and an example. For example, go to the `Request` sub-tab:
     - Type: `application/json` under Content-Type
     - Type `{"vehicleType": "train","maxSpeed": 125,"avgSpeed": 90,"speedUnit": "mph"}` under Sample
     - Save
   - In Postman
     - Set operation to `POST`
     - Set endpoint to `https://my-org.azure-api.net/echo/resource`
     - Set headers to:
       - `Content-Type`: `application/json`
       - `Ocp-Apim-Subscription-Key`: `mykey-89de6714c26795e09`
       - `Ocp-Apim-Trace`: `true`

     - Set body to:

     ```json
     {
     "vehicleType": "train-blahblahblah",
     "maxSpeed": 125,
     "avgSpeed": 90,
     "speedUnit": "mph"
     }
     ```

     - Send => Response should come back with a json object with a `vehicleType` of `train-blahblahblah`

   - Now replace url with: `http://echoapi.cloudapp.net/api/resource` => Delete the subscription headers and send again => should get the same thing. Get it?
