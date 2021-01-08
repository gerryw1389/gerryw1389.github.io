---
title: Implementing TLS
date: 2016-05-21T05:08:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/implementing-tls/
categories:
  - Networking
  - Security
tags:
  - Certificates
---
<!--more-->

### Description:

TLS is the new version of SSL and is the de facto standard in email security. I followed these steps to get it implemented on my network. Note that we have an internal mail server and a Barracuda Spam Filter device.

### To Resolve:

1. We got a certificate from Digicert (CA => Certificate Authority) for &#8220;*.example.net&#8221; which allows TLS to be implemented.

2. We installed the certificates on the Barracuda by going to Advanced => Secure Administration tab => Set it up like:

   - First two radio buttons = No
   - Web interface HTTPS/SSL port = 443.
   - Certficate type dropdown = Trusted (Signed by Trusted CA)
   - Cert. details = &#8220;CN=*.example.net/ Status = OK&#8221;. This was manually uploaded. We did this over the phone with Barracuda.

3. We opened the ports on the router to allow inbound/ outbound TLS.

4. Next we requested a duplicate cert and installed it on the mail server.

5. Once the server is configured (Barracuda device), we need to configure the clients, Outlook.

   - Open Outlook, go to File => Account Settings. Change the outbound server to &#8220;Barracuda.example.net&#8221;.

   - Go to More Settings (button on bottom right) => Advanced => Make sure the Incoming port is &#8220;995&#8221; for POP and &#8220;993&#8221; for IMAP and outgoing is 465 requires TLS.

   - Test the account settings, should be all green. If there is a message box that warns about a certificate after enabling TLS, it is probably due to a DNS issue, make sure the incoming and outgoing servers are by host name and not IP.