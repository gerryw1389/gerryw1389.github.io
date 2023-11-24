---
title: MailServer Migration
date: 2016-05-30T05:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/mailserver-migration/
tags:
  - LocalSoftware
tags:
  - Migration
---
<!--more-->

### Description:

We needed to migrate the email server running MailEnable to Server2012.

### To Resolve:

1. Follow the steps on [Create A New VM](https://automationadmin.com/2016/05/hyper-v-to-create-a-new-vm/).

2. Once the VM is created, we need to enable the IIS role (leave defaults) and install the email server software.

3. After installation, we need to export the &#8220;mailboxes&#8221; and &#8220;groups&#8221; from the old server.

   - This can be tricky, but you need to export as a text file. Then copy into Excel/Word until you get it to &#8220;username,password&#8221;

4. Open up MailEnable on the new server and select &#8220;import users&#8221; => point to that file => select the option to select a custom mailbox size, we did &#8220;500000&#8221;.

5. This will populate all the users. Now to import the groups. We did these manually as there isn't very many.

6. Now we need to enable TLS. To do this, we need to add an SSL Certificate.

   - Launch IIS Manager => Go to ServerName => Server Certificates- Create a Certificate Request. Fill out the request.
   - Login to Digicert => Request a duplicate (we already had one for the Barracuda device).
   - They will send an email. Save the certificate to a shared folder.
   - Go back into IIS => Server Certificates => Completed Certificate Request => Use friendly name: example.net / Save to Personal cert store
   - Now go to IIS => Sites => MailEnable Protocols => Bindings => Add => HTTPS for port 443. Cert should be the cert we created.
   - Now go to IIS => Sites => Default Site => Bindings => Add => HTTPS => Port 443 => Cert we just created.
   - Make sure ports 80 and 443 are being forwarded from the firewall to the web server.

7. Lastly, you just point the new Mail Server to the old mail server's IP address and make sure all configurations are the same inside the options.