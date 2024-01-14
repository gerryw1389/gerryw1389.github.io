---
title: Setup Jitbit Helpdesk
date: 2016-11-15T03:12:27+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/setup-jitbit-helpdesk/
tags:
  - WindowsServer
tags:
  - WebServer
  - Setup
---
<!--more-->

### Description:

Jitbit helpdesk is a ticketing system solution that, for a fee, will sell you the source code to their product (built on C#). My company purchased it because it is a fully customizable ticketing system that fit our needs. The software is real neat in that it includes sections for knowledge base, asset tracking, and reporting features as well. It has a hosted version or a self hosted version, we went the latter.

### To Resolve:

1. Per RTFM, here is [the guide](https://www.jitbit.com/docs/helpdesk/!!!helpdesk-software-readme.htm).

2. Once installed, create an admin user and login. The first thing you want to do is go to Administration => Email Settings => Add/remove incoming email accounts. Add an email account that will be used for all ticketing correspondence. Something like itsupport@domain.com works good here. I chose IMAP and &#8220;delete&#8221; for messages marked as read.

3. Everything is built around users so have them sign in to create an account. From here you can assign them 3 types of categories: user, tech, or admin. Tech can be thought of as a group membership, user can be like end user, and admin is keys to the castle.

4. Once you have a good group of users, go to administration => ticket categories and start creating categories that end users will use to submit tickets. This can be your ERP software, General IT, accounting, etc. Adding a group is real easy and whatever you add can be easily updated on the widget end. Once you create the categories, you add the users from the previous steps as technicians.

   - This part is pretty straight forward. You can mirror email groups as ticket categories. For example, if I have an exchange group called &#8220;it@domain.com&#8221; with 3 people: me, Tom, and Bill => you would create a category called &#8220;IT&#8221; for IT related issues and assign those three users to the category. Jitbit will automatically turn these 3 &#8220;users&#8221; into &#8220;technicians&#8221; because you placed them in a category => pretty neat!

5. Once you have users and categories, you can stop and just start using it here. You can either integrate it into your company website, have users sign in manually to create tickets, or try [other options](https://support.jitbit.com/helpdesk/KB/View/5492074-widget-for-your-website).

6. This is just the basics though, it has many more features. Remember those categories from step 4? Well, you can create knowledge base articles based off those. You can then assign those access rights so that only certain members can see certain categories. This allows me to post articles for end users and internal documentation for our IT dept. (currently <5 people so no real KB solution). I also migrated over our spreadsheets of inventory into the &#8220;Assets&#8221; feature for future tracking of IT equipment.

7. Another thing to touch base on is API's. Jitbit integrates with many systems such as Slack, but we really like the tag system you can use to work tickets directly from email. This is how it goes:

   - End user submits a ticket through our custom application based off whatever category the issue is.  
   - Jitbit fires an email to all &#8220;tech's&#8221; in that category letting us know a new ticket was created.  
   - One of the tech's can login to Jitbit and &#8220;take over&#8221; the ticket which then sends another batch of emails to all other tech's letting them know the ticket is being worked.  
   - The tech working the ticket goes back and forth with the end user until the ticket is resolved.  
   - Once the issue is resolved, the tech simply types &#8220;#close# in the subject of the email from the end user and Jitbit automatically closes the ticket for the tech. We then have an automation rule (under Administration => Automation Rules in the web GUI) that emails all other tech's in that category that the ticket is closed. The only issue is that if you are an admin and tech (like me), you will get two email for every closed ticket. Aside from that, it's a great system!

8. If you work in a company that likes to brew in house solutions, Jitbit is a great helpdesk system that can provide the functionality and UI needed for a professional environment.

9. NOTE: I am in no way affiliated with this company, just writing down some notes on their product.