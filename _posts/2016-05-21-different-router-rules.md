---
title: Different Router Rules
date: 2016-05-21T05:12:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/different-router-rules/
categories:
  - Hardware
---
<!--more-->

### Description:

You will learn quickly that every router is unique. Through experience, you will see certain things that you have to note about different routers:

#### CheckPoint Routers:

1. Web filtering is managed remotely through a portal to a &#8220;Service Center&#8221;. You can access the web GUI by typing &#8220;my.firewall&#8221; in a web browser if you don't know its IP Address.

#### SonicWall Routers:

1. When trying to access via web GUI, make sure to type out &#8220;https&#8221; prior to the IP Address of the router or try appending &#8220;:8080&#8221; on the end (called a &#8220;socket&#8221; or port number).

#### Verizon Routers:

1. Under the &#8220;System Settings&#8221; options, there is a &#8220;Local Domain&#8221; option, make sure to put in the network's Workgroup's name or Domain's name here. By default it will show up as &#8220;.home&#8221; and could interfere with networking.


   <img class="alignnone size-full wp-image-643" src="https://automationadmin.com/assets/images/uploads/2016/09/different-router-rules.png" alt="different-router-rules" width="704" height="423" srcset="https://automationadmin.com/assets/images/uploads/2016/09/different-router-rules.png 704w, https://automationadmin.com/assets/images/uploads/2016/09/different-router-rules-300x180.png 300w" sizes="(max-width: 704px) 100vw, 704px" />