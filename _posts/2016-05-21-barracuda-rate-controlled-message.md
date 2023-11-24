---
title: Barracuda Rate Controlled Message
date: 2016-05-21T05:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/barracuda-rate-controlled-message/
tags:
  - Hardware
---
<!--more-->

### Description:

The user will send a request to look at a group of emails with the following error:

   ```escape
   Your message did not reach some or all of the intended recipients.

   Subject: This is a test email  
   Sent: 6/17/2015 11:06 AM

   The following recipient(s) cannot be reached:

   example@example.com on 6/17/2015 11:06 AM  
   Server error: 450 too many emails from this sender (rate controlled)
   ```

### To Resolve:

1. First login to Barracuda. Go to Basic => Message Log => Then sort: From => Contains => (emailAddressofClient)

2. If you see a bunch of messages being sent in a short amount of time, chances are => the user has been infected. Or one of the machines that use that email has been infected, the best thing to do is to change their password.

   - ![barracuda-rate-controlled](https://automationadmin.com/assets/images/uploads/2016/09/barracuda-rate-controlled.png){:class="img-responsive"}

3. Login to &#8220;YourEmailServer&#8221; => find their account under Mailboxes and ask them to give you a password to change it to.

4. If you want to see the Rate Control settings in Barracuda, just go to Block/Accept => Rate Control. We have it set to 150 emails every 30 minutes. Anything over that, the Spam Filter will just drop the packets.

5. Tell the client they need to wait 30 minutes before sending an email again. If this happens again after 30 minutes, there is a good chance their machine has a keylogger because it is able to capture the password. Advise them to re-image their computer.