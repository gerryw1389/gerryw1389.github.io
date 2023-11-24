---
title: Postman Get Oauth Token
date: 2019-10-20T01:16:38-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/10/postman-get-token/
tags:
  - Networking
tags:
  - Scripting-RestAPI
---
<!--more-->

### Description:

In this post, I'm going to use [Postman](https://www.getpostman.com/) to get an OAuth 2.0 token for a Rest API endpoint. The API token will be stored in Postman for each request after the initial request. Here is what it looks like:

![postman-token](https://automationadmin.com/assets/images/uploads/2019/10/postman-token.jpg){:class="img-responsive"}


### To Resolve:

1. The first thing you will need to do is read the doc's for the endpoint you are going to be hitting to get the token.

   - For example, access token URL => https://server.domain.com:8443/auth/oauth2/token

2. Next, get the client identifier and client secret as well as a user that has API permissions (and their password)

3. From here, you can click the button Request Token in Postman and save it. Just know that tokens expire periodically so you might want to put the time in the display name so when you do subsequent requests you know which token to use.

4. Note that Postman handles the request for you from that point, but in case you have to do it manually, it will usually be:
   - Method: Post
   - Header: `Content-Type: application/x-www-form-urlencoded`
   - Body: Read your endpoint docs to see if anything is required
   - Send the request, the response will return something like:

   ```json
   { 
      "access_token":"eyJraWQiOiI0...",
      "token_type":"bearer", 
      "expires_in":120, 
      "refresh_token":"eyJhbGciOiJ..."
   }
   ```

5. After getting a token, it is common that you will then use a different URL to send requests to and then attach the following as a parameter in the headers `Authorization: Bearer <access-token>`

