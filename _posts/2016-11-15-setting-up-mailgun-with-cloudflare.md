---
title: Setting Up Mailgun With CloudFlare
date: 2016-11-15T05:01:48+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/setting-up-mailgun-with-cloudflare/
categories:
  - Networking
tags:
  - Cloud
  - Setup
---
<!--more-->

### Description:

After signing up for CloudFlare to host my website, I found that it will automatically disable Google's free email address that comes with the domain. I used the following steps to resolve this:

### To Resolve:

1. Signup for a free account on mailgun.com

2. Log into your account in Mailgun and add a domain from the top menu bar. Once your domain is added, you will see that Mailgun gives you a few MX records and TXT records to be added for your domain, for both successful email forwarding and verification of the domain.

3. Now go to CloudFlare's DNS panel and add those MX records and TXT records provided by Mailgun.

   - Choose your site and select DNS Settings

   - Add the CNAME record. Name = email, Value = mailgun.org, TTL = Automatic, Make sure the cloudflare cloud is gray and not orange/active => You have to click on the cloud icon.

   - Add the two MX records  
     - Name = domain.com (no www), value = mxa.mailgun.org, Priority = 10  
     - Name = domain.com (no www), value = mxb.mailgun.org Priority = 10

   - Add the two TXT records  
     - Name= domain.com (no www), value = v=spf1...  
     - Name = smtp._domainkey, value = k=rsa...

4. Log into your Mailgun account and go to Routes section from the top menu. Now add as many routes as you want.

   - For example, if your domain is example.com and you want all the mails sent to `hello@example.com` to be forwarded to `doctor@who.com` then create that route. So for me that means:

     - Expression Type = Match Recipient  
     - Recipient = `admin@gerrywilliams.net`  
     - Actions = Forward to `myemail@gmail.com`  
     - Priority = 10  
     - Description = Forwards from my domain to my Gmail.

5. If you want people to email TO you at that email, you are done, congrats. I wanted to go one step further and send email FROM that email address. To do this, I went into my Gmail and:
   - Log in to Gmail and go to settings => Accounts and Import:
     - name = Anything you want  
     - email address: `name@domain.com` (this should be the email you set up in the steps before)
     - Leave treat as an alias checked  
     - Click Next Step

6. For the following info you'll need to login to mailgun and use the info under Domain Information  

   - SMTP Server Use SMTP Hostname from Mailgun  
   - Username Use Default SMTP Login from Mailgun  
   - Password Use Default Password from Mailgun
   - I couldn't get this to work, so I created a new SMTP user and password. I plugged this into Google. So it was:
   - SMTP Server: smtp.mailgun.org PORT=587  
   - Username: MyUserEmail  
   - Password: MyUserPassword  
   - Secured connection using TLS (recommended) radio button selected
   - Now comes the hard part, Gmail will send an email to that address and you will have to open to go to the link for verification:
   - Thankfully, Mailgun is aware of people needing temp access to their mailboxes, so they created an [event API](http://blog.mailgun.com/how-to-view-your-messages/) that works like this:
   - You login to Mailgun and go to Logs for your domain and select the most recent inbox message.
   - You can see the API URL to the message along with its unique key under the "storage" section when expanding the log entry.
   - To view the message in the browser just copy the URL and enter `api` as username and your `API key` in the password box. This will let you to view the parsed message. You get your API key under Account Settings in the web GUI.
   - Copy and paste the Google verification link in another tab to "authorize" your email as a trusted sender.

6. Now you can send and receive from a mailbox that seems to be connected to your domain!
