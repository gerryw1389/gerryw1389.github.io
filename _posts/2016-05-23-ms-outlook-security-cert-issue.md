---
title: 'MS Outlook: Security Cert Issue'
date: 2016-05-23T19:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-outlook-security-cert-issue/
tags:
  - LocalSoftware
  - Security
tags:
  - MSOffice
---
<!--more-->

### Description:

This happens when you refresh the mailbox in Outlook. You may get an error stating `The server you are connected to is using a certificate that cannot be verified`.

  <img class="size-full wp-image-678 aligncenter" src="https://automationadmin.com/assets/images/uploads/2016/09/ms-office-security-cert-issue.png" alt="ms-office-security-cert-issue" width="726" height="294" srcset="https://automationadmin.com/assets/images/uploads/2016/09/ms-office-security-cert-issue.png 726w, https://automationadmin.com/assets/images/uploads/2016/09/ms-office-security-cert-issue-300x121.png 300w" sizes="(max-width: 726px) 100vw, 726px" />


### To Resolve:

1. Click the "View Certificate…" button and look at the "Issued to" name. This is usually the name that you'll need to specify for your incoming and/or outgoing server in your account configuration. In some cases, this still won't work when the certificate holds multiple names. You can then select the "Details" tab and see if the certificate holds a field called "Subject Alternative Name". If so, then you'll find other names that you could try behind the "DNS Name=" value. If none of those names work either, contact your ISP and ask for the correct name of the mail server that you should use. Another (less secure) alternative would be to disable the use of SSL for your mail account.

2. Do note that you can get it to go away by pressing &#8220;Yes&#8221;, but by doing so you are agreeing to use a self-signed certificate. Only install the certificate if you trust the domain that is specified on the certificate and if the administrator responsible for that domain has instructed you to do so.

### References:

["Cannot verify Security Certificate warning"](https://www.msoutlook.info/question/613)