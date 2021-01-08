---
title: Different Email Protocols
date: 2016-05-23T18:14:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/different-email-protocols/
categories:
  - Networking
  - SysAdmin
---
<!--more-->

### Description:

Many people get confused when talking about different email protocols so I will give a generic breakdown of each.

### To Resolve:

1. POP3/ Post Office Protocol => Is known as the &#8220;one way communication protocol&#8221;. It uses ports 110 (default) and 995 (over SSL) and is simply a way for a user to login to an email server and download all their mail in bulk intervals. Once the mail is retrieved, it is usually deleted from the server. What users do with the mail after it has been downloaded does not effect other users.

2. IMAP/ Internet Message Access Protocol => Is known as the &#8220;two way communication protocol&#8221;. It uses port 143 (default) and 993 (over SSL) and is used as a two way communication between client and server. The messages stay stored on the server and the user simply gets an interface that interacts directly with it. This is the most common protocol for web clients that don't use Exchange. When using this protocol, what one user does effects all devices (moves a folder, deletes an email, etc.)

3. SMTP/ Simple Mail Transfer Protocol => Is the only sending mail protocol (instead of receiving like the two before) and uses ports 25 (default, insecure), 2525 (insecure), and 465 (secure).

4. MAPI/Messaging Application Programming Interface => Is Microsofts proprietary format (although OpenSource versions are in the making) of IMAP for users who use MS Exchange. See more about it here (https://en.wikipedia.org/wiki/Messaging\_Application\_Programming_Interface).

5. ActiveSync => Not really a protocol, but a mobile synchronization app developed by Microsoft used to sync smart phones to Exchange to some extent (emails, calandar, contacts).