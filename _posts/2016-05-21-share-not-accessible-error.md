---
title: Share Not Accessible Error
date: 2016-05-21T23:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/share-not-accessible-error/
categories:
  - Networking
tags:
  - FileSystem
---
<!--more-->

### Description:

When trying to access a network resource, you get the following message: `(ShareName or ComputerName) is not accessible`

  <img class="alignnone size-full wp-image-709" src="https://automationadmin.com/assets/images/uploads/2016/09/share-not-accessible.png" alt="share-not-accessible" width="572" height="184" srcset="https://automationadmin.com/assets/images/uploads/2016/09/share-not-accessible.png 572w, https://automationadmin.com/assets/images/uploads/2016/09/share-not-accessible-300x97.png 300w" sizes="(max-width: 572px) 100vw, 572px" />



### To Resolve:

1. These steps will be similiar to [Mapped Network Drive Issues](https://automationadmin.com/2016/05/mapped-network-drives-issues/), but try these steps.

2. First try to ping the computer by IP. Does it work? Try by name if not => you may have a DNS issue at hand.

3. If you can ping successfully, the next step is to make sure both the `Server` and `Workstation` services are running on both the computer requesting the resource (the client) and the computer sharing the resource (the server). To do this:  

   - Run => `services.msc` => Navigate to the named services and make sure they are both running. I have seen instances where they were disabled for some reason.

4. Next, click Start => Credential Manager (in search bar) => Add a Windows credential => Add the host name of the server, the user name and password to connect into it.