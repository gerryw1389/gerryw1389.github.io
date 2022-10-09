---
title: Naked Domain Redirect CloudFlare
date: 2016-11-15T05:03:27+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/naked-domain-redirect-cloudflare/
categories:
  - Networking
tags:
  - Cloud
---
<!--more-->

### Description:

I needed a way for people to get to my site without having to type `www` in the address bar. I first used a service called `[wwwizer](http://wwwizer.com/naked-domain-redirect)` but then found that you can do this WITHIN CloudFlare by setting up `Page Rules`. 

NOTE: You only get 3 with a free domain, but you only need 1 for this.
{: .notice--success}

### To Resolve:

1. Sign into CloudFlare and then go to Page Rules. Create one that:

   ```escape
   example.com/*  
   # forwarding URL - 301 Permanent Redirect  
   http://www.example.com/$1
   ```

   - From the link: The solution is to use variables. Each wildcard corresponds to a variable when can be referenced in the forwarding address. The variables are represented by a `$` followed by a number. To refer to the first wildcard you would use `$1`, to refer to the second wildcard you would use `$2`, and so on.

   - In this case, if someone went to: `example.com/some-particular-page.html`
   - They would be redirected to: `http://www.example.com/some-particular-page.html`


### References:

["Configuring URL forwarding or redirects with Cloudflare Page Rules"](https://support.cloudflare.com/hc/en-us/articles/200172286-How-do-I-perform-URL-forwarding-or-redirects-with-CloudFlare-)