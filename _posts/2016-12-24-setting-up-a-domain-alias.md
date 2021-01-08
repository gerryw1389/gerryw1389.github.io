---
title: Setting Up A Domain Alias
date: 2016-12-24T07:35:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/setting-up-a-domain-alias/
categories:
  - Networking
---
<!--more-->

### Description:

So let's say you have a website called &#8220;visitme.example.org&#8221; and you want people to be able to type in &#8220;pleasevisitme.example.org&#8221; or &#8220;vm.example.org&#8221; to get to your site. How do you do it?

### To Resolve:

1. First, you have to make sure that your internal DNS server can see your server as pleasevisitme and vm. To do this, you need to add an &#8220;A&#8221; record to your &#8220;example.org&#8221; root domain. So on the internal DNS server, make sure you have 3 A records pointing to your server: visitme (already in prod), pleasevisitme and vm. These other two will be &#8220;aliases&#8221;.

1. Next, you want to make sure your internal DNS servers can communicate with your hosted DNS servers (public). This should already be happening or else people would not be able to hit your current website at visitme.example.org. If you have a Cisco appliance for example, you would see the following in running config:

   ```escape
   policy-map type inspect dns preset\_dns\_map  
   parameters  
   message-length maximum client auto  
   message-length maximum 512  
   policy-map global_policy  
   class inspection_default  
   inspect dns preset\_dns\_map
   # DNS is port 53 UDP by default. With this Cisco config, it can accept larger packets by the &#8220;client auto&#8221;    command.
   ```



3. After you set the A records internally, you would do the same thing externally. Login to your DNS host provider and set the same records, but pointing to your external IP. For example, your website visitme.example.org is located at 30.30.30.10. You would add pleasevisitme and vm with the same IP as A records pointing to the same site.

4. That's really all that's needed. The only other thing I have done is add &#8220;pleasevisitme.example.org&#8221; under &#8220;Site Bindings&#8221; in IIS, but I'm not sure that is entirely mandatory.