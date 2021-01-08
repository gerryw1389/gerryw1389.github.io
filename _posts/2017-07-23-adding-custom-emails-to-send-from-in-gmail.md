---
title: Adding Custom Emails To Send From In Gmail
date: 2017-07-23T05:37:28+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/adding-custom-emails-to-send-from-in-gmail/
categories:
  - WebSoftware
---
<!--more-->

### Description:

So I have purchased a couple domains from [Google Domains](http://domains.google.com) and I always liked how, if you stay with them instead of switching to CloudFlare, they will allow you to receive emails that forward to your personal Gmail. I don't know why I didn't bother with this before, but you can SEND FROM those email addresses as well.

### To Resolve:

1. First, to get email sent to you at your new domain, you just go to Email => and enter `*` and point it to your personal gmail in the &#8220;Email Forwarding&#8221; section. Pretty straightforward.

   - Said another way: Click domain => Email => Add: `*.domainname.com` => `myemail@gmail.com`

2. To send out as that person though, you have to:

   - Click on &#8220;My Account&#8221; => Sign In Options
   - Find the &#8220;App Passwords&#8221; and select Mail => Other => Enter your domain name in other. It will then generate a code, copy that.
   - Now open gmail => Settings => Accounts and Import => Add another address => Name: Your DisplayName => Email address: `admin@domain.com` => Next.
   - SMTP Server: `smtp.gmail.com` => Port: 465 => Username: `YourCurrentGmail@gmail.com` => Password: App password from above
   - Click verification email => done!

### References:

["Forward your emails"](https://support.google.com/domains/answer/3251241?hl=en)  