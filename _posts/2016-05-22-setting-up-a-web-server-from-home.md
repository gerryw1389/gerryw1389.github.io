---
title: Setting Up A Web Server From Home
date: 2016-05-22T06:43:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-a-web-server-from-home/
tags:
  - WindowsServer
tags:
  - WebServer
  - Setup
---
<!--more-->

### Description:

Follow these steps to host a website at home. Note that for this you would ideally have a server OS using IIS or Apache hosting a website. Also note that many if not all ISP's throttle network traffic and it will not be practical to host a web site from home, this is just for learning. For a real website hosting setup, you will need to search online for online hosting where they have dedicated servers and bandwidth to handle a full website.

### To Resolve:

1. Many of these steps will be similar to [Setting Up RDP For Home](https://automationadmin.com/2016/05/setting-up-rdp-for-home/). You will first need to login to router's GUI and find the tab called "Virtual Server", "Port Forwarding", or "Applications and Gaming".

2. Create a new rule to open Port 80 and forward to your server's IP address.

  <img class="alignnone size-full wp-image-705" src="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-webserver.png" alt="setting-up-a-webserver" width="726" height="228" srcset="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-webserver.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/setting-up-a-webserver-300x94.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

3. Make sure to follow the steps in the previously mentioned article to setup Dynamic DNS. Assuming it's setup, that is all that is needed. Now test from a computer outside of your home network, open up a web browser and type in your hostname for the dyamic dns and add `:80` at the end if needed, most browsers will default there automatically. Ex: Type `blah.no-ip.com:80` in the URL box.

4. THIS MAY PRESENT A SECURITY RISK TO YOUR NETWORK SO USE AT YOUR OWN RISK!!