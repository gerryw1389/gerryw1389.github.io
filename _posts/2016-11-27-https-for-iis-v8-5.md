---
title: HTTPS For IIS v8.5
date: 2016-11-27T08:29:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/https-for-iis-v8-5/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - WebServer
  - Certificates
---
<!--more-->

### Description:

I followed these steps to enable HTTPS on some of our websites. NOTE: We already had a wildcard SSL cert purchased prior to me running these steps.

### To Resolve:

1. Inside IIS Manager, go to &#8220;Server Certificates&#8221; and choose the option to &#8220;create a request&#8221;. Fill out the information:

   ```escape
   common name = FQDN of the server  
   organization = Company Nameorganizational unit = IT  
   city/ state/ province = self explanatory
   ```

2. Click Next => Choose: Microsoft RSA and 2048 bit length => Next => Export to desktop (we will delete shortly).

3. Open up web browser and go to Digicert.com and sign in. Go to Orders => click on your domain wildcard cert => Get a duplicate.

4. Paste in your key from step 2. It will say to wait a few minutes, and then you can download your keys.

5. Once you download them to your server, open IIS Manager => Server Certificates => Complete Request. Fill out the information:

   ```escape
   filename = path\to\file  
   friendly name = your domain name  
   select store = personal
   ```

6. Once the cert is installed, go to your site in the list of websites in IIS Manager. Select &#8220;bindings&#8221; and add 443 with your cert. I usually check the box for &#8220;require server name indication&#8221; and type out the FQDN of the server.

7. Next, we create an inbound rule under URL Rewrite (If it's not there, install from [here](https://www.iis.net/downloads/microsoft/url-rewrite)):

   ```escape
   name = http to https  
   Match URL:  
   Requested URL: Matches the pattern  
   Using: Regular Expressions  
   Pattern: (.*)  
   Ignore case = checked  
   Conditions:  
   Logical grouping: Match All  
   Input: {HTTPS}  
   Type: Matches the Pattern  
   Pattern: ^OFF$  
   Action:  
   Action Type: Redirect  
   Redirect URL: https://{HTTP_HOST}/{R:1}  
   Append query string = Checked  
   Redirect Type = Permanent (301)
   ```

8. Restart the website, it should start redirecting to HTTPS now. You may want to enable [SSL Rebind](https://www.iis.net/learn/get-started/whats-new-in-iis-85/certificate-rebind-in-iis85), but I didn't go that far.

### References:

["Step 1: Create Your CSR in IIS 8 or IIS 8.5 on Windows Server 2012"](https://www.digicert.com/csr-creation-microsoft-iis-8.htm)  
["Step 2: Install and Configure Your SSL Certificate in IIS 8 or IIS 8.5 on Windows Server 2012"](https://www.digicert.com/ssl-certificate-installation-microsoft-iis-8.htm)  

