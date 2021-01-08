---
title: WinSCP Client Host Key Error
date: 2016-05-23T12:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/winscp-client-host-key-error/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

When trying to connect via SFTP from client to server, you will get a message saying &#8220;The server's host key is unknown&#8221; or &#8220;Connect to unknown server?&#8221;.

   - From Filezilla:
  <img class="alignnone size-full wp-image-737" src="https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-1.png" alt="winscp-client-host-key-1" width="726" height="228" srcset="https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-1.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-1-300x94.png 300w" sizes="(max-width: 726px) 100vw, 726px" />

   - From WinSCP:
  <img class="alignnone size-full wp-image-738" src="https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-2.png" alt="winscp-client-host-key-2" width="726" height="290" srcset="https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-2.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/winscp-client-host-key-2-300x120.png 300w" sizes="(max-width: 726px) 100vw, 726px" />


### To Resolve:

1. There is no fix for this as clients are set up to always ask on first attempt, even if the certificate is valid. What you could do though is get in contact with that server's administrator and see if their key matches what you plan to connect to. Just send them a screenshot like those above just to make sure you won't fall victim to a man-in-the-middle attack.

2. Note that the servers host key has nothing to do with PKI. See [winscp.net](https://winscp.net/eng/docs/ssh_keys) to learn about different SSH Keys.


### References:

["Verifying the Host Key"](https://winscp.net/eng/docs/ssh_verifying_the_host_key)

